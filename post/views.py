from django.shortcuts import render, redirect
from .models import Post, Comment, Like
from django.http import HttpResponse, JsonResponse

def all_posts(request):
  posts = Post.objects.all().order_by('-timestamp')

  if request.method == 'POST':
    post_id = request.POST.get('like_post_id')
    comment_text = request.POST.get('comment_text')

    if post_id:  # Handle like functionality
      post = Post.objects.get(pk=post_id)
      if not Like.objects.filter(post=post, user=request.user).exists():
        like = Like.objects.create(post=post, user=request.user)
        like_count = post.like_set.count()
        return JsonResponse({'success': True, 'like_count': like_count})
      else:
        return JsonResponse({'success': False})  # Already liked

    if comment_text:  # Handle comment functionality
      post_id = request.POST.get('comment_post_id')
      post = Post.objects.get(pk=post_id)
      comment = Comment.objects.create(post=post, user=request.user, content=comment_text)
      return JsonResponse({'success': True, 'username': request.user.username})
    else:
      return JsonResponse({'success': False})  # Empty comment

  context = {'posts': posts}
  return render(request, 'post/post_list.html', context)

