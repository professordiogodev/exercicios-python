senha_nova = input("senha: ")

senha_existente = {
    "senha" = 1234
}

def save(senha_nova):

    with open("senha.txt", "w") as f:

       f.write([senha_nova])

def load(senha_existente):

    a

print("Pretende obter ou salvar uma senha?")
print("a) Obter senha")
print("b) Salvar senha")

opcao = input("Opção > ")

if opcao == "a":
    ler()
    break
elif opcao == "b":
    save()
    break
else:
    print("Opção inválida")
    break