# TakeFood

<img src="takeAdvantageOfYourFood/takeAdvantageOfYourFood/static/images/logo-rounded.png" width="120px">

**Take Advantage of your Food!**

Your favourite recipe searcher! With this web app you can upload your ingredients and the app will search in our bd for show you the recipes that has those or less of the ingredients that you have uploaded. 

Powered by [IBM Watson Visual Recognition](https://www.ibm.com/watson/services/visual-recognition/).

## Populating the Database

First at all, we need to populate the database. For default the database is populated, but if you want to change the data, you can do it.

For populate the database, we need to run the command:

```bat
pip install -r requirements.txt
python takeAdvantageOfYourFood/manage.py populateDatabase
```
This command will call the Python class "[populateDatabase.py](https://github.com/juanrarodriguez18/takefood/blob/master/takeAdvantageOfYourFood/application/management/commands/populateDatabase.py)" wich clean all the data in the database, takes the data from the csv files on folder "csv" and insert this data into the database.

## Deploying the App

We can deploy the App in several ways:

- [Python](./README.md#python) (v3)
- [Docker](./README.md#docker)

## Python

For deploy the App from Python, we should use the next commands:

```bat
pip install -r requirements.txt
python takeAdvantageOfYourFood/manage.py runserver 0.0.0.0:8000 --nostatic
```

You can change the ip and port `0.0.0.0: 8000` with the ip and port that you need.

## Docker

Para lanzarlo desde Docker usaremos los siguientes comandos:

```bat
docker build --rm -f Dockerfile -t takefood:latest .
docker run -d -p 8000:8000 --name TakeAdvantageOfYourFood --restart always takefood:latest
