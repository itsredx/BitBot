from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=False)
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = ('bio', 'username', 'profile_picture')
        labels = {
            'bio': 'Bio',
            'username': 'Username',
            'profile_picture': 'Profile Picture'
        }