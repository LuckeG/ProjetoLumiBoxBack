from rest_framework import viewsets, filters
from .models import Usuario
from .serializers import UsuarioSerializer
from django.shortcuts import render
from .services.tmdb import get_popular_movies, search_movie, get_popular_series, search_series, get_movie_genres, get_movies_by_genre, get_series_genres, get_series_by_genre
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny




class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class FilmesPopularesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        filmes = get_popular_movies()
        return Response(filmes)

class FilmesSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.GET.get('query')
        if not query:
            return Response({"error": "Parâmetro 'query' é obrigatório."}, status=400)
        
        filmes = search_movie(query)
        return Response(filmes)

class SeriesPopularesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        series = get_popular_series()
        return Response(series)

class SeriesSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.GET.get('query')
        if not query:
            return Response({"error": "Parâmetro 'query' é obrigatório."}, status=400)
        
        series = search_series(query)
        return Response(series)

class FilmesGenresView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        series = get_movie_genres()
        return Response(series)

class FilmesByGenreView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, genre_id):
        movies = get_movies_by_genre(genre_id)
        return Response(movies)

class SeriesGenresView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        genres = get_series_genres()
        return Response(genres)


class SeriesByGenreView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, genre_id):
        series = get_series_by_genre(genre_id)
        return Response(series)

# Create your views here.
def home(request):
    movies = get_popular_movies()
    return render(request, 'home.html', {'movies': movies})

def buscar_filme(request):
    query = request.GET.get('q')
    resultados = search_movie(query) if query else []
    return render(request, 'buscar.html', {'resultados': resultados})