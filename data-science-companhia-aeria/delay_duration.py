import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv("data-science-companhia-aeria/dados_voos.csv")

# Título
st.title("⏱ Duração e Atrasos")
st.caption("Analisando a distribuição da duração dos voos e dos atrasos por companhia aérea.")

# Criar abas
tab1, tab2 = st.tabs(["✈️ Duração dos voos", "🕒 Atrasos"])

# --- Duração dos voos ---
with tab1:
    st.subheader("Distribuição da duração dos voos por companhia")
    fig3, ax3 = plt.subplots()

    companhias = df["Companhia"].unique()
    cores = plt.cm.tab10.colors  # Paleta de cores

    for i, companhia in enumerate(companhias):
        ax3.hist(
            df.loc[df["Companhia"] == companhia, "Duracao_min"],
            bins=20,
            alpha=0.5,
            label=companhia,
            color=cores[i % len(cores)]
        )

    ax3.set_title("Distribuição das durações de voo")
    ax3.set_xlabel("Duração (min)")
    ax3.set_ylabel("Quantidade de voos")
    ax3.legend()
    st.pyplot(fig3)

    with st.expander("ℹ️ Interpretação"):
        st.write("Esse histograma mostra como as durações de voo variam entre as companhias. "
                 "Podemos observar se há empresas que operam voos mais curtos ou mais longos com frequência.")

# --- Atrasos ---
with tab2:
    st.subheader("Distribuição dos atrasos por companhia")
    fig4, ax4 = plt.subplots()

    for i, companhia in enumerate(companhias):
        ax4.hist(
            df.loc[df["Companhia"] == companhia, "Atraso_min"],
            bins=20,
            alpha=0.5,
            label=companhia,
            color=cores[i % len(cores)]
        )

    ax4.set_title("Distribuição dos atrasos")
    ax4.set_xlabel("Atraso (min)")
    ax4.set_ylabel("Quantidade de voos")
    ax4.legend()
    st.pyplot(fig4)

    with st.expander("ℹ️ Interpretação"):
        st.write("Aqui é possível identificar quais companhias apresentam mais voos atrasados e "
                 "se esses atrasos tendem a ser pequenos ou grandes.")
