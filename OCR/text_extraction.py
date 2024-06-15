import cv2
import easyocr


def extract_front_info(image_url):
	"""
	Extracts the text from the front of the Ghana card
	:param image_url: String 	:return:
	"""

	# Load the image
	image = cv2.imread(image_url, cv2.IMREAD_GRAYSCALE)

	# Apply CLAHE
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
	clahe_image = clahe.apply(image)

	cv2.imwrite('final_image.png', image)

	# # Initialize the EasyOCR reader
	reader = easyocr.Reader(['en'])  # 'en' stands for English language

	# # Perform OCR on the image
	results = reader.readtext(image)

	# Extract the text from the OCR results
	text = ''
	for result in results:
		text += result[1] + '\n'
	return text
