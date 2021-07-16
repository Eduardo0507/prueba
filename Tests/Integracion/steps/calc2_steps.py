from behave import *
import api
from fastapi.testclient import TestClient

@given("que deseo restar dos numeros")
def step_implementacion(context):
    context.app = TestClient(api.app)

@when('yo ingrese los numeros {num1} y {num2}')
def step_implementacion(contex, num1, num2):
    context.api_response = context.app.get(f'/restar?num1={num1}&num2={num2}')
    assert 200 == api_response.status_code

@then('el resultado {result} debe ser la resta de ambos')
def step_implementacion(context, result):
    assert str(result) == str(context.api_response.json().get('total'))