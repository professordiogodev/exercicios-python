
laranjas = 40

def comer_laranja():

    # buscar uma variável lá de fora
    global laranjas

    if (laranjas > 0):
        laranjas -= 1
        print(f"Comi, fiquei com {laranjas} 🍊.")

        # Chamar outra vez o comer laranja
        comer_laranja()
    else:
        print("acabaram-se as laranjas")


comer_laranja()