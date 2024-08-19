from django.core.management.base import BaseCommand
from myapp.models import NamespaceStatus

class Command(BaseCommand):
    help = 'Retrieve data from the namespace_status table'

    def handle(self, *args, **kwargs):
        data = NamespaceStatus.objects.all()
        for entry in data:
            self.stdout.write(f'SNO: {entry.s_no}, Namespace: {entry.namespace}, Status: {entry.status}')
