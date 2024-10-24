from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/fibonacci/{n}")
def fib(n: int):
    '''возвращает n-e число из последовательности Фибоначчи'''
    if type(n) != 'int' and n < 0:
        raise TypeError('Введите натуральное число')
    else:
        a, b = 0, 1
        while n > 0:
            a, b = b, a + b
            n -= 1
    return a


@app.get("/greet/{name}")
def greets(name: str):
    if not isinstance(name, str):
        raise TypeError('Введите строковое значение')
    return {"Hello": name.capitalize()}