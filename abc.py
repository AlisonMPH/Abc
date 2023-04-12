import pandas as pd
import numpy as np

df = pd.read_excel("planilha.xlsx")
df["Valor Total"] = df["Preço"] * df["Quantidade"]
df = df.sort_values(by="Valor Total", ascending=False)

Total               = df["Valor Total"].sum()
Individual          = (df["Valor Total"]/Total)
Individual_str      =  ["{:.2%}".format(p) for p in Individual]
df["Individual"]    = Individual_str
Material            = df["Material"]
Acumulada           = np.cumsum(df["Individual"])

def calcularAcumulada():
    porcentagens_numeros = [float(p.strip('%')) / 100 for p in df["Individual"]]
    porcentagens_index = [(p, i) for i, p in enumerate(porcentagens_numeros)]
    porcentagens_acumuladas = [sum([p[0] for p in porcentagens_index[:i+1]]) for i in range(len(porcentagens_index))]
    porcentagens_classificadas = [(porcentagens_index[i][0], porcentagens_index[i][1], porcentagens_acumuladas[i]) for i in range(len(porcentagens_index))]
    porcentagens_classificadas.sort(key=lambda x: x[1])
    classificacao_acumulada = [p[2] for p in porcentagens_classificadas]
    classificacao_acumulada = ["{:.2%}".format(p) for p in classificacao_acumulada]
    df["Acumulada"] = classificacao_acumulada

print(df["Acumulada"])



#print(Acumulada)

