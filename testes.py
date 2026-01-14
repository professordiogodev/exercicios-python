raquel = {
    "hp": 40,
    "attack": 6,
    "current_monster": "Goblin"
}


def save():

    # Verificar se o ficheiro existe
    # Caso não exista, criá-lo

    with open("senha.txt", "w") as f:

        senha = input("Introduza a senha")
        f.write(senha)
        

def load():

    with open("senha.txt") as f:

        print("A senha é ", f.read())

    



while True:

    print("Indica o que queres fazer")
    print("a) Guardar Senha")
    print("b) Ver Senha")
    print("c) Sair")

    opcao = input("Opção > ")

    if opcao == "a":
        save()
    elif opcao == "b":
        load()
    elif opcao == "c":
        print("Xauxauuuu")
        break
    else:
        print("Opção inválida")
        break
        

