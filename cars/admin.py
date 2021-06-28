from django.contrib import admin
from .models import car
from django.utils.html import format_html
# Register your models here.
@admin.register(car)
class CarAdmin(admin.ModelAdmin):
    def car_thumb(self, object):
        return format_html(f'<img src="{object.pic_front.url}" width="70px" style="border-radius:5px"/>')
    car_thumb.short_description = 'Car Photo'
    list_display = ('id','car_title','car_thumb', 'model', 'body_style', 'price', 'is_featured')
    list_display_links = ('car_thumb','id','car_title','model')
    list_filter = ('car_title','model','body_style','price', 'engine')
    search_fields = ('body_style','car_title', 'price','engine', 'description')
    list_editable = ('is_featured','price')
