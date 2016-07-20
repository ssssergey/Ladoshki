from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
import settings
from marketing.sitemap import SITEMAPS
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^', include('catalog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': SITEMAPS}),

]
