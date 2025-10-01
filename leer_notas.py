# Abrir el archivo en modo lectura
archivo = open("my_notes.txt", "r")

# Leer línea por línea con un ciclo
print("Contenido de mis notas:\n")
for linea in archivo:
    print(linea.strip())  # strip() quita saltos de línea extra

# Cerrar el archivo
archivo.close()
