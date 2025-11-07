#Exercici 2:

#Creem tres variables per a que l'usuari introdueixi tres numeros diferents.
numero1 = int(input("Introdueix el primer numero: "))
numero2 = int(input("Introdueix el segon numero: "))    
numero3 = int(input("Introdueix el tercer numero: "))

#Fem una condició per a saber quin numero es el mes gran utilitzant if, elif i else.
if numero1 >= numero2 and numero1 >= numero3:
    print("El numero mes gran es:", numero1)
elif numero2 >= numero1 and numero2 >= numero3:
    print("El numero mes gran es:", numero2)
else:
    print("El numero mes gran es:", numero3)