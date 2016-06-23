# Asynchronous tasks with django channels

This project is a sample of how to run async tasks with channels on a simple django project.

## How to run

Use: Python 3.4+

Install redis-server
```
$ # MacOS
$ homebrew install redis
$ # Debian
$ apt-get install redis-server
```

Clone and install requirements
```
$ git clone git@github.com:macndesign/chann_tasks.git
$ cd chann_tasks
$ pyvenv env
$ source env/bin/activate
$ pip install requirements.txt
```

Run Daphne
```
$ daphne chann_tasks.asgi:channel_layer --port 8000
```

Run worker
```
$ python manage.py runworker
```

Do requests
```
$ python reqs.py
```
