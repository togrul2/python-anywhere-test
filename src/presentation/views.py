from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    """View to render homepage."""

    template_name = "presentation/index.html"
