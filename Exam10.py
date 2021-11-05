import os, io
from google.cloud import vision_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'letter-recognition.json'
client= vision_v1.ImageAnnotatorClient()
with io.open("letters.png", "rb") as file:
    content = file.read()

img = vision_v1.types.Image(content=content)
response = client.document_text_detection(image = img)
text = response.full_text_annotation.text
words = text.split(" ")
for word in words:
    print([char for char in word])