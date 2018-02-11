from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post-<int:pk>/',views.PostView.as_view(), name='post-detail'),
    path('send-post/', views.SendView, name='send-post'),
]