from django.urls import path
from . import views

app_name='blog'
urlpatterns=[
    path('',views.blogs,name='blogs'),
    # path('',views.BlogListView.as_view(),name='blogs'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>',views.blog_detail,name="blog_detail"),
    path('<int:blog_id>/share', views.blog_share, name='blog_share'),
    path('create_blog/',views.create,name='create_blog'),
    path('tag/<slug:tag_slug>',views.blogs,name='blog_list_by_tag')


]