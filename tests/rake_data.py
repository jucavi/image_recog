import os
import sys
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils.report import CONTENT_FORMAT


parent, _ = os.path.split(SCRIPT_DIR)
images = os.listdir(os.path.join(parent, 'images'))

data = {}
for image in images:
    image_name = image.split('.')[0]
    print(f'Manual proccessing ogf image {image!r}')
    data[image_name] = {}
    for zone in CONTENT_FORMAT.values():
        for fields in zone['keys']:
            for field in fields:
                value = input(f'{field} = ')
                if field == 'channel_name':
                    value = 'CHARTCHAMPIONS'
                data[image_name][field] = value

fixtures = os.path.join(SCRIPT_DIR, 'fixtures', 'data.json')
with open(fixtures, 'w') as f:
    json.dump(data, f, indent=4)

