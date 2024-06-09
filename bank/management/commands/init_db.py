from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Initialize the database with SQL scripts'

    def handle(self, *args, **kwargs):
        try:
            sql_path = r"C:\Users\nikak\bank\backend\init.sql"
            with open(sql_path, 'r') as file:
                sql_statements = file.read()
            with connection.cursor() as cursor:
                cursor.executescript(sql_statements)
            self.stdout.write(self.style.SUCCESS(
                'Database initialized successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                f'Error initializing database: {e}'))
