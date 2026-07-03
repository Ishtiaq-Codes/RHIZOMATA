from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('how-to-play/', views.how_to_play, name='how_to_play'),
    path('preview/', views.preview, name='preview'),
    path('order/', views.order, name='order'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]
