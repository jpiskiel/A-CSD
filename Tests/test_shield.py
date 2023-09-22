import unittest

from Ship.Shield import Shield

class MyTestCase(unittest.TestCase):

    def setUp(self):
        #Given
        self.shield = Shield()

    def test_down_by_default(self):
        #When & Then
        self.assertFalse(self.shield.is_up())

    def test_can_be_raised(self):
        #When
        self.shield.be_raised()
        #Then
        self.assertTrue(self.shield.is_up())

    def test_shield_starts_with_4000_energy_by_default(self):
        #When & Then
        self.assertEquals(4000, self.shield.check_level())

    def test_shield_can_receive_energy_from_ship(self):
        #When
        self.shield.receive_energy(2000)
        new_level = self.shield.check_level()
        #Then
        self.assertEqual(6000, new_level)

    def test_shield_level_max_10000(self):
        #When
        self.shield.receive_energy(20000)
        new_level = self.shield.check_level()
        #Then
        self.assertEqual(10000, new_level)

if __name__ == '__main__':
    unittest.main()
