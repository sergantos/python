from functools import singledispatch

@singledispatch
def fun(arg):
    print("неизвестно")

@fun.register
def _(arg: int | float):
    print("численный целый")

@fun.register
def _(arg: float):
    print("численный с плавающей точкой")

@fun.register
def _(arg: str):
    print("строка")

fun(2)