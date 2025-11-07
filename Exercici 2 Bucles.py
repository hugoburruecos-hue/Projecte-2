#Exercici 2: Escriu un programa que llegeixi una seqüència de notes (valors de 0 a 10) i finalitzarà la seqüència amb el valor -1. Quan finalitzi ens ha d'indicar si "Hi ha hagut alguna nota que té un 10" o "No hi ha cap 10".

#Creem la variable notes per guardar les notes introduides.
notes = 0

# Creem la variable nota10 per controlar si hi ha hagut un 10.
nota10 = False

# Usem un bucle while per llegir les notes fins que s'introdueixi -1 i utilitzem un if per comprovar si hi ha hagut un 10.
while notes != -1:
    notes = int(input("Introdueix una nota del 0 al 10 o -1 per acabar: "))
    if notes == 10:
        nota10 = True

# Un cop finalitzat el bucle, utilitzem un if per mostrar el missatge si hi ha hagut algun 10 o no.
if nota10:
    print("Hi ha hagut alguna nota que té un 10.")
else:
    print("No hi ha hagut cap 10.")

