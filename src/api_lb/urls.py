from django.urls import include, path
from rest_framework import routers
from api_lb.views import UsuarioViewSet 
from .views import FilmesPopularesView, SeriesPopularesView, SeriesSearchView, FilmesSearchView, FilmesGenresView, FilmesByGenreView, SeriesGenresView, SeriesByGenreView, AnimesView, RealitiesView, FilmeDetailView, SerieDetailView, BuscarUsuariosView, IndicacaoCreateView, IndicacoesParaUsuarioView, ListaUsuarioCreateView, ListaUsuarioListView, UploadFotoPerfilView, AdicionarListaView
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()

router.register(r'auth/user', UsuarioViewSet, basename='user')

urlpatterns = [
    path("", include(router.urls)),
    
    # Populares e busca
    path('api/filmes/populares/', FilmesPopularesView.as_view(), name='filmes-populares'),
    path('api/series/populares/', SeriesPopularesView.as_view(), name='series-populares'),
    path('api/filmes/search/', FilmesSearchView.as_view(), name='filmes-search'),
    path('api/series/search/', SeriesSearchView.as_view(), name='series-search'),

    # Gêneros
    path('api/generos/filmes/', FilmesGenresView.as_view(), name='movie-genres'),
    path('api/generos/filmes/<int:genre_id>/', FilmesByGenreView.as_view(), name='movies-by-genre'),
    path('api/generos/series/', SeriesGenresView.as_view(), name='series-genres'),
    path('api/generos/series/<int:genre_id>/', SeriesByGenreView.as_view(), name='series-by-genre'),

    # Outros
    path('animes/', AnimesView.as_view(), name='animes'),
    path('realities/', RealitiesView.as_view(), name='realities'),

    # Detalhes padrão
    path('api/filmes/<int:movie_id>/', FilmeDetailView.as_view(), name='filme-detail'),
    path('api/series/<int:serie_id>/', SerieDetailView.as_view(), name='serie-detail'),

    # ROTAS PARA RANDOMIZADOS (agora sim!)
    path('api/filmes-random/<int:movie_id>/', FilmeDetailView.as_view(), name='filme-random-detail'),
    path('api/series-random/<int:serie_id>/', SerieDetailView.as_view(), name='serie-random-detail'),

    path('usuarios/buscar/', BuscarUsuariosView.as_view(), name='buscar-usuarios'),
    path('indicacoes/', IndicacaoCreateView.as_view(), name='criar-indicacao'),
    path('indicacoes/recebidas/', IndicacoesParaUsuarioView.as_view(), name='indicacoes-para-usuario'),
    path('lista/adicionar/', AdicionarListaView.as_view(), name='lista-adiciona'),
    path('lista/', ListaUsuarioListView.as_view(), name='lista-usuario'),
    path('api/usuario/upload-foto/', UploadFotoPerfilView.as_view(), name='upload-foto-perfil'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)