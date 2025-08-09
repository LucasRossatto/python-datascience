import streamlit as st

st.markdown('''
# Documentação do Projeto: Dashboard de Voos com Streamlit, Pandas e Matplotlib

## Visão Geral

Este projeto é uma **dashboard interativa** construída com **Streamlit**, utilizando dados de voos para análise de preços, duração, atrasos e frequências. A interface exibe métricas importantes e gráficos para visualização fácil e rápida dos dados.

---

## Tecnologias Utilizadas

- **Streamlit:** Framework para construção rápida de dashboards interativos em Python.
- **Pandas:** Biblioteca para manipulação e análise de dados tabulares.
- **Matplotlib:** Biblioteca para geração de gráficos estáticos e visualizações.
- **CSV:** Fonte de dados estruturados para análise (arquivo `dados_voos.csv`).

---

## Estrutura do Código

### 1. Importação de bibliotecas e dados

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data-science-companhia-aeria/dados_voos.csv")

''')