from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    """View to render homepage."""

    template_name = "presentation/index.html"


class AboutUs(TemplateView):
    template_name = "presentation/about.html"


class ServiceView(TemplateView):
    template_name = "presentation/service.html"


class ServiceDetailView(TemplateView):
    template_name = "presentation/service-details.html"


class BlogView(TemplateView):
    template_name = "presentation/blog.html"


class BlogDetailView(TemplateView):
    template_name = "presentation/blog-details.html"


class Pricing(TemplateView):
    template_name = "presentation/pricing.html"


class FAQView(TemplateView):
    template_name = "presentation/faq.html"


class ContactView(TemplateView):
    template_name = "presentation/contact.html"
