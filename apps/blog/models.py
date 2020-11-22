# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import Count, Max
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse

from django.db.models.signals import post_save
from django.contrib.auth.models import User

from apps.personalinfo.models import MyInfo

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='uploads/avatars', default='', blank=True)
    biography = models.TextField(default='', blank=True)

    def __unicode__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)

class Category(models.Model):
    order_number = models.IntegerField(default=1)
    name = models.CharField(max_length=255, null=False, unique=True)
    slug = models.SlugField(max_length=255, null=False, unique=True)
    description = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __unicode__(self):
        return self.name

    def GetArticleNum(self):
        return Article.objects.filter(category=self).filter(is_publish=True).count()
    
    def GetAbsoluteURL(self):
        return reverse('articles_of_category', kwargs={'slug':self.slug})

class Tag(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    slug = models.SlugField(max_length=128, null=False, unique=True)
    description = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = 'Tag'

    def __unicode__(self):
        return self.name
    
    def GetArticleNum(self):
        return Article.objects.filter(tag=self).count()
   
    def CalFontSizeOfTag(self):
        min_font_size = 11
        max_font_size = 35
        tag_ref_num = self.GetArticleNum()
        # query blog_article_tag table
        # select max(tag_ref_num) from(select count(*) as tag_ref_num from blog_article_tag group by tag_id) as max_ref_num;
        max_tag_num = Article.tag.through.objects.values('tag_id').annotate(tag_ref_num=Count('article')).aggregate(max_ref_num=Max('tag_ref_num'))['max_ref_num']
        if max_tag_num <= 0:
            tag_ref_num = 0
        return min_font_size + tag_ref_num * (max_font_size - min_font_size) / max_tag_num

    def GetAbsoluteURL(self):
        return reverse('articles_of_tag', kwargs={'slug':self.slug})

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=128, default='anonymous', editable=False)
    create_date = models.DateTimeField(auto_now_add=False)
    modify_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)
    text = MarkdownField(null=True)
    is_publish = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True)
    truncatewords_num = models.SmallIntegerField(default=20)

    class Meta:
        verbose_name_plural = 'Article'

    def __unicode__(self):
        return self.title

    def GetTags(self):
        # get all Tag objects for this Article.
        return Article.objects.get(id=self.id).tag.all()

    def GetCategory(self):
        return Article.objects.get(id=self.id).category

    def GetAbsoluteURL(self):
        return reverse('article', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        self.author = MyInfo.objects.order_by('id')[0].pen_name
        super(Article, self).save(*args, **kwargs)
        return;

class Config(models.Model):
    title = models.CharField(max_length=255)
    text = MarkdownField(null=True)

    def __unicode__(self):
        return self.title

class Wiki(models.Model):
    title = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='', blank=False)

    class Meta:
        verbose_name_plural = 'Wiki'

    def __unicode__(self):
        return self.title
