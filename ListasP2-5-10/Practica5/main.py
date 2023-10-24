import flet as ft # Importar librería del framework
from flet import TextField, ElevatedButton # TextField, inputs; ElevetaedButton, botones
from linked_list import LinkedList

def main(page: ft.Page): #función main que tiene una variable global de tipo page
                         #page actualiza y ahi se ingresan los controls (widgets) de la interfaz gráfica
    def on_submit(e):
        word = word_input.value #de esta manera se accede al valor que está en el input .value
        first_letter = word[0].lower()
        main_word_list.insert(word)
        column = ft.Column() #ft.Column() Creación de una columna para modificar la vista de las listas de las palabras

        if first_letter not in word_lists: #Si no hay una lista que contenga palabras que inicien
                                           # con esa palabra se crea una nueva
            word_lists[first_letter] = LinkedList()

        word_lists[first_letter].insert(word)

        for word in main_word_list.display(): #La columna local de la función se ingresan valores con el append
            column.controls.append(ft.Text(word, size=15, weight="bold")) #ft.Text() crear controles para poner texto

        container_original_words.content = column #En la sección de la lista original de palabras se cambia el contenido
        #.content es para los ft.Container()

        word_input.value = "" #El valor del input se vacía

        page.update()

    def on_divided(e):
        column = ft.Column() #Las columnas son objetos iterables (listas) se pueden acceder a sus posiciones con indicies. Los objetos se colocan uno encima del otro

        for first_letter, word_list in word_lists.items():
            column.controls.append(ft.Text(first_letter.upper(), size=20, weight="bold")) #De esta manera se personaliza los textos
            for word in word_list.display():
                column.controls.append(ft.Text(word, size=15))

        container_words.content = column

        page.update()

    word_lists = {}
    main_word_list = LinkedList()

    word_input = TextField(label="Palabras", width=300) #Input para capturar las palabras
    submit_button = ElevatedButton("Enviar", on_click=on_submit) #Boton que ejecuta la función on_submit cuando se le da click
    divided_button = ElevatedButton("Dividir", on_click=on_divided)
    container_words = ft.Container() #Contenedor personalizable
    container_original_words = ft.Container() #Contenedor personalizable

    #ft.Row acomoda los objetos una al lado del otro
    page.add(ft.Container(ft.Row([
        ft.Column([word_input, submit_button, divided_button, container_original_words], expand=True),
        ft.Column([container_words], expand=True)
        ], expand=True), alignment=ft.alignment.center, margin=ft.margin.all(15))) #Algunas de las configuraciones que tiene el contenedor


ft.app(main) #Así se ejecuta la aplicación
