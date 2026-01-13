raquel = {
    "hp": 40,
    "attack": 6,
    "current_monster": "Goblin"
}

#minha_lista = [raquel_hp, raquel_attack, current_monster]
 
# Outro Ficheiro - Save Game (save.txt)

def save(raquel):

    with open("save.txt", "w") as f:

        f.write(f"{raquel["hp"]}")
        f.write(f"{raquel["attack"]}")
        f.write(f"{raquel["current_monster"]}")
    
        print("Game Saved!")

def load(raquel):

    with open("save.txt") as f:

        save_values = []

        for line in f:
            
            value = line.strip()
            save_values.append(value)

        print(save_values)
        raquel["hp"] = save_values[0]
        raquel["attack"] = save_values[1]
        raquel["current_monster"] = save_values[2]

        print("Game Loaded!")


load(raquel)



while True:

    print("Indica o que queres fazer")
    print("a) balblabla")

    opcao = input("Opção > ")

    if opcao == "a":
        ler()
        break
    elif opcao == "b":
        escrever()
        break
    else:
        print("Opção inválida")
        break
        

