import  abc as a

def main():
    while True:
            print("1 - Opção 1")
            print("2 - Opção 2")
            print("3 - Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                # Faça algo para a opção 1
                print("Opção 1 selecionada")
                a.funcao()
            elif escolha == "2":
                # Faça algo para a opção 2
                print("Opção 2 selecionada")
            elif escolha == "3":
                # Encerra o programa
                print("Programa encerrado.")
                break
            else:
                # Trata opção inválida
                print("Opção inválida, tente novamente.\n")

# chamada da função main
if __name__ == "__main__":
    main()
