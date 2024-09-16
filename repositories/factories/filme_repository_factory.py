from repositories.filme_repository import FilmesRepository
from database.connection import get_async_session


def filme_repository_factory():

    async_session = get_async_session()

    return FilmesRepository(async_session)
