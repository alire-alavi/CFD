from django.contrib import admin
from .models import Article, Category, UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'category', 'author']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','cover']