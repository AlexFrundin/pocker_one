import unittest
import unit_test

class TestField(unittest.TestCase):
#вызывается самостоятельно
    def setUp(self):
        self.g=unit_test.Game_Field()

    def test_set(self):
        self.g.set_sign(0,0,x)
        self.assertEqual(self.g._field[0][0],'X')

    def test_check_row(self):
        self.g.set_sign(1,0,'X')
        self.g.set_sign(1,1,'X')
        self.g.set_sign(1,2,'X')
        self.assertTrue(self.test_())
