from flask import Flask
import logging
import os.path

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if os.path.isfile(os.path.join(BASE_DIR, 'config_prod.py')):
    app.config.from_object('config_prod')
else:
    app.config.from_object('config')


handler = logging.StreamHandler()
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

print("entro al init")
from nlp_api import main
