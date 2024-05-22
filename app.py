from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database" of books
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

# Endpoint to get the list of books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Endpoint to get a specific book by id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    return jsonify(book) if book else ("Book not found", 404)

# Endpoint to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(debug=True)
