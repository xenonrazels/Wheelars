from django.contrib import admin
from .models import Inquery
# Register your models here.
@admin.register(Inquery)
class InqueryAdmin(admin.ModelAdmin):
    list_display = ('first_name','email','last_name','phone','car_id','user_id')
    list_filter = ('car_id','first_name','email','last_name')
