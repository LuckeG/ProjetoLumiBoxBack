from rest_framework import viewsets, filters, generics, permissions
from .models import Indicacao, Usuario, ListaUsuario
from .serializers import DjangoUserSerializer, IndicacaoSerializer, ListaUsuarioSerializer
from django.shortcuts import render
from .services.tmdb import get_popular_movies, search_movie, get_popular_series, search_series, get_movie_genres, get_movies_by_genre, get_series_genres, get_series_by_genre, get_animes, get_reality_shows, get_movie_details, get_serie_details
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.parsers import MultiPartParser, FormParser

User = get_user_model()


class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = DjangoUserSerializer

class BuscarUsuariosView(generics.ListAPIView):
    serializer_class = DjangoUserSerializer
    permission_classes = [permissions.AllowAny]  # ou outra permissão adequada

    def get_queryset(self):
        nome = self.request.query_params.get('nome', '')
        if len(nome) < 2:
            return User.objects.none()
        return User.objects.filter(username__icontains=nome)[:10]

class IndicacaoCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Indicacao.objects.all()
    serializer_class = IndicacaoSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("Erro de validação:", serializer.errors)  # Debug aqui
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class IndicacoesParaUsuarioView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        indicacoes = Indicacao.objects.filter(usuario_destino=request.user)

        data = []
        for ind in indicacoes:
            detalhes = get_movie_details(ind.item_id)
            tipo = 'movie'

            if not detalhes or 'success' in detalhes and not detalhes['success']:
                detalhes = get_serie_details(ind.item_id)
                tipo = 'tv'

            if detalhes and not ('success' in detalhes and detalhes['success'] is False):
                data.append({
                    'item_id': ind.item_id,
                    'usuario_que_indicou': ind.usuario.username,
                    'data': ind.data_criacao,
                    'title': detalhes.get('title') or detalhes.get('name'),
                    'poster_path': detalhes.get('poster_path'),
                })
        return Response(data)

class ListaUsuarioCreateView(generics.CreateAPIView):
    queryset = ListaUsuario.objects.all()
    serializer_class = ListaUsuarioSerializer
    permission_classes = [IsAuthenticated]

class ListaUsuarioListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            lista = ListaUsuario.objects.filter(usuario=request.user)
            data = []
            for item in lista:
                data.append({
                    'item_id': item.item_id,
                    'tipo': item.tipo,  # filme ou serie
                    'data_adicao': item.data_adicao.isoformat() if item.data_adicao else None,
                    # adicione outros campos se precisar
                })
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

class AdicionarListaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        data['usuario'] = request.user.pk

        serializer = ListaUsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

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

class UploadFotoPerfilView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        usuario = request.user
        foto = request.FILES.get('foto')

        if not foto:
            return Response({"error": "Nenhuma foto enviada."}, status=400)

        usuario.foto = foto  # usa o campo correto do seu modelo
        usuario.save()

        return Response({
            "foto_url": usuario.foto.url
        })

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
        return Response({"error": "Série não encontrada"}, status=status.HTTP_404_NOT_FOUND)

# Create your views here.
def home(request):
    movies = get_popular_movies()
    return render(request, 'home.html', {'movies': movies})

def buscar_filme(request):
    query = request.GET.get('q')
    resultados = search_movie(query) if query else []
    return render(request, 'buscar.html', {'resultados': resultados})

def buscar_filme(request):
    query = request.GET.get('q')
    resultados = search_movie(query) if query else []

    return render(request, 'buscar.html', {'resultados': resultados})