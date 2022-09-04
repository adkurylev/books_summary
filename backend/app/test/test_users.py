from datetime import datetime
import sys, os
sys.path.insert(0, os.path.abspath('..'))

from app.api import app
from app.database import *
from fastapi.testclient import TestClient

client = TestClient(app)

def test_fetch_users_1():
    responce = client.get("/api/v1/users")

    assert responce.status_code == 200
    assert responce.json() == []

def test_fetch_users_2():
    users.append(User(email="mail@mail.ru"))
    responce = client.get("/api/v1/users")

    assert responce.status_code == 200
    assert responce.json()[0]['email'] == 'mail@mail.ru'

    users.clear()

def test_fetch_users_3():
    user = User(email="mail@mail.ru")
    users.append(user)

    responce = client.get("/api/v1/users")

    assert responce.status_code == 200
    assert responce.json()[0]['id'] == str(user.id)

    users.clear()

def test_fetch_users_4():
    user = User(email="mail@mail.ru")
    users.append(user)

    responce = client.get("/api/v1/users")

    assert responce.status_code == 200
    assert datetime.strptime(responce.json()[0]['timestamp'], '%Y-%m-%dT%H:%M:%S.%f') == user.timestamp

    users.clear()



def test_fetch_user_by_id_1():
    user = User(email="mail@mail.ru")
    users.append(user)

    responce = client.get(f"/api/v1/users/{user.id}")

    assert responce.status_code == 200
    assert responce.json()['id'] == str(user.id)

    users.clear()

def test_fetch_user_by_id_2():
    responce = client.get("/api/v1/users/248ce753-751e-4040-b3d8-4219fd3a4b83")

    assert responce.status_code == 404

def test_fetch_user_by_id_3():
    responce = client.get("/api/v1/users/248ce75")

    assert responce.status_code == 422



def test_register_user():
    responce = client.post("/api/v1/users", json={
        "email": "postmail@mail.ru"
    })

    assert responce.status_code == 200
    assert responce.json()['id'] == str(users[0].id)
    assert users[0].email == 'postmail@mail.ru'