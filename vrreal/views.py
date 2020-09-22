from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'home/index.html'
    
class Video(TemplateView):
    template_name='build/vrvideo.html'