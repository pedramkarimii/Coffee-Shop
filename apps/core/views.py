from django.views.generic import TemplateView
# Create your views here.


class AboutUsView(TemplateView):
    """
    Displays the about us page.
    """
    template_name = 'about/about_coffe.html'
