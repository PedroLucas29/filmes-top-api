from cache.cache_client import cache, set_cache, get_cache
from flask import Blueprint, jsonify, request
from repositories.factories.filme_repository_factory import filme_repository_factory

filmes_controller = Blueprint('filmes', __name__)


@filmes_controller.route('/filmes/genero/<genero>', methods=['GET'])
async def get(genero):
    key = f'getFilmes:{genero}'
    cache_existent = get_cache(key)
    if cache_existent:
        return cache_existent
    repository = filme_repository_factory()
    filmes = await repository.buscar_filmes_por_genero(genero)
    filmes_json = jsonify(filmes)
    set_cache(key, filmes_json, timeout=300)
    return filmes_json


@filmes_controller.route('/filmes/<int:id>', methods=['GET'])
async def get_by_id(id):
    repository = filme_repository_factory()
    filme = await repository.buscar_filme_por_id(id)
    if filme is None:
        return {"error": "Filme não encontrado"}, 404
    filme_json = jsonify(filme)
    return filme_json


@filmes_controller.route('/filmes', methods=['GET'])
async def get_all():
    key = 'getFilmes'
    cache_existent = get_cache(key)
    if cache_existent:
        return cache_existent
    repository = filme_repository_factory()
    filmes = await repository.buscar_filmes_todos_os_filmes()
    filmes_json = jsonify(filmes)
    set_cache(key, filmes_json, timeout=300)
    return filmes_json


@filmes_controller.route('/filmes/alugueis', methods=['POST'])
async def create_aluguel():
    repository = filme_repository_factory()
    data = request.get_json()
    aluguel = await repository.salvar_aluguel(data)
    return aluguel, 201


@filmes_controller.route('filmes/alugueis/<int:usuario_id>', methods=['GET'])
async def get_alugueis(usuario_id: int):
    repository = filme_repository_factory()
    alugueis = await repository.buscar_alugueis_do_usuario(usuario_id)
    return jsonify(alugueis)


@filmes_controller.route('filmes/alugueis/<int:aluguel_id>/nota', methods=['patch'])
async def rate_aluguel(aluguel_id):
    repository = filme_repository_factory()
    data = request.get_json()
    nota_int = int(data['nota'])
    if nota_int < 0 or nota_int > 10:
        return {"error": "Nota Inválida"}, 400
    alugueis = await repository.inserir_nota(aluguel_id, nota_int)
    if alugueis is None:
        return {"error": "Aluguel não encontrado"}, 404
    return alugueis, 200
