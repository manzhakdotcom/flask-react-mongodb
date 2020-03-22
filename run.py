from flask import Flask
from flask import jsonify
from bson import ObjectId
from flask_cors import CORS
from db import DBHelper

db = DBHelper()

app = Flask(__name__)

CORS(app)


@app.route('/')
def main():
    items = db.get_city('MA')
    return jsonify(items)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
