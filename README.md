# webmon

With webmon you are able to monitor your system using a static website. To ensure your monitoring is visible in your browser, put webmon's update.sh to your crontab and add webmon's url to your new tab config in your browser.

# Features

* Creating/Updating static websites which shows monitoring data
* Monitored data can be modified in update.py
* Monitoring data can be served using webmon.py or any webserver
* Automatic refresh of webmon UI every 30 seconds


# How to install dependencies?

These software dependencies are used:
* bash
* python3
* jinja2
* cherrypy


Install the python dependencies:

```
python -m venv .venv
source .venv/bin/activate
pip install -U -r requirements.txt pip
```

# How to use?

Initially you have to create the index.html. This file can be served using webmon.py or any other webserver. 

```
./update.sh
./webmon.py
```


# How to update the data automatically using cron

If you want to update every minute just add this lines to your crontab using `crontab -e`

```
* * * * * YOUR_PATH_TO_WEBMON/update.sh
```


# How to add your own cards?

Edit the card definition in update.py
