from django.urls import path
from . import views

app_name = 'scrapeApp'
urlpatterns = [
    path('', views.home, name='home'),
]
