from django.conf.urls import patterns, include, url
from registration.forms import RegistrationFormUniqueEmail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    # baseapp
    url(r'^', include('baseapp.urls')),
    # registration app
    url(r'^accounts/register/$', 'registration.views.register',
        {'form_class': RegistrationFormUniqueEmail,
         'backend': 'registration.backends.default.DefaultBackend'},       
         name='registration_register'),            
    url(r'^accounts/', include('registration.backends.default.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
