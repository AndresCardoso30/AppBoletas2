#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

from weasyprint import HTML

HTML('https://weasyprint.org/').write_pdf('weasyprint-website.pdf')

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boletas.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
