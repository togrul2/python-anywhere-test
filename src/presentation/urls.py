from django.urls import path

from presentation import views

app_name = "presentation"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about-us", views.AboutUs.as_view(), name="about-us"),
    path("services", views.ServiceView.as_view(), name="service"),
    path("services/<int:pk>", views.ServiceDetailView.as_view(), name="service-detail"),
    # path("services/<slug:slug>", views.ServiceDetailView.as_view(), name="service-detail-slug"),
    path("blogs", views.BlogView.as_view(), name="blog"),
    path("blogs/<slug:slug>", views.BlogDetailView.as_view(), name="blog-detail"),
    path("pricing", views.Pricing.as_view(), name="pricing"),
    path("faq", views.FAQView.as_view(), name="faq"),
    path("contact", views.ContactView.as_view(), name="contact"),
]
