from django.shortcuts import render, get_object_or_404
from .models import Movie


def index(request):
    """
    Movie 목록 출력
    """

    movie_list = Movie.objects.order_by('-open_movie')
    context = {'movie_list': movie_list}
    return render(request, 'main/movie_list.html', context)


def detail(request, movie_id):
    """
    Movie 내용출력
    """

    movie = get_object_or_404(Movie, id=movie_id)
    context = {'Movie': movie}
    return render(request, 'main/movie_detail.html', context)
