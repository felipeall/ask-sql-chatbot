from dataclasses import dataclass

from sqlalchemy import URL, MetaData, create_engine
from sqlalchemy.sql.ddl import CreateTable

from app.settings import settings


@dataclass
class Database:
    """A class used to represent a database."""

    def __post_init__(self):
        """Initializes the database connection and reflects the database schema."""
        url = URL.create(
            drivername="postgresql",
            username=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            database=settings.POSTGRES_DB,
        )
        self.engine = create_engine(url)
        self.meta = MetaData()
        self.meta.reflect(bind=self.engine)

    def get_ddl(self) -> str:
        """
        Retrievers the DDL (Data Definition Language) statements for all tables in the database.

        Returns
        -------
        str
            A string of concatenated DDL statements for each table in the database.
        """
        return "".join(str(CreateTable(table).compile(self.engine)) for table in self.meta.sorted_tables)
