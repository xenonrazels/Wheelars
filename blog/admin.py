from django.contrib import admin
from .models import Blog,Comment
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=('id','title','author','status')
    list_filter=('title','status','publish')
    search_fields=('title','status','publish')
    list_editable=('status','title',)
    ordering=('-publish','id')
    prepopulated_fields={'slug':('title',)}
    data_hierarchy='publish'

admin.site.register(Blog,BlogAdmin)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('id','name','email','active')
    list_editable=('active',)
    search_fields=('id','name','email','active')
    list_display_links=('name','email')
