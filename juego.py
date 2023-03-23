import random

while True:
    aleatorio = random.randrange(0,3)
    elijePc = ""
    print("1. Piedra")
    print("2. Papel") 
    print("3. Tijera")
    opcion = int(input("Elige tu opcion "))
    
    if opcion == 1:
        eligeUsuario = "Piedra"
    elif opcion == 2:
        eligeUsuario = "Papel" 
    elif opcion == 3:
        eligeUsuario = "Tijera"
    print("Elegiste: ", eligeUsuario)
    
    if aleatorio == 1:
        eligePc = "Piedra"
    elif aleatorio == 2:
        eligePc= "Papel" 
    elif aleatorio == 3:
        eligePc = "Tijera"
    print("La maquina eligio: ", eligeUsuario)
    print("...")
    
    if eligePc == "Piedra" and eligeUsuario == "Papel":
        print("Ganaste, Papel envuelve Piedra")
    elif eligePc == "Papel" and eligeUsuario == "Tijera":
        print("Ganaste, Tijera corta Papel")
    elif eligePc == "Tijera" and eligeUsuario == "Piedra":
        print("Ganaste, Piedra machaca Tijera")
    if eligePc == "Papel" and eligeUsuario == "Piedra":
        print("Perdiste, Papel envuelve Piedra")
    elif eligePc == "Tijera" and eligeUsuario == "Papel":
        print("Perdiste, Tijera corta Papel")
    elif eligePc == "Piedra" and eligeUsuario == "Tijera":
        print("Perdiste, Piedra machaca Tijera")
    elif eligePc == eligeUsuario:
        print("Empate")