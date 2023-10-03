from django.shortcuts import render
from .models import comment

# Create your views here.

def index(request):
    comments = comment.objects.all()
    return render(request, "blog/index.html", {"comments":comments})

def post_detail(request, id):
    comments = [comment.objects.get(id=id)]
    return render(request, "blog/index.html", {"comments":comments})