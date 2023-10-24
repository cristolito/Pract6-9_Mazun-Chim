import flet as ft
from flet import TextField, ElevatedButton, Text
from palindromo import Palindromo

def main(page: ft.Page):
    def on_submit(e):
        word = word_input.value
        palabra = palindromo.palindromo(word)
        word_input.value = ""

        original_word.content = Text(f"Palabra original: {word}", size=15, weight="bold")
        
        inverted_word.content = ft.Column([
            Text(f"Letras orignales: {palabra}", size=15, weight="bold"),
            Text(f"Letras volteadas: {palabra[::-1]}", size=15, weight="bold")
            ])
        
        if palabra[::-1] == palabra:
            response.value = f"Resultado: {word} es un palíndromo."
        else:
            response.value = f"Resultado: {word} no es un palíndromo."

        page.update()

    palindromo = Palindromo()
    word_input = TextField(label="Palabra")
    submit_button = ElevatedButton("Confirmar Palíndromo", on_click=on_submit)
    original_word = ft.Container()
    inverted_word = ft.Container()
    response = ft.Text("Resultado: ", size=15, weight="bold")
    container = ft.Column([word_input, submit_button, response, original_word, inverted_word])

    page.add(container)

ft.app(main)
