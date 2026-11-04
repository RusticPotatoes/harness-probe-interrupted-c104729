import unittest

from stockroom.entity import Order
from stockroom.serializer import from_dict, to_dict


class Roundtrip(unittest.TestCase):
    def test_roundtrip(self):
        rec = Order(1, "a", status="closed")
        self.assertEqual(from_dict(to_dict(rec)), rec)
