
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
        
experiencia_por_nivel = [50, 100, 200, 400, 800, 1600]

def subir_nivel(player):
    player["nivel"] += 1
    player["xp"] = 0
    player["max_hp"] += 5
    player["hp"] = player["max_hp"]
    player["max_attack"] += 1
    player["attack"] += 1
    print(f"{player['name']} subiu para o nível {player['nivel']}!")

# Função de GameOver
def is_gameover(player1, player2):
    p1_hp = player1["hp"]
    p2_hp = player2["hp"]

    if p1_hp <= 0 or p2_hp <= 0:
        if p1_hp <= 0 and p2_hp <= 0:
            print("Empate! Ambos cairam.")
        elif p1_hp <= 0:
            print(f"{player1['name']} foi derrotado!")
        else:
            print(f"{player2['name']} foi derrotado!")
        return True
    return False
