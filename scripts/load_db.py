import csv
import django
import os
import sys


ROOT_PROJECT_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
sys.path.append(ROOT_PROJECT_PATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'adjust.settings')
django.setup()

from metrics.models import Metrics


def load_dataset() ->list:
    os.chdir(os.path.dirname(__file__))

    with open("dataset.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        dataset = [Metrics(**dict(row)) for row in reader]

    csvfile.close()

    return dataset


if __name__ == '__main__':
    Metrics.objects.bulk_create(load_dataset())

    print(Metrics.objects.all().count())
