from asyncio import run
from database.connection import engine
from database.model import db


async def create_database():
    async with engine.begin() as connection:
        # Remover todas as tabelas, se existirem, e criar novas tabelas
        await connection.run_sync(db.metadata.drop_all)
        await connection.run_sync(db.metadata.create_all)

if __name__ == '__main__':
    run(create_database())


# from asyncio import run

# from database.connection import engine
# from database.model import db


# async def create_database():
#     async with engine.begin() as connection:
#         print("CONNECTION", connection)
#         await connection.run_sync(db.metadata.drop_all)
#         await connection.run_sync(db.metadata.create_all)


# if __name__ == '__main__':
#     run(create_database())
