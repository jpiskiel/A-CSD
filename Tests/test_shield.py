import unittest


class Shield:

    def __init__(self):
        self.is_raised = False

    def is_up(self):
        return self.is_raised

    def be_raised(self):
        self.is_raised = True

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.shield = Shield()

    def test_down_by_default(self):
        self.assertFalse(self.shield.is_up())

    def test_can_be_raised(self):
        self.shield.be_raised()
        self.assertTrue(self.shield.is_up())

if __name__ == '__main__':
    unittest.main()
