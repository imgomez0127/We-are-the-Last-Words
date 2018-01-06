from django.views.generic import TemplateView
from .models import Post
# Create your views here.
class IndexView(TemplateView):
    template_name = 'blogsite/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-date')
        return context
