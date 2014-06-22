from django.conf.urls import patterns, include, url
from cal import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.main, name="main"),
	url(r'^(?P<year>\d{4})$', views.main, name='year'),
	url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})$',views.month, name='month'),
	url(r'^month/(?P<day>\d{1,2})$',views.month, name='daily'),
	url(r'^cal/register/$', views.register, name='register'),
	url(r'^cal/login/$', views.user_login, name='login'),
	url(r'^cal/logout/$', views.user_logout, name='logout'),
)