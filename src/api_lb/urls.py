from django.urls import include, path
from rest_framework import routers
from api_lb.views import UsuarioViewSet 
from .views import FilmesPopularesView, SeriesPopularesView, SeriesSearchView, FilmesSearchView, FilmesGenresView, FilmesByGenreView, SeriesGenresView, SeriesByGenreView

router = routers.DefaultRouter()

router.register(r'auth/user', UsuarioViewSet, basename='user')

urlpatterns = [
    path("", include(router.urls)),
    path('api/filmes/populares', FilmesPopularesView.as_view(), name='filmes-populares'),
    path('api/series/populares', SeriesPopularesView.as_view(), name='series-populares'),
    path('api/filmes/search/', FilmesSearchView.as_view(), name='filmes-search'),
    path('api/series/search/', SeriesSearchView.as_view(), name='series-search'),
    path('api/generos/filmes/', FilmesGenresView.as_view(), name='movie-genres'),
    path('api/generos/filmes/<int:genre_id>/', FilmesByGenreView.as_view(), name='movies-by-genre'),
    path('api/generos/series/', SeriesGenresView.as_view(), name='series-genres'),
    path('api/generos/series/<int:genre_id>/', SeriesByGenreView.as_view(), name='series-by-genre'),
    

]