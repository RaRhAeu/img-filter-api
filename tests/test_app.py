from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.middleware.cors import CORSMiddleware
from app import app
from api.filters import filter_map

TEST_ROUTE = "/image_from_url?filters=vintage&url=https" + \
      "%3A%2F%2Fpicsum.photos%2F200%2F300"


def test_app_instance():
    assert isinstance(app, FastAPI)


def test_cors_policy():
    assert app.user_middleware[0].cls == CORSMiddleware


def test_image_from_url_response():
    client = TestClient(app)
    payload = {"url": "https://picsum.photos/200/300",
               "filters": filter_map.keys()}
    response = client.get("/image_from_url", params=payload)
    assert response.status_code == 200
    assert response.headers['content-type'] == 'image/jpeg'
    assert isinstance(response.content, bytes)


def test_image_post_response():
    client = TestClient(app)
    payload = {"filters": "vintage"}
    files = {'file': open('tests/img_test.jpg', 'rb')}
    result = client.post("/image", params=payload, files=files)
    assert result.status_code == 200
    assert isinstance(result.content, bytes)


def test_image_post_fails():
    client = TestClient(app)
    payload = {"filters": "gaussian"}
    files = {'file': open('tests/not_image.txt', 'rb')}
    result = client.post("/image", params=payload, files=files)
    assert result.status_code == 415
    assert result.json() == {"detail": "Unable to process the image"}
