import pandas as pd
import streamlit as st
from PIL import Image
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

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

    # Configurar opciones de la tabla con st_aggrid
    gb = GridOptionsBuilder.from_dataframe(df1[['temperatura', 'humedad']].describe())
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)

    # Personalizar el estilo de las celdas
    cellstyle_jscode = JsCode("""
    function(params) {
        return {
            'color': 'black', 
            'backgroundColor': (params.node.rowIndex % 2 === 0) ? '#F2F2F2' : '#E6FFE6',
            'font-weight': 'bold' if params.node.rowPinned else 'normal'
        };
    }
    """)
    gb.configure_column("index", cellStyle=cellstyle_jscode)
    gb.configure_column("temperatura", cellStyle=cellstyle_jscode)
    gb.configure_column("humedad", cellStyle=cellstyle_jscode)

    gridOptions = gb.build()

    AgGrid(
        df1[['temperatura', 'humedad']].describe(),
        gridOptions=gridOptions,
        enable_enterprise_modules=True,
        height=300,
        fit_columns_on_grid_load=True
    )

    min_temp = st.slider('Selecciona valor mínimo del filtro ', min_value=-10, max_value=45, value=23, key=1)
    # Filtrar el DataFrame utilizando query
    filtrado_df_min = df1.query(f"`temperatura` > {min_temp}")
    # Mostrar el DataFrame filtrado
    st.subheader("Temperaturas superiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_min)

    max_temp = st.slider('Selecciona valor máximo del filtro ', min_value=-10, max_value=45, value=23, key=2)
    # Filtrar el DataFrame utilizando query
    filtrado_df_max = df1.query(f"`temperatura` < {max_temp}")
    # Mostrar el DataFrame filtrado
    st.subheader("Temperaturas Inferiores al valor configurado.")
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_max)

else:
    st.warning('Necesitas cargar tu archivo csv excel de Grafana.')
