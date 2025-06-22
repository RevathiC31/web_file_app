import os
import sys
from io import BytesIO

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, db, User


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.drop_all()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Home Page' in response.data

def test_register_page(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert b'Register' in response.data

def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_upload_page(client):
    response = client.get('/upload')
    assert response.status_code == 200
    assert b'Upload File' in response.data

def test_user_registration(client):
    response = client.post('/register', data=dict(
        username='testuser',
        password='testpassword'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Registration successful! Please login.' in response.data

def test_user_login(client):
    client.post('/register', data=dict(
        username='testuser',
        password='testpassword'
    ), follow_redirects=True)
    response = client.post('/login', data=dict(
        username='testuser',
        password='testpassword'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Login successful!' in response.data

def test_dashboard_page(client):
    client.post('/register', data={'username': 'testuser', 'password': 'testpassword'}, follow_redirects=True)
    client.post('/login', data={'username': 'testuser', 'password': 'testpassword'}, follow_redirects=True)
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Dashboard' in response.data

def test_file_upload(client):
    client.post('/register', data=dict(
        username='testuser',
        password='testpassword'
    ), follow_redirects=True)
    client.post('/login', data=dict(
        username='testuser',
        password='testpassword'
    ), follow_redirects=True)
    data = {
        'file': (BytesIO(b'my file contents'), 'testfile.txt')
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data', follow_redirects=True)
    assert response.status_code == 200
    assert b'File successfully uploaded' in response.data
