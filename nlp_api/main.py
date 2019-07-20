from flask import Flask, jsonify, request
from nlp_api.nlp import data_processor

from nlp_api import app

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
    print("hello")
    return 'This is the Obscenities Finder API'
