import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pytesseract
import shutil
import pytesseract
from PIL import Image
import os

os.environ["TESS_PREFIX"] = "/opt/homebrew/Cellar/tesseract/5.3.1/share/tessdata/"

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
bengali_data = "images/Bengali.traineddata"
img = cv2.imread('images/bangla-image.png')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

pytesseract.pytesseract.tessdata_dir_config = '--tessdata-dir "/opt/homebrew/Cellar/tesseract/5.3.1/share/tessdata/"'
custom_config = f'-l ben+eng --tessdata-dir "{bengali_data}"'
text = pytesseract.image_to_string(grayImg, lang='ben')
print(text)


#print(gray3)
#text3 = pytesseract.image_to_string(gray3, lang='ben', config=f"--tessdata-dir {bengali_data}" )
#print(text3)