import unittest
import os
import sys
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils.report import ReportImageParser

parent, _ = os.path.split(SCRIPT_DIR)
images_folder = os.path.join(parent, 'images')
fixtures_path = os.path.join(SCRIPT_DIR, 'fixtures', 'data.json')

class TestImageParser(unittest.TestCase):
    def setUp(self):
        self.images = []
        images_paths = os.listdir(images_folder)
        images_paths.sort()
        for image_path in images_paths:
            report = ReportImageParser(os.path.join(images_folder, image_path))
            report.parse_image()
            self.images.append(report)
        with open(fixtures_path) as f:
            self.fixtures = json.load(f)

    def test_dataset(self):
        images_names = sorted(self.fixtures.keys())
        for image_parsed, fixture_image in zip(self.images, images_names):
            for attr, value in self.fixtures[fixture_image].items():
                self.assertEqual(getattr(image_parsed, attr), value, f'{fixture_image!r} asserting value {attr} = {value}')


if __name__ == '__main__':
    unittest.main()