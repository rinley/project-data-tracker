from django.conf.urls import patterns, include, url
from guestbook import views as gbviews
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('pdt.urls')),
    url(r'^guestbook/$', gbviews.index),
    url(r'^guestbook/add/$', gbviews.add),
    url(r'^admin/', include(admin.site.urls)),
)