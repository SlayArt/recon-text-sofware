"""
if this is not do already please install easyocr and pytorch with the following command :
pip install tensorflow
pip install keras-ocr
pip install Pillow

if errors persist please execut the following command :
pip install tensorflow==2.15 
"""

import keras_ocr
from PIL import Image
import numpy as np

def load_image(image_path):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    return np.array(img)

pipeline = keras_ocr.pipeline.Pipeline()

image_path = input("What is the path to your image (please provide the full url or full path) ")

img = load_image(image_path)

predictions = pipeline.recognize([img])[0]

recon_text = " ".join([text for text, box in predictions])

q_u = ""
while q_u != 't' or q_u != 'f':
    q_u = input("Did the provided image contain code? (t/T = True - f/F = False) ").lower()

    if q_u == 't':
        exec(recon_text)
    elif q_u == 'f':
        print(f'Recon text : \n {recon_text}')
    else:
        print("Invalid entry")