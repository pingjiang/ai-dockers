import os
from pprint import pprint
import dlib
from ai_server.utils.io import string_to_image

# Unexpected version found while deserializing dlib::shape_predictor.
class Detector:
	def __init__(self, **kwargs):
		predictor_path = kwargs.get('predictor_path')

		if predictor_path is None:
			raise TypeError('predictor_path is required')

		self.detector = dlib.get_frontal_face_detector()
		self.predictor = dlib.shape_predictor(predictor_path)

	def detect(self, img):
		# Ask the detector to find the bounding boxes of each face. The 1 in the
		# second argument indicates that we should upsample the image 1 time. This
		# will make everything bigger and allow us to detect more faces.
		dets = self.detector(img, 1)
		# , scores, idx
		objects = []

		# print("Number of faces detected: {}".format(len(dets)))
		for k, d in enumerate(dets):
			# print("Detection #{}: Left: {} Top: {} Right: {} Bottom: {}".format(
				# k, d.left(), d.top(), d.right(), d.bottom()))
			# Get the landmarks/parts for the face in box d.
			shape = self.predictor(img, d)
			points = [(i, shape.part(i).x, shape.part(i).y) for i in range(shape.num_parts)]
			objects.append({
				'box': [d.left(), d.top(), d.right(), d.bottom()],
				'points': points
			})
		return objects

def handle(request_params, app_params):
	"""Detect and predicate face landmark"""
	predictor_path = os.path.join(app_params.get('models'), 'shape_predictor_68_face_landmarks.dat')
	
	detector = Detector(predictor_path=predictor_path)
	img = string_to_image(request_params.get('image_base64'))
	results = detector.detect(img)
	return results
