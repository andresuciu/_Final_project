#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Book_Store.settings')
    try:
        from django.core.management import execute_from_command_line  # importa functia din Django
    except ImportError as exc:    # daca nu gaseste Django instalat, avem eroare cu mesajul de mai jos
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)  # sys.argv contine ['manage.py','runserver']


if __name__ == '__main__':   # verifica daca este rulat direct (nu importat)
    main()   # apeleaza functia principala


