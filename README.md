Gestión de Productos con Scripts Python

Este proyecto contiene scripts para cargar productos desde un CSV y exportarlos a JSON mediante Python.

─────────────────────────────
 Crear un entorno virtual:
 Windows:
python -m venv venv

Linux / macOS:
python3 -m venv venv

─────────────────────────────
 Activar el entorno virtual:

 Windows (PowerShell):
.\venv\Scripts\Activate.ps1

 Linux / macOS:
source venv/bin/activate

─────────────────────────────
 Verificar compatibilidad de Python:
 Este proyecto requiere Python 3.10 o superior.

─────────────────────────────
 Instalar dependencias:

Instalar todas las librerías:
pip install -r requirements.txt

O solo requests:
pip install requests

─────────────────────────────
 Preparar el archivo CSV productos.csv:

Formato del CSV:

Nombre,Precio
Producto 1,100.50
Producto 2,200.00

 Reglas:

Nombre → texto

Precio → decimal (no puede ser negativo)

─────────────────────────────
 Ejecutar los scripts:

 Windows:
python cargar_productos.py
python exportar_json.py

 Linux / macOS:
python3 cargar_productos.py
python3 exportar_json.py

─────────────────────────────
 Detalles de los scripts:

 cargar_productos.py:

Lee las filas del CSV con pandas

Convierte el nombre a cadena y el precio a decimal

Valida que el precio no sea negativo

Envía los datos a la API mediante POST si son válidos

Lanza error si el precio es negativo y no procesa la fila

 exportar_json.py:

Extrae los productos desde la API y los guarda en un archivo JSON

