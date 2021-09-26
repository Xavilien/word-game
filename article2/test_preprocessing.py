from unittest import TestCase
from article2.preprocessing import *


class Test(TestCase):
    def test_remove_prefix(self):
        self.assertEqual(remove_prefix(['a', 'ab'], ""), ['a'])
        self.assertEqual(remove_prefix(['a', 'ab', 'ac'], ""), ['a'])
        self.assertEqual(remove_prefix(['a', 'ab', 'ac', 'b', 'ba', 'bc'], ""), ['a', 'b'])
        self.assertEqual(remove_prefix(['dog', 'doggy', 'doggie', 'dogbone'], ""), ['dog'])
