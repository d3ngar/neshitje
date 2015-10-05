from django.contrib import admin

# Register your models here.
from .models import SourceID, CookieTracker, SessionTracker, PageTracker

class SourceIDAdmin(admin.ModelAdmin):
    list_display = ['source_name', 'http_ref', 'date_added', 'status', 'status_changed']
    class Meta:
        model = SourceID

class CookieTrackerAdmin(admin.ModelAdmin):
    list_display = ['source', 'date_added']
    class Meta:
        model = CookieTracker

class SessionTrackerAdmin(admin.ModelAdmin):
    class Meta:
        model = SessionTracker

class PageTrackerAdmin(admin.ModelAdmin):
    class Meta:
        model = PageTracker

admin.site.register(SourceID, SourceIDAdmin)
admin.site.register(CookieTracker, CookieTrackerAdmin)
admin.site.register(SessionTracker, SessionTrackerAdmin)
admin.site.register(PageTracker, PageTrackerAdmin)
