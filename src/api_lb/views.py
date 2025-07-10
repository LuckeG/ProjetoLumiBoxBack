from rest_framework import viewsets, filters
from .models import Usuario
from .serializers import UsuarioSerializer
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .services.tmdb import get_popular_movies, search_movie, get_popular_series, search_series, get_movie_genres, get_movies_by_genre, get_series_genres, get_series_by_genre, get_animes, get_reality_shows, get_movie_details, get_serie_details
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class FilmesPopularesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        page = int(request.GET.get('page', 1))
        filmes = get_popular_movies(page)
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
        page = int(request.GET.get('page', 1))
        series = get_popular_series(page)
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

class AnimesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        animes = get_animes()
        return Response(animes)

class RealitiesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        realities = get_reality_shows()
        return Response(realities)

class FilmeDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, movie_id):
        detalhes = get_movie_details(movie_id)
        if detalhes: 
            return Response(detalhes)
        return Response({"error": "Filme não encontrado"}, status=status.HTTP_404_NOT_FOUND)

class SerieDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, serie_id):
        detalhes = get_serie_details(serie_id)
        if detalhes:
            return Response(detalhes)
        return Response({"error": "Série não encontrada"}, status=staruus.HTTP_404_NOT_FOUND)

User = get_user_model()

class alterarSenha(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("Dados recebidos no backend:", request.data)
        username = request.data.get('username')
        novaSenha = request.data.get('novaSenha')
        confirmarSenha = request.data.get('confirmarSenha')

        if not username or not novaSenha:
            return Response({'error': 'Usuário e nova senha são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

        if novaSenha != confirmarSenha:
            return Response({'error': 'As senhas não coincidem.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        user.set_password(novaSenha)
        user.save()

        return Response({'message': 'Senha alterada com sucesso.'}, status=status.HTTP_200_OK)




# Create your views here.
def home(request):
    movies = get_popular_movies()
    return render(request, 'home.html', {'movies': movies})

def buscar_filme(request):
    query = request.GET.get('q')
    resultados = search_movie(query) if query else []
    return render(request, 'buscar.html', {'resultados': resultados})






