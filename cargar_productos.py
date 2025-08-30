import pandas as pd
import requests

API_URL = "http://localhost:5251/api/productos"  # Cambia el puerto si es necesario
CSV_FILE = "productos.csv"  # Ruta de tu archivo CSV

# Leer CSV
df = pd.read_csv(CSV_FILE)
print(df)

for _, row in df.iterrows():
    nombre = str(row["Nombre"]).strip()
    precio = float(row["Precio"])
    print("eyyyyy->>>>>>>",nombre,precio)

    if precio < 0:
        print(f"❌ No se admite precio negativo para '{nombre}', se omite")
        continue

    data = {"nombre": nombre, "precio": precio}
    resp = requests.post(API_URL, json=data)

    if resp.status_code == 201:
        print(f"✅ Producto '{nombre}' agregado correctamente")
    else:
        print(f"❌ Error al agregar '{nombre}': {resp.text}")
