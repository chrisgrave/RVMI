from django.core.management.base import BaseCommand
from django_auth_ldap.backend import LDAPBackend
import os
import django



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username')

    def handle(self, *args, **options):
        username = options['username']
        ldap_backend = LDAPBackend()
        ldap_backend.populate_user(username)



if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

    django.setup()