from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    #path('', views.post_list, name='post_list'),
    #path('/like/<int:pk>/', views.like_post, name='like_post'),
    #path('/comment/<int:pk>/', views.comment_on_post, name='comment_on_post'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)