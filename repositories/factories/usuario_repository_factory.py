from repositories.usuario_repository import UsuarioRepository
# Certifique-se de que o caminho está correto
from database.connection import get_async_session


def usuario_repository_factory():
    # Obtém uma sessão assíncrona através da função de conexão
    async_session = get_async_session()

    # Retorna uma instância de UsuarioRepository com a sessão assíncrona
    return UsuarioRepository(async_session)
