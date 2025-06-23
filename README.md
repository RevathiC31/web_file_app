# Flask Web Application
## Description
A Flask-based web application for user registration, authentication, and secure file management.
## Features
* User registration and login with hashed passwords
* File upload, download, view, and delete functionality
* User-specific file access control
* SQLite database integration using SQLAlchemy
* Flash messaging for user feedback
* MIME type detection for file viewing
## Technologies Used
* Flask – Web framework
* SQLAlchemy – ORM for database interaction
* Werkzeug – Password hashing and secure file handling
* OS & mimetypes – File system and MIME type support
## Installation
1. Clone the repository: https://github.com/RevathiC31/web_file_app.git
2. Install dependencies: pip install Flask Flask-SQLAlchemy Werkzeug
3. Run the application: python app.py
## Usage
* Visit http://127.0.0.1:5000/ in your browser.
* Register a new user or log in.
* Upload, view, download, or delete your files securely.
## Folder Structure
project/
?
??? app.py
??? templates/
?   ??? login.html
?   ??? register.html
?   ??? dashboard.html
??? uploads/
??? site.db
??? README.md

