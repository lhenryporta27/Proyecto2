"""Este módulo contiene funciones básicas de una calculadora."""


def multiplicar(a, b):
    """Retorna el producto de dos números."""
    return a * b


def dividir(a, b):
    """Retorna la división de dos números, si el divisor no es cero."""
    if b == 0:
        return "Error: división por cero"
    return a / b


def main():
    """Función principal para ejecutar las operaciones."""
    num1 = 6
    num2 = 3

    producto = multiplicar(num1, num2)
    division = dividir(num1, num2)

    print(f"{num1} * {num2} = {producto}")
    print(f"{num1} / {num2} = {division}")


if __name__ == "__main__":
    main()
