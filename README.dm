Librería de ejemplo

< REQUISITOS PREVIOS >

- Python 3.8 o superior
- pip (gestor de paquetes de Python) instalado
- Emulador de terminal

< PASOS PARA INSTALAR >

Clona este repositorio en github desktop, VSCode o utilizando tu método preferido (https://github.com/RubenDomingo/mi_proyecto).

Abre una terminal y sitúate en la carpeta raíz del proyecto clonado.

Ejecuta los siguientes comandos:

```bash
python -m venv .venv # Crea un entorno virtual
.venv\Scripts\activate  # En Linux o macOS: source .venv/bin/activate
pip install -r requirements.txt # Instala las dependencias
pip install -e . # Instala el proyecto en modo desarrollador
```

< UTILIDADES >

- Conversión de números a binario
- Burla de palabras, sustituye todas las vocales de un texto por la vocal deseada
- Conversión a números romanos

< DIRECTORIOS >

```
mi_proyecto/
├── mi_proyecto/
|    └── __init__.py
|    └── binario.py
|    └── burla.py
|    └── romanos.py
├── scripts/
|    └── main.py
├── test/
|    └── pytest.ini
|    └── test_binario.py
|    └── test_burla.py
|    └── test_romanos.py
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## 🦺 Ejecutar Pruebas

```bash
pytest
```

Rubén Rodríguez Tártalo - Proyecto licenciado bajo la Licencia MIT.
