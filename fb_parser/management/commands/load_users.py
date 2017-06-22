from django.core.management.base import BaseCommand
from lxml import html
from tqdm import tqdm

from fb_parser.models import FbThread, FbUser


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, **options):
        file_path = options['file']
        with open(file_path, 'r', encoding='utf-8') as fp:
            tresc = fp.read()

        root = html.fromstring(tresc)
        facebook_users = root.xpath('//*[@class="contents"]//*[@class="thread"]')
        ids = []
        for element in tqdm(facebook_users):
            speakers = str(element.text).split(',')
            for s in speakers:
                s.replace('@facebook.com', '')
                ids.append(s)
            user = FbUser.objects.get_or_create(threads=element.text, facebook_id=s)

        for p in element.xpath('./p'):
            fbuser = FbUser(
                facebook_id=user,
                threads=
            )
            ids.append(fbuser)
