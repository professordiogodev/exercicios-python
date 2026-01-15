import os

raquel = {
    "hp": 40,
    "attack": 6,
    "current_monster": "Goblin"
}


def save():

    with open("senha.txt", "w") as f:
        senha = input("Introduza a senha")
        f.write(senha)
    

def load():

    # Antes de ler, ver se o ficheiro existe
    if os.path.exists("senha.txt"):

        with open("senha.txt") as f:

            print("A senha é ", f.read())

    else:
        print("Sumimasen, o ficheiro não existe.")

def erase():
    if os.path.exists("senha.txt"):
        os.remove("senha.txt")
        print("Senha super apagada!!!!")
    else:
        print("Já estava apagado.")


while True:

    print("Indica o que queres fazer")
    print("a) Guardar Senha")
    print("b) Ver Senha")
    print("c) Apagar Senha")
    print("d) Sair")

    opcao = input("Opção > ")

    if opcao == "a":
        save()
    elif opcao == "b":
        load()
    elif opcao == "c":
        erase()
    elif opcao == "d":
        print("Xauxauuuu")
        break
    else:
        print("Opção inválida")
        break
        
    # Linha de intervalo
    print()
