from database.model import Filme, Aluguel
from sqlalchemy.future import select
from sqlalchemy import insert, update


class FilmesRepository:
    def __init__(self, session):
        self.session = session

    async def buscar_filmes_por_genero(self, genero):
        async with self.session() as session:
            query = select(Filme).filter(Filme.genero == genero)
            result = await session.execute(query)
            filmes = result.scalars().all()
            filmes_dict = [self._filme_to_dict(filme) for filme in filmes]
            return filmes_dict

    async def buscar_filme(self, id):
        async with self.session() as session:
            query = select(Filme).filter(Filme.id == id)
            result = await session.execute(query)
            filme = result.scalars().one_or_none()
            if filme is None:
                return None
            filme_dict = self._filme_to_dict(filme)
            return filme_dict

    async def buscar_filmes_todos_os_filmes(self):
        async with self.session() as session:
            query = select(Filme)
            result = await session.execute(query)
            filmes = result.scalars().all()
            filmes_dict = [self._filme_to_dict(
                filme) for filme in filmes]
            return filmes_dict

    async def salvar_aluguel(self, data):
        async with self.session() as session:
            query = insert(Aluguel).values(data).returning(Aluguel)
            result = await session.execute(query)
            await session.commit()
            aluguel_salvo = result.mappings().one()
            print(aluguel_salvo.id)
            aluguel_dict = self._aluguel_to_dict(aluguel_salvo)
            return aluguel_dict

    async def buscar_alugueis_do_usuario(self, id_usuario):
        async with self.session() as session:
            query = (
                select(Aluguel, Filme.titulo,
                       Aluguel.nota, Aluguel.data_locacao, Aluguel.id)
                .join(Filme, Aluguel.filme_id == Filme.id)
                .where(Aluguel.usuario_id == id_usuario)
            )
            result = await session.execute(query)
            # ou result.scalars().all() se estiver retornando apenas uma coluna
            alugueis = result.all()

            alugueis_dict = [
                {
                    "id": aluguel.id,
                    "titulo": aluguel.titulo,
                    "nota": aluguel.nota,
                    "data_locacao": aluguel.data_locacao
                }
                for aluguel in alugueis
            ]

        return alugueis_dict

    async def buscar_alugueis_do_usuario(self, id_usuario):
        async with self.session() as session:
            query = (
                select(Aluguel, Filme.titulo,
                       Aluguel.nota, Aluguel.data_locacao, Aluguel.id)
                .join(Filme, Aluguel.filme_id == Filme.id)
                .where(Aluguel.usuario_id == id_usuario)
            )
            result = await session.execute(query)
            # ou result.scalars().all() se estiver retornando apenas uma coluna
            alugueis = result.all()

            alugueis_dict = [
                {
                    "id": aluguel.id,
                    "titulo": aluguel.titulo,
                    "nota": aluguel.nota,
                    "data_locacao": aluguel.data_locacao
                }
                for aluguel in alugueis
            ]

        return alugueis_dict

    async def inserir_nota(self, aluguel_id, nota):
        async with self.session() as session:
            stmt = (
                update(Aluguel)
                .where(Aluguel.id == aluguel_id)
                .values({'nota': nota})
                .returning(Aluguel)
            )

        result = await session.execute(stmt)
        aluguel = result.scalars().first()

        # Confirma a transação
        await session.commit()
        return aluguel

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

    def _aluguel_to_dict(self, aluguel):
        return {
            "filme_id": aluguel.filme_id,
            "usuario_id": aluguel.usuario_id,
            "data_aluguel": aluguel.data_aluguel,
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
