# Asynchronous tasks with django channels

This project is a sample of how to run async tasks with channels on a simple django project.

## How to run

Use: Python 3.4+

```
pyvenv env
source env/bin/activate
pip install requirements.txt
```

Run Daphne
```
daphne chann_tasks.asgi:channel_layer --port 8000
```

Run worker
```
python manage.py runworker
```

Do requests
```
python reqs.py
```
