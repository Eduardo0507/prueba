from fastapi import FastAPI
from calc import Calc

app = FastAPI()
calc = Calc()

@app.get("/sumar")
def read_sumar(num1: int = 0, num2: int = 0):
    return {calc.sumar(num1,num2)
    }

@app.get("/restar")
def read_restar(num1: int = 0, num2: int = 0):
    return {calc.restar(num1,num2)
    }

@app.get("/multiplicar")
def read_multiplicar(num1: int = 0, num2: int = 0):
    return {calc.multiplicar(num1,num2)
    }

@app.get("/dividir")
def read_dividir(num1: int = 0, num2: int = 0):
    return {calc.dividir(num1,num2)
    }



