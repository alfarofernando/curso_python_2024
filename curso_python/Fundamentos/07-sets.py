### SETS ###

# al igual que las listas (mutables) y las tuplas (inmutables)
# los sets tratan de manejar los arrays ya que estos no existen en python
# los constructores serian
miSet = set()
miOtroSet = {}

print(type(miSet)) # devuelve tipo de dato SET
print(type(miOtroSet)) # inicialmente devuelve tipo de dato DICT

miOtroSet = {"Fernando" , "Alfaro" , 1.84 , 30}
print(type(miOtroSet)) # cuando relleno mi set con elementos, el mismo cambia a tipo de dato SET

# similitudes con listas y tuplas
print(len(miOtroSet)) #retorna cantidad de elementos en el set
miOtroSet.remove("Alfaro") # podemos elminar una coincidencia dentro del set
print(miOtroSet)
miSet = miOtroSet.copy() # copiamos el set en otra variable
miSet.clear() # .clear limpia de datos la variable set
print(len(miSet)) # al estar limpia devuelve una longitud de 0 elementos
del miSet # elimina la variable miSet y todo su contenido dejando la variable undefined

# diferencias con listas y tuplas

# print(miOtroSet[0]) nos da un error al intentar acceder a un elemento del set mediante indice
miOtroSet.add("rojo") # un set no es una estructura ordenada y por eso mismo no podemos acceder por indice
miOtroSet.add("rojo") # un set no admite elemenetos repetidos por lo que ignora el add(elementoRepetido)
print(miOtroSet)
#para verificar la existencia de un elemento dentro de un set debemos 
print("Fernando" in miOtroSet) # devuelve true la comprobacion
print("fernandito" in miOtroSet) # devuelve false la comprobacion
miSet = {10,20,30,40}
print(miSet)
print(miOtroSet)
miSuperSet = miSet.union(miOtroSet) # al unirse dos sets se omiten los elementos repetidos
print(miSuperSet)
miSuperSet.union({"matanza" ," cudi"}) # agrega elementos no repetidos del set pasadao por parametro
print(miSuperSet.difference(miSet)) # imprime los valores que contiene set1 que carece set2



