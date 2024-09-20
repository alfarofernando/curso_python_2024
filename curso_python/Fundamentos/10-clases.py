### CLASES ###


class PersonaVacia:
    pass


class MiPersona:  # definimos clase
    def __init__(
        self, nombre, apellido
    ):  # __init__ crea constructor de clase donde se definen los parametros que va a aceptar la misma
        self.nombre = nombre  # self seria como this.propiedad
        self.apellido = apellido  # la logica seria que el self.parametro = creaamos variable donde se guardara ese valor que nos llega


persona01 = MiPersona("fernando", "alfaro")
print(persona01.nombre, persona01.apellido)


class OtraPersona:  # definimos otra clase persona
    def __init__(self, nombre, apellido):  # definimos otro constructor
        # tambien podemos decirle que cree una variable y que guarde en ella los valores que le llegar por parametro
        self.nombre_completo = f"{nombre} {apellido}"


persona02 = OtraPersona("Denise", "Luana")
# de esta manera a la hora de llamar a los atributos que tiene nuestro objeto no podremos acceder directamente
# a los dos valores que le dimos por parametro a la hora de crear al objeto en cuestion; sino que
# solo podremos acceder al atributo que definimos en nuestro constructor como "nombre_completo"
print(persona02.nombre_completo)


class Perro:
    def __init__(self, nombre, apodo):
        self.nombre = nombre
        self.nombre = apodo
        self.nombre_apodo = f"{nombre} {apodo}"

    def camina(self):
        # al definir un metodo este puede aceptar parametros, cuando los parametros que aceptan los metodos
        # provienen del mismo constructor de clase, se le coloca self para luego extraer los valores que precisa de
        # los parametros dados en al construccion del objeto
        print(f"{self.nombre_apodo} camina hacia su cucha")


perro = Perro("chucho", "canucho")
perro.camina()


class Pajaro:
    def __init__(
        self, nombre="pajaruuuu"
    ):  # si en el constructor le doy un valor por defecto luego en la construccion del objeto
        # va a ser un parametro que no voy a tener que darle si o si aunque si acepta que le pasemos un valor por parametro
        # el cual sobreescribira el valor por defecto que tenia el constructor.
        self.nombre = nombre

    def echar_pajaro(self):
        print(f"juuuuiiiiiraaa {self.nombre}")


pajarito = Pajaro()
pajarito.echar_pajaro()


class Gato:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # al colocar __atributo lo que creamos es una variable privada que solo puedo acceder mediante la creacion de un metodo
        self.__edad = edad  # propiedad privada

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre
        return self.__nombre


gatito = Gato("michi")  # instanciamos objeto y le damos un nombre por parametro
print(
    gatito.get_nombre()
)  # accedemos al metodo get_nombre para acceder a dicho parametro

gatito.set_nombre(
    "naranjita"
)  # accedemos al metodo set_nombre para cambiar el valor de la propiedad nombre
print(
    gatito.get_nombre()
)  # imprimimos y comprobamos que se alla cambiado satisfactoriamente,.
