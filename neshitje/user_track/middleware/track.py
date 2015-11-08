from datetime import datetime
from django.http import HttpResponse
from django.db import models
from django.utils import timezone
from django.contrib import auth
from user_track.models import PageTracker, SessionTracker, CookieTracker, SourceID, Bot
from neshitje.nonrepofiles.secrets import Secrets
import xml.etree.ElementTree as ET
import urllib2, json


class UserSessionTracking(object):

    def set_session(self, request, cookie_id, expires=None):

        ip = request.META['REMOTE_ADDR']

        user_id = None
        try:
            auth_user = request.user
            user_id = auth_user.id
        except KeyError:
            user_id = 0

        referrer = None
        try:
            referrer = request.META['HTTP_REFERER']
        except KeyError:
            referrer = "unknown"

        user_agent = None
        try:
            user_agent = request.META['HTTP_USER_AGENT']
        except KeyError:
            user_agent = ""



        print "Current URL " + request.path
        print "Query String: " + request.META['QUERY_STRING']

        print "User: " + str(auth_user)


        ## Get things
        source_id = self.get_source_id(request)

        print("starting a new session")

        geoip = self.getGeoIPJSON(ip)
        if geoip.get("type") == "error":
            geoip['city'] = 'unknown'
            var = {'code':'999'}
            geoip['country'] = var


        session = SessionTracker(source_id=source_id, ref_url=referrer, session_start=timezone.now(), ip_v4=ip, user_agent=user_agent, country_code=geoip.get('country').get('code'), city=geoip.get('city'), cookie=cookie_id, mktg_trck_id='', language_code='en-gb', session_owner=user_id)
        session.save()

        request.session['session_id'] = session.id

        # not yet used, but for longer logged in window:
        # request.session.set_expiry(5184000)

    def bot_check(self, request):
        bot = False

        try:
            cli_ip_v4=request.META['REMOTE_ADDR']
            bot_ipv4 = Bot.objects.exclude(ip_v4='')
            for ob in bot_ipv4:
                if cli_ip_v4.find(ob.ip_v4) > -1:
                    bot = True
                    return bot
        except:
            print("Bot checker: no ip")

        try:
            cli_ref = request.META['HTTP_USER_AGENT']
            bot_ref = Bot.objects.exclude(user_agent='')
            for ob in bot_ref:
                if cli_ref.find(ob.user_agent) > -1:
                    bot = True
                    return bot
        except KeyError:
            print("Bot checker: no user agent")

        return bot

    def get_source_id(self, request):
        source_id = None

        try:
            sid = request.GET['sourceid']
            try:
                source_id = SourceID.objects.get(pk=sid)
            except KeyError:
                source_id = SourceID.objects.get(pk=1)

        except:
            referrer = None
            try:
                referrer = request.META['HTTP_REFERER']
            except KeyError:
                referrer = "unknown"

            if not referrer == "unknown":
                implicit_sources = SourceID.objects.exclude(http_ref=None)
                for ob in implicit_sources:
                    if referrer.find(ob.http_ref) > -1:
                        source_id = ob
                if source_id == None:
                    source_id = SourceID.objects.get(pk=1)
            else:
                source_id = SourceID.objects.get(pk=22)

        request.session['source_id'] = source_id.id
        return source_id

    def is_current_session(self, request):
        lv = datetime.strptime(request.session.get('last_visit'), "%Y-%m-%d %H:%M:%S")
        td = (timezone.now() - timezone.make_aware(lv, timezone.get_default_timezone())).total_seconds()
        if td > 72000:
            return False
        else:
            return True


    #This one is somewhat outdated and is prone to cause lags.
    def getGeoIPXML(self, ip):
        geo_ip = {}

        try:
            url = "http://freegeoip.net/xml/" + ip
            print "Getting the GEO IP for: " + url
            f = urllib2.urlopen( url )
            tree = ET.ElementTree(file=f)
            address_element = tree.getroot()
            geo_ip = dict((e.tag, e.text) for e in address_element.getchildren())
        except:
            geo_ip = {'error':'Geo IP error'}
        return geo_ip


    def getGeoIPJSON(self, ip):
        url = "http://geoip.nekudo.com/api/" + ip + "/en/short"
        print("Getting the GEO IP for: " + url)
        f = urllib2.urlopen(url).read()
        json_data = json.loads(f)
        return json_data


    def process_request(self, request):
        ## Stuff that comes from the page meta
        return None

    def process_response(self, request, response):
        page_views = 0

        if not request.session.get('bot_check', False):
            is_bot = self.bot_check(request)
            request.session['bot_check'] = is_bot

        if request.session.get('bot_check') == False:

            try:
                cid = request.get_signed_cookie('cookie_id', salt=Secrets.salt)
                response.set_signed_cookie('cookie_id', cid, salt=Secrets.salt, max_age=5184000)
                response.set_signed_cookie('last_visit', datetime.strftime(timezone.now(), "%Y-%m-%d %H:%M:%S"), salt=Secrets.salt, max_age=5184000)
                cookie_id = CookieTracker.objects.get(pk=cid)

                if not request.session.get('session_id', False):
                    print("starting a new session")
                    self.set_session(request, cookie_id)
                    request.session['page_views'] = page_views

            except:
                source_id = self.get_source_id(request)
                cookie = CookieTracker(date_added=timezone.now(), source_id=source_id.id)
                cookie.save()
                response.set_signed_cookie('cookie_id', cookie.id, salt=Secrets.salt, max_age=5184000)
                response.set_signed_cookie('last_visit', datetime.strftime(timezone.now(), "%Y-%m-%d %H:%M:%S"), salt=Secrets.salt, max_age=5184000)
                print("Visitor isn't recognised, setting cookie: " + str(cookie.id))

                print("starting a new session")
                self.set_session(request, cookie)
                request.session['page_views'] = page_views

            ## Logging the page view:
            referrer = None
            try:
                referrer = request.META['HTTP_REFERER']
            except KeyError:
                referrer = "unknown"

            page_views = request.session.get('page_views')

            session = SessionTracker.objects.get(pk=request.session.get('session_id'))
            pv = PageTracker(session = session, time_stamp=timezone.now(), user_agent=request.META['HTTP_USER_AGENT'], ip_v4=request.META['REMOTE_ADDR'], ref_url=referrer, source_id=request.session.get('source_id'), page_count=page_views, curr_url=request.path)
            pv.save()

            request.session['page_views'] = int(page_views) +1

            if session.session_owner == None and request.user.is_authenticated:
                session.session_owner = request.user.id
                session.save()

            return response


        else:
            print("The session was identified to be a bot")
