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

#tesseract environment variables
os.environ["TESS_PREFIX"] = "/opt/homebrew/Cellar/tesseract/5.3.1/share/tessdata/"
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
bengali_data = "images/Bengali.traineddata"
pytesseract.pytesseract.tessdata_dir_config = '--tessdata-dir "/opt/homebrew/Cellar/tesseract/5.3.1/share/tessdata/"'
custom_config = f'-l ben+eng --tessdata-dir "{bengali_data}"'

folder_dir = "/Users/meganthurston/Documents/PythonWorkspace/images"
imageList = []
for file in os.listdir(folder_dir):
    # check if the image ends with png or jpg or jpeg
    if (file.endswith(".png")):
        imageList.append(file)

for imgFileName in imageList:
    #extract bangla text from image with tesseract
    imgDir = 'images/' + imgFileName
    print(imgDir)
    img = cv2.imread(imgDir)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    banglaText = pytesseract.image_to_string(grayImg, lang='ben')
    banglaSentences = banglaText.split('\n')

    #navigate to google translate home page
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('https://translate.google.com/')
    chrome_driver.maximize_window()
    if not "Google" in chrome_driver.title:
        raise Exception("Could not load page")

    #send bangla text to google translate input box
    translationInput = chrome_driver.find_element(By.CLASS_NAME, "er8xn")
    for sentence in banglaSentences:
        translationInput.send_keys(sentence)
    time.sleep(15)

    #open file and write bangla text
    f = open("englishTranslationOutput.txt", "a")
    f.write("\n")
    f.write(banglaText)
    f.write("\n")

    #write english translation in file after bangla text\
    className = "ryNqvb"
    translationOutputs = chrome_driver.find_elements(By.CLASS_NAME, className)
    for output in translationOutputs:
        f.write(output.text)
        f.write("\n")
    f.close()

    chrome_driver.close()


