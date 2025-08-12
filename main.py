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

    # Run inference
    results = model(img) # The model can directly take a PIL image

    # 3. PROCESS RESULTS FOR YOLOv8
    # The '.pandas()' method does not exist here. We build the JSON manually.
    predictions = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # Get coordinates, confidence, and class
            xyxy = box.xyxy[0].tolist()
            conf = box.conf[0].item()
            cls = int(box.cls[0].item())
            class_name = model.names[cls]

            predictions.append({
                "xmin": xyxy[0],
                "ymin": xyxy[1],
                "xmax": xyxy[2],
                "ymax": xyxy[3],
                "confidence": conf,
                "class": cls,
                "name": class_name
            })
            
    # Filter for dachshunds (optional if it's the only class)
    dachshund_predictions = [p for p in predictions if p['name'] == 'dachshund']

    return dachshund_predictions