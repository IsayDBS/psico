import pandas as pd
import streamlit as st
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

st.title("Analizador Bases CSV y Excel")

st.write(
    """Introduce un archivo con extensión .csv, .xls , .xlsx , .xlsm , .xlsb , .odf , .ods y .odt  
    """
)

#Leemos entrada de archivo
uploaded_file = st.file_uploader("Elige algún archivo")

if uploaded_file is not None:
    try:
        if ".csv" in uploaded_file.name:
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        #Sidebar
        with st.sidebar:
            #Forms
            with st.form("my_form"):
                columnasAfiltrar = st.multiselect("Filtra columnas", df.columns)
                for column in columnasAfiltrar:
                    left, right = st.columns((1, 20))
                    left.write("↳")
                        
                    # Treat columns with < 10 unique values as categorical
                    if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                        user_cat_input = right.multiselect(
                                        f"Valores para {column}",
                                        df[column].unique(),
                                        default=list(df[column].unique()),
                        )
                        df = df[df[column].isin(user_cat_input)]
                    elif is_numeric_dtype(df[column]): #Usado para columnas con numeros  
                                #_min = st.number_input("Minimo: ")
                                #_max = st.number_input("Maximo: ")
                            _min = float(df[column].min())
                            _max = float(df[column].max())
                            step = (_max - _min) / 100
                            user_num_input = right.slider(
                                f"Valores para {column}",
                                _min,
                                _max,
                                (_min, _max),
                                step=step,
                            )
                            df = df[df[column].between(*user_num_input)]
                                #_min = st.number_input("Minimo: ")
                                #_max = st.number_input("Maximo: ")
                                #df = df[df[column].between(_min, _max)]
                                #Valor puntual
                                #valor = st.number_input("Valor: ")
                                #df = df[df[column].isin([valor])]
                    elif is_datetime64_any_dtype(df[column]): #Usado para columnas con fechas
                        user_date_input = right.date_input(
                        f"Valores para {column}",
                        value=(
                            df[column].min(),
                            df[column].max(),
                        ),
                        )
                        if len(user_date_input) == 2:
                            user_date_input = tuple(map(pd.to_datetime, user_date_input))
                            start_date, end_date = user_date_input
                            df = df.loc[df[column].between(start_date, end_date)]
                    else:#Usado para columnas con texto
                        user_text_input = right.text_input(
                        f"Subcadena o regex in {column}",
                        )
                        if user_text_input:
                            df = df[df[column].str.contains(user_text_input, na=False)]
                submit = st.form_submit_button('Filtrar')
            boton = st.button("Convertir a excel")
            st.write(boton)

            #boton utilizado para convertir a excel
            if boton:
                df.to_excel("./files/filtered-files/" + uploaded_file.name)
        st.dataframe(df)
        
    except:
        st.warning('Archivo no aceptado, intenta de nuevo', icon="⚠️")