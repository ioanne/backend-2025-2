lista = [1,2,3,3]
id(lista) # Consultamos la posición en memoria

VALOR_FIJO: int = 100 # Constante
entero: int = 10 # int
flotante: float = 10.1 # float
cadena_texto: str = "Hola" # str | Snake case
lista: list = [1,2] # lista
conjunto: set = {1,2,3} # set
diccionario: dict = {1:1} # dict
tupla: tuple = (1,2) # tuple

nombre = "Pedro"
cadena = f"Hola {nombre}"


# funcion
def foo() -> None:
    print("ejecutando Foo")

def foo2(foo: function) -> None:
    print("ejecutando Foo2")
    foo()


def print2(printgg):
    printgg("Hola!!")


def foo(a,b,c,d=10,*args,**kwargs):
    print(a,b,c)
    print(args) # tuple
    print(kwargs) # diccionario




def mi_funcion(a,b,c,d,e):
    print(a,b,c,d,e)

mi_funcion(1,2,3,4,5)


def mi_funcion(a=1,b=2,c=3,d=4,e=5):
    print(a,b,c,d,e)

def mi_funcion(a,b,d,e=5,c=10):
    print(a,b,c,d,e)

mi_funcion(1,2,3,4,5)
mi_funcion(1,2,3)
mi_funcion(1,2,3,e=4,c=5)
mi_funcion(1,2,3,c=5,e=4)


def mi_funcion(a,b,c):
    print(a,b,c)

mi_funcion(1,2,3)
mi_funcion(1,2,c=10)
mi_funcion(a=1,b=2,c=10)
mi_funcion(c=1,a=2,b=10)
    
def foo(a,b,c=None):
    print(a,b,c)

foo(1,2)

foo2(print)
"""
str ->       entero int("100")
float ->     entero int(2.0)

int -> str   str(100)
"""
def es_mayor_18(edad):
    if edad > 18:
        print("Mayor de 18")
    else:
        print("Menor de 18")

validaciones = {
    "mayor_18": es_mayor_18
}

variable = "mayor_18"
edad = 10

estructura = [("mayor_18", 20), ("mayor_18", 12), ("mayor_18", 10)]

for dato in estructura:
    validacion, edad = dato
    try:
        validaciones[validacion](edad)
    except KeyError:
        print("No existe validacion")
