from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html
from web.models import Application, SolvedApplication, User


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'blank_link_to_trademark', 'phone_number', 'person_name',
                    'description', 'is_check_trademark', 'is_done']
    list_display_links = ['id', 'created_at', 'updated_at', 'phone_number', 'person_name', 'description',
                          'is_check_trademark', 'is_done']

    fields = list_display
    readonly_fields = ['id', 'created_at', 'updated_at', 'blank_link_to_trademark', 'phone_number', 'person_name',
                       'description', 'is_check_trademark']

    search_fields = ('phone_number', 'person_name')
    list_filter = (
        ('is_check_trademark', admin.BooleanFieldListFilter),
        ('is_done', admin.BooleanFieldListFilter),
        'created_at',
        'updated_at'
    )

    def blank_link_to_trademark(self, obj):
        if obj.trademark:
            return format_html(
                f'<a  href="{settings.MEDIA_URL + str(obj.trademark)}" class="button" target="_blank">Файл</a>&nbsp;',
            )
        else:
            return ''

    blank_link_to_trademark.short_description = 'Товарный знак'
    blank_link_to_trademark.allow_tags = True


@admin.register(SolvedApplication)
class SolvedApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'title', 'history', 'result']
    list_display_links = ['id', 'created_at', 'updated_at', 'title', 'history', 'result']
    readonly_fields = ['id', 'created_at', 'updated_at']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'email', 'is_staff', 'telegram_user_id']
    list_display_links = ['id', 'created_at', 'updated_at', 'email', 'is_staff', 'telegram_user_id']
    readonly_fields = ['id', 'created_at', 'updated_at', 'password']

    list_filter = (
        ('is_staff', admin.BooleanFieldListFilter),
    )
