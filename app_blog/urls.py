from django.urls import path
from .views import BlogListView, BlogDetailView
from .views import AboutPageView

urlpatterns = [
path("about/",AboutPageView.as_view(),name="about"),
path("post/<int:pk>/",BlogDetailView.as_view(), name="post_detail"),
path("",BlogListView.as_view(),name="home"),
]
