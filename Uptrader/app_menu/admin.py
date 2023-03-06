from django.contrib import admin
from .models import Menu, Category


# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'path', 'menu', 'slug')
    prepopulated_fields = {'slug': ('title',)}
