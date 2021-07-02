from django.urls import path
from . import views


app_name='cars'
urlpatterns=[

    path('',views.cars,name='chome'),
    path('car_details/<int:id>', views.car_details, name='car_details'),
    path('search/',views.search,name='search'),

]