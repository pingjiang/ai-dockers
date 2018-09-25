import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from flask import Flask
from flask import request
from flask import jsonify
# from flask import abort, redirect, url_for
from ai_server.handlers import face_detection, matting

application = Flask(__name__)

config = {
    'models': os.path.join(application.root_path, './models')
}

@application.route('/api/face_detection', methods=['GET', 'POST'])
def handle_face_detection() :
    try:
        # request .json, .args, .forms, .files
        results = face_detection.handle(request, config)
        return jsonify( {
            'code' : 0,
            'msg': 'success',
            'data': results,
        })
    except Exception as err:
        return jsonify( {
            'code' : 1,
            'msg': 'invoke handler error: ' + str(err),
        })

@application.route('/api/matting', methods=['GET', 'POST'])
def handle_matting() :
    try:
        # request .json, .args, .forms, .files
        results = matting.handle(request, config)
        return jsonify( {
            'code' : 0,
            'msg': 'success',
            'data': results,
        })
    except Exception as err:
        return jsonify( {
            'code' : 1,
            'msg': 'invoke handler error: ' + str(err),
        })

if __name__ == '__main__':
    application.run(debug = True, host = '0.0.0.0')
