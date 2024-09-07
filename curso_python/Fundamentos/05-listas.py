### LISTAS ###
# el tipo de dato lista es un array con metodos propios

#constructores de listas
miLista = list() # list() vacia la variable lista del contenido
miOtraLista = [] # al asignar [] a una variable tambien definimos la variable como te tipo lsita

# con [ valor1 , valor2 , valor3] creamos un array de elementos
miLista = [30 , 24, 45, 20 ,23 , 23 , 17]

# en python no infiere el tipo de dato guardado en un array
miOtraLista = [35 , 1.84 , "Fernando", "Alfaro"]
# al utilizar el metodo type() nos devuelve que la varialbe es tel tipo lista
print(type(miOtraLista))

# podemos imprimir los elementos de la lista llamndo a sus indices
# las listas como los arrays le dan indice 0 al primer elemento
print(miOtraLista[1]) # retorna segundo elemento de la lista con indice 1
# asi mismo le dan indice -1 al ultimo elemento de la lista
print(miOtraLista[-1]) # retorna cuarto elemento de la lista con indice 3
# si colocamos un indice fuera del rango nos devuelve el error= list index out of range

# podemos buscar coincidencias en nuestra lista con .count()
print(miLista.count(23)) # como el valor 23 esta repetido dos veces me devuelve 2
print(miOtraLista.count("Fernando")) # tambien podemos buscar srings

# podemos asignarle los elementos de una lista a variables
# teniendo en cuenta que al definir nuestras variables , estas tomaran el mismo orden
# que el indice de los elementos dentro de la lista
edad, altura, nombre , apellido = miOtraLista
# edad, altura, nombre = miOtraLista
# si no damos la cantidad de variables para todos los elementos, da un error de unpack
print(nombre)

# tambien se pueden concatenar listas
superLista = miLista + miOtraLista
print(miLista + miOtraLista)
print(superLista)

# tambien hay que tener en cuenta que python al ser un lenguaje dinamico nos permite
# cambiar el tipo de dato
superLista = "hola mundo"
# pasando de haber declarado una variable como lista 
# pero luego cambiarle el tipo de dato como un string u otro
# lo que puede ser un hervidero de errores al ser debilmente tipado.

# no existen las constantes pero por convencion 
# se indica la variable toda en mayusculas e iniciando con CONST_
CONST_NOMBREDELACONSTANTE = "constante"

# append(elemento) agrega el elemento indicado por parametro a una lista
print(miOtraLista) # retorna lista con 4 elementos
miOtraLista.append("CUDI") # agregamos elemento nuevo al final
print(miOtraLista) # retorna lista con 5 elementos 

# insert(indice,elemento) agrega un elemento en el indice indicado
# esto empuja los otros elementos al indice siguiente
miOtraLista.insert(1 , "azul")
print(miOtraLista)

# remove(elemento) elimina la primer coincidencia desde el indice 0 de una lista
miLista.remove(23) # retorna la lista habiendo eliminado el 23 del indice 4 
print(miLista)

# pop() elimina el ultimo elemento de la lista
miLista.pop()
print(miLista)

# para eliminar un elemento en concreto 
# del nombreLista[indiceAEliminar]
del miLista[2]
print(miLista) 

# podemos cambiar el valor de un elemento dentro de una lista 
# llamando a la lista[indiceACambiar] = nuevoValor
miOtraLista[1] = "rojo"
print(miOtraLista)

# podemos copiar una lista de dos maneras : 
# creando una nueva variable y asignarle como valor una lista
miNuevaLista = miLista
# creando una nueva variable y asignarle como valor una lista adozandole el .copy() 
miOtraNuevaLista = miLista.copy()
print(miNuevaLista)
print(miOtraNuevaLista)

# con clear() podemos elminiar el contenido de una lista
miOtraNuevaLista.clear()
print(miOtraNuevaLista)

# con .reverse() podemos invertir los indices de los elemntos
miNuevaLista.reverse()
print(miNuevaLista)

# con .sort() por defecto ordenamos la lista de menor a mayor
miLista.sort()
print(miLista)
# podemos agregar por parametro el atributo reverse que
# reverse = False nos devuelve la lista de menor a mayor
# reverse = True nos devuelve la lista de mayor a menor
miLista.sort(reverse=True)
print(miLista)
# el sort() solo sirve elementos del mismo tipo de dato por lo que al intentarlo con 
#  una lista que contenga numeros y strings la misma nos devolvera un typeerror 
# miOtraLista.sort(reverse=False)
# print(miOtraLista)

# probamos con una lista de strings
listaStrings = ["azul" , "rojo" , "naranja" , "morado" , "negro" , "blanco"]
print(listaStrings)
listaStrings.sort()
print(listaStrings)
# devolviendonos la lista ordenada de menor a mayor teniendo en cuenta el valor ASCII 
# sumado de todos los caracteres
# por lo que si ingresamos un elemento con valor aaaa y un elemento con valor zzzz
# el primero estara en el primer indice  y el otro en el ultimo indice
listaStrings.append("aaaa")
listaStrings.append("zzzz")
print(listaStrings)
# pudiendo ahora si utilizar el atributo reverse para manipular el orden de los elementos
listaStrings.sort(reverse=False)
print(listaStrings)
listaStrings.sort(reverse=True)
print(listaStrings)



