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


@login_required(login_url='/accounts/login/')
def edit(request):
    profile = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/edit_profile.html', locals())

@login_required(login_url='/accounts/login/')
def newhood(request):
    if request.method == 'POST':
        hoodform = HoodForm(request.POST, request.FILES)
        if hoodform.is_valid():
            upload = hoodform.save(commit=False)
            upload.profile = request.user.profile
            upload.save()
            return redirect('home_page')
    else:
        hoodform = HoodForm()
    return render(request,'newhood.html',locals())


@login_required(login_url='/accounts/login')
def upload_business(request):
    hood = NeighborHood.objects.get(id=request.user.profile.neighborhood.id)
    if request.method == 'POST':
        businessform = BusinessForm(request.POST, request.FILES)
        if businessform.is_valid():
            upload = businessform.save(commit=False)
            upload.user=request.user
            upload.neighborHood=request.user.profile.neighborhood
            upload.save()
        return redirect('hood',request.user.profile.neighborhood.id)
    else:
        businessform = BusinessForm()
    return render(request,'Business.html',locals())


