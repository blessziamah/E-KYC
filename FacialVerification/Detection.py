# Import necessary libraries
import cv2
import numpy as np
import requests
from PIL import Image
from deepface import DeepFace
from retinaface import RetinaFace


def get_image(url: str):
	"""
	Accepts a URL and returns the image as a numpy array
	:param url: String
	:return: Numpy array of the image
	"""
	try:
		response = requests.get(url, stream=True)
		image = Image.open(response.raw)
		return np.array(image)
	except Exception as e:
		return e


def extract_card_face(url: str):
	"""
	Accepts a URL and returns the extracted face from the image
	:param url: String
	:return: Numpy array of the extracted face from the url's image
	"""
	try:
		image = get_image(url)
		extracted_face = DeepFace.extract_faces(img_path=image, detector_backend="retinaface")
	except:
		return "No face was detected"
	return extracted_face[0]["face"]


def get_video(url: str, output_file="Bless.mp4", chunk_size=256):
	"""
	Accepts a URL and returns the image as a numpy array
	:param url: String
	:return: Numpy array of the image
	"""
	try:
		response = requests.get(url=url, stream=True)
		with open(output_file, "wb") as file:
			for chunk in response.iter_content(chunk_size=chunk_size):
				file.write(chunk)
		response.close()
		return output_file
	except requests.RequestException as e:
		return e


def get_face_frame(video_url, confidence=0.99):
	"""
	Accepts a video URL and returns the frame with the face
	:param video_url: String
	:param confidence: Confidence level of detected face
	:return: A frame with the detected face
	"""
	temp_video = get_video(video_url)
	cap = cv2.VideoCapture(video_url)
	try:
		while cap.isOpened():
			detected, frame = cap.read()
			if not detected:
				return

			face_props = DeepFace.extract_faces(img_path=frame, detector_backend="retinaface")
			if len(face_props) > 0 and face_props[0]["confidence"] > confidence:
				return frame
	finally:
		cap.release()


# os.remove(temp_video)


def face_verify(card_url, video_url):
	"""
	Accepts a card URL and a video URL and returns the verification result
	:param video_url:
	:param card_url: String	:param video_url: String
	:return: boolean
	"""
	try:
		card_image = get_image(card_url)
		video_image = get_image(video_url)
		# video_image = get_face_frame(video_url)
		result = DeepFace.verify(img1_path=card_image, img2_path=video_image, detector_backend="retinaface", model_name="Facenet512")
	except:
		return "No face was detected"
	return result


def face_verify_cmd(card_url, video_url):
	"""
	Same as the face verify url but runs in the command line for testing purposes
	"""
	try:
		card_image = get_image(card_url)
		video_image = get_image(video_url)
		# video_image = get_face_frame(video_url)
		result = DeepFace.verify(img1_path=card_image, img2_path=video_image, detector_backend="retinaface", model_name="Facenet512")
	except:
		return "No face was detected"
	return result


def get_facial_landmarks(image_url):
	"""
	Accepts an image URL and returns the facial landmarks
	:param image_url:
	:return:
	"""
	try:
		image = get_image(image_url)
		facial_landmarks = RetinaFace.detect_faces(image)
	except:
		return "No face was detected"
	return facial_landmarks


def get_facial_embeddings(image_url):
	"""
	Accepts an image URL and returns the facial embeddings
	:param image_url:
	:return:
	"""
	image = get_image(image_url)
	facial_embeddings = RetinaFace.extract_faces(img_path=image)
	return facial_embeddings
