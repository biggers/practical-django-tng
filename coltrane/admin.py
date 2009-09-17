from django.contrib import admin

from coltrane.models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }


admin.site.register(Category, CategoryAdmin)
