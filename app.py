import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')  # lendo os dados


st.header('ANÁLISE DE VENDAS DE CARROS')  # título do aplicativo


# Criar botões
hist_button = st.button('Criar histograma')
scatter_button = st.button('Criar gráfico de dispersão')

# Se o botão de histograma for clicado
if hist_button:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    fig_hist = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig_hist, use_container_width=True)

# Se o botão de gráfico de dispersão for clicado
if scatter_button:
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    fig_scatter = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig_scatter, use_container_width=True)
