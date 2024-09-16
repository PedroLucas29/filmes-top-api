from os import getenv
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# Carrega as variáveis do arquivo .env
load_dotenv()

DATABASE_URL = getenv('DATABASE_URL')
print("DATABASE_URL: ", DATABASE_URL)

# Cria o engine assíncrono


# Cria a fábrica de sessões assíncronas

# Retorna uma nova sessão assíncrona


def get_async_session():
    engine = create_async_engine(DATABASE_URL, echo=True)
    return sessionmaker(
        engine, class_=AsyncSession
    )


# from os import getenv

# from dotenv import load_dotenv
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import sessionmaker

# # Carrega as variáveis do arquivo .env
# load_dotenv()

# DATABASE_URL = getenv('DATABASE_URL')
# print(DATABASE_URL)
# engine = create_async_engine(DATABASE_URL)
# print("**ENGINE: ", engine)
# async_session = sessionmaker(
#     engine, class_=AsyncSession, expire_on_commit=False)


# def get_async_session():
#     return async_session
