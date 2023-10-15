from django.views.generic import TemplateView


class HomeView(TemplateView):
    """View to render homepage."""

    template_name = "presentation/index.html"


class AboutUs(TemplateView):
    template_name = "presentation/about.html"


class FAQView(TemplateView):
    template_name = "presentation/faq.html"


class ContactView(TemplateView):
    template_name = "presentation/contact.html"


class MapView(TemplateView):
    template_name = "presentation/map/map.html"
