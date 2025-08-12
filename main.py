import io
import torch
from fastapi import FastAPI, UploadFile, File
from PIL import Image
import pandas as pd
from torchvision import transforms

app = FastAPI(title="Detector Perros Salchichas API 🐕")

# Loading your custom YOLO model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/exp3_lr0.001_wd1e-05_optAdamW_best.pt', force_reload=True)

#PreProcessing for implementing the model
transform = transforms.Compose([
    transforms.Resize((480, 480)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])
# Set the model to evaluation mode
model.eval()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Receives an image, applies preprocessing, runs YOLOv5 inference,
    and returns detected objects.
    """
    # Read image from the upload
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")

    # Apply preprocessing to the image
    img_tensor = transform(img)

    # Add a batch dimension (from [C, H, W] to [B, C, H, W])
    # The model expects a batch of images, so we create a batch of 1
    img_batch = img_tensor.unsqueeze(0)

    # Run inference on the preprocessed image tensor
    results = model(img_batch)

    # Process results and convert to JSON 
    predictions_df = results.pandas().xyxy[0]
    dachshund_predictions = predictions_df[predictions_df['name'] == 'dachshund']
    return dachshund_predictions.to_dict(orient="records")