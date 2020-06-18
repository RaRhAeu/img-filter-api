from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.middleware.cors import CORSMiddleware

from app import app

URL = "/image_from_url?filters=vintage&url=https" + \
      "%3A%2F%2Fpicsum.photos%2F200%2F300"


def test_app_instance():
    assert isinstance(app, FastAPI)


def test_cors_policy():
    assert app.user_middleware[0].cls == CORSMiddleware


def test_image_from_url_response():
    client = TestClient(app)
    response = client.get(URL)
    assert response.status_code == 200
    assert response.headers['content-type'] == 'image/jpeg'
    assert isinstance(response.content, bytes)
