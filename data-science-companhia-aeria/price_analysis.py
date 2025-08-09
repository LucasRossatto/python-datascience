import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data-science-companhia-aeria/dados_voos.csv")

st.title("💰 Análise de Preços")
st.caption("Explorando os preços das passagens por companhia e ao longo dos meses.")

tab1, tab2 = st.tabs(["📊 Preço médio por companhia", "📅 Distribuição de preços por mês"])

with tab1:
    st.subheader("Preço médio por companhia")
    fig1, ax1 = plt.subplots()
    df.groupby("Companhia")["Preco_R$"].mean().plot(kind="bar", ax=ax1, color="skyblue", edgecolor="black")
    ax1.set_ylabel("Preço médio (R$)")
    ax1.set_xlabel("Companhia")
    ax1.set_title("Preço médio das passagens por companhia aérea")
    st.pyplot(fig1)

    with st.expander("ℹ️ Detalhes"):
        st.write("Esse gráfico mostra o preço médio das passagens agrupado por companhia aérea. "
                 "Ele ajuda a identificar quais companhias têm preços mais altos ou mais baixos.")

with tab2:
    st.subheader("Distribuição dos preços por mês")
    fig2, ax2 = plt.subplots()
    dados_por_mes = [df.loc[df["Mes"] == mes, "Preco_R$"] for mes in sorted(df["Mes"].unique())]
    ax2.boxplot(dados_por_mes)
    ax2.set_title("Distribuição dos preços por mês")
    ax2.set_xlabel("Mês")
    ax2.set_ylabel("Preço (R$)")
    ax2.set_xticklabels(sorted(df["Mes"].unique()))
    st.pyplot(fig2)

    with st.expander("ℹ️ Detalhes"):
        st.write("O boxplot permite visualizar a variação dos preços por mês, detectando valores "
                 "muito altos ou muito baixos (outliers) e identificando períodos com maior variação.")
