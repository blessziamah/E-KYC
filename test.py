"""
This is a script for running various api function in the command line
"""


import os
from FacialVerification.Detection import face_verify_cmd, get_facial_landmarks, get_facial_embeddings
from FacialVerification.helper import convert_to_int_or_float
from OCR.text_extraction import extract_front_info
from deepface import DeepFace

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

data = face_verify_cmd("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkEWQr35q0sLBoqTTmOe9xMylBK93XkqRCfQ&s", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLLj7bR5wjYqBJxqROueYz0-tN_bfjK6v9lw&s")
print(data)
