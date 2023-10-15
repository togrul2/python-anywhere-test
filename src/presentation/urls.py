from django.urls import path

from presentation import views

app_name = "presentation"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about-us", views.AboutUs.as_view(), name="about-us"),
    path("faq", views.FAQView.as_view(), name="faq"),
    path("contact", views.ContactView.as_view(), name="contact"),
]
