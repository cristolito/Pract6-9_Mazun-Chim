import flet as ft
from flet import TextField, ElevatedButton, Text
from pila import Pila

def main(page: ft.Page):
    def on_submit(e):
        numero1 = number1.value
        numero2 = number2.value
        resultado_suma = pila.sumar_numeros_grandes(numero1, numero2)

        number1.value = ""
        number2.value = ""

        response.value = f"Resultado: {resultado_suma}"

        page.update()

    pila = Pila()
    number1 = TextField(label="Número 1")
    number2 = TextField(label="Número 2")
    submit_button = ElevatedButton("Suma", on_click=on_submit)
    response = ft.Text("Resultado: ", size=15, weight="bold")
    container = ft.Column([number1, number2, submit_button, response])

    page.add(container)

ft.app(main)
