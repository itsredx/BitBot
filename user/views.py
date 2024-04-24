from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'user/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_view')
    else:
        form = ProfileForm()
    return render(request, 'user/edit_profile.html', {'form': form})