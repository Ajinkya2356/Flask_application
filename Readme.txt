1.project
Website/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── auth.py
│   ├── templates/
│   └── static/
├── requirements.txt
├── app.py
└── README.md

2.Install Dependencies
pip install -r requirements.txt

3.Database setup
CREATE DATABASE your_database_name;
CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'localhost';
FLUSH PRIVILEGES;

4.Run on localhost
python app.py

5.API Endpoints
API Endpoints:
Sign Up Endpoint:

Endpoint: /signup
Method: POST
Data: form-data payload with keys email, username, password, cpassword.

Login Endpoint:

Endpoint: /login
Method: POST
Data: form-data payload with keys username and password.