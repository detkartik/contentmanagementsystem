from django.contrib import admin
from .models import Content,Category
# Register your models here.
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    # fields = ['title', 'description', 'price',
    #           'published', 'is_published', 'cover']
    list_display = ['title', 'body', 'summary', 'document']
    list_filter = ['title', 'document', 'category']
    search_fields = ['title']
admin.site.register(Category)

