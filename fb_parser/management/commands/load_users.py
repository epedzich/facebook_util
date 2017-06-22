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
            all_speakers = str(element.text)
            speakers = all_speakers.partition(',')

                for s in speakers:

            user = FbUser.objects.get_or_create(users=element.text)
            for p in element.xpath('./p'):
                fbuser = FbUser(
                    facebook_id=user,
                    threads=
                )
                ids.append(fbuser)

