# Librerias
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Datos
df = pd.read_csv("https://raw.githubusercontent.com/jsaraujott/datos/refs/heads/main/iris.csv")
df["type"] = df["type"].astype(str)

# Titulo de la app
st.header('Relación de variables', divider = "gray")

# Boton Descargar
st.download_button(
    label = "Descargar dataset", 
    data = df.to_csv(index=False), 
    file_name = "df.csv"
)
#Crea un espacio entre secciones de la app:
st.divider()

# Seleccionador de variables a analizar por el usuario
opciones = list(df.columns)[0:4]

v = st.multiselect(
    label = "Seleccione máximo 2 variables:",
    options = opciones,
    max_selections = 2
)

# Boton de ejecutar análisis
analisis_b = st.button(
    label = "Analizar"
)
# Crea un espacio entre secciones de la app:
st.divider()

# Analisis
if analisis_b:
    try:

        col1, col2 = st.columns(2)
        
        # Histograma de variable 1
        with col1:
    
            hist_plot01 = px.histogram(df, x = v[0], title = f"Distribución {v[0]}", color = "type")
            st.plotly_chart(hist_plot01, use_container_width=True)

            c1, c2, c3 = st.columns(3)

            with c1: 
                prom1 = np.mean(df[v[0]])
                st.metric(
                    label = "Media",
                    value = "{}".format(round(prom1,1))
                )
            with c2:
                med1 = np.median(df[v[0]])
                st.metric(
                    label = "Mediana",
                    value = "{}".format(round(med1,1))
                )
            with c3:
                desv1 = np.std(df[v[0]])
                st.metric(
                    label = "Desviación",
                    value = "{}".format(round(desv1,1))
                )

        # Histograma de variable 2
        with col2:
            
            hist_plot02 = px.histogram(df, x = v[1], title = f"Distribución {v[1]}", color = "type")
            st.plotly_chart(hist_plot02, use_container_width=True)

            c4, c5, c6 = st.columns(3)

            with c4: 
                prom2 = np.mean(df[v[1]])
                st.metric(
                    label = "Media",
                    value = "{}".format(round(prom2,1))
                )
            with c5:
                med2 = np.median(df[v[1]])
                st.metric(
                    label = "Mediana",
                    value = "{}".format(round(med2,1))
                )
            with c6:
                desv2 = np.std(df[v[1]])
                st.metric(
                    label = "Desviación",
                    value = "{}".format(round(desv2,1))
                )
            
        #Grafica de dispersion
        disp_plot = px.scatter(df, x = v[0], y = v[1], color = "type", title = f"Dispersión {v[1]} vs. {v[0]}")
        st.plotly_chart(disp_plot, use_container_width=True)

        correl = np.corrcoef(df[v[0]],df[v[1]])
        st.metric(
            label = "Correlación de Pearson",
            value = "{}%".format(round(correl[0,1]*100,1))
        )

    except:
        
        st.write("Faltan variables por seleccionar")