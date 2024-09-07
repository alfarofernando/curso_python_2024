### TUPLAS ###

# podemos definir una tupla con el constructor tuple
miTupla = tuple()
# tambien podemos definirla asignando () a una variable
miOtraTupla = ()

# le asignamos valores a nuestras tuplas
miTupla = (30 , 184 , "Fernando" , "Alfaro")
miOtraTupla = (10,20,30,40,50,60)
print(miTupla)
print(miOtraTupla)

# nos devuelve un objeto del tipo tupla
print(type(miTupla))
print(type(miOtraTupla))
# comparten similitudes con las listas
print(miTupla[0]) #imprime valor en primer indice
print(miTupla[-1]) # imprimer valor en ultimo indice
print(miTupla.count(30)) # retorna 1 coincidencia
print(miTupla.index("Fernando")) # indes(parametro) retorna el primer indice de parametro dado
print(miTupla + miOtraTupla) # se nos permite concatenar tuplas
miSuperTupla = miTupla + miOtraTupla # podemos asignar a una nueva tupla concatenaciones de tuplas
print(miSuperTupla)
print(miSuperTupla[3:8]) # podemos cortar las tuplas


# la diferencias mas grande con respecto a las listas
# las tuplas son inmutables por lo que una vez inicializada de una forma no es posible cambiarla
# miTupla[1] = 1.85 retorna typeError ya que la tupla no soporta la asignacion de elementos

# podemos transformar una tupla logrando sortear la inmutabilidad de esta y modificarla
# aunque realzar esta operacion ES UNA MALA PRACTICA DE PROGRAMACION
miTupla = list(miTupla) # convertimos la tupla en lista
print(type(miTupla)) # retorna tipo lista
miTupla.insert(1,"celeste") # agregamos en el indice 1 el elemento "celeste"
miTupla = tuple(miTupla) # transformamos nuevamente la lista en tupla
print(type(miTupla)) # nos devuelve tipo tupla
print(miTupla) # nos imprime todos los elementos incluido el agregado durante la transformacion en lista

# podemos intentar guardar un solo string en una tupla para simular una "constante"
# pero hay que tener en cuenta que se debe colocar la , al final para poder acceder al valor guardado 
# con el indice 0 quedando tupla[0] 
url = tuple("http://aguanteBrown.com",) 
print(url)
# pero la misma no guardara un string en si, sino que guardara un array de caracteres

# al intentar utilizar la palabra reservada del tenemos dos interacciones
# del miTupla[-1] el cual da error ya que siguiendo la inmutabilidad no se pueden eliminar los elementos de la misma
# pero si utilizamos del nombreTupla esta nos deja la variable undefined lo que provoca un error
# del miTupla
# print(miTupla)



