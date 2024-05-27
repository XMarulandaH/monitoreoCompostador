import pandas as pd
import streamlit as st
from PIL import Image


# CSS personalizado para cambiar el color de las tablas
table_css = """
<style>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
        color: white;
        background-color: #00BF63;  /* Cambiar el color del encabezado de la tabla */
    }

    .dataframe tbody tr {
        background-color: #B9DBBA;  /* Cambiar el color de las filas de la tabla */
    }

    .dataframe tbody tr:nth-child(even) {
        background-color: #e6ffe6;  /* Cambiar el color de las filas pares */
    }
</style>
"""

st.markdown('<h2 style="color: green;text-align: center;">Análisis de temperatura y humedad de mi compostador</h2>', unsafe_allow_html=True)
image = Image.open('images2.jpg')
st.image(image)

uploaded_file = st.file_uploader('Carga tu archivo CSV')

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)

    # Renombrar las columnas para que sean más manejables
    df1.columns = ['Time', 'temperatura', 'humedad']

    st.subheader('Perfil gráfico de las variables medidas')
    df1 = df1.set_index('Time')
    st.line_chart(df1)

    st.write(df1)
    st.subheader('Estadísticos básicos de los sensores')
    st.dataframe(df1[['temperatura', 'humedad']].describe())

    min_temp = st.slider('Selecciona valor mínimo del filtro ', min_value=-40, max_value=100, value=23, key=1)
    # Filtrar el DataFrame utilizando query
    filtrado_df_min = df1.query(f"`temperatura` > {min_temp}")
    # Mostrar el DataFrame filtrado
    st.subheader("Temperatura y humedad superiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_min)

    max_temp = st.slider('Selecciona valor máximo del filtro ', min_value=-40, max_value=100, value=23, key=2)
    # Filtrar el DataFrame utilizando query
    filtrado_df_max = df1.query(f"`temperatura` < {max_temp}")
    # Mostrar el DataFrame filtrado
    st.subheader("Temperatura y humedad inferiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_max)

else:
    st.warning('Necesitas cargar tu archivo csv excel de Grafana.')
