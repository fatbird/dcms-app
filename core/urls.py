from django.conf.urls import patterns, include, url
from dcms import urls

from core import views

from django.contrib import admin

from rest_framework import routers

router = routers.DefaultRouter()
router.register('content', views.Content)
router.register('log_entries', views.LogEntries)
router.register('images', views.Images)
router.register('users', views.Users)

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^api/', include(router.urls), name='api'),
    url(r'^dcms/', include(urls), name='api'),
    url(r'^$', views.Home.as_view(), name='home'),
]
