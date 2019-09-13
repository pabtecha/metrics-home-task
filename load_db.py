import os, django

print(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

ROOT_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
SETTINGS_PATH = f'{ROOT_PATH}/adjust/settings'

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_PATH)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'adjust.settings')
django.setup()

print('hello world')
