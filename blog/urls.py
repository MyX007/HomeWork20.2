from django.urls import path

from blog.views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, \
    toggle_is_published, PostArchiveListView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('', PostListView.as_view(), name='list'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit'),
    path('view/<int:pk>/', PostDetailView.as_view(), name='view'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    path('is_published/<int:pk>', toggle_is_published, name='is_published'),
    path('archive/', PostArchiveListView.as_view(), name='archive'),

]

