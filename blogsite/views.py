from django.views.generic import TemplateView, ListView, DetailView
from .models import Post, Reccommended_Book
from django.db.models import Q
# Create your views here.

class IndexView(TemplateView):
    template_name = 'blogsite/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-date')[:5]
        return context

class PostView(ListView):
    template_name = 'blogsite/posts.html'
    context_object_name = "posts"
    paginate_by = 5
    def get_queryset(self):
        return Post.objects.all().order_by('-date')
class PostDetailView(DetailView):
    template_name = 'blogsite/postview.html'
    model = Post
    context_object_name = 'post'
class BookView(ListView):
    template_name = 'blogsite/books.html'
    context_object_name = 'books'
    paginate_by = 8
    def get_queryset(self):
        return Reccommended_Book.objects.all()
class BookDetailView(DetailView):
    template_name = 'blogsite/bookview.html'
    model = Reccommended_Book
    context_object_name = 'book'
class AboutMeView(TemplateView):
    template_name='blogsite/aboutme.html'

class SearchView(ListView):
    template_name = 'blogsite/posts.html'
    context_object_name = "posts"
    paginate_by = 5
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            result = Post.objects.filter(Q(title__icontains=query))
        else:
            return []
        return result
