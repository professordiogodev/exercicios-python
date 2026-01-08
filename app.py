# Exercício:
# Os jogadores agora têm de ter mana
# Raquel, ao utilizar o spell, vai perder 5 de mana

# Inicializar Jogadores
diogo = {
    "name": "Diogo",
    "hp": 40,
    "attack": 5,
    "defense": 3,
    "mana" : 50
}

def heal_spell(origin, target):
    #Raquel Spell
    origin["hp"] += 12
    origin["mana"] -= 5
    target["attack"] -= 1

    print(f"{origin["name"]} ficou com {origin["hp"]} pontos de vida e {origin["mana"]} de mana!")
    print(f"{target["name"]} ficou com {target["hp"]} pontos de vida e {target["attack"]} pontos de ataque!")

raquel = {
    "name": "Raquel",
    "hp": 50,
    "attack": 3,
    "defense": 5,
    "critatk": 3 * 2,
    "mana" : 50,
    "spell": heal_spell
}

def attack(source, target):
    src = source["name"]
    trgt = target["name"]
    
    # Lógica do Ataque
    print(f"{src} ataca {trgt}!")
    target["hp"] -= source["attack"]
    print(f"{trgt} ficou com {target["hp"]} pontos de vida!")

# Code Smell - estamos a violar o princípio DRY
def crit_attack(source, target):
    src = source["name"]
    trgt = target["name"]
    
    # Lógica do Ataque
    print(f"{src} ataca {trgt}!")
    target["hp"] -= source["critatk"] # desta vez, raquel ataca com critak em vez de ataque
    print(f"{trgt} ficou com {target["hp"]} pontos de vida!")

def is_gameover(player1, player2):

    p1 = player1["name"]
    p2 = player2["name"]
    p1_hp = player1["hp"]
    p2_hp = player2["hp"]

    # Lógica do Game Over:
    if p1_hp <= 0 and p2_hp <= 0:
        print("Tie!")
    elif player1["hp"] < 0:
        print(p1 + " Defeated!")
    elif player2["hp"] < 0:
        print(p2 + " Defeated!")
    else:
        print("O jogo continua... (ambos vivos)")


# Turno 1
attack(diogo, raquel) # Passas a ter 45 de hp
attack(raquel, diogo) # Passa a ter 37 de hp
is_gameover(diogo, raquel)
print("------------------------")

# Turno 2

attack(diogo, raquel)
crit_attack(raquel, diogo)
is_gameover(diogo, raquel)
print("------------------------")

# Turno 3

attack(diogo,raquel)
raquel["heal_spell"](raquel, diogo)
is_gameover(diogo, raquel)
print("------------------------")







"""
Todo - Implementar lógica dos pontos de defesa
# Cálculo do ataque em função da defesa
if diogo["defense"] > raquel["attack"]:
    diogo["hp"] -= 0
elif diogo["defense"] < raquel["attack"]:
    diogo["hp"] -= (raquel["attack"] - diogo["defense"])

if raquel["defense"] > diogo["attack"]:
    raquel["hp"] -= 0
elif raquel["defense"] < diogo["attack"]:
    raquel["hp"] -= (diogo["attack"] - raquel["defense"])

print(f"Raquel ficou com {raquel["hp"]} pontos de vida!")
print(f"Diogo ficou com {diogo["hp"]} pontos de vida!")
"""