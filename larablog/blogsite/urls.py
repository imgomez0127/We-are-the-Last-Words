from django.conf.urls import url
from . import views
app_name = "blogsite"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^all-posts/$', views.PostView.as_view(), name='posts'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post-view'),
    url(r'all-books/$', views.BookView.as_view(), name='books')
]