# E-KYC System

An Electronic Know Your Customer (E-KYC) verification system that combines facial recognition, ID card verification, and Optical Character Recognition (OCR) to automate identity verification processes.

## Overview

This project provides a FastAPI-based REST API service for verifying user identities through:
- **Facial Recognition**: Comparing faces from ID cards with live photos/videos
- **Facial Landmark Detection**: Extracting and analyzing facial features
- **OCR (Optical Character Recognition)**: Extracting text information from ID cards

## Features

### 1. Face Verification
- Compare faces from ID card images with user photos/videos
- Uses DeepFace library with RetinaFace detector and FaceNet512 model
- High accuracy facial recognition with confidence scoring
- Supports both image URLs and video processing

### 2. Facial Landmark Detection
- Extract detailed facial landmarks from images
- Uses RetinaFace for robust face detection
- Returns coordinate points for facial features

### 3. OCR Text Extraction
- Extract text information from ID cards (Ghana Card format)
- Uses EasyOCR for text recognition
- Includes image preprocessing with CLAHE (Contrast Limited Adaptive Histogram Equalization)

## Project Structure

```
E-KYC/
├── main.py                          # FastAPI application entry point
├── test.py                          # Command-line testing script
├── requirements.txt                 # Python dependencies
├── FacialVerification/
│   ├── Detection.py                 # Core facial verification functions
│   └── helper.py                    # Utility functions for data conversion
├── OCR/
│   ├── text_extraction.py           # EasyOCR implementation
│   ├── claudeapi_ocr.py            # Claude AI API integration (example)
│   └── openapi_ocr.py              # OpenAI API integration (example)
└── data/
    └── card/                        # Sample ID card images
        ├── bless_card.jpg
        └── card_back.jpg
```

## Technology Stack

- **Framework**: FastAPI
- **Computer Vision**: OpenCV, DeepFace, RetinaFace
- **OCR**: EasyOCR
- **Deep Learning**: TensorFlow, Keras
- **Image Processing**: PIL, NumPy
- **HTTP Requests**: requests, httpx
- **AI APIs**: Anthropic Claude, OpenAI GPT-4

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd E-KYC
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Note: The `requirements.txt` file appears to have encoding issues. You may need to install packages manually:

```bash
pip install fastapi uvicorn
pip install deepface retinaface
pip install opencv-python pillow numpy
pip install easyocr
pip install tensorflow keras
pip install requests httpx
pip install anthropic openai
```

## Usage

### Starting the API Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### 1. Homepage
```http
GET /
```
Returns a welcome message.

#### 2. Face Verification
```http
POST /verify
```
**Parameters:**
- `card_url`: URL to ID card image
- `video_url`: URL to user's photo/video

**Response:**
```json
{
  "verified": true,
  "distance": 0.25,
  "threshold": 0.30,
  "model": "Facenet512",
  "detector_backend": "retinaface"
}
```

#### 3. Facial Landmarks Detection
```http
POST /face-landmarks/
```
**Parameters:**
- `image_url`: URL to face image

**Response:**
```json
{
  "face_1": {
    "facial_area": [x, y, width, height],
    "score": 0.99,
    "landmarks": {
      "right_eye": [x, y],
      "left_eye": [x, y],
      "nose": [x, y],
      "mouth_right": [x, y],
      "mouth_left": [x, y]
    }
  }
}
```

#### 4. OCR Text Extraction
```http
POST /get-ocr
```
Extracts text from the ID card image stored locally.

**Response:**
```
Extracted text from the ID card...
```

### Command-Line Testing

Use the `test.py` script for quick testing:

```bash
python test.py
```

This script demonstrates face verification using sample image URLs.

## Key Functions

### FacialVerification/Detection.py

- `get_image(url)`: Downloads and converts image from URL to NumPy array
- `extract_card_face(url)`: Extracts face region from ID card image
- `get_video(url)`: Downloads video from URL
- `get_face_frame(video_url, confidence)`: Extracts frame with detected face from video
- `face_verify(card_url, video_url)`: Compares faces from card and video/photo
- `get_facial_landmarks(image_url)`: Detects and returns facial landmark coordinates
- `get_facial_embeddings(image_url)`: Generates facial embeddings for comparison

### OCR/text_extraction.py

- `extract_front_info(image_url)`: Extracts text from Ghana Card using EasyOCR
  - Applies grayscale conversion
  - Uses CLAHE for image enhancement
  - Performs OCR with English language model

## Configuration

### Environment Variables

The application sets the following environment variable:
```python
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
```
This disables TensorFlow oneDNN optimizations for compatibility.

### API Keys

For OCR alternatives using AI APIs, you'll need to configure:
- **Claude API**: Set `api_key` in `OCR/claudeapi_ocr.py`
- **OpenAI API**: Set `api_key` in `OCR/openapi_ocr.py`

## Model Details

### Face Recognition
- **Detector**: RetinaFace (high accuracy face detection)
- **Recognition Model**: FaceNet512 (512-dimensional face embeddings)
- **Library**: DeepFace (unified interface for face recognition)

### OCR
- **Engine**: EasyOCR
- **Language**: English
- **Preprocessing**: CLAHE for contrast enhancement

## Sample Data

The `data/card/` directory contains sample ID card images for testing:
- `bless_card.jpg`: Front of Ghana Card
- `card_back.jpg`: Back of Ghana Card

## Error Handling

The API handles common errors gracefully:
- Returns `"No face was detected"` when facial detection fails
- Handles network errors for image/video downloads
- Manages TensorFlow warnings and GPU optimizations

## Performance Considerations

- Face verification uses high-confidence thresholds (default 0.99) for reliable results
- Video processing extracts frames with detected faces for comparison
- Image preprocessing improves OCR accuracy

## Future Enhancements

Potential improvements:
- [ ] Add support for multiple ID card formats
- [ ] Implement batch processing for multiple verifications
- [ ] Add database integration for storing verification results
- [ ] Implement rate limiting and authentication
- [ ] Add support for liveness detection
- [ ] Create a web-based frontend interface
- [ ] Add comprehensive error logging and monitoring

## Acknowledgments

- [DeepFace](https://github.com/serengil/deepface) for facial recognition
- [RetinaFace](https://github.com/serengil/retinaface) for face detection
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) for text extraction
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework
