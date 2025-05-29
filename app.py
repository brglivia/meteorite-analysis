import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="Análise de Meteoritos", layout="wide")

st.title("🌠 Análise de Meteoritos no Mundo")

# Upload do arquivo
st.sidebar.header("📂 Upload do Arquivo")
file = st.sidebar.file_uploader("Envie o arquivo Excel", type=["xlsx"])

if file:
    df = pd.read_excel(file)

    st.subheader("🔍 Visualização dos Dados")
    st.dataframe(df)

    # Verificando dados ausentes
    st.subheader("📊 Dados Ausentes")
    st.text(df.isnull().sum())

    # Informações gerais
    st.subheader("📄 Informações Gerais")
    buffer = io.StringIO()      # Cria buffer para capturar a saída
    df.info(buf=buffer)         # Redireciona saída para o buffer
    info_str = buffer.getvalue()# Obtém o conteúdo do buffer como texto
    st.text(info_str)           # Exibe no Streamlit

    # Estatísticas básicas
    st.subheader("📈 Estatísticas Básicas")
    st.dataframe(df.describe())

    # Limpeza de dados (longitude > 300 não faz sentido)
    df_clean = df[df["reclong"] < 300]

    st.subheader("📅 Quantidade de Meteoritos por Ano")
    d = df['year'].value_counts()
    met = pd.DataFrame({'ano': d.index, 'cont': d.values}).sort_values(by='ano')
    met = met[(met['ano'] > 1958) & (met['ano'] < 2013)]

    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(met['ano'], met['cont'], color="red")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Quantidade")
    ax.set_title("Quantidade de Meteoritos por Ano")
    ax.grid(True)
    st.pyplot(fig)

    st.subheader("🪨 Média da Massa dos Meteoritos por Classe")
    barras = df.groupby("recclass").agg({
        "mass (g)": "mean",
        "id": "count"
    }).reset_index()

    barras = barras[barras["id"] > 300]  # Mantendo classes mais relevantes

    fig2, ax2 = plt.subplots(figsize=(12,6))
    bar_container = ax2.bar(barras["recclass"], barras["mass (g)"], color="green")
    ax2.set_xlabel("Classe")
    ax2.set_ylabel("Média da Massa (g)")
    ax2.set_title("Média da Massa por Classe")
    ax2.grid(axis="y")
    ax2.bar_label(bar_container, fmt='%.0f')
    plt.xticks(rotation=90)
    st.pyplot(fig2)

    st.subheader("🌍 Localização dos Meteoritos")
    fig3, ax3 = plt.subplots(figsize=(10,6))
    ax3.scatter(df_clean["reclong"], df_clean["reclat"])
    ax3.set_xlabel("Longitude")
    ax3.set_ylabel("Latitude")
    ax3.set_title("Localização dos Meteoritos")
    ax3.grid(True)
    st.pyplot(fig3)

    st.subheader("📊 Histogramas de Latitude e Longitude")

    bins = st.slider("Escolha o número de bins (divisões)", min_value=5, max_value=50, value=10)

    # Histogramas lado a lado
    fig4, (ax4, ax5) = plt.subplots(1, 2, figsize=(15,5))

    ax4.hist(df_clean["reclong"], bins=bins, edgecolor='black')
    ax4.set_title("Distribuição da Longitude")
    ax4.set_xlabel("Longitude")
    ax4.set_ylabel("Frequência")
    ax4.grid(True)

    ax5.hist(df_clean["reclat"], bins=bins, color='green', edgecolor='black')
    ax5.set_title("Distribuição da Latitude")
    ax5.set_xlabel("Latitude")
    ax5.set_ylabel("Frequência")
    ax5.grid(True)

    plt.tight_layout()
    st.pyplot(fig4)

    st.subheader("📍 Latitude e Longitude no Mesmo Gráfico")

    fig5, ax6 = plt.subplots(figsize=(15,5))
    ax6.hist(
        [df_clean['reclat'], df_clean['reclong']],
        bins=bins,
        label=['Latitude', 'Longitude'],
        color=['green', 'blue'],
        alpha=0.6,
        edgecolor='black'
    )
    ax6.set_xlabel("Valores")
    ax6.set_ylabel("Frequência")
    ax6.set_title("Distribuição de Latitude e Longitude")
    ax6.legend(loc='upper right')
    ax6.grid(True)
    st.pyplot(fig5)
else:
    st.info('👈 Faça upload de um arquivo Excel para começar.')
