import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

arq_carioca = pd.read_csv('relat_fs01_carioca01_tutor.csv')
carioca_df = pd.DataFrame(arq_carioca)

st.title(":one: Relatório fase 01 - Ação Cidadã")
st.logo('images/logo1.jpeg')
paginas = st.sidebar.selectbox("Selecione trailer:",['Carioca', "Rio"])

#seleção das páginas:
if paginas == "Carioca":    
    with st.sidebar:
        variaveis_carioca, contingencia, lista_suspensa_carioca_x, lista_suspensa_carioca_y = list(carioca_df.columns), [], 0, 0
        st.title("Escolha as variáveis:")
        lista_suspensa_carioca_x = st.selectbox('variavel em X', options=variaveis_carioca, index=None)
        lista_suspensa_carioca_y = st.selectbox('variavel em Y', options=variaveis_carioca, index=None)
        if lista_suspensa_carioca_x is not None and lista_suspensa_carioca_y is not None:
            contingencia = round(pd.crosstab(carioca_df[lista_suspensa_carioca_x],carioca_df[lista_suspensa_carioca_y], normalize=True)*100,2)
    # fora do sidebar
    if contingencia is not None:
        st.markdown("<h1 style='text-align: center;'>Gráfico em frequências relativas(%)</h1>", unsafe_allow_html=True)
        st.bar_chart(
            contingencia,
            x_label=lista_suspensa_carioca_x,
            y_label=lista_suspensa_carioca_y,
            )
        st.markdown("<h1 style='text-align: center;'>Tabela c/ às frequências relativas(%)</h1>", unsafe_allow_html=True)
        st.table(contingencia)
    else:
        st.header("Aguardando Escolha das variáveis!")