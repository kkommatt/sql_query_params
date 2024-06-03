# SqlQueryParams

SqlQueryParams is a Python project for convenient, fast and flexible work with data using FastAPI and SQLAlchemy

## Installation

In order to install pip packages locally, you can use the make requirements command.

```bash
make requirements
```

## Usage

```python
# ActionTree
#       |- select list[str]
#       |- filter col.eq=5 | relation.sub_relation.id=4
#       |- sort col.asc | relation.sub_relation.id.asc
#       |- limit: int > 0
#       |- offset: int >= 0
#       |- relations dict[str, ActionTree]

s = parser.parse("q=(id, created_at, todo(id)).filter(todo.id=2)")
```

## OpenAPI doc

![image](https://github.com/kkommatt/sql_query_params/assets/100029063/4d3fec41-f1b1-47ce-a502-2f4324dcef29)

## DB diagram

![image](https://github.com/kkommatt/sql_query_params/assets/100029063/0a84d3d5-75f8-4d1a-a68e-43668177ba3e)


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
