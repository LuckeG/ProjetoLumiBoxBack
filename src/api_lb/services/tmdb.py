import requests

TMDB_API_KEY = '2091cdad051d5d0a0cbe40d7d3d2c043'
BASE_URL = 'https://api.themoviedb.org/3'

def get_popular_movies(page=1):
    url = f'{BASE_URL}/movie/popular?api_key={TMDB_API_KEY}&language=pt-BR&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    return []


def search_movie(query):
    url = f'{BASE_URL}/search/movie?api_key={TMDB_API_KEY}&language=pt-BR&query={query}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    return []

def search_series(query):
    """Busca uma série de TV específica pelo título."""
    url = f'{BASE_URL}/search/tv?api_key={TMDB_API_KEY}&language=pt-BR&query={query}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    return []

def get_popular_series(page=1):
    url = f'{BASE_URL}/tv/popular?api_key={TMDB_API_KEY}&language=pt-BR&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    return []


def get_movie_genres():
    """Retorna a lista completa de gêneros de filmes com seus IDs."""
    url = f'{BASE_URL}/genre/movie/list?api_key={TMDB_API_KEY}&language=pt-BR'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['genres']
    return []

def get_movies_by_genre(genre_id):
    """Busca filmes que pertencem a um gênero específico, usando o ID do gênero."""
    url = f'{BASE_URL}/discover/movie?api_key={TMDB_API_KEY}&language=pt-BR&with_genres={genre_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    return []

def get_series_genres():
    """Retorna a lista completa de gêneros de filmes com seus IDs."""
    url = f'{BASE_URL}/genre/tv/list?api_key={TMDB_API_KEY}&language=pt-BR'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['genres']
    return []

def get_series_by_genre(genre_id):
    """Busca filmes que pertencem a um gênero específico, usando o ID do gênero."""
    url = f'{BASE_URL}/discover/tv?api_key={TMDB_API_KEY}&language=pt-BR&with_genres={genre_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    return []

def get_reality_shows():
    """Busca séries do gênero 'Reality Show' (ID: 10764)."""
    url = f'{BASE_URL}/discover/tv?api_key={TMDB_API_KEY}&language=pt-BR&with_genres=10764'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    return []

def get_animes():
    """
    Busca animes usando o gênero 'Animação' (ID: 16) e idioma japonês.
    TMDb não tem gênero 'anime', então usamos animação em japonês como proxy.
    """
    url = f'{BASE_URL}/discover/tv?api_key={TMDB_API_KEY}&language=pt-BR&with_genres=16&with_original_language=ja'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    return []

def get_movie_details(movie_id):
    url = f'{BASE_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}&language=pt-BR'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_serie_details(serie_id):
    url = f'{BASE_URL}/tv/{serie_id}?api_key={TMDB_API_KEY}&language=pt-BR'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None



