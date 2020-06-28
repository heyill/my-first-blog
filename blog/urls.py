from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    re_path(r'^post/\d+/about/$', views.about, name='site_about'),
    re_path(r'^post/\d+/edit/about/$', views.about, name='site_about'),
    path('post/new/about', views.about, name='site_about'),
    path('about', views.about, name='site_about'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
