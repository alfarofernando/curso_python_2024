### CONDICIONALES ###
# los condicionales nos permiten alterar el flujo del programa.

###  IF  ###
# el condicional if nos permite encapsular codigo que solo se ejecutara si la condicion que maneja es verdadera.

miCondicion = True
if miCondicion:
    print("1ra linea impresa")

# si una variable tiene un valor asignado (que no sea expresamente un booleano) la condicion la toma como verdadera
miCondicion = 5 * 2
if miCondicion:
    print("2da linea impresa")

# si una variable no le fue asignado ningun valor se lo toma como falso
miCondicion = ""
if miCondicion:
    print("3ra linea impresa")

# miCondicion == valor estamos comprobando si nuestra variable es igual a un determinado valor.
miCondicion = 12
if miCondicion == 12:
    print("4ta linea impresa")
if miCondicion >= 10:
    print("5ta linea impresa")

if miCondicion <= 10:
    print("miCondicion contiene un numero menor o igual a 12")
else:
    print("miCondicion contiene un numero mayor que 10")

if miCondicion > 5 and miCondicion < 15:
    print(
        "al utiliar AND en dos condiciones ambas deben cumplirse para que la condicion sea verdadera"
    )

if 5 < miCondicion < 15:
    print("otra forma de utilizar una condicion a la hora de comprobar numeros.")

if miCondicion > 5 or miCondicion < 15:
    print(
        "esta condicion utiliza dos valores que si almenos uno da verdadero la condicion es verdadera"
    )

miCondicion = 10

if miCondicion > 10:
    print("numero mayor a 10")
elif miCondicion < 10:
    print("numero menor a 10")
else:
    print("el numero es exactamente 10")

if miCondicion != 10:
    print("el numero no es diez")
elif not miCondicion:
    print("miCondicion es falsa")
