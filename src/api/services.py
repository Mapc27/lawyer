from django.core.mail import send_mass_mail
from django.conf import settings


def get_email_data(obj):
    if obj.is_check_trademark:
        title = "Новая заявка на проверку товарного знака"
        description_list = [f"Товарный знак: {obj.trademark if obj.trademark else ''}"]
    else:
        title = "Новая заявка"
        description_list = []

    description_list += [
        f"Телефон: {obj.phone_number}",
        f"Имя: {obj.person_name if obj.person_name else ''}",
        f"Описание: {obj.description if obj.description else ''}",
    ]

    description = "\n".join(description_list)
    return title, description


def send_email(users, obj):
    data_list = []
    for user in users:
        title, description = get_email_data(obj)
        data = (title, description, settings.DEFAULT_FROM_EMAIL, [user.email])
        data_list.append(data)
    send_mass_mail(data_list)
