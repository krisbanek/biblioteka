from flask import Flask, jsonify
from models import books
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/api/v1/books/", methods=["GET"])
def books_list_api_1():
    return jsonify(books.all())

@app.route("/api/v1/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    return jsonify({"book": book})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}))

@app.route("/api/v1/books/", methods=["POST"])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        "id": books.all()[-1]['id'] + 1,
        "tytul": request.json['tytul'], 
        "autor": request.json['autor'], 
        "przeczytane": False
    }
    books.create(book)
    return jsonify({'book': book}), 201

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}))

@app.route("/api/v1/books/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    result = books.delete(book_id)
    if not result:
        abort(404)
    return jsonify({'result': result})

@app.route("/api/v1/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'tytul' in data and not isinstance(data.get('tytul'), str),
        'autor' in data and not isinstance(data.get('autor'), str),
        'przeczytane' in data and not isinstance(data.get('przeczytane'), bool)
    ]):
        abort(400)
    book = {
        'tytul': data.get('tytul', book['tytul']),
        'autor': data.get('autor', book['autor']),
        'przeczytane': data.get('przeczytane', book['przeczytane'])
    }
    books.update(book_id, book)
    return jsonify({'book': book})


if __name__ == "__main__":
    app.run(debug=True)