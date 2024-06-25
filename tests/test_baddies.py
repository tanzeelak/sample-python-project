import unittest
from src.baddie import Baddie

class TestInitBaddie(unittest.TestCase):
    def test_default(self):
        baddie = Baddie(
            name="hee", 
            age=10, 
            vibe="thot"
        )
        self.assertEqual(baddie.name, "hee")
        self.assertEqual(baddie.age, 10)
        self.assertEqual(baddie.vibe, "thot")
