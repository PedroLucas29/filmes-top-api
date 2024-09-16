from asyncio import run
from database.connection import engine
from database.model import db


async def create_database():
    async with engine.begin() as connection:
        await connection.run_sync(db.metadata.drop_all)
        await connection.run_sync(db.metadata.create_all)

if __name__ == '__main__':
    run(create_database())
