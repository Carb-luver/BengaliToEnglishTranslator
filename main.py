import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pytesseract
import shutil
import pytesseract
from PIL import Image
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import googletrans
from googletrans import Translator
from tkinter import *
from translate import Translator
import translators
from deep_translator import MyMemoryTranslator
from deep_translator import GoogleTranslator
from google_trans_new import google_translator



os.environ["TESS_PREFIX"] = "/opt/homebrew/Cellar/tesseract/5.3.1/share/tessdata/"

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
bengali_data = "images/Bengali.traineddata"
img = cv2.imread('images/page1.png')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

pytesseract.pytesseract.tessdata_dir_config = '--tessdata-dir "/opt/homebrew/Cellar/tesseract/5.3.1/share/tessdata/"'
custom_config = f'-l ben+eng --tessdata-dir "{bengali_data}"'
banglaText = pytesseract.image_to_string(grayImg, lang='ben')
# print(banglaText)
banglaWords = banglaText.split(' ')
print(banglaWords)
print(banglaWords[1])
word1 = banglaWords[0]

translator = google_translator()
englishText = translator.translate(word1,lang_tgt='en')
print(englishText)
# englishText = translator.translate(banglaWords[1],lang_tgt='en')
# print(englishText)



# translator = Translator(from_lang= 'Bengali',to_lang='English')
# banglaTextSubString = banglaText[0:5]
# Translation = translator.translate(banglaTextSubString)
#
# print(Translation)

# print(googletrans.LANGUAGES)
#
# translator = Translator(service_urls=['translate.google.com'])
# print("translator instantiated")
# translated_text = translator.translate('.')
# # translated_text = translator.translate(banglaText)
# print(translated_text)

# englishText = translators.google(banglaText, from_language='bn', to_language='en')
# print(englishText)