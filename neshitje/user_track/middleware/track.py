from datetime import datetime
from django.db import models
from django.utils import timezone
from user_track.models import PageTracker, SessionTracker, CookieTracker

class UserSessionTracking(object):

    def is_current_session(self, request):
        lv = datetime.strptime(request.session.get('last_visit'), "%Y-%m-%d %H:%M:%S")
        td = (timezone.now() - timezone.make_aware(lv, timezone.get_default_timezone())).total_seconds()
        if td > 72000:
            return False
        else:
            return True


    def process_request(self, request):
        ## Stuff that comes from the page meta

        print "=== Middleware User Session tracking executed ==="

        auth_user = None
        try:
            auth_user = request.META['REMOTE_USER']
        except KeyError:
            auth_user = "None"

        referrer = None
        try:
            referrer = request.META['HTTP_REFERER']
        except KeyError:
            referrer = ""


        print "Referrer: " + referrer
        print "User Agent: " + request.META['HTTP_USER_AGENT']
        print "Client IP: " + request.META['REMOTE_ADDR']
        print "Query String: " + request.META['QUERY_STRING']
        print "User: " + auth_user
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
