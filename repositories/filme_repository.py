from database.model import Filme
from sqlalchemy.future import select


class FilmesRepository:
    def __init__(self, session):
        self.session = session

    async def buscar_filmes_por_genero(self, genero):
        async with self.session() as session:
            async with session.begin():
                # Realiza a consulta para buscar todos os filmes
                query = Filme.query().all()
                result = await session.execute(query)
                filmes = result.scalars().all()

                # Converte os filmes em dicionários
                filmes_dict = [self._filme_to_dict(filme) for filme in filmes]

                # Retorna a lista de filmes em formato de dicionário
                return filmes_dict

    async def buscar_filmes_todos_os_filmes(self):
        print("** SESISION", self.session)
        async with self.session() as session:
            async with session.begin():
                # Realiza a consulta para buscar todos os filmes
                query = select(Filme)
                result = await session.execute(query)
                filmes = result.scalars().all()

                # Converte os filmes em dicionários
                filmes_dict = [self._filme_to_dict(filme) for filme in filmes]

                # Retorna a lista de filmes em formato de dicionário
                print("**DICT ", filmes_dict)
                return filmes_dict

    def _filme_to_dict(self, filme):
        return {
            "id": filme.id,
            "titulo": filme.titulo,
            "genero": filme.genero,
            "ano": filme.ano,
            "sinopse": filme.sinopse,
            "diretor": filme.diretor,
            "nota_final": filme.nota_final,
            "total_avaliacoes": filme.total_avaliacoes
        }


# from database.model import Filme
# from sqlalchemy.future import select
# from sqlalchemy import text


# class FilmesRepository:
#     def __init__(self, session):
#         self.session = session

#     async def buscarFilmes(self):
#         async with self.session() as session:
#             async with session.begin():
#                 query = select(Filme)
#                 result = await session.execute(query)
#                 filmes = result.scalars().all()

#                 filmes_dict = [self._filme_to_dict(filme) for filme in filmes]
#                 return filmes_dict

#                 # filmes_dict = [dict(zip(result.keys(), row))
#                 #                for row in filmes]
#                 # return filmes_dict
#     def _filme_to_dict(self, filme):
#         return {
#             "id": filme.id,
#             "titulo": filme.titulo,
#             "genero": filme.genero,
#             "ano": filme.ano,
#             "sinopse": filme.sinopse,
#             "diretor": filme.diretor,
#             "nota_final": filme.nota_final,
#             "total_avaliacoes": filme.total_avaliacoes
#         }
