from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^article/(?P<slug>\S+)/$', views.ArticleDetail.as_view(), name='article_ex'),
    url(r'^article/(?P<slug>\S+)$', views.ArticleDetail.as_view(), name='article'),
    url(r'^category/(?P<slug>[-\w]+)/$', views.ArticlesOfCategory, name='articles_of_category'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.ArticlesOfTag, name='articles_of_tag'),
    url(r'^tag$', views.TagOverview, name='tag_overview'),
    url(r'^category$', views.CategoryOverview, name='category_overview'),
    url(r'^$', views.Home, name='home'),
    url(r'^archives$', views.Archives, name='archives'),
    url(r'^works$', views.Works, name='works'),
    url(r'^donates$', views.Donates, name='donates'),
    url(r'^me$', views.Me, name='me'),
    url(r'^book/', views.Book, name='book'),
    url(r'^activity/', views.Activity, name='activity'),
    url(r'^proxy/$', views.Proxy, name='proxy'),
    url(r'^wiki$', views.WK, name='wiki'),
    url(r'^wiki/', views.WikiQueryOrDetail, name='wiki_query'),
)
