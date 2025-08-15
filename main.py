import io
import torch
from fastapi import FastAPI, UploadFile, File
from PIL import Image
from ultralytics import YOLO 
from torchvision import transforms

app = FastAPI(title="Detector Perros Salchichas API 🐕")

# 2. LOAD MODEL DIRECTLY WITH ULTRALYTICS
# This is more robust than torch.hub
model = YOLO('model/exp3_lr0.001_wd1e-05_optAdamW_best.pt')

# Preprocessing - This part might not even be necessary, as YOLO can often handle raw images.
# You can try commenting this section out later if you want.
transform = transforms.Compose([
    transforms.Resize((480, 480)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])
# model.eval() is not needed for YOLO object

@app.get("/")
def read_root():
    return {"status": "ok", "message": "API de Detección de Salchichas está en línea!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...), confidence: float = 0.85):
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")

    # Realizar la inferencia
    results = model(img) 

    # Procesar los resultados para obtener las probabilidades
    probs = results[0].probs 
    
    # Crear un diccionario para acceder fácilmente a las confianzas por nombre de clase
    confidences = {model.names[i]: p for i, p in enumerate(probs.data)}
    
    # Obtener la confianza específica para la clase 'dachshund'
    dachshund_confidence = confidences.get('dachshund', 0)

    # Comparamos la confianza con el umbral que recibimos
    if dachshund_confidence >= confidence:
        prediction_value = 1
        prediction_text = "Es un perro salchicha!"
    else:
        prediction_value = 0
        prediction_text = "No es un perro salchicha!"
    
    return {
        "prediction_text": prediction_text,
        "prediction_value": prediction_value,
        "confidence_score": dachshund_confidence
    }