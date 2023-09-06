import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

app = Celery('hello_django')

app.config_from_object('django.conf:settings', namespace='CELERY')



app.conf.broker_connection_retry_on_startup = True

app.autodiscover_tasks()
app.conf.beat_schedule = {

'test scheduling': {
        'task': 'tasks.test scheduling',
        'schedule': crontab(minute='0', hour='0'),
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
