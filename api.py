from movies import *

@app.route('/api/movies', methods=['GET'])
def get_movies():
    return jsonify({'Movies': Movie.get_all_movies()})

@app.route('/api/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    return_value = Movie.get_movie(id)
    return jsonify(return_value)

@app.route('/api/movies', methods=['POST'])
def add_movie():
    request_data = request.get_json() #getting data from client
    Movie.add_movie(request_data['title'], request_data['year'], request_data['genre'])
    response = Response('Movie Added', 201, mimetype='application/json')
    return response

@app.route('/api/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    request_data = request.get_json() #getting data from client
    Movie.update_movie(id, request_data['title'], request_data['year'], request_data['genre'])
    response = Response('Movie Updated', status=200, mimetype='application/json')

@app.route('/api/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    Movie.delete_movie(id)
    response = Response("Movie Delete", status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)