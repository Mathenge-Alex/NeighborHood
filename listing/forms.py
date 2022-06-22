from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Business,Profile,NeighborHood,Post,Business,Comment

    # Forms
        
class HoodForm(forms.ModelForm):
    class Meta:
        model = NeighborHood
        exclude= ['occupants']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','profile','neighborHood']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','neighborhood','business']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','neighborHood','pub_date']

