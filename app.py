# Exercício:
# Os jogadores agora têm de ter mana
# Raquel, ao utilizar o spell, vai perder 5 de mana

# Inicializar Jogadores
diogo = {
    "hp": 40,
    "attack": 5,
    "defense": 3
}

raquel = {
    "hp": 50,
    "attack": 3,
    "defense": 5,
    "critatk": 3 * 2
}

# Turno 1
print("Diogo ataca Raquel!")
raquel["hp"] -= diogo["attack"] # Passas a ter 45 de hp

print("Raquel ataca Diogo!")
diogo["hp"] -= raquel["attack"] # Passa a ter 37 de hp

# Lógica do Game Over:
if diogo["hp"] < 0:
    print("Diogo Defeated!")
elif raquel["hp"] < 0:
    print("Raquel Defeated!")
else:
    print("O jogo continua... (ambos vivos)")

print(f"Raquel ficou com {raquel["hp"]} pontos de vida!")
print(f"Diogo ficou com {diogo["hp"]} pontos de vida!")

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

# Ex 4 - Os jogadores vão atacar-se de novo.
# O Diogo dá um ataque normal.
# A Raquel dá um ataque *crítico* - dá 2x o seu dano

# Diogo Ataca Raquel
print("Diogo ataca Raquel!")
raquel["hp"] -= diogo["attack"]

print("Raquel acerta um ataque crítico em Diogo")
diogo["hp"] -= raquel["critatk"]

print(f"Raquel ficou com {raquel["hp"]} pontos de vida!")
print(f"Diogo ficou com {diogo["hp"]} pontos de vida!")

# Ex 5 - Os jogadores vão atacar-se de novo.
# O Diogo dá um ataque normal.
# A Raquel dá um spell que se cura 12 pontos de vida e retira 1 ponto de *ataque* ao Diogo.

print("Diogo ataca Raquel!")
raquel["hp"] -= diogo["attack"]

print(f"0 hp de Raquel agora é de {raquel["hp"]}")

print("Raquel utiliza um spell")

#Raquel Spell
raquel["hp"] += 12
diogo["attack"] -= 1

print(f"Raquel ficou com {raquel["hp"]} pontos de vida!")
print(f"Diogo ficou com {diogo["hp"]} pontos de vida e {diogo["attack"]} pontos de ataque!")

# Ex maximus brutal: Implementar o TIE (ambos se derrotaram, empate)

if diogo["hp"] <= 0 and raquel["hp"] <= 0:
    print("Empate!")
else:
    print("O jogo continua... (ambos vivos)")