from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm

# Create a new blog post
from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

def create_blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('blog_list')  # Redirect to blog list or another page
    else:
        form = BlogPostForm()
    return render(request, 'create_blog.html', {'form': form})



# Edit a blog post
def edit_blog_post(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'blog/edit_blog.html', {'form': form})


# Delete a blog post
def delete_blog_post(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        blog_post.delete()
        return redirect('blog_list')
    return render(request, 'blog/delete_blog.html', {'blog_post': blog_post})

# views.py
def blog_list(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'blog_posts': blog_posts})
