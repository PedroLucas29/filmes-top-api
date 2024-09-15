from repositories.filme_repository import FilmesRepository
from database.connection import get_async_session


def filme_repository_factory():
    # Obtém uma sessão assíncrona
    async_session = get_async_session()

    # Retorna uma instância de FilmesRepository com a sessão assíncrona
    return FilmesRepository(async_session)


# from repositories.filme_repository import FilmesRepository
# from database import connection


# def filme_repository_factory():
#     # Cria uma sessão assíncrona
#     async_session = connection.get_async_session()

#     # Retorna uma instância de FilmesRepository com a sessão assíncrona
#     return FilmesRepository(async_session)
