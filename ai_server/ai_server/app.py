from flask import Flask
from flask import jsonify
from ai_server import handlers

app = Flask(__name__)

config = {
    'models': './models'
}

def invoke_handler(name, params):
    results = handlers[name].handle(params, config)
    return results

@app.route('/api/face_detection')
def face_detection() :
    try:
        results = invoke_handler('face_detection', params)
        return jsonify( {
            'code' : 0,
            'msg': 'success',
            'data': results,
        })
    except:
        return jsonify( {
            'code' : 1,
            'msg': 'error' + err,
        })

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
