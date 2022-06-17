from django.views import generic


class HomeView(generic.TemplateView):
    """
    Home Page
    """
    template_name = "home.html"
