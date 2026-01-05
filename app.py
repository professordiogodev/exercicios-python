# Criar stats para dois personagens
# Fazer um personagem atacar outro (sem funções)

# Variáveis para Diogo
diogo_hp = 40
diogo_attack = 5
diogo_defense = 3

# Variáveis para Raquel
raquel_hp = 50
raquel_attack = 3
raquel_defense = 5

# Resolução Ex 2:
# Diogo Ataca Raquel
print("Diogo ataca Raquel!")
raquel_hp -= diogo_attack # Passas a ter 45 de hp

# Raquel Ataca Diogo
print("Raquel ataca Diogo!")
diogo_hp -= raquel_attack # Passas a ter 45 de hp


# Lógica do Game Over:
if diogo_hp < 0:
    print("Diogo Defeated!")
elif raquel_hp < 0:
    print("Raquel Defeated!")
else:
    print("O jogo continua... (ambos vivos)")



print(f"Raquel ficou com {raquel_hp} pontos de vida!")
print(f"Diogo ficou com {diogo_hp} pontos de vida!")


# 🟣 Para cada exercício:
# 🟣 Até 15 minutos a tentar, se não der, pedir ajuda da AI

# ⚠️ Ex 3 - Problema a resolver: Se a defesa for maior do que o ataque, o adversário cura-se... 🥶 Devia só dar 0 de dano
## Podes resolver isto utilizando um if, por exemplo:
###### Se a defesa for maior do que o ataque, retirar apenas 0
###### Se a defesa for menor que o ataque, retirar (ataque - defesa) - é o que a gente já tem

# Ex 4 - Os jogadores vão atacar-se de novo.
# O Diogo dá um ataque normal.
# A Raquel dá um ataque *crítico* - dá 2x o seu dano


# Ex 4 - Os jogadores vão atacar-se de novo.
# O Diogo dá um ataque normal.
# A Raquel dá um ataque *crítico* - dá 2x o seu dano


# Ex 5 - Os jogadores vão atacar-se de novo.
# O Diogo dá um ataque normal.
# A Raquel dá um spell que se cura 12 pontos de vida e retira 1 ponto de *ataque* ao Diogo.


# Ex maximus brutal: Implementar o TIE (ambos se derrotaram, empate)
