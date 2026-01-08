# Criar outros monstros e fazer a raquel combater cada um deles
# Obs. No final de cada nível, acrescentar o gold dos inimigos derrotados à Raquel

diogo = {
    "name": "Diogo",
    "hp": 60,
    "attack": 3
}

raquel = {
    "name": "Raquel",
    "hp": 50,
    "attack": 4,
    "gold": 0
}

slime = {
    "name": "Slime",
    "hp": 10,
    "attack": 2,
    "gold": 5
}

pixie = {
    "name": "Pixie",
    "hp": 20,
    "attack": 3,
    "gold": 7
}

# ... outros monstros ...

def attack(source, target):
    src = source["name"]
    trgt = target["name"]

    target["hp"] -= source["attack"]
    print(f"{src} atacou {trgt} que ficou com {target['hp']} pontos de vida!")


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
        print("O jogo continua... (ambos vivos)")
        return False



# Nível 1
while not is_gameover(raquel, slime):
    attack(raquel, slime)
    attack(slime, raquel)

# Nível 2
# A pixie cura-se 2 se tiver menos de 5 pontos de vida
while not is_gameover(raquel, slime):
    attack(raquel, pixie)

    # Lógica? não é só atacar...
    attack(pixie, raquel)


# Nível 3
# Raquel vs Goblin
# O goblin dá ataque crítico a cada dois turnos


# No fim do Nível 3, recuperar a vida da Raquel para nível máximo e subir de nível (+1 atk, +5 hp)


# Nível 4
# Raquel vs Troll
# O Troll reduz o ataque de raquel em 1 a cada turno
# No final da luta, não esquecer de retornar o ataque de raquel ao máximo


# Nível 5 - Raquel vs Diogo (Raquel agora tem o spell de cura)
# while not is_gameover(diogo, raquel):
#     # Turno do Diogo - diogo ataca raquel
#     attack(diogo, raquel)

#     # Turno da Raquel - raquel ataca diogo
#     if raquel["hp"] < 20:
#         raquel["hp"] += 100
#     else:
#         attack(raquel, diogo)
    
