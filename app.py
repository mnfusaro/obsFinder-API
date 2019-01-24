from flask import Flask, jsonify, request
from nlp import text_processor

app = Flask(__name__)


@app.route('/data_process', methods=['POST'])
def data_process():
    text = request.json["data"]

    response = text_processor(str(text))

    return jsonify(response)


@app.route('/')
def hello_world():

    return 'This is the Obscenities Finder API'


if __name__ == '__main__':
    app.run()
