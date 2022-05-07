import re
from urllib import request
from django.shortcuts import render

from django.http import HttpResponseRedirect
from landing.models import Post

def detail(request):
    return render(request, "landing/detail.html")

def landing_post_create(request):
    if request.method == "GET":
        return render(request, "landing/create.html")
    elif request.method == "POST":
        new_post = Post()
        new_post.title = request.POST["title"]
        new_post.content = request.POST["content"]
        new_post.save()
        return HttpResponseRedirect("/landing/create/")

def landing_home(request):
    post_list = Post.objects.all().order_by("-pk")
    context = {
        "post_list": post_list
    }
    return render(request, "landing/read.html", context)

def landing_post_read(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post": post
    }
    return render(request, "landing/post.html", context)

def landing_post_update(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(pk=post_id)
        context = {
            "post": post
        }
        return render(request, "landing/update.html", context)
    elif request.method == "POST":
        post = Post.objects.get(pk=post_id)
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.save()
        return HttpResponseRedirect(f"/landing/post-read/{post_id}/")

def landing_post_delete(request, post_id):
    target_post = Post.objects.get(pk=post_id)
    target_post.delete()
    return HttpResponseRedirect("/landing/home/")

def landing_post_collect(request):
    if request.method == "GET":
        return render(request, "landing/detail.html")
    if request.method == "POST":
        new_post = Post()
        new_post.phonenumber = request.POST["phonenumber"]
        new_post.read_book = request.POST["read_book"]
        new_post.save()
        return HttpResponseRedirect("/landing/detail/")