import requests
import time

BASE_URL = "http://127.0.0.1:8000"

# Crear una nueva incidencia
nueva_incidencia = {
    "latitud": 41.38879,
    "longitud": 2.15899,
    "descripcion": "Farola rota en la calle Mallorca",
    "email": "ciudadano1@example.com"
}

print("\n➡️ Creando incidencia...")
r = requests.post(f"{BASE_URL}/incidencias", json=nueva_incidencia)
print(r.status_code)
print(r.json())
id_creada = r.json().get("id", 1)

# Esperar un segundo para no saturar el servidor en pruebas
time.sleep(1)

# Listar incidencias por usuario
print("\n➡️ Listando incidencias por usuario...")
r = requests.get(f"{BASE_URL}/incidencias/usuario/ciudadano1@example.com")
print(r.status_code)
print(r.json())

# Listar incidencias por estado
print("\n➡️ Listando incidencias por estado 'Abierta'...")
r = requests.get(f"{BASE_URL}/incidencias/estado/Abierta")
print(r.status_code)
print(r.json())

# Cambiar el estado de la incidencia creada
print(f"\n➡️ Cambiando estado de la incidencia {id_creada} a 'En curso'...")
r = requests.put(f"{BASE_URL}/incidencias/{id_creada}/estado", params={"nuevo_estado": "En curso"})
print(r.status_code)
print(r.json())

# Verificar el cambio listando por estado 'En curso'
print("\n➡️ Verificando incidencia en estado 'En curso'...")
r = requests.get(f"{BASE_URL}/incidencias/estado/En%20curso")
print(r.status_code)
print(r.json())

# Eliminar la incidencia
print(f"\n➡️ Eliminando incidencia {id_creada}...")
r = requests.delete(f"{BASE_URL}/incidencias/{id_creada}")
print(r.status_code)
print(r.json())

# Intentar eliminarla de nuevo (debería fallar)
print(f"\n➡️ Intentando eliminar nuevamente la incidencia {id_creada}...")
r = requests.delete(f"{BASE_URL}/incidencias/{id_creada}")
print(r.status_code)
print(r.json())
