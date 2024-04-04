number1 = float(input("Ingresa el Primer Valor: "))

number2 = float(input("Ingresa el Segundo Valor: "))

eleccion = 0
while eleccion != 6:
    
    print("""
    Indique la operación a realizar:
    1. suma
    2. resta
    3. multiplicación
    4. división
    5. salir
    """)
    
    eleccion = int(input())
    if eleccion == 1:
        print(" ")
        print("Resultado:", number1, "+", number2, "=", number1 + number2)
    if eleccion == 2:
        print(" ")
        print("Resultado:", number1, "-", number2, "=", number1 - number2)
    if eleccion == 3:
        print(" ")
        print("Resultado:", number1, "*", number2, "=", number1 * number2)
    if eleccion == 4:
        print(" ")
        print("Resultado:", number1, "/", number2, "=", number1 / number2)
    if eleccion == 5:
        print("Gracias por participar")