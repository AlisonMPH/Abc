import abc_1
import app
import time
import flask
import os
import webbrowser
import threading

def gerar_planilha():
    # Coloque aqui o código para gerar a planilha usando as funções do arquivo abc.py
    abc_1.funcao()
    print("Planilha gerada com sucesso!")

def mostrar_planilha():
    # Coloque aqui o código para mostrar a planilha na web usando as funções do arquivo app.py
    #app.mostrar_planilha()
    app1 = flask.Flask(__name__)
    app1.template_folder = 'C:\Projetos\Abc'
    app.mostrar_planilha()
    app.mostrar_grafico()
    print("Planilha mostrada na web com sucesso!")

while True:
    print("Selecione uma opção:")
    print("1 - Gerar planilha")
    print("2 - Mostrar planilha na web")
    print("3 - Sair")
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        thread = threading.Thread(target=gerar_planilha)
        thread.start()
        thread.join()
    elif opcao == "2":
        url = 'http://127.0.0.1:5000/planilha'
        webbrowser.open(url)
        app.executar_app()        
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")