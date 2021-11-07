from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.views import generic


def reservation(request):
    movie_list = Movie.objects.order_by('id')
    context = {'movie_list': movie_list}
    return render(request, 'main/movie_reservation.html', context)


"""
FBV
"""
# def index(request):
#     """
#     Movie 목록 출력
#     """
#     movie_list = Movie.objects.order_by('id')
#     context = {'movie_list': movie_list}

#     # login_session = request.session.get('login_session', '')

#     # if login_session == '':
#     #     context['login_session'] = False
#     # else:
#     #     context['login_session'] = True

#     return render(request, 'main/movie_list.html', context)

"""
CBV
"""


class IndexView(generic.ListView):

    """
    Movie 목록 출력
    """
    template_name = 'main/movie_list.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        return Movie.objects.order_by('id')


# class DetailView(generic.DetailView):

#     """
#     Movie 내용 출력
#     """
#     model = Movie
#     template_name = 'main/movie_detail.html'

#     def get_object(self):

#         object = get_object_or_404(Movie, id=self.kwargs['id'])
#         return object
def detail(request, movie_id):
    """
    Movie 내용출력
    """

    movie = get_object_or_404(Movie, id=movie_id)
    context = {'Movie': movie}
    return render(request, 'main/movie_detail.html', context)
