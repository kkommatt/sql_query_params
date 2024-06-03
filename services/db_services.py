"""
This module sets up the database connection and session for a To-Do application using SQLAlchemy.

The module performs the following tasks:
1. Defines a base class for declarative class definitions.
2. Creates an engine connected to a SQLite database named 'ToDoDB.db'.
3. Checks if the database exists, and if not, creates it.
4. Configures a session factory for interacting with the database.

Attributes:
    Base (DeclarativeMeta): A base class for declarative class definitions using SQLAlchemy's ORM.
    engine (Engine): An SQLAlchemy Engine instance connected to the 'ToDoDB.db' SQLite database.
    SessionLocal (sessionmaker): A configured session factory for creating new session instances.
    session (Session): An instance of a session created from SessionLocal, used for interacting with the database.

Modules:
    sqlalchemy.orm: Provides the base class and sessionmaker for ORM.
    sqlalchemy: Provides the create_engine function for database connection.
    sqlalchemy_utils: Provides utility functions like database_exists and create_database.
"""

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


Base = declarative_base()

engine = create_engine(
    "sqlite:///ToDoDB.db",
    connect_args={"check_same_thread": False},
    echo=True,
)
create_database(engine.url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

if not database_exists(engine.url):
    create_database(engine.url)
    Base.metadata.create_all(bind=engine)
