from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    post_list = Post.objects.all()
    per_page = request.GET.get('per_page', 5)
    paginator = Paginator(post_list, per_page)  # Получаем количество постов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})
