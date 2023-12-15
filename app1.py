from flask import Flask, request, jsonify, render_template
import psycopg2
from pymongo import MongoClient

app = Flask(__name__)

conn = psycopg2.connect(
    dbname = 'registrations',
    user = 'postgres',
    password = '09041997',
    host = 'localhost'
)

curr = conn.cursor()

client = MongoClient('mongodb://localhost:27017/')
db = client['registrations']
user_picture = db['profile_picture']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    # data = request.get_json()
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    picture = request.files['picture']


    curr.execute('select user from user_details where email = %s', (email,))
    if curr.fetchone():
        return jsonify({'message':'Email already exists'}), 400
    
    curr.execute('insert into user_details (first_name, email, password, phone) values(%s, %s, %s, %s) returning user_id', (name.split()[0], email, password, phone))
    user_id = curr.fetchone()[0]

    if picture:
        # Read the file content and convert it to bytes
        picture_data = picture.read()
        
        # Create a BSON binary object from the file content
        profile_picture_data = {'user_id': user_id, 'profile_picture': picture_data}
        user_picture.insert_one(profile_picture_data)

    conn.commit()
    return jsonify({'message': 'User registered Successfully', 'user_id': user_id}), 201

    conn.commit()
    return jsonify({'message': 'User registered Successfully', 'user_id': user_id}, 201)

import base64

@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    curr.execute('SELECT * FROM user_details WHERE user_id = %s', (user_id,))
    data = curr.fetchone()
    if not data:
        return jsonify({'message': 'User does not exist'}), 404

    profile_picture_data = user_picture.find_one({'user_id': user_id})
    if not profile_picture_data:
        return jsonify({'message': 'Profile picture not found for the user'}), 404

    user = {
        'user_id': user_id,
        'name': data[1],
        'email': data[2],
        'password': data[3],  # Note: Sending passwords in responses is not recommended for security reasons
        'phone': data[4],
        'profile_picture': base64.b64encode(profile_picture_data['profile_picture']).decode('utf-8')
    }
    return jsonify(user), 200




if __name__ == '__main__':
    app.run(debug=True)