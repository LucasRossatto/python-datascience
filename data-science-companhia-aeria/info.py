import streamlit as st

st.markdown('''

# 📊 Documentação do Projeto: Dashboard de Voos com Streamlit, Pandas e Matplotlib

## 1. Visão Geral

Este projeto consiste em uma **dashboard interativa** desenvolvida com **Streamlit** para análise de dados de voos.  
O objetivo é fornecer uma interface simples e intuitiva para visualizar métricas relevantes e gerar insights a partir de um conjunto de dados contendo preços, duração, atrasos e rotas de voos.

O sistema apresenta:

- **Métricas resumidas** sobre os voos.
- **Gráficos interativos e estáticos** para exploração visual.
- **Filtros e comparações** entre companhias, meses e origens/destinos.
- **Perguntas-chave** para guiar a análise exploratória.

---

## 2. Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/):** Framework Python para criação rápida de dashboards interativos.
- **[Pandas](https://pandas.pydata.org/):** Biblioteca para análise e manipulação de dados tabulares.
- **[Matplotlib](https://matplotlib.org/):** Biblioteca para visualizações estáticas e personalizadas.
- **CSV:** Formato de dados tabulares para leitura via Pandas (`dados_voos.csv`).

---

## 3. Como Executar o Projeto

### Pré-requisitos
- **Python 3.8+**
- Instalar as dependências:
```bash
pip install streamlit pandas matplotlib
```

### Executando a aplicação
```bash
python -m streamlit run data-science-companhia-aeria/stream_app.py
```

---

## 4. Estrutura de Arquivos

```
data-science-companhia-aeria/
│
├── dados_voos.csv          # Arquivo com dados de voos
├── main.py                 # Página inicial (Visão Geral)
├── info.py                 # Página de informações adicionais
├── stream_app.py           # Script principal do Streamlit
└── README.md               # Documentação do projeto
```

---

## 5. Estrutura do Código

### 5.1 Importação de bibliotecas e leitura de dados
```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data-science-companhia-aeria/dados_voos.csv")
```

### 5.2 Exibição de métricas
Utiliza-se `st.metric()` para apresentar informações resumidas, como preço médio, mediana da duração e atrasos médios.

### 5.3 Criação de gráficos
- **Gráficos de barras** para médias de preços por companhia.
- **Boxplots** para distribuição de preços por mês.
- **Histogramas** para duração dos voos.
- **Mapas de calor** para correlação entre variáveis.

### 5.4 Perguntas para guiar análise
O código inclui perguntas estratégicas para auxiliar na interpretação dos dados.

---

## 6. Funcionalidades da Dashboard

1. **Visão Geral**  
   - Preço médio das passagens.
   - Mediana da duração dos voos.
   - Companhia com maior preço médio.
   - Mês com maior preço médio.
   - Rota mais frequente.

2. **Análise de Preços**  
   - Gráfico de barras com preço médio por companhia.
   - Boxplot com distribuição de preços por mês.

3. **Duração e Atrasos**  
   - Histograma das durações de voos por companhia.

4. **Insights Avançados**  
   - Mapa de calor mostrando correlações entre preço, duração e atraso.
   - Tabela de correlações com destaque visual.

---

## 7. Possíveis Melhorias Futuras

- Adicionar **filtros interativos** (por mês, companhia, origem, destino).
- Integrar **Mapas Geográficos** para exibir rotas.
- Implementar **previsões de preços** usando modelos de Machine Learning.
- Disponibilizar exportação de gráficos e relatórios em PDF.

---

## 8. Referências

- [Documentação Streamlit](https://docs.streamlit.io/)
- [Documentação Pandas](https://pandas.pydata.org/docs/)
- [Documentação Matplotlib](https://matplotlib.org/stable/contents.html)

---

''')