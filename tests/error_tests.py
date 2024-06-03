import pytest
from services.error import RestException, ValidationException, SQLGenerationException


def test_rest_exception():
    """
    Test that RestException can be raised and caught correctly.
    """
    with pytest.raises(RestException) as exc_info:
        raise RestException("This is a REST exception")
    assert str(exc_info.value) == "This is a REST exception"


def test_validation_exception():
    """
    Test that ValidationException can be raised and caught correctly.
    """
    with pytest.raises(ValidationException) as exc_info:
        raise ValidationException("This is a validation exception")
    assert str(exc_info.value) == "This is a validation exception"
    assert isinstance(exc_info.value, RestException)


def test_sql_generation_exception():
    """
    Test that SQLGenerationException can be raised and caught correctly.
    """
    with pytest.raises(SQLGenerationException) as exc_info:
        raise SQLGenerationException("This is an SQL generation exception")
    assert str(exc_info.value) == "This is an SQL generation exception"
    assert isinstance(exc_info.value, RestException)
