from django.test import TestCase
from core.models import *


class MapTestCase(TestCase):

    def test_maps_generate(self):
        """Maps is generated different sizes"""

        map = Map(name="test")
        map.generate(10, 10)

        self.assertEqual(map.generate(10, 10), True, "Squared map is generated")
        self.assertEqual(len(map.map), 10, "Map width equal 10")
        self.assertEqual(len(map.map[0]), 10, "Map height equal 10")
        self.assertEqual(map.name, "test", "Map name equal test")