api_key = "api_key"

import base64
import httpx
import anthropic

# Specify the image file path
image_path = "../data/card/bless_card.jpg"

# Read the image file in binary mode
with open(image_path, "rb") as image_file:
    image_data = image_file.read()


image1_url = "Data/card/bless_card.jpg"
image1_media_type = "image/jpeg"
image1_data = base64.b64encode(image_data).decode("utf-8")

# image2_url = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg"
# image2_media_type = "image/jpeg"
# image2_data = base64.b64encode(httpx.get(image2_url).content).decode("utf-8")


client = anthropic.Anthropic(api_key=api_key)
message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image1_media_type,
                        "data": image1_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Perform ocr on the image and return a json."
                }
            ],
        }
    ],
)
print(message)
