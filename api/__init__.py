from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from misc.store import Store
from misc.validate import validate_request_body
from misc.response import check_word


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

store = Store()

@app.route('/api/v1/guess/', methods=['POST'])
@cross_origin()
def guess():
    request_body = request.json

    validate_message, validate_status = validate_request_body(request_body, store)
    if validate_status != 200:
        return validate_message, validate_status

    return jsonify(check_word(request_body, store))


def get_app():
    return app
