from sqlalchemy.engine import create_engine

database_url = "sqlite+pysqlite:///./database/checkout.db"

engine = create_engine(
    url=database_url,
    echo=False,
    future=True,
    connect_args={"check_same_thread": False},
)
