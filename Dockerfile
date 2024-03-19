# syntax=docker/dockerfile:1
FROM python:3.8-slim
WORKDIR /code

RUN apt-get update && apt-get install -y git r-base
RUN git clone https://github.com/dicaso/pycassos.git .
RUN pip install --no-cache-dir -r requirements.txt

