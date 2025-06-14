import re

def burla_A(_text: str) -> str:
    return re.sub(r'[aeiouáéíóúAEIOUÁÉÍÓÚ]', lambda m: 'A' if m.group().isupper() else 'a', _text)

def burla_E(_text: str) -> str:
    return re.sub(r'[aeiouáéíóúAEIOUÁÉÍÓÚ]', lambda m: 'E' if m.group().isupper() else 'e', _text)

def burla_I(_text: str) -> str:
    return re.sub(r'[aeiouáéíóúAEIOUÁÉÍÓÚ]', lambda m: 'I' if m.group().isupper() else 'i', _text)

def burla_O(_text: str) -> str:
    return re.sub(r'[aeiouáéíóúAEIOUÁÉÍÓÚ]', lambda m: 'O' if m.group().isupper() else 'o', _text)

def burla_U(_text: str) -> str:
    return re.sub(r'[aeiouáéíóúAEIOUÁÉÍÓÚ]', lambda m: 'U' if m.group().isupper() else 'u', _text)