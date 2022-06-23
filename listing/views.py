from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Profile,User,Post,Business,NeighborHood,Comment
from django.contrib.auth.models import User
import datetime as dt
from .forms import BusinessForm,ProfileForm,HoodForm,PostForm,CommentForm

# Create your views here.


def home_page(request):
    date = dt.date.today()
    hoods = NeighborHood.objects.all()
    return render(request,'home.html',locals())

