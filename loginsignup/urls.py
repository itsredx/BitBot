from django.urls import path, include
from .views import home, signup, signin, signout

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    #path('activate/<uidb64>/<token>', activate, name='activate'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    #path('accounts/', include('django.contrib.auth.urls')),
]