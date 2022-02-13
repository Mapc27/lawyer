import json

from services import telegram

from web.models import Application, User


def send_notification():
    applications = Application.objects.filter(is_notified=False)
    result = []
    for application in applications:
        result.append({
            "id": application.id,
            "phone_number": application.phone_number,
            "person_name": application.person_name,
            "description": application.description,
        })
    result = json.dumps(result, indent=4, ensure_ascii=False)
    telegram.send_message(User.objects.first().telegram_user_id, result)

    for application in applications:
        application.is_notified = True
