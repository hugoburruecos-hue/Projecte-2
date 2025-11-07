#Exercici 1: Realitza un programa que mostri tots els nombres parells que hi ha entre 1 i 200. 

#Creem la variable a on guardarem els nombres parells
a=0

#Usem un bucle for per recórrer els nombres de l'1 al 200 i comprovem si són parells amb el if el % i despres els imprimim.
for a in range(1, 201):
    if a % 2 == 0:
        print(a)
