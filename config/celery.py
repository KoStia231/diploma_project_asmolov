from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# Установка переменной окружения для настроек проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создание экземпляра объекта Celery
app = Celery('config')

# Загрузка настроек из файла Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из файлов tasks.py в приложениях Django
app.autodiscover_tasks()


# Инициализируем Celery, чтобы работать с Django
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
