import os

# Obtener la ruta absoluta del directorio actual
dir_path = os.path.abspath(os.getcwd())

# Obtener el listado de archivos y directorios en el directorio actual
file_list = os.listdir(dir_path)

# Filtrar solo los directorios
dir_list = [f for f in file_list if os.path.isdir(os.path.join(dir_path, f))]

# Imprimir la lista de directorios
print(dir_list)