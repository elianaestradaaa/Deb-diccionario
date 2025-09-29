# diccionario con datos
informacion_personal = {
    "nombre": "Eliana Estrada",
    "edad": 20,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

# cambiar ciudad
informacion_personal["ciudad"] = "Cuenca"

# si no hay telefono lo agrego
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# quitar edad
informacion_personal.pop("edad", None)

# mostrar el resultado
print("Mi diccionario final:")
print(informacion_personal)
