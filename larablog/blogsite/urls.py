from django.conf.urls import url
from . import views
app_name = "blogsite"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^all-posts/$', views.PostView.as_view(), name='posts')
]