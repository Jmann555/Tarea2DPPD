# Tarea 2- Desarrollo de Proyectos y Producto de Datos

Alumno: Julio Felipe Assmann Segura

## Descripción del proyecto

Este proyecto consiste en la implementación de un modelo de Machine Learning como API, se utilizara un YOLO generado en Visualización Computacional sobre una clasificación de perros Salchichas!🐕

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
├── requirements.txt (dependencias necesarias para utlizar el modelo)
└── test.ipynb   (notebook de ejmplo que utiliza la Url de render para probar la detección)
```
## Pasos previos usando Conda:
#### Prerequisito : tener [CONDA](https://docs.conda.io/en/latest/) instalado en tu computador:
Vamos a usar Conda para construir un entorno virtual nuevo..

#### 1. Creando el entorno virtual (Virtual Environment)
Asumiremos que tenemos instalado conda. El primer paso es crear un nuevo enviroment para desarrollar. Para crear uno usando Python 3.12 debemos ejecutar el siguiente comando:
```
conda create --name producto-datos-lab python=3.12
```
Luego debemos activarlo usando el comando:
```
conda activate TAREA2DPPD
```
Todo el trabajo que realicemos con este código será en este entorno. Así que al trabajar con estos archivos siempre tienen que estar activas estas dependencias.

#### 2. Instalando las dependencias usando PIP
Antes de seguir, verifica que en el terminal de Anaconda estés dentro del directorio `TAREA2DPPD` el cual incluye el archivo `./requirements.txt`. Este archivo enlista todas las dependencias necesarias y podemos usarlo para instalarlas todas:

```
pip intstall -r ./requirements.txt
```
Este comando puede demorar un rato dependiendo de la velocidad del computador y la de la conexión a Internet.

### 3. Implementación desde Github
Puedes usar este repositorios directamente o puedes generar una copia de la siguiente forma: 
1. ingresa a este Github ( si por casualidad obtuviste este codigo por otro lado) [Gvagg555/Tarea2DPPD](https://github.com/Jmann555/Tarea2DPPD) 

2. Presiona el boton verde que dice `<> Code` arriba de las carpetas de archivo como en la imagen a continuación:
![Boton Descarga](./assets/downloadbutton.jpg)

3. Copia la URL del repositorio , o tambien puedes abrirlo mediante GitHub Desktop.
```
https://github.com/Jmann555/Tarea2DPPD.git
```

4. Abre TerminalTerminalGit Bash.

5. Cambial al directorio o locación que quieras dejar tu directorio clonado.

6. Escribe `git clone` y luego pega la URL que copiastes anteriormente.
```
git clone https://github.com/Jmann555/Tarea2DPPD.git
```
 y listo 😉

### 4. Generación de la Api mediante Render

Esta api ya se encuentra creada y puedes usarla libremente!, solo te pido que antes de utilizar sus beneficios ingresa a la siguiente [URL de Render](https://sera-perrosalchicha-o-no.onrender.com) para poder activar la API antes de su uso ( ya que está realizado con el plan free 😄 )

```
https://sera-perrosalchicha-o-no.onrender.com
```

De no ser asi, y tu plan es utilizar este codigo para aprendizaje, favor sigue los siguientes pasos para poder implementarlo tu solo:

- Ingresa a [Render](https://dashboard.render.com/)
- Inicia sesión o crea tu cuenta.
- Agrega tu cuenta de Github en donde tienes copiado el 
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