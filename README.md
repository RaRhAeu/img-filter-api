# img-filter-api
Simple image filtering API built with [FastAPI](https://fastapi.tiangolo.com/).

## Description
This project uses Fast Api framework.
It exposes simple and extendable api for image manipulation.
To get started read the installation guide, move to the docs, 
and then read the section "Extending api with custom filters".

## Installation
Clone the repository
```
$ git clone https://github.com/RaRhAeu/img-filter-api
```
Install dependencies via pipenv
```
$ pipenv install
```
Activate pipenv shell
```python
$ pipenv shell
```
Run the uvicorn server
```
(venv)$ uvicorn app:app
```
Alternatively you can use avalable Dockerfile. 
After that, api documentation will be available at 
```http://127.0.0.1:8000/docs```

## Extending api with custom filters

To get started with your own filters, all you have to do is
add a function to ```filters.py```, with the following header:
```python
def my_filter(img: np.ndarray) -> np.ndarray:
    # do smth with img
    return new_img
```
and then add its name to filter_map, which maps functions names
to its objects
```python
filter_map = {
    ...
    "my_filter": my_filter
}
```
now you can request the api endpoints giving it the ?filter 
parameter equals to my_filter


### TODOS:
- add tests including flake8 and mypy test
- create git workflow
- configure coverage badge