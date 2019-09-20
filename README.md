# kcc3
KCC3 is a simple badge server developed for
[Kraków Chombo Club](https://chombo.club/). It puts the focus on providing
simple interface, automate as much as possible and provide features especially
useful for Rīchi Mahjong players.


## Features
* Player database (tied with their USMA and Discord IDs)
* Static (manually-assigned) badges
* Dynamic badges that are updated automatically by querying given remote server
  that returns list of badge bearers
* Chombo event database
* Lightweight web user interface
* Easy to use admin panel
* RESTful API to get the data stored


## Quickstart
```
pip install -r requirements.txt
cp kccbadgeserver/settings/{development_settings.py.example,local_settings.py}
python manage.py migrate
python manage.py runserver
```

### Running the workers
Make sure you have [RabbitMQ](https://www.rabbitmq.com/download.html) installed.

```
celery -A kcc3 worker --beat --scheduler django --loglevel=info
```


## Creating own badge clients
Any third party can create their own dynamic badge by setting up a so called
badge client. Badge client is a web service that gets queried once per given
interval and returns a list of players that should be awarded the badge. The
badge client can make use of KCC3's RESTful API to get all the data needed for
granting the badge.

The communication uses conveniently defined models for data interchange
(with accompanying Serializer classes) as well as generated token for verifying
message authentication. To implement such service, one can either use
a small library inside `/badgeupdater/client/` (as well as common files
inside `/badgeupdater/`), or just implement the protocol (which is as easy
as parsing/serializing simple JSONs and comparing tokens).

First-parties can use convenient class called LocalBadgeClient and access
the database directly, without the API as a middleware.


## Local badge clients
There are some predefined local badge clients that can be used for creating
some specific dynamic badges easily.

### `/badge-clients/badges/test/`
Simple test client that grants a badge to all existing Players.

### `/badge-clients/chombos/chombos/`
Grants the badge to each player that has ever done a chombo.
