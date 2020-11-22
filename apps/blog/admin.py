from django.contrib import admin
from django.contrib.sites.models import Site
from adminfiles.admin import FilePickerAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from models import Article, Category, Tag, Config, Wiki, UserProfile

class ProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'
    max_num = 1

class PostAdmin(FilePickerAdmin):
	adminfiles_fields = ('text',)

class CustomUserAdmin(UserAdmin):
	inlines = [ProfileInline,]

class MyAdmin(admin.ModelAdmin):
	list_display = ("username", "first_name", "email",)
	fieldsets = (
        (None, {
            'fields': ('username',)
        }),
        ('Advanced options', {
            #'classes': ('collapse',),
            'fields': ("first_name", "email",)
        }),
    )
	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj=None):
		return False

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Wiki)
admin.site.register(Article, PostAdmin)
admin.site.register(Config, PostAdmin)

#admin.site.register(User, CustomUserAdmin)
admin.site.register(User, MyAdmin)
