from .views import HomePageView
from django.urls import path

# Create your models here.
urlpatterns =[
    path('',HomePageView.as_view(),name='home'),
]
