from django.urls import path, include
from .views import home, signUp, signIn, signOut, activate

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signUp, name='signup'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('signin/', signIn, name='signin'),
    path('signout/', signOut, name='signout'),
    #path('accounts/', include('django.contrib.auth.urls')),
]