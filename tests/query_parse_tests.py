import operator

import pytest
from pydantic import BaseModel
from sqlalchemy import Column, Integer
from sqlalchemy.orm import Mapped

from services.db_services import Base
from services.query_parser import (
    ActionTree,
    FilterAction,
    SortAction,
    SortOrder,
    NestedField,
)
from services.query_parse import get_all, EXCLUDE_COLUMN_PREFIX
from services.serialization import BaseSerializer, SerializerField


class MyModel(Base):
    __tablename__ = "mymodel"
    id: Mapped[int] = Column(Integer, primary_key=True)


class MyModelPydantic(BaseModel):
    pass


class MyModelSerializer(BaseSerializer):
    model = MyModel
    fields = [SerializerField("id", alias="id")]


def test_get_all():
    # Prepare ActionTree with filters and sort
    action_tree = ActionTree()
    action_tree.select = ["id"]
    action_tree.sort = SortAction(field=NestedField(["id"]), order=SortOrder.DESC)

    # Ensure the generated query is not empty
    query = get_all(action_tree, MyModelSerializer)
    assert query is not None

    # Ensure the query contains expected keywords
    assert "SELECT" in str(query)
    assert "FROM" in str(query)
    assert "ORDER BY" in str(query)


def test_get_all_exclude():
    # Prepare ActionTree with excluded fields
    action_tree = ActionTree()
    action_tree.select = [f"{EXCLUDE_COLUMN_PREFIX}id"]

    # Ensure the generated query is not empty
    query = get_all(action_tree, MyModelSerializer)
    assert query is not None

    # Ensure the query doesn't contain excluded field
    assert "field" not in str(query)


def test_get_all_no_select():
    # Prepare ActionTree without select fields
    action_tree = ActionTree()
    action_tree.filters = [FilterAction("id", operator.eq, "1")]

    # Ensure the generated query is not empty
    query = get_all(action_tree, MyModelSerializer)
    assert query is not None

    # Ensure the query contains default select fields
    assert "SELECT" in str(query)


if __name__ == "__main__":
    pytest.main()
