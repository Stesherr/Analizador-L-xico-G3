# Proyecto - Editor y Analizador de Código PHP

Grupo 3
- Stefano Suarez
- Luis Quezada
- Kevin Valle

## Funcionalidades:
### Edición de código
El usuario podrá escribir sentencias básicas en PHP.
### Ejecución
El usuario podrá ejecutar el código ingresado y el aplicativo mostrará el resultado, similar a un IDE.
### Verificador de sentencias
El aplicativo analizará el script ingresado y validará si se cumplen las normativas establecidas en el proyecto. En caso de no haberlo, mostrará un mensaje de error indicando el problema.
### Generador de log
El aplicativo generará un log indicando los resultados y posibles errores luego de la verificación.

## Consideraciones:
- Para poder usar la funcionalidad de **Ejecución** se requiere tener instalado PHP 8.3 en una ruta específica del disco local C. Se recomienda instalarlo usando el package manager
"Chocolatey", ya que hace el proceso de forma automática.
1. Seguir los pasos propuestos en el siguiente enlace: https://chocolatey.org/install
2. Una vez instalado Chocolatey, ingresar el siguiente comando:
```
choco install php
```
3. Confirmar a todo y esperar.
- Para poder usar la funcionalidad de **Verificador de sentencias** se requiere ejecutar primero los archivos Analizador_lexico.py y Analizador_semantico.py.
