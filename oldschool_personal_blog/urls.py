from django.urls import path
from .views import post_detail_view, post_list_view, create_post

app_name = 'blog'
urlpatterns = [
    # List of all posts ordered by creation-date
    path('post_list_view', post_list_view, name='post_list_view'),
    # Detailed view of post
    path('post/<int:post_id>/', post_detail_view, name='post_detail_view'),
    # Create post
    path('create/', create_post, name='create_post'),
    # Set landing page
    path('', post_list_view, name='post_list_view')
]
