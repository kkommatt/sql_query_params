import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, drop_database, create_database
from sqlalchemy.orm import sessionmaker
from services.db_services import Base, engine, SessionLocal, session


@pytest.fixture(scope="module")
def test_engine():
    """
    Create a test database engine and ensure it is properly cleaned up after tests.
    """
    test_engine = create_engine(
        "sqlite:///test_ToDoDB.db",
        connect_args={"check_same_thread": False},
        echo=True,
    )
    if not database_exists(test_engine.url):
        create_database(test_engine.url)
    yield test_engine


@pytest.fixture(scope="module")
def test_session(test_engine):
    """
    Create a session factory bound to the test database engine.
    """
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=test_engine)


def test_session_creation(test_session):
    """
    Test that the session is created and bound to the test database engine.
    """
    assert test_session is not None, "Session should be created."


def test_base_declarative():
    """
    Test that the Base class is a declarative base class.
    """
    assert hasattr(Base, "metadata"), "Base should have a metadata attribute."


def test_session_local_creation():
    """
    Test that the SessionLocal is configured correctly.
    """
    test_session_local = SessionLocal()
    assert test_session_local is not None, "SessionLocal should create a session."
    test_session_local.close()


def test_session_instance():
    """
    Test that the global session instance is created correctly.
    """
    assert session is not None, "Global session instance should be created."

