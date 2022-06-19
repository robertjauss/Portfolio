from django.views import generic


class HomeView(generic.TemplateView):
    """
    Home Page
    """
    template_name = "home.html"


class AboutView(generic.TemplateView):
    """
    About Me page
    """
    template_name = "about.html"


class ResumeView(generic.TemplateView):
    """
    My Resume
    """
    template_name = "resume.html"


class ProjectsView(generic.TemplateView):
    """
    My noteworthy projects
    """
    template_name = "projects.html"
