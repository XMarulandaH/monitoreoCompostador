import pandas as pd
import streamlit as st
from PIL import Image

# Centrar el texto del título
st.markdown(
    """
    <h1 style="color: red; text-align: center;">Análisis de datos de Sensores en Mi Ciudad</h1>
    """, unsafe_allow_html=True
)

# Cambiar el color de fondo de la página
st.markdown(
    """
    <style>
    body {
        background-color: #e6f7ff;
    }
    </style>
    """, unsafe_allow_html=True
)

# Centrar la imagen
st.markdown(
    """
    <style>
    .image-container {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True
)

# Ajustar el tamaño de la imagen
image = Image.open('images2.jpg')
st.markdown('<div class="image-container">', unsafe_allow_html=True)
st.image(image, width=500)
st.markdown('</div>', unsafe_allow_html=True)

# Cargar el archivo
uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)

    # Mostrar las columnas del DataFrame
    st.write("Columnas del archivo CSV:")
    st.write(df1.columns)

    st.subheader('Perfil gráfico de la variable medida.')
    df1 = df1.set_index('Time')
    st.line_chart(df1)

    st.write(df1)
    st.subheader('Estadísticos básicos de los sensores.')

    # Verifica si las columnas existen antes de intentar usarlas
    if "temperatura ESP32" in df1.columns:
        st.dataframe(df1["temperatura"].describe())
    else:
        st.warning('La columna "temperatura ESP32" no se encontró en el archivo CSV.')

    if "Humedad" in df1.columns:
        st.dataframe(df1["Humedad"].describe())
    else:
        st.warning('La columna "Humedad" no se encontró en el archivo CSV.')

    min_temp = st.slider('Selecciona valor mínimo del filtro ', min_value=-10, max_value=45, value=23, key=1)
    # Filtrar el DataFrame utilizando query
    if "temperatura ESP32" in df1.columns:
        filtrado_df_min = df1.query(f"`temperatura ESP32` > {min_temp}")
        # Mostrar el DataFrame filtrado
        st.subheader("Temperaturas superiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_min)

    max_temp = st.slider('Selecciona valor máximo del filtro ', min_value=-10, max_value=45, value=23, key=2)
    # Filtrar el DataFrame utilizando query
    if "temperatura ESP32" in df1.columns:
        filtrado_df_max = df1.query(f"`temperatura ESP32` < {max_temp}")
        # Mostrar el DataFrame filtrado
        st.subheader("Temperaturas Inferiores al valor configurado.")
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_max)

else:
    st.warning('Necesitas cargar un archivo csv excel.')
