# Tarea 2- Desarrollo de Proyectos y Producto de Datos

Alumno: Julio Felipe Assmann Segura

## Descripción del proyecto

Este proyecto consiste en la implementación de un modelo de Machine Learning como API, se utilizara un YOLO generado en Visualización Computacional sobre la identificación de perros Salchichas!🐕

Para ello realizaremos 3 labores 
- 1. Implementación de la API en FastAPI
- 2. Despliegue de la API en Render
- 3. Pruebas desde un Cliente Externo

## Comenzando

Es importante recordar que deben haber bajado todos los archivos a una carpeta y en la terminal de Anacondallegar a este Direciorio
```
TAREA2DPPD/ (este directorio)
├── model/ (el modelo a utilizar)
│   └── exp3_lr0.001_wd1e-05_optAdamW_best.pt 
├── main.py   (Backend FastAPI con modelo de predicción serverless.)
└── requirements.txt (dependencias necesarias para utlizar el modelo)
```
## Pasos previos usando Conda:
#### Prerequisito : tener [CONDA](https://docs.conda.io/en/latest/) instalado en tu computador:
Vamos a usar Conda para construir un entorno virtual nuevo..

#### 1. Creando el entorno virtual (Virtual Environment)
Asumiremos que tenemos instalado conda. El primer paso es crear un nuevo enviroment para desarrollar. Para crear uno usando Python 3.12 debemos ejecutar el siguiente comando:
```
conda create --name producto-datos-lab python=3.8
```
Luego debemos activarlo usando el comando:
```
conda activate TAREA2DPPD
```
Todo el trabajo que realicemos con este código será en este entorno. Así que al trabajar con estos archivos siempre tienen que estar activas estas dependencias.





1. You may use this repository directly or [create your own repository from this template](https://github.com/render-examples/fastapi/generate) if you'd like to customize the code.
2. Create a new Web Service on Render.
3. Specify the URL to your new repository or this repository.
4. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
5. Specify the following as the Start Command.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.

Or simply click:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/render-examples/fastapi)

## Thanks

Thanks to [Harish](https://harishgarg.com) for the [inspiration to create a FastAPI quickstart for Render](https://twitter.com/harishkgarg/status/1435084018677010434) and for some sample code!