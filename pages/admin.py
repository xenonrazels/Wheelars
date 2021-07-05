from django.contrib import admin
from  .models   import Team,Contact
from django.utils.html import format_html
# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def photo(self, object):
        return format_html(f'<img src="{object.profile_img.url}" width="40px" style="border-radius:10px"/>')
    # photo.short_description = 'Photo'
    list_display_links = ('id','first_name','last_name',)
    list_filter = ('first_name','last_name','designation')
    search_fields = ('email','designation','first_name','last_name')
    list_display = ('id','first_name','last_name','photo','email','designation')
    ordering = ('id',)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','subject')