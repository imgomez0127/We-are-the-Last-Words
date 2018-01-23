from django.conf.urls import url
from . import views
app_name = "blogsite"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^all-posts/$', views.PostView.as_view(), name='posts'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post-view'),
    url(r'all-books/$', views.BookView.as_view(), name='books'),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BookDetailView.as_view(), name='book-view'),
    url(r'^about-me/$', views.AboutMeView.as_view(), name='about-me'),
    url(r'^search/$', views.SearchView.as_view(), name='search-view')
]