"""
WSGI config for chat_or_quiz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/home/ipanzek/public_html/chat-or-quiz/chat_or_quiz/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'chat_or_quiz.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
