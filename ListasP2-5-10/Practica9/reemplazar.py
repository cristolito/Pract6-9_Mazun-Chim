class Reemplazar:
    def reemplazar_valor(self, array, viejo, nuevo):
        for i in range(len(array)):
            if array[i] == viejo:
                array[i] = nuevo

        return array