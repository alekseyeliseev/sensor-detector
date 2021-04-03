from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
from pydantic import BaseModel
from typing import List
import io
import numpy as np
import sys

import predict

app = FastAPI()

class Prediction(BaseModel):
  prediction: float


@app.get('/')
def root_route():
  return { 'error': 'Use GET /prediction instead of the root route!' }

@app.post('/prediction/', response_model=Prediction)
async def prediction_route(file: UploadFile = File(...)):

  if file.content_type.startswith('image/') is False:
    raise HTTPException(status_code=400, detail=f'File \'{file.filename}\' is not an image.')

  try:
    # Read image contents
    contents = await file.read()
    pil_image = Image.open(io.BytesIO(contents))

    pil_image = pil_image.resize((predict.imgsz, predict.imgsz))

    # Convert from RGBA to RGB *to avoid alpha channels*
    if pil_image.mode == 'RGBA':
      pil_image = pil_image.convert('RGB')

    pil_image.save('data/images/img.jpg', 'JPEG')

    # Generate prediction
    prediction = predict.predict()

    return {
      'prediction': prediction
    }

  except:
    e = sys.exc_info()[1]
    raise HTTPException(status_code=500, detail=str(e))