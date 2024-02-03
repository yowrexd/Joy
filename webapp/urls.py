from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('services/', views.services, name='services'),
    path('patient/', views.patient, name='patient'),
    path('form/', views.form, name='form'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact_page, name='contact_page'),
    
    path('navbar/', views.nav_bar, name='nav_bar'),
    path('footer/', views.footer, name='footer'),
    
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
