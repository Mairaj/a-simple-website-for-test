from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$','openerpwebsiteapp.views.home',name='home_urlname'),

#	url(r'base/^','openerpwebsiteapp.views.base',name='base_urlname'),
	url(r'^content/(?P<title>[a-zA-Z/]+)','openerpwebsiteapp.views.content',name='content_urlname'),
	url(r'^contactus/','openerpwebsiteapp.views.contactus',name='contactus_urlname'),

    # url(r'^$', 'openerpwebsite.views.home', name='home'),
    # url(r'^openerpwebsite/', include('openerpwebsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
)
