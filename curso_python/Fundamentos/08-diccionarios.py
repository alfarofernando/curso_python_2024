### DICCIONARIOS ###

# constructores de diccionarios
miDiccionario = dict()
miOtroDiccionario = {}  # comparten el constructor con los sets
print(type(miDiccionario))  # ambos devuelven el tipo diccionario
print(type(miOtroDiccionario))  # ambos devuelven el tipo diccionario

# LOS DICCIONARIOS SE COMPONEN DE ELEMENTOS DOTADOS DE CLAVE:VALOR
# NOS PERMITE RELACIONAR DATOS

miDiccionario = {
    "nombre": "Fernando",
    "apellido": "Alfaro",
    "edad": 30,
    "altura": 1.84,
    # podemos crear estructuras complejas añadiendo un set dentro de un diccionario
    "lenguajes": {"python", "c#", "JavaScript"},
    # podemos tambien añadir listas dentro del diccionario
    "colores": ["azul", "rojo", "amarillo", "naranja"],
    # podemos añadir tuplas al mismo
    "animales": ("gato", "perro", "pajaro"),
    1: 1.77,
}
miOtroDiccionario = {"numero1": 10, "numero2": 20, "numero3": 30, "numero4": 40}

print(miDiccionario)
print(miOtroDiccionario)

print(
    len(miDiccionario)
)  # devuelve 6 ya que cuenta las claves y no los valores asociados
print(len(miOtroDiccionario))  # devuelve 4 ya que es el numero de claves que contiene

# para acceder a los valores dentro de los diccionarios debemos
# llamar al diccionario["clave"]
print(miDiccionario["nombre"])  # retorna los valores dentro de la clave nombre
# no permite llamar al diccionario[indice]
# print(miDiccionario["altura"]) devuelve un keyerror

# podemos chekear si existe una clave dentro del diccionario
print("animal" in miDiccionario)  # devuelve falso
print("animales" in miDiccionario)  # devuelve true
# no podemos comprobar si existe un elemento llamandolo directamente sin llamar a su clave.
print("azul" in miDiccionario)  # retorna false
print("rojo" in miDiccionario)  # retorna false


# podemos agregar valores
miDiccionario["calle"] = "arredondo 3517"
print(miDiccionario)  # devuelve el diccionario con la clave agregada
# asi mismo podemos eliminar valores
del miDiccionario["calle"]
print(
    miDiccionario
)  # retorna el diccionario con la clave y los valores asociados eliminados

# podemos ver un listado de items  que contienen el diccionario (clave,valor)
print(miDiccionario.items())
# podemos ver un listado de las claves que existen dentro del diccionario
print(miDiccionario.keys())
# podemos ver un listado de los valores omitiendo las claves
print(miDiccionario.values())

# podemos crear una copia de otro diccionario tomando solo sus claves y omitiendo sus valores contenidos
# nuevaVariable = dict.fromkeys(diccionarioACopiar)
miNuevoDiccionario1 = dict.fromkeys(miDiccionario)
print(miNuevoDiccionario1)

# o  podemos crear una copia de otro diccionario tomando solo sus claves y asignarle a todas las claves valores por parametro
# nuevaVariable = dict.fromkeys(diccionarioACopiar , (valores))
miNuevoDiccionario2 = dict.fromkeys(miDiccionario, ("ayer", "hoy"))
print(miNuevoDiccionario2)  # devuelve las claves
