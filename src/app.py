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


def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns
    Args:
        df (pd.DataFrame): Original dataframe
    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Agrega filtros")

    if not modify:
        return df

    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
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

    #print(df)
    return df

#Leemos entrada de archivo
uploaded_file = st.file_uploader("Elige algún archivo")

if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    try:
        if ".csv" in uploaded_file.name:
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        df_aux = filter_dataframe(df)
        st.dataframe(df_aux)

        #Boton utilizado para convertir a excel
        boton = st.button("Convertir a excel")
        st.write(boton)
        if boton:
            #print(df_aux)
            df_aux.to_excel("./files/filtered-files/" + uploaded_file.name)


        #print(df)
        #print(uploaded_file.name)
    except:
        st.warning('Archivo no aceptado, intenta de nuevo', icon="⚠️")