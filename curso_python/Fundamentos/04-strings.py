### STRINGS ###

miString = "mi string"
miOtroString = "mi otro string"

# len() devuelve cantidad de caracteres de un string
print(len(miString))
print(len(miOtroString))

# podemos concatenar strings
print(miString + " " + miOtroString) 

# \n realiza salto de linea  
stringConSaltoDeLinea = "este es un string \n con un salto de linea"
print(stringConSaltoDeLinea)

# \t realiza una tabulacion
stringConTabulacion = "este string contiene una \t tabulacion " 
print(stringConTabulacion)

# \\ realiza un escapado de linea
stringConEscapado = " \\t este string tiene \\n escapado de linea"
print(stringConEscapado)

### FORMATEO ###

# creamos dos variables separandolas con , y asignandoles valor a cada una separandolas
# con , tambien
nombre , apellido , edad = "fernando" , "alfaro" , 30

# llamamos a las variables dentro del print de tres maneras
# la primera con el metodo format indicando la posicion de las varialbes con {} 
# y llamandolas al final del string 
print("mi nombre es {} , mi apellido es {} y mi edad es {}".format(nombre,apellido,edad))
# podemos llamar las variables como si de C se tratase %s string %d int %f float %b bool
print("mi nombre es %s , mi apellido es %s y mi edad es %d" %(nombre,apellido,edad))
# o con interpolacion de variables agregandole f delante de las comillas y llamando
# a las variables dentro de llaves {}
print(f"mi nombre es {nombre} , mi apellido es {apellido} ,mi edad es {edad}")

### unpack de caracteres ###

lenguaje = "python"
# al asignar dos variables a un string, python interpreta que queres guardar cada caracter
#del string en una variable diferente por lo que te solicita crees
# la cantidad de variables adecuadas, como python contiene 6 caracteres el lenguaje
# necesita de 6 variables diferentes
a , b,c,d,e,f = lenguaje
# ahora al imprimir las variables nos devuelve en consola la letra guardada en el mismo
# orden que indicamos en la creacion de variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

### DIVISION DE STRINGS ###
# podemos indicar la posicion desde donde queremos que corte un string 
# con [posicionDesde : posicionHasta]
lenguajeCortado = lenguaje[1:3]
print(lenguajeCortado)
# si solo dejamos [posicionDesde : ] nos imprime desde el indice indicado hasta el final 
lenguajeCortado = lenguaje[1:]
print(lenguajeCortado)
# si solo dejamos [ : posicionHasta] nos imprime desde el indice 0 hasta el indice indicado
lenguajeCortado = lenguaje[:3]
print(lenguajeCortado)
# con un numero negativo [ indiceNegativo ] nos cuenta la cantidad de espacios desde el final 
# y luego imprime esa letra 
lenguajeCortado = lenguaje[-2]
print(lenguajeCortado)

### REVERSE STRINGS ###
lenguajeAlReves = lenguaje [ :: -1]
# para imprimir al reves los strings basta con asignarles este indice a la variable [ :: -1 ]
print(lenguajeAlReves) 

### METODOS ###
# capitalize() muestra la primera letra en mayuscula
print(lenguaje.capitalize())
# upper() muestra todo en mayusculas
print(lenguaje.upper())
# count (caracter/string a buscar) cuenta las coincidencias en un string
print(lenguaje.count("t")) 
# devuelve un buleano al comprobar si la variable es un numero
print(lenguaje.isnumeric()) #devuelve false
print("1".isnumeric()) # devuelve true
# lower() pasa el string en minusculas
print(lenguaje.lower())
# tambien tenemos el metodo isupper() que devuelve un booleano al comprobar si 
# el string esta en mayusculas
print(lenguaje.upper().isupper()) # devuelve true
# aunque isupper solo devuelve true si TODO el string esta en mayusculas
print(lenguaje.capitalize().isupper()) # devuelve false
# tambien podemos verificar si un string comienza con determinados caracteres
# con el metodo startswith("CARACTERES A COMPROBAR")
print(lenguaje.startswith("py")) #retorna true
