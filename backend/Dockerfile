FROM python:3.10-slim-buster

WORKDIR /backend

RUN apt-get update && apt-get install -y \
  gcc

RUN pip install --upgrade pip

COPY ./requirements.txt /backend/requirements.txt

RUN pip install -r requirements.txt

COPY . /backend

CMD ["uvicorn", "app.main:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8000"]