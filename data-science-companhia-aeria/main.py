import streamlit as st
import pandas as pd
df = pd.read_csv("data-science-companhia-aeria/dados_voos.csv")

st.title("Visão Geral da Companhia Aérea")
st.caption("Dashboard criada com Streamlit, Pandas e visualizações interativas.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Preço médio das passagens", f"R$ {df['Preco_R$'].mean():,.2f}")
    st.metric("Mediana da duração dos voos (min)", f"{df["Duracao_min"].median()} min")
with col2:
    st.metric("Companhia com maior preço médio", df.groupby("Companhia")["Preco_R$"].mean().idxmax())
    st.metric("Mês com o maior preço médio", df.groupby("Mes")["Preco_R$"].mean().idxmax())
with col3:
    st.metric("Atraso médio dos voos", f"{df['Atraso_min'].mean():,.2f} min")

frequencia = df.groupby(["Origem", "Destino"]).size().reset_index(name="Quantidade")
mais_frequente = frequencia.sort_values("Quantidade", ascending=False).iloc[0]
st.write("Rota (origem/destino) mais frequente")
st.success(
    f"**Rota mais frequente:** {mais_frequente['Origem']} → {mais_frequente['Destino']} "
    f"({mais_frequente['Quantidade']} vezes)"
)

with st.expander("🔍 Ver tabela de dados bruta"):
    st.dataframe(df, use_container_width=True)

with st.expander("📌 Top 5 rotas mais frequentes"):
    top_rotas = frequencia.sort_values("Quantidade", ascending=False).head(5)
    st.table(top_rotas)

if st.checkbox("Mostrar estatísticas descritivas"):
    st.write(df.describe())
