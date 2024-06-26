import pandas as pd
import streamlit as st
from PIL import Image

st.markdown('<h2 style="color: green;text-align: center;">Análisis de temperatura y humedad de mi compostador</h2>', unsafe_allow_html=True)
image = Image.open('images2.jpg')
st.image(image)

uploaded_file = st.file_uploader('Carga tu archivo CSV')

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)

    # Renombrar las columnas para que sean más manejables
    df1.columns = ['Time', 'temperatura', 'humedad']

    st.write('<h3 style="color: green;">Perfil gráfico de las variables medidas</h3>', unsafe_allow_html=True)
    df1 = df1.set_index('Time')
    st.line_chart(df1)

    st.write(df1)
    st.write('<h3 style="color: green;">Estadísticos básicos de los sensores</h3>', unsafe_allow_html=True)
    st.dataframe(df1[['temperatura', 'humedad']].describe())

    min_temp = st.slider('Selecciona el valor mínimo del filtro ', min_value=-40, max_value=100, value=23, key=1)
    # Filtrar el DataFrame utilizando query
    filtrado_df_min = df1.query(f"`temperatura` > {min_temp}")
    # Mostrar el DataFrame filtrado
    st.write('<h3 style="color: green;">Temperatura y humedad superiores al valor configurado</h3>', unsafe_allow_html=True)
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_min)
    
    max_temp = st.slider('Selecciona el valor máximo del filtro ', min_value=-40, max_value=100, value=23, key=2)
    # Filtrar el DataFrame utilizando query
    filtrado_df_max = df1.query(f"`temperatura` < {max_temp}")
    # Mostrar el DataFrame filtrado
    st.write('<h3 style="color: green;">Temperatura y humedad inferiores al valor configurado</h3>', unsafe_allow_html=True)
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_max)

else:
    st.warning('Necesitas cargar tu archivo csv excel de Grafana')
