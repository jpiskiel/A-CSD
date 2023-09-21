import unittest


class Shield:

    def __init__(self):
        self.is_raised = False

    def is_up(self):
        return self.is_raised

    def be_raised(self):
        self.is_raised = True

    def check_level(self):
        return 4000


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.shield = Shield()

    def test_down_by_default(self):
        self.assertFalse(self.shield.is_up())

    def test_can_be_raised(self):
        self.shield.be_raised()
        self.assertTrue(self.shield.is_up())

    def test_shield_starts_with_4000_energy_by_default(self):
        self.assertEquals(4000, self.shield.check_level())



if __name__ == '__main__':
    unittest.main()
