# img-filter-api
Simple image filtering API built with [FastAPI](https://fastapi.tiangolo.com/).

## Description
The project uses Fast Api framework, and it is easily 
extendable with your own filters, all you have to do is
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
now you can request the api endpoint giving it the ?filter 
parameter equals to my_filter

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