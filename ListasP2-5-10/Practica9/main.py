import flet as ft
from flet import TextField, ElevatedButton
from reemplazar import Reemplazar

def main(page: ft.Page):
    def on_submit(e):
        old_number_value = float(old_number.value)
        new_number_value = float(new_number.value)
        numbers = [float(number) for number in list_number.value.split()]
        new_numbers = reemplazador.reemplazar_valor(numbers.copy(), old_number_value, new_number_value)

        old_number.value = ""
        new_number.value = ""
        list_number.value = ""

        fila_1 = ft.Row()
        response.controls.append(ft.Text("Números orignales", size=15, weight="bold"))
        response.controls.append(fila_1)
        for number in numbers:
            fila_1.controls.append(ft.Text(number))

        fila_2 = ft.Row()
        response.controls.append(ft.Text("Números cambiadas", size=15, weight="bold"))
        response.controls.append(fila_2)
        for number in new_numbers:
            fila_2.controls.append(ft.Text(number))

        page.update()

    reemplazador = Reemplazar()
    list_number = TextField(label="Ej: 1 12 13 15")
    old_number = TextField(label="Número viejo (¿Cuál quieres cambiar?)")
    new_number = TextField(label="Número nuevo (Este va a sustituir)")
    submit_button = ElevatedButton("Suma", on_click=on_submit)
    # ft.Text("Resultado: ", size=15, weight="bold")
    response = ft.Column()
    container = ft.Column([list_number, old_number, new_number, submit_button, ft.Container(response)])

    page.add(container)

ft.app(main)
