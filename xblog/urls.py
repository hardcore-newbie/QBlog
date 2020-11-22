from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from haystack.views import SearchView
from haystack.query import SearchQuerySet

sqs = SearchQuerySet().order_by('-create_date')

urlpatterns = [
	url(r'^adminfiles/', include('adminfiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^search/', SearchView(load_all=False, searchqueryset=sqs,), name='haystack_search',),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += url(r'^', include('apps.blog.urls')),

handler404 = 'apps.blog.views.Error404'
handler500 = 'apps.blog.views.Error500'
