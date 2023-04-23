import time
import pandas as pd
import numpy as np
from app import Flask, render_template

valorA        = float
valorB        = float

def funcao():
    # Lê a planilha e calcula o valor total de cada item
    df = pd.read_excel("planilha.xlsx")
    df["Valor Total"] = df["Preço"] * df["Quantidade"]

    # Ordena os valores totais do maior para o menor
    df = df.sort_values(by="Valor Total", ascending=False)

    # Calcula as porcentagens individuais do valor total
    Total = df["Valor Total"].sum()
    Individual = (df["Valor Total"] / Total)
    Individual_str = ["{:.7%}".format(p) for p in Individual]
    df["Individual"] = Individual_str
    time.sleep(1)
    # Calcula a classificação acumulada das porcentagens
    porcentagens_numeros = [float(p.strip('%')) / 100 for p in df["Individual"]]
    porcentagens_index = [(p, i) for i, p in enumerate(porcentagens_numeros)]
    porcentagens_acumuladas = [sum([p[0] for p in porcentagens_index[:i+1]]) for i in range(len(porcentagens_index))]
    porcentagens_classificadas = [(porcentagens_index[i][0], porcentagens_index[i][1], porcentagens_acumuladas[i]) for i in range(len(porcentagens_index))]
    porcentagens_classificadas.sort(key=lambda x: x[1])
    classificacao_acumulada = [p[2] for p in porcentagens_classificadas]
    classificacao_acumulada = ["{:.7%}".format(p) for p in classificacao_acumulada]
    df["Acumulada"] = classificacao_acumulada
    time.sleep(1)
    # Imprime a classificação acumulada das porcentagens
    #print(df["Acumulada"])
    classificacao = []
    resultado = []
    print("Digite o valor de A: ")
    valorA = float(input())    
    print("Digite o valor de B: ")
    valorB = float(input())
    for porcentagem in df["Acumulada"]:
        if float(porcentagem.rstrip('%')) <= valorA:
            resultado.append('A')
        elif float(porcentagem.rstrip('%')) <= valorB:
            resultado.append('B')
        else:
            resultado.append('C')

    classificacao = ''.join(resultado)

    for i, classif in enumerate(classificacao):
        df.at[i, "Classificação"] = classif

    classificacao_acumulada = [p[2] for p in porcentagens_classificadas]
    classificacao_acumulada = ["{:.2%}".format(p) for p in classificacao_acumulada]
    df["Acumulada"] = classificacao_acumulada
    Individual_str = ["{:.2%}".format(p) for p in Individual]
    df["Individual"] = Individual_str
    print(df)
    df.to_excel('exportada.xlsx', index=False)

    app = Flask(__name__)
    df = pd.read_excel('exportada.xlsx')

# chamada da função main
if __name__ == "__main__":
    app = Flask(__name__)
    #valorA = input("Valor de A: ")
    #valorB = input("Valor de B: ")
    #time.sleep(1)
    funcao()
