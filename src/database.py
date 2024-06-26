from colorama import Fore
from sqlalchemy.engine import create_engine
from src.config import settings
from sqlalchemy.orm import DeclarativeBase, sessionmaker


engine = create_engine(url=settings.database_url_psycopg, echo=False,)
session_maker = sessionmaker(engine)


# async def get_async_session() -> AsyncGenerator[AsyncSession]:
#     async with async_session_maker() as session:
#         yield session


class Base(DeclarativeBase):
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        name_value_pairs = []
        for field_name, field_value in self.dict().items():
            name_value_pairs.append(f'{Fore.BLUE}{field_name}{Fore.RESET}={field_value}')

        fields = ', '.join(name_value_pairs)
        return f'{Fore.YELLOW}{class_name}{Fore.RESET}({fields})'

    def dict(self):
        class_dict = self.__dict__.copy()
        class_dict.pop('_sa_instance_state')
        return class_dict
