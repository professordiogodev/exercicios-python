# No turno da raquel, se ela tiver menos de 20 de vida, curar-se com 100 pontos de vida.

#Jogadores

diogo = {
    "name": "Diogo",
    "hp": 60,
    "attack": 3
}

raquel = {
    "name": "Raquel",
    "hp": 50,
    "attack": 4
}

def attack(source, target):
    src = source["name"]
    trgt = target["name"]

    target["hp"] -= source["attack"]
    print(f"{src} atacou {trgt} que ficou com {target['hp']} pontos de vida!")

while diogo["hp"] > 0 and raquel["hp"] > 0:
    # Turno do Diogo - diogo ataca raquel
    attack(diogo, raquel)

    # Turno da Raquel - raquel ataca diogo
    if raquel["hp"] < 20:
        raquel["hp"] += 100
    else:
        attack(raquel, diogo)
    

# Lógica do Game Over:
if diogo["hp"] <= 0 and raquel["hp"] <= 0:
    print("Tie!")
elif diogo["hp"] <= 0:
    print("Diogo Defeated!")
elif raquel["hp"] <= 0:
    print("Raquel Defeated!")