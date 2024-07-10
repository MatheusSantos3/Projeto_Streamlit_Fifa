import streamlit as st
import pandas as pd
import webbrowser as wb
from datetime import datetime

if 'data' not in st.session_state:
    df_data = pd.read_csv('CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)']>0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data

st.markdown('# FIFA 2023 OFFIAL DATASET ⚽')
st.sidebar.markdown('Desenvolvido por [Matheus Santos](https://github.com/MatheusSantos3)')


btn = st.link_button('Acesse os dados no Kaggle',
                     'https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')


st.markdown(
    '''
    O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece
    informações abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados
    demográficos do jogador, características físicas, estatísticas de jogo, 
    detalhes de contrato e afiliações de clubes. 
'''
)

