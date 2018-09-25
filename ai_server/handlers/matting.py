import os, sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# import os
from uuid import uuid4
from pprint import pprint
import subprocess
from ai_server.utils import io

def uniq_file():
  return './__autosaved_' + str(uuid4()) + '.png'

def matting(image_base64, image_base64_trimap):
  tmp_filepath = uniq_file()
  io.save_base64_image(tmp_filepath, image_base64)
  tmp_filepath_trimap = uniq_file()
  io.save_base64_image(tmp_filepath_trimap, image_base64_trimap)
  tmp_filepath_out = uniq_file()

  cmd = ['./ai_server/bin/matting', tmp_filepath, tmp_filepath_trimap, tmp_filepath_out]

  result = 'error'
  image_base64_result = None
  
  try:
    print('begin matting')
    run_result = subprocess.run(cmd, stdout=subprocess.PIPE)
    print('end matting')
    result = str(run_result.stdout)
    image_base64_result = io.read_file_as_base64(tmp_filepath_out)
  except Exception as e:
    print('matting error', e)
    result = 'run exception'
    os.remove(tmp_filepath)
    os.remove(tmp_filepath_trimap)
    os.remove(tmp_filepath_out)
  
  return {
    "raw_results": result,
    "image_base64": str(image_base64_result, encoding='utf-8')
  }

def get_request_param(request, name, is_required = False):
  """Detect and predicate face landmark"""
  value = None

  if value is None and request.args != None and name in request.args:
    value = request.args.get(name)

  if value is None and request.form != None and name in request.form:
    value = request.form.get(name)

  if value is None and request.json != None and name in request.json:
    value = request.json.get(name)

  if is_required is True and value is None:
    raise TypeError(name + ' is required')

  return value

def handle(request, config):
  """Detect and predicate face landmark"""
  image_base64 = get_request_param(request, 'image_base64', True)
  image_base64_trimap = get_request_param(request, 'image_base64_trimap', True)
  return matting(image_base64, image_base64_trimap)
  
if __name__ == '__main__':
  import sys
  ret = matting(io.read_file_as_base64(sys.argv[1]), io.read_file_as_base64(sys.argv[2]))
  pprint(ret)
