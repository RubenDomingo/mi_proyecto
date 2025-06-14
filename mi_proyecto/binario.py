def get_binario(_numero: int) -> str:
    if not isinstance(_numero, int):
        raise TypeError("El número debe ser un entero.")
    return bin(_numero)[2:]