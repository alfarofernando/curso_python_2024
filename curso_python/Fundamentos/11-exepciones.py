### MANEJO DE ERRORES ###

numeroUno = 5
numeroDos = "1"

# python al no ser capaz de sumas un numero con un string nos da error. y rompe el programa no dejandolo continuar.
# print(numeroUno + numeroDos)

# si utilizamos un condicional if-else , no nos libramos del error anterior nisiquiera cuando la condicion es falsa
# if numeroUno > 3:
# a menos que se compruebe directamente sobre el tipo de dato que contiene una variable y como esa variable da false
# es que el programa no rompe porque no intenta la sumatoria lo que si daria error.
if type(numeroDos) == int:
    print(numeroUno + numeroDos)
else:
    print("no se cumple la condicion")

### TRY - EXCEPT ###
print()
print("TRY - EXCEPT")
print()
# a diferencia de un condicional el bloque try no lleva condiciones ni argumentos , solo es un bloque que se utiliza
#  para evaluar si nuestro codigo daria algun error que rompiera con la ejecucion de la aplicacion.
try:
    print("estamos en el bloque try")  # retorna este print porque no da error
    print(numeroDos + numeroUno)  # se captura el error en el bloque except
    # luego de la linea que da error, el codigo que restaba no es leido.
    print("linea despues del error")
# de ser asi, captura ese error en un bloque except donde le daremos instrucciones sobre que hacer en caso falle
# el bloque try
except:
    print("no se cumplio el try")


###  TRY - EXCEPT - ELSE  ###
print()
print("TRY - EXCEPT - ELSE")
print()

try:
    # print(numeroDos + numeroUno)  # se captura el error en el bloque except
    print(numeroUno + numeroUno)  # continua la ejecucion del bloque else
except:
    print("no se cumplio el segundo try")  # retorna mensaje al capturar un error
# el bloque else se ejecuta solamente si el bloque try finaliza sin capturar ningun error
else:
    print("la ejecucion continua correctamente")


### TRY - EXCEPT - ELSE - FINALLY ###
print()
print("TRY - EXCEPT - ELSE - FINALLY")
print()

try:
    # print(numeroDos + numeroUno) si forzamos un error en el blocke try podemos ver que se ejecuta finally
    print(numeroUno + numeroUno)  # sin errores podemos ver q se ejecuta finally
except:
    print("fallo el bloque try y se ejecuta blocke except")
else:
    print("se ejecuto blocke try sin errores y entra el blocke else en ejecucion")
# finally es un blocke de codigo que a diferencia de los blockes try y except,
# se ejecuta independientemente de si se capturo un error o no.
finally:
    print("estamos en el blocke finally")


### CAPTURA DE EXCEPCIONES POR TIPO ###
print()
print("CAPTURA DE EXCEPCIONES POR TIPO")
print()

# podemos tambien asignarle los tipos de errores que queremos que maneje el blocke except
# en este ejemplo. podemos realizar una excepcion del tipo de error TYPEERROR que nos da el sistema por no poder
# sumar un entero con un string;
# dejando de lado todos los demas posibles errores haciendo que la ejecucion se corte.
try:
    print(numeroUno + numeroDos)
    print("bloque try ejecutado correctamente")
# except ValueError: corta la ejecucion al no poder manejar el error
except TypeError:  # maneja el error y sigue con la ejecucion
    print("TypeError manejado bebe")
# se pueden colocar varios blockes except para scopear errores por tipos.
except ValueError:
    print("ValueError manejado pap")


### CAPTURA DE LA INFORMACION DE LA EXCEPTION ###
print()
print("CAPTURA DE LA INFORMACION DE LA EXCEPTION")
print()

try:
    print(numeroUno + numeroDos)
    print("bloque try ejecutado correctamente")
except TypeError as error:  # as nombre variable
    print(error)
# de esta manera no solo se maneja el error sino que guardamos en una variable la razon por la que se ejecuto el blocke except

try:
    print(numeroUno + numeroDos)
    print("bloque try ejecutado correctamente")
# asi como podiamos scopear los tipos de errores, podemos llamar a Exception as error para manejar los errores
# de forma generalizada y guardar la informacion dentro de una variable
except Exception as error:
    print(error)
