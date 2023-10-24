class Palindromo:
    def palindromo(self, palabra):
        palabra = palabra.lower()  # Convertir a minúsculas para hacer la comparación insensible a mayúsculas y minúsculas
        palabra = ''.join(c for c in palabra if c.isalnum())  # Eliminar caracteres no alfanuméricos

        return palabra