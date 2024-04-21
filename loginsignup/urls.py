from django.urls import path, include
from .views import authView, home

urlpatterns = [
    path('signup/', authView, name='authView'),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]