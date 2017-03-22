import unittest
import controller


class MainTests(unittest.TestCase):

    def __init__(self):
        self.con = controller.Controller()

    def test_1(self):
        self.x = 5
        self.assertTrue(self.x == 5, "the value of x should be 5!")

    def test_02(self):
        print(2)
        self.x = 6
        self.assertEqual(6, 3 * 2)

    @unittest.skip('I have not coded how this will work yet.')
    def test_01(self):
        print(1)
        self.assertTrue(None is 42)
        self.x = 666

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main(verbosity=1)  # with more details
    # unittest.main()
