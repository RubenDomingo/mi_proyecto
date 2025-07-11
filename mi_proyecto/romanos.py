def num_romanos(numero):
    if not (0 < numero < 4000):
        raise ValueError("El número debe estar entre 1 y 3999")

    valores = [
        (1000, "M"), (900, "CM"),
        (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"),
        (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"),
        (5, "V"), (4, "IV"),
        (1, "I")
    ]

    resultado = ""
    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    return resultado