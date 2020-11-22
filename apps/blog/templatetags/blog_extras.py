from django import template
from apps.blog.models import Category, Tag, Config

register = template.Library()

@register.inclusion_tag('blog/categories_list.html', takes_context=True)
def GetCategories(context):
	categories = Category.objects.order_by('-order_number')
	return {'categories':categories}

@register.inclusion_tag('blog/tags_cloud.html', takes_context=True)
def GetTags(context):
	tags = Tag.objects.all().order_by('?')
	return {'tags':tags}
	
@register.inclusion_tag('blog/copyright.html', takes_context=True)
def GetCopyright(context):
	try:
		copyright = Config.objects.get(title='copyright')
		return {'copyright':copyright}
	except Config.DoesNotExist:
		pass


