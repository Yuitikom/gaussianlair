from django import forms
from home.models import Profile
from django.contrib.auth.models import User


class EditProfile(forms.ModelForm):
    ocupation = forms.CharField(max_length=255, required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(max_length=2500,required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    github_url = forms.CharField(max_length=255,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    twitter_url = forms.CharField(max_length=255,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    facebook_url = forms.CharField(max_length=255,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    instagram_url = forms.CharField(max_length=255,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['picture', 'bio', 'github_url', 'twitter_url', 'facebook_url',
                  'instagram_url',]


class EditUser(forms.ModelForm):
    first_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

