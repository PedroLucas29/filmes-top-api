from cache.cache_client import cache
from flask import Blueprint, jsonify
from repositories.factories.filme_repository_factory import filme_repository_factory

filmes_controller = Blueprint('filmes', __name__)


@filmes_controller.route('/filmes/genero/<genero>', methods=['GET'])
async def get(genero):
    key = f'getFilmes:{genero}'
    print("**CACHE", cache)
    cache_existent = cache.get(key)
    # if cache_existent:
    #     return cache_existent
    repository = filme_repository_factory()
    filmes = await repository.buscar_filmes_por_genero(genero)
    filmes_json = jsonify(filmes)
    # cache.set(key, filmes_json, timeout=300)
    return filmes_json


@filmes_controller.route('/filmes', methods=['GET'])
async def get_all():
    try:
        key = 'getFilmes'
        print("**CACHE", cache)
        # cache_existent = cache.get(key)
        # if cache_existent:
        #     return cache_existent
        repository = filme_repository_factory()
        filmes = await repository.buscar_filmes_todos_os_filmes()
        filmes_json = jsonify(filmes)
        # cache.set(key, filmes_json, timeout=300)
        return filmes_json
    except Exception as e:
        return jsonify({"error": "Ocorreu um erro"}), 500
