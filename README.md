
---

# User Registration & Profile Picture Storage System

This Flask-based web application facilitates user registration and stores profile pictures in either a local file system or a database. The project consists of two versions (`app1.py` and `app2.py`) that handle user registration and profile picture storage differently.

## Features

- **User Registration:** Allows users to register by providing their name, email, password, phone number, and profile picture.
- **Profile Picture Storage:** Stores user profile pictures either in a local file system or a database.
- **User Retrieval:** Fetches user information, including profile pictures, based on user ID.

## Versions

### App1.py

- **Database:**
    - **User Details:** PostgreSQL (`user_details` table).
    - **Profile Pictures:** MongoDB (`profile_picture` collection).
- **Endpoints:**
    - `/add_user` (POST): Registers users and stores their profile pictures.
    - `/get_user/<user_id>` (GET): Retrieves user details and their profile picture by user ID.

### App2.py

- **Database:** PostgreSQL (`users` and `profile` tables).
- **Endpoints:**
    - `/add_user` (POST): Registers users and saves their profile pictures to a specified upload folder.
    - `/get_user/<user_id>` (GET): Fetches user details, including their profile picture, by user ID.

## Setup Instructions

1. **Clone the Repository:**
    ```
    git clone <repository_url>
    cd user-registration-profile-picture
    ```

2. **Install Dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Database Setup:**

    - **PostgreSQL Setup:**
        - Install PostgreSQL and ensure it's running locally.
        - Access PostgreSQL shell using `psql` or a GUI like pgAdmin.
        - Create a database named `registrations`:

            ```
            CREATE DATABASE registrations;
            ```

        - For `app1.py`:
            - Run the following SQL commands to create necessary tables:

                ```sql
                CREATE TABLE user_details (
                    user_id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50),
                    email VARCHAR(100) UNIQUE,
                    password VARCHAR(100),
                    phone VARCHAR(20)
                );

                CREATE TABLE profile (
                    user_id INTEGER PRIMARY KEY,
                    profile_picture BYTEA,
                    FOREIGN KEY (user_id) REFERENCES user_details(user_id)
                );
                ```

        - For `app2.py`:
            - Run the following SQL commands to create necessary tables:

                ```sql
                CREATE TABLE users (
                    user_id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50),
                    email VARCHAR(100) UNIQUE,
                    password VARCHAR(100),
                    phone VARCHAR(20)
                );

                CREATE TABLE profile (
                    user_id INTEGER PRIMARY KEY,
                    picture_path VARCHAR(255),
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                );
                ```

4. **Run the Application:**
    - For App1:
        ```
        python app1.py
        ```
    - For App2:
        ```
        python app2.py
        ```

## User Interface (index.html)

The `index.html` file, located in the `templates` directory, provides a simple and intuitive user interface for user registration. It contains a form with fields for user details and profile picture upload.

### User Registration Form

- **Name:** Enter the user's full name.
- **Email:** Provide a valid email address for user identification.
- **Password:** Set a secure password for account access.
- **Phone:** Enter a valid phone number for user contact.
- **Profile Picture (JPG only):** Upload a profile picture in JPG format.

### How to Use

1. Open the application in a web browser.
2. Access the user registration form by navigating to the root URL (`/`) in your browser.
3. Fill in the required details: name, email, password, phone, and select a profile picture.
4. Click the "Submit" button to register the user.

Note: Ensure that all fields are correctly filled out, and the profile picture is in JPG format before submitting the form.

## Note

- **Security:** Storing passwords in plaintext is not recommended for production applications. Consider hashing passwords before storage.
- **Deployment:** For production, ensure to configure security measures, handle exceptions, and use appropriate database setups.

## Contributors

- [@Hrithik-Vashishtha](https://github.com/Hrithik-Vashishtha)


---
