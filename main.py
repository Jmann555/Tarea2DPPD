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
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")

    # Let the YOLO model handle all internal preprocessing
    results = model(img) 

    # --- PROCESS RESULTS AS A CLASSIFIER ---
    # Get the probabilities from the first result object
    probs = results[0].probs 
    
    # Get the top 5 predicted classes and their confidences
    top5_indices = probs.top5
    top5_confidences = probs.top5conf.tolist()
    
    predictions = []
    for i, index in enumerate(top5_indices):
        class_name = model.names[index]
        confidence = top5_confidences[i]
        predictions.append({"class": class_name, "confidence": confidence})

    return predictions