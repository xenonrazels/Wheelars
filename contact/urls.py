from django.urls import path
from . import views
app_name='contact'

urlpatterns=[
    path('inquery',views.inquery,name='inquery'),
]