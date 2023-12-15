from flask import Flask, request, jsonify, render_template
import psycopg2
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'C:/Users/Hrithik/Desktop/x_pay_assignment/upload_folder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

conn = psycopg2.connect(
    dbname='registrations',
    user='postgres',
    password='09041997',
    host='localhost'
)
curr = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/add_user', methods=['POST'])
# def add_user():
    # Extracting form data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    picture = request.files['picture']

    # Checking for existing email and phone
    curr.execute('SELECT * FROM users WHERE email = %s', (email,))
    if curr.fetchone():
        return jsonify({'message': 'Email already exists'}), 400

    curr.execute('SELECT * FROM users WHERE phone = %s', (phone,))
    if curr.fetchone():
        return jsonify({'message': 'Phone already exists'}), 400

    # Inserting into 'users' table and getting the 'user_id' generated
    curr.execute('INSERT INTO users (first_name, email, password, phone) VALUES (%s, %s, %s, %s) RETURNING user_id',
                 (name.split()[0], email, password, phone))
    user_id = curr.fetchone()[0]

    # Inserting picture content into 'profile' table
    picture_name = os.path.join(app.config['UPLOAD_FOLDER'], picture.filename)
    picture.save(picture_name)

    curr.execute('INSERT INTO profile (user_id, picture_path) VALUES (%s, %s)', (user_id, picture_name))
    conn.commit()

    return jsonify({'message': 'User Registered Successfully', 'user_id': user_id}), 201

@app.route('/add_user', methods=['POST'])
def add_user():
    # Extracting form data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    picture = request.files['picture']

    # Checking for existing email and phone
    with conn.cursor() as curr:
        curr.execute('SELECT * FROM users WHERE email = %s', (email,))
        if curr.fetchone():
            return jsonify({'message': 'Email already exists'}), 400

        curr.execute('SELECT * FROM users WHERE phone = %s', (phone,))
        if curr.fetchone():
            return jsonify({'message': 'Phone already exists'}), 400

        # Inserting into 'users' table and getting the 'user_id' generated
        curr.execute('INSERT INTO users (first_name, email, password, phone) VALUES (%s, %s, %s, %s) RETURNING user_id',
                     (name.split()[0], email, password, phone))
        user_id = curr.fetchone()[0]

        # Inserting picture content into 'profile' table
        picture_name = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(picture.filename))
        picture.save(picture_name)

        curr.execute('INSERT INTO profile (user_id, picture_path) VALUES (%s, %s)', (user_id, picture_name))
        conn.commit()

    return jsonify({'message': 'User Registered Successfully', 'user_id': user_id}), 201


@app.route('/get_user/<int:user_id>',methods=['GET'])
def get_user(user_id):
    if not user_id:
        return jsonify({'message':'user_id is invalid'})
    curr.execute('select * from users where user_id = %s',(user_id,))
    data = curr.fetchone()
    if not data:
        return jsonify({'message':'User does not exist'})
    
    curr.execute('select * from profile where user_id = %s',(user_id,))
    profile_data = curr.fetchone()
    if not profile_data:
        return jsonify({'message':'profile does not exist'})
    user = {'name':data[1], 'email':data[2], 'phone': data[3], 'password': data[4], 'profile_picture': profile_data[1]}
    return jsonify(user), 200


if __name__ == '__main__':
    app.run(debug=True)
