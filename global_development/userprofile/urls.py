from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^$', 'userprofile.views.dashboard_overview'),
        url(r'^welcome/$', 'userprofile.views.dashboard_welcome'),
        url(r'^profile/$', 'userprofile.views.profile', name='profile'),
        url(r'^profile/edit/$', 'userprofile.views.edit_profile', name='edit_profile'),
        url(r'^map/$', 'userprofile.views.dashboard_map', name='map'),
        url(r'^resources/$', 'userprofile.views.dashboard_resources'),
        url(r'^help/$', 'userprofile.views.help_home'),
)
