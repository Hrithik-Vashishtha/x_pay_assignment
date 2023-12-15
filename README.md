Absolutely! Here’s a comprehensive README file for your project:

---

# User Registration & Profile Picture Storage System

This Flask-based web application facilitates user registration and storage of profile pictures in either a local file system or a database. The project consists of two versions (`app1.py` and `app2.py`) that handle user registration and profile picture storage differently.

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

## Usage

- Access the application via a web browser or API client like Postman.
- Register users by providing necessary details, including a profile picture.
- Retrieve user information using their user ID.

## Note

- **Security:** Storing passwords in plaintext is not recommended for production applications. Consider hashing passwords before storage.
- **Deployment:** For production, ensure to configure security measures, handle exceptions, and use appropriate database setups.

## Contributors

- [@Hrithik-Vashishtha](https://github.com/Hrithik-Vashishtha)


---
