from os import getenv
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = getenv('DATABASE_URL')
print("DATABASE_URL: ", DATABASE_URL)


def get_async_session():
    engine = create_async_engine(DATABASE_URL, echo=True)
    return sessionmaker(
        engine, class_=AsyncSession
    )
