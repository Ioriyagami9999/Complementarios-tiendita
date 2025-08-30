import requests
import json

API_URL = "http://localhost:5251/api/productos"  # Cambia el puerto si es necesario
OUTPUT_FILE = "productos.json"

# Obtener productos desde la API
resp = requests.get(API_URL)
if resp.status_code == 200:
    productos = resp.json()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(productos, f, indent=4, ensure_ascii=False)
    print(f"Productos exportados a {OUTPUT_FILE}")
else:
    print(f"Error al obtener productos: {resp.status_code}")
