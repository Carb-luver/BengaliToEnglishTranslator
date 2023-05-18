import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pytesseract
import shutil
import pytesseract
from PIL import Image
import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import clipboard as c
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
banglaSentences = banglaText.split('\n')

chrome_driver = webdriver.Chrome()
chrome_driver.get('https://translate.google.com/')
chrome_driver.maximize_window()
if not "Google" in chrome_driver.title:
    raise Exception("Could not load page")

translationInput = chrome_driver.find_element(By.CLASS_NAME, "er8xn")
for sentence in banglaSentences:
    translationInput.send_keys(sentence)
    time.sleep(1)

f = open("englishTranslationOutput.txt", "a")
f.write(banglaText)
f.write("\n")
className = "ryNqvb"
translationOutputs = chrome_driver.find_elements(By.CLASS_NAME, className)
# translationOutput = translationOutputs.pop()

for output in translationOutputs:
    f.write(output.text)
    f.write("\n")
f.close()
# copyButton = chrome_driver.find_element(By.CLASS_NAME, "gb_pd gb_cd gb_dd")
# copyButton = chrome_driver.find_element(By.XPATH, '//button[3]')
# copyButton.click()
# englishText = c.paste()
# f = open("englishTranslationOutput.txt", "a")
# f.write(sentence)
# f.write("\n")


# clearButton = chrome_driver.find_element(By.CLASS_NAME, "VfPpkd-Bz112c-RLmnJb")
# clearButton.click()

