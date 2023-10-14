from django.urls import path

from src.presentation import views

app_name = "presentation"

urlpatterns = [
    path("/", views.HomeView.as_view(), name="home"),
]
