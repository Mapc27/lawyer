from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse


def get_email_data(obj, request):
    if obj.is_check_trademark:
        title = "Новая заявка на проверку товарного знака"
        description_list = [
            f"Товарный знак: "
            f"{request.build_absolute_uri(settings.MEDIA_URL + str(obj.trademark)) if obj.trademark else ''}"
        ]
    else:
        title = "Новая заявка"
        description_list = []

    url = request.build_absolute_uri(
        reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', args=(obj.id,))
    )
    description_list += [
        f"Телефон: {obj.phone_number}",
        f"Имя: {obj.person_name if obj.person_name else ''}",
        f"Описание: {obj.description if obj.description else ''}",
        f"Ссылка: {url}",
    ]

    description = "\n".join(description_list)
    return title, description


def send_email(obj, request):
    title, description = get_email_data(obj, request)
    data = (title, description, settings.DEFAULT_FROM_EMAIL, [settings.DESTINATION_EMAIL])

    send_mail(*data)
