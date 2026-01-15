from raquel import raquel
from game import attack, is_gameover
from monsters import monsters

# --- CICLO DE BATALHA ---

for monster in monsters:
    print(f"\n--- UM NOVO DESAFIANTE APARECE: {monster['name']} ---")
    
    # Lutar com cada monstro enquanto estiverem vivos
    while not is_gameover(raquel, monster):
        
        # Imprimir Informações de Batalha
        print(f"\nRaquel: {raquel['hp']}/{raquel['max_hp']} HP | {monster['name']}: {monster['hp']} HP")
        print("O que Raquel vai fazer? a) Atacar | b) Curar | c) Spell")
        opcao = input("opção > ")

        # Tratar das Opções
        if opcao == "a":
            raquel["attack_logic"](raquel, monster)
        elif opcao == "b":
            raquel["heal"](raquel)
        elif opcao == "c":
            raquel["spell"](raquel, monster)
        else:
            print("Opção inválida! Perdeste a vez.")

        # Após ação de Raquel, verificar se monstro está vivo
        if is_gameover(raquel, monster):
            break

        # TURNO DO MONSTRO
        print(f"Turno do {monster['name']}!")
        monster["attack_logic"](monster, raquel)

    # --- FIM DA BATALHA ---
    if raquel["hp"] > 0:
        # -- Aumentar Gold & XP --
        raquel["gold"] += monster["gold"]
        raquel["xp"] += monster["xp"]
        print(f"\nVITÓRIA! Ganhaste {monster['gold']} gold e {monster['xp']} XP.")
        
        # Recuperação pós-batalha
        # Max HP: é o número mínimo entre max_hp e hp + 5
        # Se eu tiver 78/80 e ganhar 5, quero ficar com 80 e não 83
        raquel["hp"] = min(raquel["hp"] + 5, raquel["max_hp"])
        print(f"Raquel recuperou 5 HP. HP Atual: {raquel['hp']}")
        
        # Todo - Check Level_Up
    else:
        print("GAME OVER! A jornada de Raquel terminou.")
        break # Sai do loop de monstros se morrer

