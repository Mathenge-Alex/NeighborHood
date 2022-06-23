from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Business,Profile,NeighborHood,Post,Business,Comment

    # Form

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','neighborhood','business']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','profile','neighborHood']


class HoodForm(forms.ModelForm):
    class Meta:
        model = NeighborHood
        exclude= ['occupants']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','neighborHood','pub_date']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']