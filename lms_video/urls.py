from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categories_list, name='categories-list'),
    path('classes-rank/', views.classes_rank_list, name='classes-rank-list'),
    path('subjects/', views.subjects_list, name='subjects-list'),
    path('authors/', views.authors_list, name='authors-list'),
    path('videos/', views.video_list, name='videos-list'),
    path('videos/<int:pk>/', views.video_detail, name='video-detail'),
    path('subscribe/', views.subscribe_list, name='subscribe-list'),
    path('create-subscription/', views.create_subscription_request, name='create-subscription'),
    path('subcategories/', views.list_subcategories, name='subcategories'),
]
