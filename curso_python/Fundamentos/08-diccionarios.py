### DICCIONARIOS ###

#constructores de diccionarios
miDiccionario = dict()
miOtroDiccionario = {} # comparten el constructor con los sets
print(type(miDiccionario)) # ambos devuelven el tipo diccionario
print(type(miOtroDiccionario)) # ambos devuelven el tipo diccionario

# LOS DICCIONARIOS SE COMPONEN DE ELEMENTOS DOTADOS DE CLAVE:VALOR 
# NOS PERMITE RELACIONAR DATOS

miDiccionario = {
    "nombre":"Fernando" ,
    "apellido":"Alfaro" , 
    "edad":30 , 
    "altura":1.84 , 
    # podemos crear estructuras complejas añadiendo un set dentro de un diccionario
    "lenguajes": {"python" , "c#" , "JavaScript"} , 
    # podemos tambien añadir listas dentro del diccionario
    "colores": ["azul","rojo","amarillo","naranja"],
    # podemos añadir tuplas al mismo
    "animales":("gato","perro","pajaro") ,
    1:1.77
    }
miOtroDiccionario = {"numero1":10 ,"numero2":20 ,"numero3":30 ,"numero4":40}

print(miDiccionario)
print(miOtroDiccionario)

print(len(miDiccionario)) # devuelve 6 ya que cuenta las claves y no los valores asociados
print(len(miOtroDiccionario)) # devuelve 4 ya que es el numero de claves que contiene

#para acceder a los valores dentro de los diccionarios debemos
# llamar al diccionario["clave"] 
print(miDiccionario["nombre"]) # retorna los valores dentro de la clave nombre



