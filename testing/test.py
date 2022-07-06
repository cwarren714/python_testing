import unittest
import main
# don't care about repeating, testing doesn't make it to production so it doesn't matter a s much


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'hfghfgh'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def tearDown(self) -> None:
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()
