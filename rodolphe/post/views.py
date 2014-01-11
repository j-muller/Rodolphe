from django.shortcuts import render_to_response
from django.template import RequestContext
from post.models import Post
from post.forms import PostForm

# Create your views here.

def home(request):
    return page(request)

def page(request, page_id='1'):
    context = RequestContext(request, {
        'page': page_id,
        'posts': Post.objects.filter(parent=None),
        'form': PostForm()
    })
    return render_to_response('index.html', context)

def post(request, post_id):
    context = RequestContext(request, {
        'post': Post.objects.get(id=int(post_id), parent=None)
    })
    return render_to_response('post.html', context)

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, instance=Post.default())
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    context = RequestContext(request, {
        'form': form
    })
    return render_to_response('new.html', context)
