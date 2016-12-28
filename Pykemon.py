#Pykemon
from random import randint
#Variables
combate = True
partida = 0
pykemon = ""
rival = 0
pykemonVs = ""
decision = ""
turno = True
print("-----Pykemon!--------")
print("Bienvenido a Pykemon!")
print("Combatirás contra un pykemon misterioso, pero primero: ")
print("Selecciona tu Pykemon inicial: ")
print(" --Pykachu \n --Pynsir \n --Pydgey")

while partida != 1:
    pykemon = str(input())
    if pykemon == "Pykachu":
        print("----------------------")
        print("Has elegido a Pykachu!")
        nombreAtaque= " Impactrueno"
        vida = 100
        ataque = 10
        defensa = 8
        partida = 1
    elif pykemon == "Pynsir":
        print("---------------------")
        print("Has elegido a Pynsir!")
        nombreAtaque=" Tacleo"
        vida = 100
        ataque = 7
        defensa = 9
        partida = 1
    elif pykemon == "Pydgey":
        print("---------------------")
        print("Has elegido a Pidgey!")
        nombreAtaque=" Remolino"
        vida = 100
        ataque = 9
        defensa = 10
        partida = 1
    elif (pykemon != "Pykachu") and (pykemon !="Pynsir") and (pykemon !="Pydgey"):
        print("Por favor, elige a uno de los iniciales...")
        print(" --Pykachu \n --Pynsir \n --Pydgey")
        continue
#Juego
print("Tu "+pykemon+" esta listo para combatir")
#Rivales
rival = randint(1,3)
if rival == 1:
    pykemonVs = "Pyrmeleon"
    nombreAtaqueVs= " Flama"
    vidaVs = 100
    defensaVs = 9
    ataqueVs = 8
elif rival == 2:
    pykemonVs = "Pygikarp"
    nombreAtaqueVs= " Salpicadura"
    vidaVs = 100
    defensaVs = 6
    ataqueVs = 6
elif rival == 3:
    pykemonVs = "Pynix"
    nombreAtaqueVs= " Terremoto"
    vidaVs = 100
    defensaVs = 10
    ataqueVs = 9
print("-------------------------")
print(pykemonVs + " salvaje aparece!")
#Inicio de combate
print("-------------------------")
print("Los combates consisten en movimientos por turnos. \n En estos turnos puedes decidir entre:")
print("1-Atacar \n2-Defenderte")
print("-------------------------")
print("Tu vas primero. \n Listo?. \n YA!")
print("-------------------------")
print("Que deseas hacer primero?")
print("1-Ataca\n2-Defiende")
while combate == True:
    #Turno usuario
    while turno == True:
        if combate==True:
            decision = int(input())
            if decision == 1:
                print("*******************")
                print(pykemon+" ha utilizado "+nombreAtaque+" para atacar!")
                vidaVs = vidaVs-ataque
                if vidaVs <= 0:
                    combate = False
                    print("Has ganado!")
                    continue
            print(pykemonVs+" ahora tiene "+str(vidaVs)+" de salud!")
            print("--------------------")
            print("Es turno de "+pykemonVs)
            turno=False
        elif decision==2:
            print(pykemon+" se ha defendido")
            vida=vida+3
            print(pykemon+" vida actual: "+str(vida))
            print("--------------------")
            print("Es turno de "+pykemonVs)
            turno=False
        #Turno de pykemonVs
        while turno==False:
            decisionVs=randint(1,2)
            if decisionVs==1:
                print(pykemonVs+" ha utilizado"+nombreAtaqueVs+" para atacarte!")
                vida = vida-ataqueVs
                if vidaVs <= 0:
                    combate = False
                    print("Te han derrotado")
                print("Tu "+pykemon+" ahora tiene "+str(vida)+" de salud!")
                print("--------------------")
                print("Es tu turno")
                print("1-Ataca\n2-Defiende: ")
                turno = True
            elif decisionVs == 2:
                print(pykemonVs+" se ha defendido")
                vidaVs = vidaVs+3
                print(pykemonVs+" vida actual: "+str(vidaVs))
                print("--------------------")
                print("Es tu turno ")
                print("1-Ataca\n2-Defiende: ")
                turno = True
                continue

