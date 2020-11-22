#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from collections import defaultdict
from collections import OrderedDict
from django.db.models import Count
import operator
from django.views.generic.detail import DetailView
from models import Article, Category, Tag, Config
from apps.personalinfo.models import MyInfo, MyWorks, MyDonates
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response, get_object_or_404
import urllib2

def PaginateArticles(articles, per_page, page_num):
    paginator = Paginator(articles, per_page)
    try:
        paging_articles = paginator.page(page_num)
    except PageNotAnInteger:
        paging_articles = paginator.page(1)
    except EmptyPage:
        paging_articles = paginator.page(paginator.num_pages)
    return paging_articles

def Home(req):
    static_page = req.get_full_path().split('/')[-1]
    suffix = static_page.split('.')[-1]
    if suffix == 'html' or suffix == 'htm':
        return render_to_response(static_page)
    articles = Article.objects.filter(is_publish=1).order_by('-create_date')
    articles = PaginateArticles(articles, 6, req.GET.get('page'))
    myinfo = ''
    try:
        myinfo = MyInfo.objects.order_by('id')[0]
    except IndexError:
        pass
    context = {'articles':articles, 'myinfo':myinfo, 'nbar':'index'}
    return render_to_response('blog/home.html', context)

def Works(req):
    # myworks = MyWorks.objects.order_by('-order_number')
    # context = {'works':myworks, 'nbar':'works'}
    # return render_to_response('blog/works.html', context)
    return "sjfld"

def Donates(req):
    mydonates = MyDonates.objects.order_by('-order_number')
    context = {'donates':mydonates, 'nbar':'donates'}
    return render_to_response('blog/donates.html', context)

def Me(req):
    myinfo = MyInfo.objects.order_by('id')[0]
    context = {'me':myinfo, 'nbar':'about'}
    return render_to_response('blog/me.html', context)

def Book(req):
    book = Config.objects.get(title='book')
    context = {'book':book, 'nbar':'book'}
    return render_to_response('blog/book.html', context)

def Activity(req):
    activity = Config.objects.get(title='activity')
    context = {'activity':activity, 'nbar':'activity'}
    return render_to_response('blog/activity.html', context)

def TagOverview(req):
    tags = Tag.objects.all()
    tag_table = dict()
    for tag in tags:
        tag_table[tag.id] = (tag.GetArticleNum(), tag.id, tag)
    order_table = sorted(tag_table.items(), key=operator.itemgetter(1, 1), reverse=True)
    context = {'tags':tags, 'order_table':order_table}
    return render_to_response('blog/tag_overview.html', context)

def CategoryOverview(req):
    categories = Category.objects.all()
    category_table = dict()
    for category in categories:
        category_table[category.id] = (category.GetArticleNum(), category.id, category)
    order_table = sorted(category_table.items(), key=operator.itemgetter(1, 1), reverse=True)
    context = {'categories':categories, 'order_table':order_table}
    return render_to_response('blog/category_overview.html', context)

def Archives(req):
    articles = Article.objects.filter(is_publish=1).order_by('-create_date')
    years = list()
    articles_by_year = defaultdict(list)
    year = articles[0].create_date.year
    years.append(year)
    for article in articles:
        cur_year = article.create_date.year
        articles_by_year[cur_year].append(article)
        if year != cur_year:
            year = cur_year
            years.append(year)

    archives = OrderedDict()
    for year in years:
        archives[year] = articles_by_year[year]

    context = {'archives':archives, 'nbar':'archives'}
    return render_to_response('blog/archives.html', context)

def ArticlesOfTag(req, slug):
    cur_tag = get_object_or_404(Tag, slug=slug)
    articles = Article.objects.filter(tag=cur_tag).filter(is_publish=1).order_by('-create_date')
    articles = PaginateArticles(articles, 6, req.GET.get('page'))
    myinfo = MyInfo.objects.order_by('id')[0]
    context = {'articles':articles, 'cur_tag':cur_tag, 'myinfo':myinfo, 'nbar':'tags_home'}
    return render_to_response('blog/articles_of_tag.html', context)

def ArticlesOfCategory(req, slug):
    cur_category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=cur_category).filter(is_publish=1).order_by('-create_date')
    articles = PaginateArticles(articles, 6, req.GET.get('page'))
    myinfo = MyInfo.objects.order_by('id')[0]
    context = {'articles':articles, 'cur_category':cur_category, 'myinfo':myinfo, 'nbar':'categories_home'}
    return render_to_response('blog/articles_of_category.html', context)

class ArticleDetail(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

def Error404(req):
    req_url = req.path_info
    context = {'req_url':req_url}
    return render_to_response('404.html', context)

def Error500(req):
    req_url = req.path_info
    context = {'req_url':req_url}
    return render_to_response('500.html', context)
