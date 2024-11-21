import datetime
from typing import Union
from fastapi import FastAPI, Request
from database import add_user, get_user_by_name, get_user_names, initialize_db
from utils import get_fib
from contextlib import asynccontextmanager
from src.routers.users import router as user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await initialize_db()
    yield
    # shutdown

async def printer(req: Request, call_next):
    # ---- логика до запроса----
    print(req.client.host)
    start_time = datetime.datetime.now()

    #выполнение запроса
    response = await call_next(req)

    # ---- логика после запроса----
    end_time = datetime.datetime.now() - start_time

    print(f"Обработан запрос за {end_time}")

    return response


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)

app.middleware('http')(printer)

@app.get("/fibonacci/{n}")
def fib(n: int):
    '''проверяет корректность введенных данных'''
    if type(n) != 'int' or n < 0:
        raise TypeError('Введите натуральное число')
    else:
        return get_fib(n)