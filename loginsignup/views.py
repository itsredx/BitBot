from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login



@login_required
def home(request):
    return render(request, "home.html", {})



def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username_or_email, email=username_or_email)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to your desired page after successful login
        else:
            # Handle invalid login attempt (e.g., display an error message)
            return render(request, 'registration/login.html', {'error': 'Invalid username or email/password'})
    return render(request, 'registration/login.html')


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or none)
        if form.is_valid():
            form.save()
    
    else:
        form = UserCreationForm()


    return render(request, "registration/signup.html", {"form": form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to login page after logout
    return render(request, 'logout.html')