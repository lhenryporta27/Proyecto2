"""Este módulo contiene funciones de saludo y suma."""


def saludo(nombre):
    """Imprime un saludo personalizado."""
    print("Hola, " + nombre)


def sumar(a, b):
    """Retorna la suma de dos números."""
    return a + b


def main():
    """Función principal que ejecuta el saludo y la suma."""
    saludo("Juan")
    resultado = sumar(3, 4)
    print("La suma es:", resultado)


if __name__ == "__main__":
    main()
