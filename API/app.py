from flask import Flask, jsonify, request
from API.nlp import data_processor

app = Flask(__name__)

"""
{"data" : "Si hablamos de una mujer, un hombre"}
y usar los header content-type y accept
"""

@app.route('/api/1.0/text_process', methods=['POST'])
def text_process():

    text = request.json["data"]
    response = data_processor(str(text))

    return jsonify(response)


@app.route('/')
def hello_world():

    return 'This is the Obscenities Finder API'


if __name__ == '__main__':
    app.run()
