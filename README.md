# Analizador archivos excel para La Facultad de Psicología de la UNAM

## Programas utilizados para el proyecto


+ [python](https://www.python.org/downloads/)
+ [pandas](https://pandas.pydata.org/docs/getting_started/install.html):       ``` pip install pandas```
+ [streamlit](https://docs.streamlit.io/library/get-started/installation):    ``` pip install streamlit```


## Forma de utilizar el programa

Estando en la raíz del proyecto, correr el siguiente comando

```
    streamlit run ./src/app_precision.py
    streamlit run ./src/app_slider.py
```

Abrirá en el navegador predeterminado http://localhost:8501/, donde después se le pedirá agregar añgún documento con extensión .csv, .xls , .xlsx , .xlsm , .xlsb , .odf , .ods y .odt. 

Se mostrará la información pertinente de los archivos, y se puede hacer uso de filtros para la iformación, en caso de que se necesite pasar la información a excel, estando ya filtrada, hasta abajo hay un botón con esta opción. El archivo resultante estará guardado en _./files/filtered-files_.

Existe otra carpeta en files, el cual es _unfiltered-files_, donde podrás guardar los archivos que quieras analizar, aunque no es necesario.

La existencia de los dos archivos es una cuestión de precision, en _app\_precision_, al querer filtrar los números escribiendolos el usuario, con una precisión de 2 decimales, y en _app\_slider_ , teniendo una barra donde se encuentran los valores posibles del filtro.

## Instrucciones



1. [Clonar este repositorio](https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository).
2. Una vez clonado, nos paramos a la altura del README.md.
3. Corremos el comando ``` 
streamlit run ./src/app_precision.py 
streamlit run ./src/app_slider.py```
4. Nos abrirá el navegador prederteminado, donde correrá el software.