from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.
def blog(request):
    return render_to_response('blog/main.html')

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    template = 'blog/detail.html'
    context = {'post': post}
    return render(request, template, context)

def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.post = post
            entry.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    template = "blog/comment.html"
    context = {'form':form}
    return render(request, template, context)