docker build -t ivancsousa/python-docker:v2 .
docker push ivancsousa/python-docker:v2
docker run -p 5000:5000 -d python-docker:v2

