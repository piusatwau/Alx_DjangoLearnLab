from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.views import View

# Create your views here.

# FUNCTION BASED VIEWS
def blog_post_list(request):
    if request.method == 'GET':
        blog_posts=BlogPost.objects.all()
        return render(request, 'posts/blog_post_list.html', {'blog_posts': blog_posts})
    elif request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        new_post = BlogPost.objects.create(title=title, content=content)
        new_post.save()
        return redirect('blog-post-list')

# CLASS BASED VIEWS

class BlogPostView(View):
    def get(self, request, *args, **kwargs):
        # Use case: Display a list of all blog posts
        blog_posts_cbv = BlogPost.objects.all()
        return render(request, 'posts/blog_post_list_cbv.html', {'blog_posts_cbv': blog_posts_cbv})

    def post(self, request, *args, **kwargs):
        # Use case: Create a new blog post
        title = request.POST['title']
        content = request.POST['content']
        new_post = BlogPost.objects.create(title=title, content=content)
        new_post.save()
        return redirect('blog-post-list-cbv')

    def put(self, request, *args, **kwargs):
        # Use case: Update a blog post
        post_id = kwargs['post_id']
        post = get_object_or_404(BlogPost, id=post_id)
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('blog-post-list-cbv')

    def delete(self, request, *args, **kwargs):
        # Use case: Delete a blog post
        post_id = kwargs['post_id']
        post = get_object_or_404(BlogPost, id=post_id)
        post.delete()
        return redirect('blog-post-list-cbv')