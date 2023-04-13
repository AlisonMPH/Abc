from flask import Flask, render_template
import pandas as pd
import plotly.graph_objs as go

app = Flask(__name__)
app.template_folder = 'C:\Projetos\Abc'

df = pd.read_excel('exportada.xlsx')
df1 = df
df1['Individual'] = df1['Individual'].str.rstrip('%').astype('float')
df1['Individual'] = df1['Individual'].astype(float)
df_top10 = df1.nlargest(20, 'Individual')
# Cria um gráfico de barras
fig = go.Figure(data=[go.Bar(y=df_top10['Individual'].apply(lambda y: '{:.2f}%'.format(y)),x=df_top10['Material'].apply(lambda x: x.split()[0]))])

# Adiciona um título ao gráfico
fig.update_layout(title='Meu gráfico de barras')

# Converte o gráfico para um HTML que pode ser renderizado na interface web
grafico_html = fig.to_html(full_html=False)

# Rota da página principal
@app.route('/planilha')
def mostrar_planilha():
    # ler a planilha como um objeto DataFrame    
    # converter o DataFrame em uma tabela HTML
    tabela_html = df.to_html()
    
    # renderizar a tabela no modelo HTML usando Jinja2
    return render_template('planilha.html', tabela_html=tabela_html)

@app.route('/grafico')
def mostrar_grafico():
    return render_template('grafico.html', grafico_html=grafico_html)

if __name__ == '__main__':
    app.run(debug=True)
