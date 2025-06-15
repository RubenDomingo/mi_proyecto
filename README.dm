Librería de ejemplo


<<<< REQUISITOS PREVIOS >>>>

- Python 3.8 o superior
- pip (gestor de paquetes de Python) instalado
- Un editor de código (opcional, pero recomendado)
- Emulador de terminal
- Este paquete, se descarga desde https://github.com/RubenDomingo/mi_proyecto


<<<< PASOS PARA INSTALAR >>>>

Abre una terminal y sitúate en la carpeta raíz del proyecto clonado.

Esta librería viene con un script de instalación desatendida que puedes ejecutar con el siguiente comando:
    python .\scripts\instalar.py

No olvides activar el entorno virtual tras la instalación. Puedes hacerlo con el siguiente comando:
    .venv\Scripts\activate

Si prefieres instalarlo manualmente, puedes usar los siguientes comandos en el orden escrito:
    python -m venv venv
    .venv\Scripts\activate
    pip install -r .\requirements.txt
    pip install -e .


<<<< UTILIDADES >>>>

binario.py
    get_binario()
        Conversión de números a binario.

burla.py
    burla_A()
        Burla de palabras, sustituye todas las vocales de un texto por la vocal 'A'.
    burla_E()
        Burla de palabras, sustituye todas las vocales de un texto por la vocal 'E'.
    burla_I()
        Burla de palabras, sustituye todas las vocales de un texto por la vocal 'I'.
    burla_O()
        Burla de palabras, sustituye todas las vocales de un texto por la vocal 'O'.
    burla_U()
        Burla de palabras, sustituye todas las vocales de un texto por la vocal 'U'.

romanos.py
    get_romano()
        Conversión a números romanos, limitado a números del 1 al 3999 ya que es el rango de números representables en números romanos.


<<<< FUNCIONAMIENTO >>>>

Para obtener un ejemplo de los resultados, puedes usar el siguiente comando:
    python -m scripts.main


<<<< PRUEBAS >>>>

Asegúrate de que el entorno virtual está activado y ejecuta el siguiente comando desde el directorio raíz del proyecto:
    pytest


<<<< DIRECTORIOS >>>>

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
├── pyproject.toml
├── README.md
└── requirements.txt

Rubén Rodríguez Tártalo - Proyecto licenciado bajo la Licencia MIT.