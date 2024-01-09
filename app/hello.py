import configparser
from flask import Flask
from pathlib import Path
import os

config = configparser.RawConfigParser()
path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "config.properties")
config.read(config_path)

app = Flask(__name__)

if config.getboolean("features", "feature_1") == True:
	message = "Hello, Olexii!"
else:
	message = "Hello, World!"

@app.route("/")
def hello():
	return message 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050)
