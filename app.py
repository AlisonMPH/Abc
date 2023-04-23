from flask import Flask, render_template
import pandas as pd
import plotly.graph_objs as go
import threading

app = Flask(__name__)
app.template_folder = 'C:\Projetos\Abc'

'''df = pd.read_excel('exportada.xlsx')
df1 = df
df1['Individual'] = df1['Individual'].str.rstrip('%').astype('float')
df1['Individual'] = df1['Individual'].astype(float)
df_top10 = df1.nlargest(20, 'Individual')
# Cria um gráfico de barras
fig = go.Figure(data=[go.Bar(y=df_top10['Individual'].apply(lambda y: '{:.2f}%'.format(y)),x=df_top10['Material'].apply(lambda x: x.split()[0]))])

# Adiciona um título ao gráfico
fig.update_layout(title='Meu gráfico de barras')

# Converte o gráfico para um HTML que pode ser renderizado na interface web
grafico_html = fig.to_html(full_html=False)'''

# Rota da página principal
@app.route('/planilha')
def mostrar_planilha():
    app = Flask(__name__)
    app.template_folder = 'C:\Projetos\Abc'

    df = pd.read_excel('exportada.xlsx')
    df1 = df
    df1["Valor Total"] = df["Valor Total"].apply(lambda x: "{:.2f}".format(x))
    # ler a planilha como um objeto DataFrame    
    # converter o DataFrame em uma tabela HTML
    tabela_html = df1.to_html()
    
    # renderizar a tabela no modelo HTML usando Jinja2
    return render_template('planilha.html', tabela_html=tabela_html)

@app.route('/grafico')
def mostrar_grafico():
    df = pd.read_excel('exportada.xlsx')
    df1 = df
    df1['Individual'] = df1['Individual'].str.rstrip('%').astype('float')
    df1['Individual'] = df1['Individual'].astype(float)
    df_top10 = df1.nlargest(11, 'Individual')

    # Define as cores para as barras
    cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aaffc3']

    # Cria um gráfico de barras com rótulos e legenda
    fig = go.Figure(data=[go.Bar(
        y=df_top10['Individual'].apply(lambda y: '{:.2f}%'.format(y)),
        x=df_top10['Material'],
        marker_color=cores
        )])
    fig.update_layout(
        title='Meu gráfico de barras',
        xaxis_title='Materiais',
        yaxis_title='Porcentagem Individual',
        legend_title='Classificação',
        plot_bgcolor='#f5f5f5', # Define a cor do fundo do gráfico
        font=dict(size=16) # Define o tamanho da fonte dos rótulos
    )

    # Converte o gráfico para um HTML que pode ser renderizado na interface web
    grafico_html = fig.to_html(full_html=False)

    return render_template('grafico.html', grafico_html=grafico_html)


@app.route('/pizza')
def mostrar_grafico_pizza():
    df = pd.read_excel('exportada.xlsx')
    df1 = df.copy()
    df1['Individual'] = df1['Individual'].str.rstrip('%').astype('float')
    df1['Individual'] = df1['Individual'].astype(float)
    
    # Agrupa os dados por classificação e calcula a soma dos valores individuais
    df_agrupado = df1.groupby('Classificação').agg({'Individual': 'sum'})
    
    # Ordena as categorias pela soma dos valores individuais
    df_agrupado = df_agrupado.sort_values(by='Individual', ascending=False)
    
    # Cria um gráfico de pizza
    fig = go.Figure(data=[go.Pie(labels=df_agrupado.index, values=df_agrupado['Individual'], hole=0.3)])
    
    # Adiciona um título ao gráfico
    fig.update_layout(title='Curva ABC por Classificação', 
                      font=dict(size=18))
    
    # Adiciona informações nos rótulos do gráfico
    fig.update_traces(textposition='inside', textinfo='percent+label')
    
    # Define as cores das fatias do gráfico
    cores = ['rgb(215, 48, 39)', 'rgb(244, 109, 67)', 'rgb(253, 174, 97)', 'rgb(254, 224, 139)', 'rgb(217, 239, 139)', 
             'rgb(166, 217, 106)', 'rgb(102, 189, 99)', 'rgb(26, 152, 80)']
    fig.update_traces(marker=dict(colors=cores))
    
    # Converte o gráfico para um HTML que pode ser renderizado na interface web
    grafico_html = fig.to_html(full_html=False)

    return render_template('pizza.html', grafico_html=grafico_html)

def executar_app():
    thread = threading.Thread(target=app.run)
    thread.start()

if __name__ == '__main__':
    app.run(debug=True)
