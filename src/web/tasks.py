from lawyer.celery import app
from web.services.notifications import send_notification


@app.task(queue="default")
def send_notification_task():
    send_notification()
