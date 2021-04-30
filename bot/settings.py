import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    print('You have forgot to set BOT_TOKEN')
    quit()

START_TEXT = '''
Salam! Mən sağam. *Mənə sual ver.*

Mənə göndərdiyiniz hər hansı bir mesaj bir sual kimi qəbul edilir.

Müvafiq kod parçalarını cavablandıracağam. Cari sualın növbəti cavabını almaq üçün /next göndərə bilərsiniz.
'''

HELP_TEXT = '''
Mənə göndərdiyiniz hər hansı bir mesaj bir sual kimi qəbul edilir.

Müvafiq kod parçalarını cavablandıracağam. Cari sualın növbəti cavabını almaq üçün /next göndərə bilərsiniz.
'''

BOT_COMMANDS = [
    ('start', 'check whether i am alive'),
    ('help', 'know more about me'),
    ('next', 'get next answer'),
]


