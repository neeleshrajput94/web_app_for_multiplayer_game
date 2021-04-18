from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),

    path('services/',views.services_page, name = "services"),
    path('gallery/', views.gallery_page, name = "gallery"),
    path('about/', views.about_page, name = "about"),
    path('contact/', views.contact_page, name = "contact"),
]