from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username')
        parser.add_argument('email')
        parser.add_argument('password')

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            for user in settings.ADMINS:
                username = options['username'].replace(' ', '')
                email = options['email']
                password = options['password']
                print('Creating account for %s (%s)' % (username, email))
                User.objects.create_superuser(email=email, username=username, password=password)
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
