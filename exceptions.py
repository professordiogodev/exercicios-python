
def conectar_internet():
    return True

try:
    print("Vamos testar se conseguimos conectar à internet")

    # Executar uma função que conecta à internet
    conexão = conectar_internet()

    if not conexão:
        raise Exception("Não tas ligado à internet.")
    else:
        print("Bem vindo à app!")

except Exception:
    opção = input("oh meu deusss, houve um erro! Pretende tentar de novo? (s/n) > ")
    if opção.lower() == "s":
        print("Vamos tentar de novo então.")

else:
    print("Tudo correu bem")

finally:
    print("A remover a conexão da internet.")

print("Fim do programa.")