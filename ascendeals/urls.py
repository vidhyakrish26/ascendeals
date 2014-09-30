from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalog/(?P<slug>[\w-]+)/$', 'catalogs.views.preview', name='catalog_preview'),
    url(r'^category/(?P<slug>[\w-]+)/$', 'catalogs.views.categoryview', name='category_view'),
    url(r'^$', 'products.views.home', name='product_home'),
)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)