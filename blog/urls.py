from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-posts/', views.all_posts, name='all_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('create-post/', views.create_post, name='create_post'),
]
