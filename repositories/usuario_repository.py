from database.model import Filme
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


class FilmesRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def buscarFilmes(self):
        async with self.session() as session:
            async with session.begin():
                # Construir a query para selecionar todos os filmes
                query = select(Filme)

                # Executar a query e capturar o resultado
                result = await session.execute(query)

                # Extrair todos os resultados na forma de objetos de filme
                filmes = result.scalars().all()

                # Converter a lista de objetos de filme em dicionários
                filmes_dict = [self._filme_to_dict(filme) for filme in filmes]
                return filmes_dict

    def _filme_to_dict(self, filme: Filme):
        """
        Converte um objeto Filme em um dicionário para que ele possa ser 
        serializado como JSON.
        """
        return {
            "id": filme.id,
            "titulo": filme.title,
            "genero": filme.genre,
            "ano": filme.year,
            "sinopse": filme.synopsis,
            "diretor": filme.director,
            "nota_final": filme.final_rating,
            "total_avaliacoes": filme.total_reviews
        }
