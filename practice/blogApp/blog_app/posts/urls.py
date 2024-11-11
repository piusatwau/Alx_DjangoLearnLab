from django.urls import path
from . import views
from .views import BlogPostView

urlpatterns = [
    path('blog/', views.blog_post_list, name='blog-post-list'),
    path('blogcbv/', BlogPostView.as_view(), name='blog-post-list-cbv'),
    path('blog/create/', BlogPostView.as_view(), name='blog-post-create'),
    path('blog/update/<int:post_id>/', BlogPostView.as_view(), name='blog-post-update'),
    path('blog/delete/<int:post_id>/', BlogPostView.as_view(), name='blog-post-delete'),
]

