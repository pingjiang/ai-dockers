import io
import numpy as np 
from PIL import Image
import base64
from imageio import imread
import cv2

def decode_base64_image(base64_string):
  found = base64_string.find(',')
  if found != -1:
    base64_string = base64_string[(found + 1):]

  return base64.b64decode(base64_string)

def string_to_image_imageio(base64_string):
  imgdata = decode_base64_image(base64_string)
  img = imread(io.BytesIO(imgdata))
  return img

# 8bit gray or RGB image
def string_to_image(base64_string):
  imgdata = decode_base64_image(base64_string)
  img = np.asarray(bytearray(imgdata), dtype="uint8")
  ret = cv2.imdecode(img, cv2.IMREAD_COLOR)
  return ret

def read_file(filepath, encoding):
  with io.open(filepath, 'r', encoding=encoding) as f:
    return f.read()
