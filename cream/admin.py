from django.contrib import admin

from feincms.admin import editor

from cream.models import Category


class CategoryAdmin(editor.TreeEditor):
    list_display = ('name', 'slug')
    list_filter = ('parent',)
    prepopulated_fields = {
        'slug': ('name',),
        }

admin.site.register(Category, CategoryAdmin)
