# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN  python -u "./src/main.py"
