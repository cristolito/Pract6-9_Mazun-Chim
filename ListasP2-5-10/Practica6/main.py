import flet as ft
from flet import TextField, ElevatedButton, Text
from linked_list import LinkedList


def main(page: ft.Page):
    def reverse_word(word):
        reversed_list = LinkedList()

        for char in word:
            reversed_list.insert(char)

        return reversed_list
    
    def on_submit(e):
        word = word_input.value
        reversed_word_list = reverse_word(word)

        word_input.value = ""


        original_word.content = Text(f"Palabra original: {word}", size=15, weight="bold")
        
        inverted_word.content = Text(f"Palabra invertida: {reversed_word_list.display()}", size=15, weight="bold")

        page.update()

    word_input = TextField(label="Palabra")
    submit_button = ElevatedButton("Invertir", on_click=on_submit)
    original_word = ft.Container()
    inverted_word = ft.Container()
    container = ft.Column([word_input, submit_button, original_word, inverted_word])

    page.add(container)

ft.app(main)
