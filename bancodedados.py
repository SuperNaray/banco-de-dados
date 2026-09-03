import pickle
import time
import sys
def pagnormal():
    while True:
        with open("nomes.pkl","rb") as arquivo:
            nomes = pickle.load(arquivo)
        print("")
        print("en: use help to know the commands")
        print("pt/br: use help para conhecer os comandos")
        comandos = input("you: ")
    
        if comandos == "show message":
            try:
                with open("dados.pkl", "rb")as arquivo:
                    dados = pickle.load(arquivo)
                    print("")
                    print(dados)
            except(FileNotFoundError, EOFError):
                print("")
                print("não tem nada por aqui")
        elif comandos == "delete message":
                with open("dados.pkl" , "rb") as arquivo:
                    dados = pickle.load(arquivo)
                    dados = {}
                    msg_input = input("digite a mensagem ")
                    user_input = input("digite o nome do usuario")
                    encontrado = False
                    for item in dados:
                        if item["menssange"] == msg_input and item["author"] == user_input.capitalize():
                            dados.remove(item)
                            encontrado = True
                            break
                    if encontrado:
                        with open("dados.pkl", "wb") as arquivo:
                            pickle.dump(dados, arquivo)
                        print("Mensagem deletada com sucesso!")
                    else:
                        print("mensagem não encontrada")


        elif comandos == "publish message":
            with open("nomes.pkl","rb") as arquivo:
                        nomes = pickle.load(arquivo)
            nome2 = input("digite seu nome")
            if nome2 in nomes:
                print("")
                mensagem = input("digite o que você quer falar")
            nova_publicação = {
                "author": nome2.capitalize(),
                "menssange": mensagem
            }
            with open("dados.pkl", "wb") as arquivo:
                pickle.dump(nova_publicação, arquivo)
            print("mensagem publicada")
        elif comandos == "help":
            print("")
            print("use show message para ver as mensages publicadas")
            print("para deletar uma mensagem use delete message")
            print("para sair use quit")
            print("para criar uma mensagem use republish message")
        elif comandos == "quit":
            sys.exit()
        else:
            print("error: comando não existe")
            time.sleep(2)


def login():
    nome = input("seja bem-vindo digite seu nome (lembre bem do seu nome)")
    with open("nomes.pkl", "wb") as arquivo:
        pickle.dump(nome, arquivo)
    with open("nomes.pkl", "rb") as arquivo:
        dados = pickle.load(arquivo)
        if nome in dados:
            print("")
            print("olá de volta", nome)
            pagnormal()
        elif nome is None:
            print("")
            print("tente novamente outra vez")
        else:
            print("")
            print("seja bem vindo pela primeira vez", nome)
            pagnormal()
def senha1(senha2):
    if senha2 == "s":
        login()
    else:
        print("acesso negado")
print("seja bem-vindo ao banco de dados beta v2")
senha = input("digite a senha de acesso ")
senha1(senha)

