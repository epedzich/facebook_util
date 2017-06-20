from django.core.management.base import BaseCommand
from lxml import html
from tqdm import tqdm

from fb_parser.models import FbThread, FbMessage


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, **options):
        file_path = options['file']
        with open(file_path, 'r', encoding='utf-8') as fp:
            tresc = fp.read()

        root = html.fromstring(tresc)
        threads = root.xpath('//*[@class="contents"]//*[@class="thread"]')
        messages = []
        for element in tqdm(threads):
            thread = FbThread.objects.create(users=element.text)
            for p in element.xpath('./p'):
                div = p.getprevious()
                message = FbMessage(
                    thread=thread,
                    text=html.tostring(p),
                    user=div.find('.//*[@class="user"]').text,
                    meta=div.find('.//*[@class="meta"]').text
                )
                messages.append(message)
        FbMessage.objects.bulk_create(messages)
