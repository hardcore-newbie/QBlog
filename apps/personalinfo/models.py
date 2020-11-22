import datetime
from django.db import models
from storage import OverwriteStorage

class MyInfo(models.Model):
	pen_name = models.CharField(max_length=128, default='unknown')
	name = models.CharField(max_length=128, default='unknown')
	idea = models.TextField(null=True, default=' ... ')
	birthday = models.DateField(auto_now_add=False, default=datetime.datetime.now)
	GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
	gender = models.CharField(max_length=64, default='Male', choices=GENDER_CHOICES)
	email = models.EmailField(max_length=64, default='example@iolala.com')
	qq = models.CharField(max_length=64, default='1234567890', verbose_name='QQ')
	github = models.CharField(max_length=255, default='https://github.com', null=True, verbose_name='GitHub')
	stackoverflow = models.CharField(max_length=255, default='http://', null=True, verbose_name='StackOverflow')
	avator_local = models.ImageField(upload_to='avator/', storage=OverwriteStorage(), null=True)
	avator_online = models.CharField(max_length=128, default='http://')
	avator_hyperlink = models.CharField(max_length=128, default='http://')
	is_use_local_avator = models.BooleanField(default=True)
	is_show_idea = models.BooleanField(default=True)
	is_show_qq = models.BooleanField(default=True)
	is_show_email = models.BooleanField(default=True)
	is_show_github = models.BooleanField(default=True)
	is_show_stackoverflow = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = 'ME'

	def __unicode__(self):
		return self.name

class MyWorks(models.Model):
	order_number = models.IntegerField(default=1)
	name = models.CharField(max_length=128, default='io')
	image_link = models.CharField(max_length=256, default='http://')
	homepage = models.CharField(max_length=256, default='http://www.iolala.com')
	desc = models.TextField(blank=True, default='This is a ...')
	keytech = models.TextField(blank=True, default='Python,Django,MySQL')

	class Meta:
		verbose_name_plural = 'Works'

	def __unicode__(self):
		return self.name

class MyDonates(models.Model):
	order_number = models.IntegerField(default=1)
	name = models.CharField(max_length=128, default='wechat')
	desc = models.TextField(blank=True, default='Donate ...')
	image_link = models.CharField(max_length=256, default='http://', verbose_name="QRCode link")

	class Meta:
		verbose_name_plural = 'Donates'

	def __unicode__(self):
		return self.name
