import pandas as pd

df = pd.read_excel("planilha.xlsx")
df["Valor Total"] = df["Preço"] * df["Quantidade"]
df = df.sort_values(by="Valor Total", ascending=False)

def calcularTotal():
    for i in range(len(df)):
        Total = Total + df["Valor Total"]
    return Total

Total               = df["Valor Total"].sum()
Individual          = (df["Valor Total"]/Total)
Individual_str      =  ["{:.2%}".format(p) for p in Individual]
df["Individual"]    = Individual_str
Material    = df["Material"]

print(df)

