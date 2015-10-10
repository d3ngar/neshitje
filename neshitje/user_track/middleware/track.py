from datetime import datetime
from django.db import models
from django.utils import timezone
from user_track.models import PageTracker, SessionTracker, CookieTracker
import xml.etree.ElementTree as ET
import urllib2
import json

class UserSessionTracking(object):

    def is_current_session(self, request):
        lv = datetime.strptime(request.session.get('last_visit'), "%Y-%m-%d %H:%M:%S")
        td = (timezone.now() - timezone.make_aware(lv, timezone.get_default_timezone())).total_seconds()
        if td > 72000:
            return False
        else:
            return True


    def getGeoIPXML(self, ip):
        geo_ip = {}

        try:
            url = "http://freegeoip.net/xml/" + ip
            print url
            f = urllib2.urlopen( url )
            tree = ET.ElementTree(file=f)
            address_element = tree.getroot()
            geo_ip = dict((e.tag, e.text) for e in address_element.getchildren())
        except:
            geo_ip = {'error':'Geo IP error'}
        return geo_ip


    def getGeoIPJSON(self, ip):
        url = "http://geoip.nekudo.com/api/" + ip + "/en/short"
        f = urllib2.urlopen(url).read()
        json_data = json.loads(f)
        return json_data


    def process_request(self, request):
        ## Stuff that comes from the page meta

        ip = request.META['REMOTE_ADDR']

        print "=== Middleware User Session tracking executed ==="


        auth_user = None
        try:
            auth_user = request.user
        except KeyError:
            auth_user = "None"


        referrer = None
        try:
            referrer = request.META['HTTP_REFERER']
        except KeyError:
            referrer = ""


        print "Referrer: " + referrer
        print "Current URL " + request.path
        print "User Agent: " + request.META['HTTP_USER_AGENT']
        print "Client IP: " + ip
        print "Query String: " + request.META['QUERY_STRING']
        print "User: " + str(auth_user)
        print "Remote Host: " + request.META['REMOTE_HOST']


        ## Get things
        source_id = None
        try:
            source_id = request.GET['sourceid']
        except:
            source_id = 0
        print "Source ID: " + str(source_id)


        now = timezone.now()
        print "=== Trying some cookie stuff ==="
        if not request.session.get('cookie_id', False):
            print "no such cookie exists"
            cookie = CookieTracker (date_added=timezone.now())
            geoip = self.getGeoIPJSON(ip)
            print geoip
            cookie.save()
            request.session['cookie_id'] = cookie.id
            request.session['last_visit'] = datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
            request.session.set_expiry(5184000)
        else:
            print "Cookie id: " + str(request.session.get('cookie_id'))
            print str(self.is_current_session(request))
            print "Last visit ended: " + request.session.get('last_visit')
            request.session['last_visit'] = datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
            request.session.set_expiry(5184000)


        return None
