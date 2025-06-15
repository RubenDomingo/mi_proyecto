import subprocess
import os
import sys
import platform

def ejecutar(comando, shell=False):
    print(f'→ {" ".join(comando) if isinstance(comando, list) else comando}')
    subprocess.run(comando, check=True, shell=shell)

def main():
    print('Creando entorno virtual...')
    ejecutar([sys.executable, '-m', 'venv', 'venv'])

    sistema = platform.system()
    if sistema == 'Windows':
        activar = '.\\venv\\Scripts\\activate'
        pip = '.\\venv\\Scripts\\pip.exe'
    else:
        activar = 'source ./venv/bin/activate'
        pip = './venv/bin/pip'

    print('Instalando dependencias en el entorno virtual...')
    ejecutar([pip, 'install', '-r', 'requirements.txt'])

    print('Instalando el paquete en modo desarrollo en el entorno virtual...')
    ejecutar([pip, 'install', '-e', '.'])

    print('\n¡Instalación completada!')
    print(f'No olvides activar el entorno con: {activar}')

if __name__ == '__main__':
    main()

# import os
# import subprocess
# import sys
# import platform

# def ejecutar(comando, **kwargs):
#     print(f"Ejecutando: {' '.join(comando)}")
#     subprocess.run(comando, check=True, **kwargs)

# def main():
#     print("Creando entorno virtual...")
#     ejecutar('python -m venv venv')
#     print("Activando entorno virtual...")
#     ejecutar('.venv\Scripts\\activate')
#     print("Instalando dependencias...")
#     ejecutar('pip install -r .\\requirements.txt')
#     print("Instalando el paquete en modo editable...")
#     ejecutar('pip install -e .')
    
# main()