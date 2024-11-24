from django.db.models.expressions import result
from django.shortcuts import render, redirect
from django.template.defaultfilters import title
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from viewer.forms import MovieForm
from viewer.mixins import StaffRequiredMixin
from viewer.models import Movie, Genre, Actor


# Create your views here.
# class MoviesView(View):
#     def get(self, request):
#         return render(request, template_name='movies.html',
#                       context={'movies': Movie.objects.all()})

# class MoviesView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {'movies': Movie.objects.all()}

def index(request):
    return redirect('/movies')


# CRUD: Create, Read, Update, Delete
# Read - folosim HTTP GET
# Create, Update, Delete - folosim HTTP POST

class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie

class MoviesViewDetail(PermissionRequiredMixin, DetailView):
    template_name = 'movies_detail.html'
    model = Movie

    # pentru numele permisiunilor: '<nume-app>.<actiuni>_<nume-model>'
    permission_required = 'viewer.view_movie'

class GenreMoviesView(ListView):
    template_name = 'movies.html'
    model = Movie

    def get_queryset(self):
        qs = super().get_queryset()
        genre = Genre.objects.get(name=self.kwargs['genre_name'])
        return qs.filter(genre=genre)


class ActorDetailView(DetailView):
    template_name = 'actor_detail.html'
    model = Actor


class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = MovieForm
    permission_required = 'viewer.add_movie'

    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     cleaned_data = form.cleaned_data
    #     Movie.objects.create(
    #         title = cleaned_data['title'],
    #         genre=cleaned_data['genre'],
    #         rating=cleaned_data['rating'],
    #         released=cleaned_data['released'],
    #         description=cleaned_data['description']
    #     )
    #     return result

    def form_invalid(self, form):
        print('User provided invalid data')
        return super().form_invalid(form)

class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movie-list')
    permission_required = 'viewer.change_movie'

    def form_invalid(self, form):
        print('User provided invalid data')
        return super().form_invalid(form)

class MovieDeleteView(StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('movie-list')
    permission_required = 'viewer.delete_movie'
