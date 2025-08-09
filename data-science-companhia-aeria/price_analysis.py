import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data-science-companhia-aeria/dados_voos.csv")

df["Receita"] = df["Preco_R$"]
ticket_medio_geral = df["Preco_R$"].mean()

st.title("💰 Dashboard Completo - Análise de Voos")

tab_revenue, tab_prices, tab_distribution,tab_ticket_mes = st.tabs([
    "💵 Receita e Ticket Médio por Companhia",
    "📊 Preço Médio por Companhia",
    "📅 Distribuição de Preços por Mês",
    "📅Ticket medio por data"
])

with tab_revenue:
    st.header("Receita e Ticket Médio por Companhia")
    companhias = df["Companhia"].unique()
    companhia_selecionada = st.selectbox("Selecione a Companhia", companhias)
    df_filtrado = df[df["Companhia"] == companhia_selecionada]

    receita_total = df_filtrado["Receita"].sum()
    ticket_medio = df_filtrado["Preco_R$"].mean()
    media_venda = df_filtrado['Receita'].mean()
    

    st.metric(f"Receita Total - {companhia_selecionada}", f"R$ {receita_total:.2f}")
    st.metric(f"Ticket Médio - {companhia_selecionada}", f"R$ {ticket_medio:.2f}")
    st.metric(f"Média por venda - {companhia_selecionada}", f"R$ {media_venda:,.2f}")


with tab_prices:
    st.header("Preço Médio por Companhia")
    fig, ax = plt.subplots()
    df.groupby("Companhia")["Preco_R$"].mean().plot(kind="bar", ax=ax, color="skyblue", edgecolor="black")
    ax.set_ylabel("Preço médio (R$)")
    ax.set_xlabel("Companhia")
    ax.set_title("Preço médio das passagens por companhia")
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    with st.expander("ℹ️ Detalhes"):
        st.write("Esse gráfico mostra o preço médio das passagens agrupado por companhia aérea.")

with tab_distribution:
    st.header("Distribuição dos Preços por Mês")
    fig, ax = plt.subplots()
    meses_ordenados = sorted(df["Mes"].unique())
    dados_por_mes = [df.loc[df["Mes"] == mes, "Preco_R$"] for mes in meses_ordenados]
    ax.boxplot(dados_por_mes)
    ax.set_title("Distribuição dos preços por mês")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Preço (R$)")
    ax.set_xticklabels(meses_ordenados)
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    with st.expander("ℹ️ Detalhes"):
        st.write("Boxplot que mostra a variação dos preços por mês, permitindo identificar outliers e meses com maior variação.")

with tab_ticket_mes:
    df["Ticket-medio"] = df_filtrado["Preco_R$"].mean()
    st.subheader("Ticket Médio mensal")
    fig, ax = plt.subplots()
    df.groupby("Mes")["Ticket-medio"].sum().plot(ax=ax)
    st.pyplot(fig)