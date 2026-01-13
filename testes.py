raquel_hp = 60
raquel_attack = 4
current_monster = "Slime"

minha_lista = ["teste", "chá", "mesa", "cadeira"]

# Outro Ficheiro - Save Game (save.txt)
with open("demofile.txt", "a") as f:
  
    for elemento in minha_lista:

        f.write(f"{elemento}\n")