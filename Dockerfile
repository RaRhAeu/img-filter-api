FROM python:3.7

RUN pip install pipenv

COPY . .

RUN pipenv sync

EXPOSE 80

CMD ["pipenv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80" ]