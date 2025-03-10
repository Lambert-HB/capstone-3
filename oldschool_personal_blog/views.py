from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost


# Create a new blog post
def create_post(request):
    # Check if method is POST
    if request.method == 'POST':
        # Retrieve post title and text from request
        post_title = request.POST.get('post_title')
        post_text = request.POST.get('post_text')

        # Check if both title and text were provided
        if post_title and post_text:
            # Create BlogPost object from request
            post = BlogPost(author=request.user,
                            post_title=post_title,
                            post_text=post_text)
            # Save post to BlogPost objects
            post.save()
            # Redirect to list view of posts
            return redirect('blog:post_list_view')
    # Render create post template
    return render(request, 'create_post.html')


# List view of all posts
def post_list_view(request):
    # Create a list of BlogPost objects ordered by creation time
    post_list = BlogPost.objects.all().order_by('-created_at')
    # Render template for list view of posts
    return render(request, 'post_list_view.html', {'post_list': post_list})


# Detailed view of specified post
def post_detail_view(request, post_id):
    # Find BlogPost object by post_id as primary key or return 404 error
    post = get_object_or_404(BlogPost, pk=post_id)
    # Render template for detailed view of post
    return render(request, 'post_detail_view.html', {'post': post})
