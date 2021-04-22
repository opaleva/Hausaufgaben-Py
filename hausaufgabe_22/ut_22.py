import unittest
from hausaufgabe_22 import Time


class TestTime(unittest.TestCase):
    @unittest.expectedFailure
    def test_minutes(self):
        self.assertRaises(AssertionError, Time(20, 70, 20))

    @unittest.expectedFailure
    def test_seconds(self):
        self.assertRaises(AssertionError, Time(20, 50, 90))

    def test_add_time(self):
        a = Time(10, 50, 40)
        a.add_time(10, 15, 35)
        self.assertEqual(a, Time(21, 6, 15))


if __name__ == '__main__':
    unittest.main()
