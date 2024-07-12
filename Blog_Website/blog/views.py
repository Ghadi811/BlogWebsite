
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import User
from .models import Post
from .models import Comment
from .models import Category

def myusers(request):
    myusers = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))

def mypost(request):
    myposts = Post.objects.all().values()
    template = loader.get_template('blogs.html')
    context = {
        'myposts': myposts,
    }
    return HttpResponse(template.render(context, request))

def blogdetails(request, id):
    mypost = get_object_or_404(Post, id=id)
    context = {
        'myposts': mypost,
    }
    return render(request, 'blogdetails.html', context)

def mycomment(request, id):
    mypost = get_object_or_404(Post, id=id)
    mycomments = Comment.objects.filter(post=mypost)
    context = {
        'myposts': mypost,
        'mycomments': mycomments,
    }
    return render(request, 'comments.html', context)

#def mycomment(request,id):
   # myposts = Post.objects.get(id=id)
    #mycomments = Comment.objects.filter(Post=myposts.pk)
    #template = loader.get_template('comments.html')
    #context = {
    #   'myposts':myposts,
    #   'mycomments': mycomments,
    #}
    #return HttpResponse(template.render(context, request))

def mycategory(request):
    mycategory = Category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'mycategory': mycategory,
    }
    return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

