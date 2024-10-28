# urls.py
from django.contrib import admin
from django.urls import path
from blog.views import create_blog_post, edit_blog_post, delete_blog_post, blog_list

urlpatterns = [
    path('',create_blog_post, name='create-blog'),
    path('api/edit<int:post_id>/', edit_blog_post, name='edit-blog'),
    path('api/delete<int:post_id>/', delete_blog_post, name='delete-blog'),
    path('api/bloglist', blog_list, name='blog-list'),  # Blog listing view
]
