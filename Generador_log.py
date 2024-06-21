import os
from datetime import datetime

grupo_3 = {
    'stefano_suarez': 'Stesherr',
    'kevin_valle': 'codeswax',
    'luis_quezada': 'LuisAntonioQuezadaAristega'
}

fecha_log = datetime.today().strftime('%d%m%Y')
hora_log = datetime.today().strftime('%Hh%M')
ext_log = '.txt'

logs_lexico = 'logs_lexico'
logs_sintactico = 'logs_sintactico'
algoritmos_folder = 'algoritmos'
os.makedirs(logs_lexico, exist_ok=True)

algoritmos_3 = {}

resultados = {}

def obtener_alg():
    for integrante in grupo_3.items():
        ruta = os.path.join(algoritmos_folder, f"{integrante[0]}.txt")
        with open(ruta, "r") as file:
            algoritmos_3[integrante[0]] = file.read()

def generar_log_lexico(resultados):
    for integrante, usuario_log in grupo_3.items():
        nombre_log_lexico = os.path.join(
            logs_lexico, f"lexico-{usuario_log}-{fecha_log}-{hora_log}{ext_log}")
        with open(nombre_log_lexico, 'w') as file:
            file.write('\n'.join((resultados[integrante])))
        print(f"Se creó el archivo de {integrante} con el nombre: '{nombre_log_lexico}'")

def generar_log_sintactico(resultados):
    for integrante, usuario_log in grupo_3.items():
        nombre_log_sintactico = os.path.join(logs_sintactico, f"sintactico-{usuario_log}-{fecha_log}-{hora_log}{ext_log}")
        with open(nombre_log_sintactico, 'w') as file:
            file.write('\n'.join((resultados[integrante])))
        print(f"Se creó el archivo de {integrante} con el nombre: '{nombre_log_sintactico}'")