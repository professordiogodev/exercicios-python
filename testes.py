raquel_hp = 60
raquel_attack = 4
current_monster = "Slime"

minha_lista = [raquel_hp, raquel_attack, current_monster]

# Outro Ficheiro - Save Game (save.txt)
with open("save.txt", "a") as f:
  
    for elemento in minha_lista:

        f.write(f"{elemento}\n")