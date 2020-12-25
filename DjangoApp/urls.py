"""
Definition of urls for DjangoApp.
"""

from datetime import datetime
from django.conf.urls import url
from app.forms import BootstrapAuthenticationForm
from app.views import *
from app.models import *
from django.contrib.auth.views import *

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^app/', include('app.urls', namespace='app')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', home, name='home'),
    url(r'^organization', organization, name='organization'),
    url(r'^figures', figures, name='figures'),
    url(r'^g_photos', g_photos, name='g_photos'),
    url(r'^g_videos', g_videos, name='g_videos'),
    url(r'^contact', contact, name='contact'),
    url(r'^events', events, name='events'),
    url(r'^googled6ad0f10bcbda8f2', googled6ad0f10bcbda8f2, name='googled6ad0f10bcbda8f2'),
    url(r'^login/$', login, {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$', logout, {  'next_page': '/'  },        name='logout')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
