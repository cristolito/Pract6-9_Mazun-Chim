class Pila:
    def sumar_numeros_grandes(self, num1, num2):
        resultado = []
        carry = 0

        # Asegurar que ambos números tienen la misma longitud
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        for d1, d2 in zip(reversed(num1), reversed(num2)):
            suma_digitos = int(d1) + int(d2) + carry
            carry, digito = divmod(suma_digitos, 10)
            resultado.append(str(digito))

        if carry:
            resultado.append(str(carry))

        return ''.join(reversed(resultado))