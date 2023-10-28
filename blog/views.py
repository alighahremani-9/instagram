from django.shortcuts import render
from .models import Comment ,Post
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from .forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    # comments = comment.objects.all()
    return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, id):
    post_object = Post.objects.get(id=id)
    if request.method == "GET":
        return render(request, "blog/post_detail.html", {"post_from_view": post_object})
    elif request.method == "POST":
        user_name = request.POST["user_name"]
        body = request.POST["body"]
        comment = Comment.objects.create(user_name=user_name,body=body,post=post_object)
        comment.save()
        messages.add_message(request, messages.INFO, f"comment was saved successfully!")
        return redirect(reverse("index"))
    

def create_post(request):
    posts = Post.objects.all()
    if request.method == "GET":
        form = PostForm()
        return render(request, "blog/createpost.html", {"posts":posts ,"form":form})
    elif request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # ticket = Ticket.objects.create(**form.cleaned_data)
            # ticket.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, f"Your post Was created Successfuly !")
        else:
            messages.add_message(request, messages.ERROR, f"invalid argumentes!")

        return redirect(reverse("index"))


def post(request):
    return render(request,"blog/post.html",{})