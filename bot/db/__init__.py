from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker


def create_engine(db_url: str) -> AsyncEngine:
    return create_async_engine(
        db_url,
        future=True,
    )


def create_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(
        engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )
    