import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data-science-companhia-aeria/dados_voos.csv")

st.title("🔍 Insights Avançados")
st.caption("Analisando correlações entre preço, duração e atraso nos voos.")

cols_correlacionadas = df[["Preco_R$", "Duracao_min", "Atraso_min"]].corr()

fig, ax = plt.subplots()
im = ax.imshow(cols_correlacionadas, interpolation="nearest", cmap="coolwarm")

cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.ax.set_ylabel("Correlação", rotation=-90, va="bottom")

ax.set_xticks(range(len(cols_correlacionadas.columns)))
ax.set_yticks(range(len(cols_correlacionadas.columns)))
ax.set_xticklabels(cols_correlacionadas.columns)
ax.set_yticklabels(cols_correlacionadas.columns)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
ax.set_title("Correlação entre Preço, Duração e Atraso")
plt.tight_layout()

st.pyplot(fig)

st.markdown("""
### 🧐 Perguntas para investigação
- Existe relação entre **duração** e **preço**?
- O atraso médio está ligado ao **mês** ou à **companhia**?
- Alguma companhia tem **preços fora do padrão**?
""")

with st.expander("📊 Ver tabela de correlações"):
    st.dataframe(cols_correlacionadas.style.background_gradient(cmap="coolwarm"))
