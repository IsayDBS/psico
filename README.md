# Analizador archivos excel para La Facultad de Psicología de la UNAM

## Programas utilizados para el proyecto


+ [python](https://www.python.org/downloads/)
+ [pandas](https://pandas.pydata.org/docs/getting_started/install.html):       ``` pip install pandas```
+ [streamlit](https://docs.streamlit.io/library/get-started/installation):    ``` pip install streamlit```


## Forma de utilizar el programa

Estando en la raíz del proyecto, correr el siguiente comando

```
    streamlit run ./src/app.py
```

Abrirá en el navegador predeterminado http://localhost:8501/, donde después se le pedirá agregar añgún documento con extensión .csv, .xls , .xlsx , .xlsm , .xlsb , .odf , .ods y .odt. 

Se mostrará la información pertinente de los archivos, y se puede hacer uso de filtros para la iformación, en caso de que se necesite pasar la información a excel, estando ya filtrada, hasta abajo hay un botón con esta opción. El archivo resultante estará guardado en _./files/filtered-files_.

Existe otra carpeta en files, el cual es _unfiltered-files_, donde podrás guardar los archivos que quieras analizar, aunque no es necesario.