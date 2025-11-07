#Exercici 3: Escriu un programa que llegeixi 10 nombres, quan acabi ha d'indicar si "hi havia almenys un nombre negatiu" o "no hi ha cap nombre negatiu".

#Creem una llista per guardar els nombres.
nombres = []
for i in range(10):
    num = int(input("Introdueix un nombre: "))
    nombres.append(num)

#Mira si hi ha algun nombre negatiu a la llista.
hi_ha_negatiu = False
for n in nombres:
    if n < 0:
        hi_ha_negatiu = True
        break

#Mostra el resultat dels nomnres introduits.
if hi_ha_negatiu:
    print("Hi havia un nombre negatiu.")
else:
    print("No hi ha cap nombre negatiu.")
