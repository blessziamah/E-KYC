import os
from fastapi import FastAPI
from FacialVerification.Detection import face_verify, get_facial_landmarks, get_facial_embeddings
from FacialVerification.helper import convert_to_int_or_float
from OCR.text_extraction import extract_front_info

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

app = FastAPI()


@app.get("/")
def index():
	return {"message": "This is the homepage"}


@app.post("/face-landmarks/")
async def face_landmarks(image_url):
	result = get_facial_landmarks(image_url)
	return convert_to_int_or_float(result)


@app.post("/verify")
async def verify(card_url, video_url):
	return face_verify(card_url, video_url)


@app.post("/get-ocr")
async def ocr_front():
	return extract_front_info("Data/card/bless_card.jpg")
