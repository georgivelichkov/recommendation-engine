from flasgger import Swagger
from flasgger import swag_from
from flask import Flask, request, jsonify, Response
from flask_cors import cross_origin, CORS

from books import recommend_books
from movies import recommend_shows

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
swagger = Swagger(app)


# API endpoint
@app.route('/api/recommend', methods=['POST'])
@swag_from('swagger_doc.yml')
@cross_origin()
def process_request():
    # Parse received JSON request
    user_input = request.get_json()

    try:
        # Extract movie/book title
        title = user_input['title']

        # Extract category
        category = user_input['category']
    except:
        return jsonify({"message": "Missing one of the mandatory parameters title or category"})

    # Call recommendation engine
    if category == "movies":
        recommended_dict = recommend_shows(title)
    else:
        recommended_dict = recommend_books(title)

    return Response(recommended_dict.to_json(orient="records"), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
