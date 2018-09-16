import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from pprint import pprint
from ai_server.utils import io
from ai_server.handlers import face_detection

if __name__ == '__main__':
	request_params = {
		'image_base64': io.read_file('./test/image.b64', 'utf8')
	}

	app_params = {
		'models': './models'
	}

	results = face_detection.handle(request_params, app_params)
	pprint(results)

