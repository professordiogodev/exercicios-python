from game import attack

# Monstro 1 - Slime (apenas ataca)
def slime_attack(origin, target):
    attack(origin, target)

slime = {
    "name": "Slime",
    "hp": 10,
    "attack": 2,
    "gold": 5,
    "xp": 10,
    "attack_logic": slime_attack
}

# Monstro 2 - Pixe (Cura-se)
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
    "xp": 15,
    "attack_logic": pixie_attack
}

# Monstro 3 - Goblin (Dano Crítico)
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
    "gold": 20,
    "xp": 20,
    "has_critical": False,
    "attack_logic": goblin_attack
}

# Monstro 4 - Troll (Dá debuff)
def troll_attack(origin, target):
    attack(origin, target)
    target["attack"] -= 1
    if target["attack"] < 1:
        target["attack"] = 1
    print(f"{target["name"]} lost 1 Attack Point!")

troll = {
    "name": "Troll",
    "hp": 50,
    "attack": 6,
    "gold": 20,
    "xp": 40,
    "attack_logic": troll_attack
}

# Monstro 5 - Tomato (Explode)
def tomato_attack(origin, target):
    if origin["hp"] < 5:
        print("Tomato explodiu!")
        origin["hp"] = 0
        target["hp"] -= 20
    else:
        attack(origin, target)

tomato = {
    "name": "Tomato", 
    "hp": 12, 
    "attack": 1, 
    "gold": 15, 
    "xp": 25, 
    "attack_logic": tomato_attack
}

monsters = [slime, pixie, goblin, troll, tomato]