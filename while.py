# Criar outros monstros e fazer a raquel combater cada um deles
# Obs. No final de cada nível, acrescentar o gold dos inimigos derrotados à Raquel

# Trabalho a Seguir - Tentar Implementar Pontos de Experiência e Níveis
experiencia_por_nivel = [50, 100, 200, 400, 800, 1600]

#                        1,  2,   3,   4,   5,   6
#  (só que no array ->)  0,  1,   2,   3,   4,   5

# Tou no nível 2 - preciso de 100xp
# if raquel["xp"] > experiencia_por_nivel[nivel - 1]:
#   subir_nivel(raquel)

def subir_nivel(player):
    # Restaurar Pontos de Vida
    player["hp"] = player["max_hp"]
    player["max_attack"] += 1
    player["attack"] += 1

# Função de Atacar
def attack(source, target, is_critical = False):
    src = source["name"]
    trgt = target["name"]

    if not is_critical:
        target["hp"] -= source["attack"]
        print(f"{src} atacou {trgt} que ficou com {target['hp']} pontos de vida!")
    else:
        # Ataque crítico
        target["hp"] -= source["attack"] * 2
        print(f"CRITICO - {src} atacou {trgt} que ficou com {target['hp']} pontos de vida!")
        
# Função de GameOver
def is_gameover(player1, player2):

    p1 = player1["name"]
    p2 = player2["name"]
    p1_hp = player1["hp"]
    p2_hp = player2["hp"]

    # Lógica do Game Over:
    if p1_hp <= 0 and p2_hp <= 0:
        print("Tie!")
        return True
    elif player1["hp"] < 0:
        print(p1 + " Defeated!")
        return True
    elif player2["hp"] < 0:
        print(p2 + " Defeated!")
        return True
    else:
        # O jogo continua... (ambos vivos)
        return False


def raquel_attack(origin, target):
    attack(origin, target)
    # Habilidade da Raquel - Curar-se 1 ponto de vida a cada ataque
    print(f"{origin["name"]} curou-se 1 hp!")
    origin["hp"] += 1

raquel = {
    "name": "Raquel",
    "hp": 50,
    "max_hp": 50,
    "attack": 4,
    "max_attack": 4,
    "gold": 0,
    "nivel": 1,
    "attack_logic": raquel_attack
}

def slime_attack(origin, target):
    attack(origin, target)

slime = {
    "name": "Slime",
    "hp": 10,
    "attack": 2,
    "gold": 5,
    "attack_logic": slime_attack
}

def pixie_attack(origin, target):
    if origin["hp"] < 5:
        origin["hp"] += 2
        print(f"{origin["name"]} curou-se +2 HP")
    else:
        attack(origin, target)

pixie = {
    "name": "Pixie",
    "hp": 20,
    "attack": 3,
    "gold": 7,
    "attack_logic": pixie_attack
}

goblin_has_critical = False

def goblin_attack(origin, target):

    global goblin_has_critical

    attack(origin, target, goblin_has_critical)
    
    if not goblin_has_critical:
        # Passar a ter crítico no turno a seguir
        goblin_has_critical = True
    else:
        # Tem crítico - passa a não ter no turno a seguir
        goblin_has_critical = False

goblin = {
    "name": "Goblin",
    "hp": 15,
    "attack": 3,
    "gold": 10,
    "has_critical": False,
    "attack_logic": goblin_attack
}

def troll_attack(origin, target):
    attack(origin, target)
    target["attack"] -= 1
    print(f"{target["name"]} lost 1 Attack Point!")

troll = {
    "name": "Troll",
    "hp": 50,
    "attack": 6,
    "gold": 20,
    "attack_logic": troll_attack
}

monsters = [slime, pixie, goblin, troll]

for monster in monsters:
    while not is_gameover(raquel, monster):

        while True:
            print(f"Monstro {monster["name"]} vai atacar!")
            print("O que vai Raquel fazer?")
            print("a) Atacar")
            print("b) Curar-se")
            print("c) Spell")
            opção = input("Opção > ")
            if opção == "a":
                print("Raquel ataca")
                raquel["attack_logic"](raquel, monster)
                break
            elif opção == "b":
                print("Raquel cura")
                # raquel["heal"] <- Falta Implementar !!!!
                break
            elif opção == "c":
                print("Raquel spell")
                # raquel["spell"] <- Falta Implementar !!!!!!!!
                break
            

        monster["attack_logic"](monster, raquel)
        print("-- Turn End -- \n")

    print("\n -- BATTLE END -- \n")


# Criar um monstro Tomato, se tiver menos de 5 hp, explode (morre e tira 20hp)


# Dar a possibilidade da Raquel:
# a. Atacar
# b. Curar-se
# c. Usar Spell


# Depois de cada luta, Raquel recupera 5hp.
