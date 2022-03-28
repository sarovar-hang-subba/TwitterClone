
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    #If the method is Post
    if request.method == 'POST':
       form = PostForm(request.POST)
      #If the form is valid
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
       else:
           return HttpResponseRedirect(form.errors.as_json())

    posts = Post.objects.all().order_by('-created_at') [:20]
    
    return render(request,'posts.html',{ 'posts': posts})


def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')
 

def like_post(request,post_id):
    like = Post.objects.get( id=post_id)
    like.likes += 1 
    like.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    posts = Post.objects.get(id=post_id)
    if request.method == "GET":
        posts = Post.objects.get(id=post_id)
        return render(request, "edit.html", {"posts": posts})
    if request.method == "POST":
        editposts = Post.objects.get(id=post_id)
        form = PostForm(request.POST, request.FILES, instance=editposts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
             return HttpResponse("not valid")