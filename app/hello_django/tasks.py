from celery import shared_task



@shared_task
def test_scheduling():
    print("hello this is a test")