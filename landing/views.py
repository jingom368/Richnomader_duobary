from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

from landing.models import Post


def base(request):
    return render(request, "base.html")

def duobary(request):
    return render (request, "landing/duobary.html")

def detail(request):
    return render(request, "landing/detail.html")

def landing_index(request):
    return render(request, "landing/landing_index.html")

def landing_post_create(request):
    if request.method == "GET":
        return render(request, "landing/create.html")
    elif request.method == "POST":
        new_post = Post()
        new_post.title = request.POST["title"]
        new_post.content = request.POST["content"]
        if request.FILES.get("image"):
            new_post.head_image = request.FILES["image"]
        new_post.save()
        return HttpResponseRedirect(reverse("landing:create"))

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

def landing_test(request):
    context = {
		"weather_data": {
			"weather": "흐림",
			"temperature": "3",
	},
    "top_average": [  # Dictionary로 이루어진 List 입니다.
        {
            "name": "이정후",
            "average": 0.347
        }, {
            "name": "강백호",
            "average": 0.347,
        }, {
            "name": "전준우",
            "average": 0.347
        }
		]
}
    return render(request, "landing/test.html", context)