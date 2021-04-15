from flask_cors import CORS
from flask import Flask, request, jsonify

import netflix_model

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
        return 'Welcome to Nutplease Movie Recommendation System :)'

@app.route('/movies', methods=['GET'])
def recommendate_movies():
        res = netflix_model.movies_result(request.args.get('title'))
        return jsonify(res)

if __name__ == '__main__':
        app.run(port=4000, debug=True)