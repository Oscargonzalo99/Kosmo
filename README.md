# Kosmo - Reto
Creacion de API REST que recibe una lista de oraciones en español y devuelve una lista de las entidades nombras identificadas en cada oracion

# Script de extracción de entidades nombradas utilizando spaCy y Flask
Este script es una aplicación Flask que utiliza el modelo de spaCy para el procesamiento del lenguaje natural y la extracción de entidades nombradas en oraciones en español. Permite realizar una solicitud POST a la ruta /ner y recibir una respuesta JSON con las entidades nombradas identificadas en cada oración.

## Requisitos
- Python 3.6 o superior
- Flask
- spaCy
- Modelo de spaCy para el español es_core_news_sm

## Instalación
1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python 3.6 o superior instalado.
3. Crea un entorno virtual (opcional pero recomendado).
4. Instala las dependencias ejecutando el siguiente comando:

```shell
 pip install -r requirements.txt
```

# USO
1. Ejecuta el script Kosmo.py

```shell
 python Kosmo.py
```
2. La aplicación Flask se ejecutará en la dirección http://localhost:5000/ner.
3. Realiza una solicitud POST a esa ruta con un cuerpo JSON que contenga una lista de oraciones en el campo "oraciones".


### Oscar Padilla
