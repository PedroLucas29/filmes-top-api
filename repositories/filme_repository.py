from database.model import Filme, Aluguel
from sqlalchemy.future import select
from sqlalchemy import insert, update, func


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

    async def buscar_filme_por_id(self, id):
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
            query = insert(Aluguel).values(data).returning(Aluguel.id, Aluguel.nota,
                                                           Aluguel.usuario_id, Aluguel.filme_id, Aluguel.data_locacao)
            result = await session.execute(query)
            await session.commit()
            aluguel_salvo = result.mappings().one()
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
            # Atualiza a nota no aluguel
            stmt_update_aluguel = (
                update(Aluguel)
                .where(Aluguel.id == aluguel_id)
                .values({'nota': nota})
                .returning(Aluguel)
            )

            # Executa a atualização do aluguel
            result = await session.execute(stmt_update_aluguel)
            aluguel = result.scalars().first()

            if aluguel is None:
                return None

            # Busca o filme relacionado ao aluguel
            query = select(Filme).filter(Filme.id == aluguel.filme_id)
            result = await session.execute(query)
            filme = result.scalars().one_or_none()

            if not filme:
                return None

            # Conta o total de avaliações (exclui as avaliações com nota nula)
            stmt_count = select(func.count(Aluguel.nota)).where(
                Aluguel.filme_id == filme.id)
            result_count = await session.execute(stmt_count)
            total_avaliacoes = result_count.scalar()

            # Soma todas as notas atribuídas anteriormente
            stmt_sum = select(func.sum(Aluguel.nota)).where(
                Aluguel.filme_id == filme.id)
            result_sum = await session.execute(stmt_sum)
            soma_notas = result_sum.scalar() or 0

            # Calcula a média levando em consideração a nova avaliação
            nota_final = soma_notas / total_avaliacoes if total_avaliacoes > 0 else 0

            # Atualiza o filme com o total de avaliações e a média da nota final
            stmt_update_filme = (
                update(Filme)
                .where(Filme.id == filme.id)
                .values({'total_avaliacoes': total_avaliacoes, 'nota_final': nota_final}).returning(Filme.id, Filme.titulo, Filme.genero, Filme.ano, filme.nota_final, filme.total_avaliacoes)
            )

            # Executa a atualização do filme
            execution = await session.execute(stmt_update_filme)
            filme = execution.mappings().one()
            # Commit das mudanças
            await session.commit()

            # Retorna os dados atualizados do filme
            return {
                "id": filme.id,
                "titulo": filme.titulo,
                "genero": filme.genero,
                "ano": filme.ano,
                "nota_final": nota_final,
                "total_avaliacoes": total_avaliacoes
            }

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
            "id": aluguel.id,
            "nota": aluguel.nota,
            "usuario_id": aluguel.usuario_id,
            "filme_id": aluguel.filme_id,
            "data_locacao": aluguel.data_locacao,
        }
