from django.urls import path
from . import views

urlpatterns = [
    # path(URL_pattern, View_Function, Name_Reference)
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'), # <-- Add this line\
    path('project-detail/', views.projectdetail, name='project-detail'),
    path('project/', views.project, name='project'), # <-- Add this line
    path('service-detail/', views.servicedetail, name='service-detail'),
    path('single-post/', views.singlepost, name='single-post'), # <-- Add this line
    path('team/', views.team, name='team'), # <-- Add this line
    path('testimonial/', views.team, name='testimonial'), # <-- Add this line
    path('forforpage/', views.forforpage, name='forforpage'), # <-- Add this line
]

