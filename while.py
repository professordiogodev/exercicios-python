# No turno da raquel, se ela tiver menos de 20 de vida, curar-se com 100 pontos de vida.
diogo_hp = 60
raquel_hp = 50
diogo_attack = 3
raquel_attack = 4

while diogo_hp > 0 and raquel_hp > 0:
    # Turno do Diogo - diogo ataca raquel
    raquel_hp -= diogo_attack
    print(f"Diogo atacou Raquel, que ficou com {raquel_hp}")
    # Turno da Raquel - raquel ataca diogo
    diogo_hp -= raquel_attack
    print(f"Raquel atacou Diogo, que ficou com {diogo_hp}")

# Lógica do Game Over:
if diogo_hp <= 0 and raquel_hp <= 0:
    print("Tie!")
elif diogo_hp <= 0:
    print("Diogo Defeated!")
elif raquel_hp <= 0:
    print("Raquel Defeated!")