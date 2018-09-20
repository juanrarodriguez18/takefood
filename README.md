# takefood
Take advantage of your food!

## Deploying the App

We can deploy the App in several ways:

- [Python](./README.md#python) (v3)
- [Docker](./README.md#docker)

## Python

For deploy the App from Python, we should use the next commands:

```bat
pip install -r requirements.txt
python takeAdvantageOfYourFood/manage.py runserver 0.0.0.0:8000
```

You can change the ip and port `0.0.0.0: 8000` with the ip and port that you need.

## Docker

Para lanzarlo desde Docker usaremos los siguientes comandos:

```bat
docker build --rm -f Dockerfile -t takefood:latest .
docker run -d -p 8000:8000 --name TakeAdvantageOfYourFood --restart always takefood:latest
