# PDFtoPNG
Se utiliza la librería PyMuPDF para hacer una simple demostración de conversión de archivo PDF a PNG

# COMO UTILIZAR

---- Crear ambiente virtual para proyecto ---- 

Se utiliza anaconda como gestor de paquetes
conda create --name PDFtoPNGenv python

conda install flask

---- Instalar PyMUPDF con comando pip ----

pip install PyMUPDF

---- Ejecutar proyecto con POSTMAN ----

Realizar una llamada tipo GET http://127.0.0.1:5000/ y click en SEND

Si se ejecuta correctamente, devolverá un JSON {'Terminó' : True}



--> Recordar import fitz en la clase de su proyecto, para utilizar las funciones de la librería