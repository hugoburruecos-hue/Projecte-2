#Training 5 Funcions


#Usarem def per definir funcions i posarem els exercicis dins de les funcions. 

#Exercici 1 Variables
def calcular_area_quadrat():
    midadelateral = float(input("Posa la mida lateral del quadrat: "))
    area = midadelateral * midadelateral
    print("L'area del quadrat es:", area)

#Exercici 2 Variables
def operacions_basiques(a, b):
    a = float(input("Numero 1: "))
    b = float(input("Numero 2: "))
    suma = a + b
    print("La suma es:", suma)

    resta = a - b
    print("La resta es:", resta)

    multiplicacio = a * b
    print("La multiplicació es:", multiplicacio)

    divisio = a / b
    print("La divisió es:", divisio)

#Exercici 3 Variables
def conectar_paraules():
    a = input("Escriu una paraula: ")
    b = input("Escriu una altra paraula: ")
    c = input("Escriu una ultima paraula: ")
    print("Les paraules concatenades son:", a + b + c)

#Exercici 4 Variables
def operacions_casting():
    x = int(1.6)
    z = int("3")

    suma = (x + z)
    resta = (z - x)

    print(x)
    print(z)
    print("La suma es:", suma)
    print("La resta es:", resta)

#Exercici 1 Bucles
def comptar_fins_a_numero():
    a=0
    for a in range(1, 201):
        if a % 2 == 0:
            print(a)

#Exercici 2 Bucles
def veure_notes():
    notes = 0
    nota10 = False
    while notes != -1:
        notes = int(input("Introdueix una nota del 0 al 10 o -1 per acabar: "))
        if notes == 10:
            nota10 = True
    if nota10:
        print("Hi ha hagut alguna nota que té un 10.")
    else:
        print("No hi ha hagut cap 10.")

#Exercici 3 Bucles
def nombres_negatius():
    nombres = []
    for i in range(10):
        num = int(input("Introdueix un nombre: "))
        nombres.append(num)

    hi_ha_negatiu = False
    for n in nombres:
        if n < 0:
            hi_ha_negatiu = True
            break

    if hi_ha_negatiu:
        print("Hi havia un nombre negatiu.")
    else:
        print("No hi ha cap nombre negatiu.")

#Exercici 1
def edad_usuari():
    a = input("Introduiex la teva edad:")
    if int(a) >= 18:
        print("Ets major d'edat")
    else:
        print("Ets menor d'edat")

#Exercici 2
def numero_mes_gran():
    numero1 = int(input("Introdueix el primer numero: "))
    numero2 = int(input("Introdueix el segon numero: "))    
    numero3 = int(input("Introdueix el tercer numero: "))

    if numero1 >= numero2 and numero1 >= numero3:
        print("El numero mes gran es:", numero1)
    elif numero2 >= numero1 and numero2 >= numero3:
        print("El numero mes gran es:", numero2)
    else:
        print("El numero mes gran es:", numero3)

#Exercici 3
def numero_positiu_negatiu():
    a=int(input("Introdueix un numero:"))

    if a <0:
        print("El numero es negatiu")
    else:
        print("El numero es positiu")

#Una vegada ja em posat els exercicis anteriors dins de les funcions, farem un menu per a poder triar quin exercici volem executar.

#Menu principal

#Utilitzarem un bucle while per a que el menu es repeteixi fins que l'usuari vulgui sortir.

#Utilitzarem un match-case per a gestionar les diferents opcions del menu.
while True:
    print("\nMenu d'Exercicis:")
    print("1. Calcula l'area d'un quadrat")
    print("2. Operacions basiques amb dos numeros")
    print("3. Concatena tres paraules")
    print("4. Operacions amb casting")
    print("5. Comptar fins a 200 els nombres parells")
    print("6. Veure si hi ha un 10 entre les notes")
    print("7. Comprovar si hi ha nombres negatius")
    print("8. Comprovar si ets major d'edat")
    print("9. Trobar el numero mes gran entre tres numeros")
    print("10. Comprovar si un numero es positiu o negatiu")
    print("0. Sortir")

    opcio = input("Tria una opcio (0-10): ")
    match opcio:
        case '1':
            calcular_area_quadrat()
        case '2':
            operacions_basiques(0, 0)
        case '3':
            conectar_paraules()
        case '4':
            operacions_casting()
        case '5':
            comptar_fins_a_numero()
        case '6':
            veure_notes()
        case '7':
            nombres_negatius()
        case '8':
            edad_usuari()
        case '9':
            numero_mes_gran()
        case '10':
            numero_positiu_negatiu()
        case '0':
            print("Sortint del programa...")
            break
        case _:
            print("Opcio no valida, torna-ho a intentar.")