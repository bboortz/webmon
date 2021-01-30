# webmon

With webmon you are able to monitor your systems using a static website. To ensure your monitoring is visible in your browser, put webmon's update.sh to your crontab and add webmon's url to your new tab config in your browser.

![Screenshot](/screenshot.png?raw=true "Screenshot")


# Features

* Gathing monitoring data using gather.py
  * Monitored data can be modified in gather.py
* Creating/Updating static websites which shows monitoring data using render.py
  * Able to render monitoring data from different system. Just put all the monitoring data into the tmp dir. render.py will take it and render one big screen.
* Monitored data can be served using webmon.py or any webserver
* Automatic refresh of webmon UI every 30 seconds


# How to install dependencies?

These software dependencies are used mainly:
* bash
* python3
* jsonpickle
* jinja2
* cherrypy


Install the python dependencies:

```
./scripts/install.sh
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

Edit the card definition in gather.py
