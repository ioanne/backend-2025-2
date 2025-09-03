def foo(funcion, param):
    return funcion(param)


foo(print)

funcionalidades = {
    "print": print,
    "int": int,
}


run = funcionalidades.get("print")
run("Hola mundo") if run is not None else None