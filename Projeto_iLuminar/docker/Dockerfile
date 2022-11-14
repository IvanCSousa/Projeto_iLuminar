# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
MAINTAINER Ivan Sousa
WORKDIR /app
COPY ./Luminar .
RUN pip3 install -r requirements.txt; mkdir /logs; 
ENV FLASK_APP luminar.py
EXPOSE 5000
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]
