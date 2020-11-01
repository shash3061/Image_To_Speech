import pytesseract
from PIL import Image
from gtts import gTTS
import os

IMAGE_PATH = "./img.jpg"
img = Image.open(IMAGE_PATH)

text = pytesseract.image_to_string(img)
print(text)

language = "en"

speech = gTTS(text = text, lang = language, slow = False)

speech.save("text.mp3")