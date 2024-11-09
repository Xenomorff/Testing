from typing import Union
from fastapi import FastAPI
from database import add_user, get_user_by_name, get_user_names, initialize_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await initialize_db()
    yield
    # shutdown

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/fibonacci/{n}")
def fib(n: int):
    '''возвращает n-e число из последовательности Фибоначчи'''
    if type(n) != 'int' or n < 0:
        raise TypeError('Введите натуральное число')
    else:
        a, b = 0, 1
        while n > 0:
            a, b = b, a + b
            n -= 1
    return a


@app.get("/greet/{name}")
async def greets(name: str):
    if not isinstance(name, str):
        raise TypeError('Введите строковое значение')
    user = await get_user_by_name(name)
    if user:
        return {"Уже виделись": name.capitalize()}
    else:
        await add_user(name)
        return {"Hello": name.capitalize()}
    

@app.get("/get")
async def get_names():
    users = await get_user_names()
    return {"users": users}