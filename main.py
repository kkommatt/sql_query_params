import uvicorn
from fastapi import FastAPI

from services.db_services import Base, engine
from todo.views import todo_router
from todo_slave.views import todo_slave_router
from todo_slave_details.views import todo_slave_details_router
from exc_handlers import (
    ValidationException,
    SQLGenerationException,
    validation_exception_handler,
    sql_exception_handler,
)
from user.views import user_router

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)


app.include_router(todo_router)
app.include_router(todo_slave_router)
app.include_router(todo_slave_details_router)
app.include_router(user_router)

app.add_exception_handler(ValidationException, validation_exception_handler)
app.add_exception_handler(SQLGenerationException, sql_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app)
