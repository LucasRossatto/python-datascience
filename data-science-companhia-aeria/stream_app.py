import streamlit as st

pages = {
    "Visão Geral": [
        st.Page("main.py", title="Métricas principais"),
        st.Page("info.py", title="Info"),
    ],
    "Análises": [
        st.Page("price_analysis.py", title="Análises de Preço"),
        st.Page("delay_duration.py", title="Duração e Atrasos"),
    ],
    "Insights Avançados": [
        st.Page("insights.py", title="Correlação e Padrões"),
    ]
}

pg = st.navigation(pages)
pg.run()
