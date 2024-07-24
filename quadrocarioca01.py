import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

arq_carioca = pd.read_csv('relat_fs01_carioca01_tutor.csv')
arq_rio1 = pd.read_csv('relat_fs01_rio01_tutor.csv')
carioca_df = pd.DataFrame(arq_carioca)
rio01_df = pd.DataFrame(arq_rio1)

def intro():
    import streamlit as st
    st.image('images/logo1.jpeg')

def tutores():
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    from scipy import stats
    tab1,tab2,tab3 = st.tabs(['Escolha das Análises','Gráficos', 'Tabelas Resumo'])
    col1,col2, col3 = st.columns([2,2,8],)    
#seleção das páginas:
    if opcoes_tutores == "Carioca":
        with tab1:
            # Escolha da variavel X
            with col1:
                x_carioca_lista = list(carioca_df.columns[1:])
                variavel_x = st.radio(
                    "**Escolha a Variável X**",
                    x_carioca_lista,
                )
                x_carioca_lista.pop(x_carioca_lista.index(variavel_x))
                y_carioca_lista = x_carioca_lista
            # Escolha da variavel Y
            with col2:        
                variavel_y = st.radio(
                    "**Escolha a Variável Y**",
                    y_carioca_lista,
                )
            ctab = pd.crosstab(carioca_df[variavel_x],carioca_df[variavel_y])
            res = stats.chi2_contingency(ctab)
            with col3:
                if min(ctab.min())>4:
                    if float(res.pvalue) > 0.05:
                        st.markdown("### As variáveis escolhidas são independentes")
                        st.write("pvalue:", round(float(res.pvalue),3))
                    else:
                        st.markdown("### As variáveis escolhidas são *dependentes*")
                        st.write("pvalue:", round(float(res.pvalue),3))
                elif min(ctab.min())<5:
                    st.markdown(
                        """ As Variáveis escolhidas possuem
                        *Células* com valores menores que 5
                        não sendo possível realizar o teste de hipótese
                                escolhido.""")
                    st.table(ctab)
    #with st.sidebar:
    #    variaveis_carioca, contingencia, lista_suspensa_carioca_x, lista_suspensa_carioca_y = list(carioca_df.columns), [], 0, 0
    #   st.title("Escolha as variáveis:")
    #    lista_suspensa_carioca_x = st.selectbox('variavel em X', options=variaveis_carioca, index=None)
    #    lista_suspensa_carioca_y = st.selectbox('variavel em Y', options=variaveis_carioca, index=None)
    #    if lista_suspensa_carioca_x is not None:
    #        contingencia = round(pd.crosstab(carioca_df[lista_suspensa_carioca_x],carioca_df[lista_suspensa_carioca_y], normalize=True)*100,2)
    # fora do sidebar
    #if contingencia is not None:
    #    st.markdown("<h1 style='text-align: center;'>Gráfico em frequências relativas(%)</h1>", unsafe_allow_html=True)
    #    st.bar_chart(
    #        contingencia,
    #       x_label=lista_suspensa_carioca_x,
    #       y_label=lista_suspensa_carioca_y,
    #        )
    #    st.markdown("<h1 style='text-align: center;'>Tabela c/ às frequências relativas(%)</h1>", unsafe_allow_html=True)
    #    st.table(contingencia)
    #else:
    #    st.header("Aguardando Escolha das variáveis!")
        
pags = {
    "---":intro,
    "relatorio censo tutores":tutores,
}

with st.sidebar:
    st.logo('images/logo.ico')
    selecao = st.selectbox("Selecione a opção:", pags.keys())

    if selecao == "relatorio censo tutores":
        opcoes_tutores = st.radio(
            "**Qual trailer deseja o relatório**",
            ['Carioca', 'Rio'])
    elif selecao=="---":
        st.success("*Escolha uma opção*")

pags[selecao]()