import folium.map
import streamlit as st

st.sidebar.title('Opciones')

opciones = st.sidebar.selectbox('Selecciona una opción:',['Introducción','Interfaz básica'])

if opciones == 'Introducción':
    st.title('Bienvenidos a la Masterclass de Streamlit')

else:

    st.title('Masterclass de Streamlit---')
    st.write('En esta clase veremos algunas de las opciones que podéis realizar en Streamlit')

    ###################################################################################################
    st.markdown('---')  # Línea horizontal
    ###################################################################################################
    st.markdown('---')  # Línea horizontal
    ###################################################################################################

    st.header('Interfaz básica')

    name = st.text_input('Ingresa tu nombre')
    st.write(f'Hola, {name}!')

    edad = st.slider('Selecciona tu edad:', 0, 100, 25)
    st.write(f'Tiene {edad}años.')

    if st.button('Saludar'):
        st.write('Hola a todos!')

    ###################################################################################################
    st.markdown('---')  # Línea horizontal
    ###################################################################################################
    st.markdown('---')  # Línea horizontal
    ###################################################################################################

    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    import pandas as pd

    st.title('Visualización del dataset del Titanic')

    df = sns.load_dataset('titanic')

    st.write(df.head())

    st.header('Numero de pasajeros por Clase')

    fig, ax = plt.subplots()
    sns.countplot(data=df, x='class',ax=ax)
    st.pyplot(fig)

    ###################################################################################################
    st.markdown('---')  # Línea horizontal
    ###################################################################################################
    st.markdown('---')  # Línea horizontal
    ###################################################################################################

    from PIL import Image

    st.header('Visualización de Imágenes')

    imagen = Image.open('img/Colmar.jpg')
    st.image(imagen, caption='Imagen IA de Colmar (Francia)')

    ###################################################################################################
    st.markdown('---')  # Línea horizontal
    ###################################################################################################
    st.markdown('---')  # Línea horizontal
    ###################################################################################################

    import folium
    from streamlit_folium import st_folium

    st.header('Mapas con folium')

    mapa = folium.Map(location=[45.5236, -122.6750], zoom_start=20)
    folium.Marker([45.5236, -122.6750], popup='Portland, OR').add_to(mapa)

    st_folium(mapa, width=700, height=500)

    ###################################################################################################
    st.markdown('---')  # Línea horizontal
    ###################################################################################################
    st.markdown('---')  # Línea horizontal
    ###################################################################################################