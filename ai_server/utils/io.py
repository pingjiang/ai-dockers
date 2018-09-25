import io
import base64
import numpy as np 
import cv2

def decode_base64_image(base64_string):
  found = str(base64_string).find(',')
  if found != -1:
    base64_string = base64_string[(found + 1):]

  return base64.b64decode(base64_string)

def save_base64_image(filepath, base64_string):
  imgdata = decode_base64_image(base64_string)
  print('save image file length', filepath, len(imgdata))
  write_file(filepath, bytearray(imgdata))

def string_to_image(base64_string):
  imgdata = decode_base64_image(base64_string)
  img = np.asarray(bytearray(imgdata), dtype="uint8")
  ret = cv2.imdecode(img, cv2.IMREAD_COLOR)
  return ret

def read_file(filepath, encoding):
  with io.open(filepath, 'r', encoding=encoding) as f:
    return f.read()

def write_file(filepath, content):
  with io.open(filepath, 'wb') as f:
    return f.write(content)

def read_file_as_base64(filepath):
  with io.open(filepath, 'rb') as f:
    return base64.b64encode(f.read())