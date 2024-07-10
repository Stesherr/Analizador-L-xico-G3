import os
from datetime import datetime

group_members = {
    'stefano_suarez': 'Stesherr',
    'kevin_valle': 'codeswax',
    'luis_quezada': 'LuisAntonioQuezadaAristega'
}

log_date = datetime.today().strftime('%d%m%Y')
log_time = datetime.today().strftime('%Hh%M')
log_ext = '.txt'

# logs_lexico = 'logs_lexico'
# logs_sintactico = 'logs_sintactico'
# logs_semantico = 'logs_semantico'

algorithms_folder = 'algoritmos'
editor_folder = 'editor_code'

# os.makedirs(logs_lexico, exist_ok=True)
# os.makedirs(logs_sintactico, exist_ok=True)
# os.makedirs(logs_semantico, exist_ok=True)

os.makedirs(editor_folder, exist_ok=True)

algorithms_3 = {}
# editor_txt = []
# resultados = {}

def get_random_algorithms():
    for member in group_members.items():
        ruta = os.path.join(algorithms_folder, f"{member[0]}.txt")
        with open(ruta, "r") as file:
            algorithms_3[member[0]] = file.read()

def create_log(lexical,syntax,semantic):
    test_log = os.path.join(
        editor_folder, f"log-{log_date}-{log_time}{log_ext}")
    with open(test_log, 'w') as file:
        for lex in lexical:
            file.write(f"{lex}\n")
        for syn in syntax:
            file.write(f"{syn}\n")
        for sem in semantic:
           file.write(f"{sem}\n")
    print(f"Se creó el archivo log con nombre: '{test_log}'")

# def generar_log_sintactico(resultados):
#     for integrante, usuario_log in group_members.items():
#         nombre_log_sintactico = os.path.join(logs_sintactico, f"sintactico-{usuario_log}-{log_date}-{log_time}{log_ext}")
#         with open(nombre_log_sintactico, 'w') as file:
#             file.write('\n'.join((resultados[integrante])))
#         print(f"Se creó el archivo de {integrante} con el nombre: '{nombre_log_sintactico}'")

# def generar_log_semantico(resultados):
#     for integrante, usuario_log in group_members.items():
#         nombre_log_semantico = os.path.join(logs_semantico, f"semantico-{usuario_log}-{log_date}-{log_time}{log_ext}")
#         with open(nombre_log_semantico, 'w') as file:
#             file.write('\n'.join((resultados[integrante])))
#         print(f"Se creó el archivo de {integrante} con el nombre: '{nombre_log_semantico}'")