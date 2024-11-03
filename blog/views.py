from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Follow

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        if len(title) >= 5 and len(description) >= 25:
            Post.objects.create(author=request.user, title=title, description=description, image=image)
            return redirect('home')
        else:
            error_message = "Title must be at least 5 characters and description at least 25 characters."
            return render(request, 'create_post.html', {'error_message': error_message})

    return render(request, 'create_post.html')

def home(request):
    if request.user.is_authenticated:
        followed_users = request.user.following.values_list('following', flat=True)
        posts = Post.objects.filter(author__in=followed_users)
    else:
        posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'all_posts.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})
