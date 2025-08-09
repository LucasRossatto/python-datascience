import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data-science-companhia-aeria/dados_voos.csv")

st.title("Dashboard de Voos")
st.markdown(
    """ 
    Bem vindo a Dashboard de voos, feita em Streamlit, pandas e Matplotlib 
    """
)

st.metric("Preço médio das passagens", f"R$ {df["Preco_R$"].mean():,.2f}")
st.metric("Mediana da duração dos voos (min)", df["Duracao_min"].median())
st.metric("Companhia com maior preço médio", df.groupby("Companhia")["Preco_R$"].sum().idxmax())
st.metric("Atraso médio dos voos", f"{df['Atraso_min'].mean():,.2f} (min)")
st.metric("Valor máximo e mínimo dos preços", f"Máximo: {df['Preco_R$'].idxmax()}" " " f"Mínimo: {df['Preco_R$'].idxmin()}")
st.metric("Mês com o maior preço médio das passagens", df.groupby("Mes")["Preco_R$"].mean().idxmax())
st.metric("Origem com maior atraso médio", df.groupby("Origem")["Atraso_min"].mean().idxmax())
st.metric("Companhia com a menor duração média*", df.groupby("Companhia")["Duracao_min"].mean().idxmin())
frequencia = df.groupby(["Origem", "Destino"]).size().reset_index(name="Quantidade")

mais_frequente = frequencia.sort_values("Quantidade", ascending=False).iloc[0]
origem = mais_frequente["Origem"]
destino = mais_frequente["Destino"]
quantidade = mais_frequente["Quantidade"]
st.write("Rota (origem/destino) mais frequente")
st.success(f"**{origem} → {destino}**, aparecendo **{quantidade}** vezes.")

preco_medio = df.groupby("Companhia")["Preco_R$"].mean()
comp_maior = preco_medio.idxmax()
valor_maior = preco_medio.max()
comp_menor = preco_medio.idxmin()
valor_menor = preco_medio.min()
diferenca = valor_maior - valor_menor
st.write(f"Companhia com maior preço médio: **{comp_maior}** (R$ {valor_maior:.2f})")

st.write(f"Companhia com menor preço médio: **{comp_menor}** (R$ {valor_menor:.2f})")
st.metric(label="Diferença de preço médio entre a companhia mais cara e a mais barata",value=f"R$ {diferenca:.2f}")

st.subheader("Preço médio por companhia")
fig1, ax1 = plt.subplots()
df.groupby("Companhia")["Preco_R$"].mean().plot(kind="bar",ax=ax1)

fig2, ax2 = plt.subplots()
dados_por_mes = [df.loc[df["Mes"] == mes, "Preco_R$"] for mes in df["Mes"].unique()]

ax2.boxplot(dados_por_mes)
ax2.set_title("Distribuição dos preços por mês")
ax2.set_xlabel("Mês")
ax2.set_ylabel("Preço (R$)")
ax2.set_xticklabels(df["Mes"].unique())

fig3, ax3 = plt.subplots()
distri_voos = [df.loc[df["Companhia"] == companhia, "Duracao_min"] for companhia in df["Companhia"].unique()]
ax3.hist(distri_voos, bins=20)
ax3.set_title('Distribuição das durações de voo')
ax3.set_xlabel("Companhia")
ax3.set_ylabel("Duração (min)")


tab1, tab2, tab3 = st.tabs(["Preço médio por companhia", "Distribuição dos preços por mês", 'Distribuição das durações de voo'])

with tab1:
    st.header("Preço médio por companhia")
    st.pyplot(fig1)
with tab2:
    st.header("Distribuição dos preços por mês")
    st.pyplot(fig2)
with tab3:
    st.header('Distribuição das durações de voo')
    st.pyplot(fig3)

    
"""
- Criar um **mapa de calor** da correlação entre preço, duração e atraso.
- Existe relação entre **duração** e **preço**?
- O atraso médio parece estar ligado ao mês ou à companhia aérea?
- Alguma companhia apresenta **preços muito fora do padrão** (outliers)?
"""

