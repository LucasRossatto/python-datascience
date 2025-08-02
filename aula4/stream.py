import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("aula4/vendas_loja.csv")
df["Receita"] = df["Quantidade"] * df["Preço_unitario"]
df["Data"] = pd.to_datetime(df["Data"])
df["Mês"] = df["Data"].dt.to_period("M")
df["Produto_Mais_Vendido"] = df["Produto"]("Quantidade")
df["Ticket-medio"] = df["Receita"].sum() / df["Quantidade"].sum() 
st.title("Dashboard de vendas")
st.markdown(
    """ 
    Bem vindo a Dashboard de vendas, feita em Streamlit, pandas e Matplotlib 
    """
)

st.metric("Total de vendas", f"R$ {df["Receita"].sum():,.2f}")
st.metric("Média por venda", f"R$ {df['Receita'].mean():,.2f}")
st.metric("Ticket Médio", f"R$ {df['Ticket-medio'].mean():,.2f}")
st.metric("Produto Mais vendido", f"R${df['Produto_Mais_Vendido']}")

categorias = df["Categoria"].unique()
categoria_selecionada = st.selectbox("Selecione a categoria", categorias)
df_filtrado = df[df["Categoria"] == categoria_selecionada]

# Grafico por produto
st.subheader("Receita por produto")
fig1, ax1 = plt.subplots()
df_filtrado.groupby("Produto")["Receita"].sum().plot(kind="bar", ax=ax1)
st.pyplot(fig1)

st.subheader("Ticket Médio por categoria")
fig4, ax4 = plt.subplots()
df_filtrado.groupby("Produto")["Ticket-medio"].sum().plot(kind="bar", ax=ax4)
st.pyplot(fig4)


st.write("Ticket médio por produto")
todos_produtos = df["Produto"].unique().tolist()
with st.container(border=True):
    produtos = st.multiselect("Produtos", todos_produtos, default=todos_produtos)

df_filtrado = df[df["Produto"].isin(produtos)].copy()
df_filtrado["Ticket-medio"] = df_filtrado["Receita"] / df_filtrado["Quantidade"]

ticket_produto = df_filtrado.groupby("Produto")["Ticket-medio"].mean().reset_index()
ticket_produto = ticket_produto.set_index("Produto")
# Formatado para R$
ticket_produto["Ticket-medio"] = ticket_produto["Ticket-medio"].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))


tab1, tab2 = st.tabs(["Gráfico", "Tabela"])
tab1.line_chart(ticket_produto, height=250)
tab2.dataframe(ticket_produto, height=250, use_container_width=True)

st.subheader("Receita mensal")
fig2, ax2 = plt.subplots()
df.groupby("Mês")["Receita"].sum().plot(ax=ax2)
st.pyplot(fig2)

st.subheader("Ticket Médio mensal")
fig3, ax3 = plt.subplots()
df.groupby("Mês")["Ticket-medio"].sum().plot(ax=ax3)
st.pyplot(fig3)