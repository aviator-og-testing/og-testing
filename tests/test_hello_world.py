import unittest
from io import StringIO
import sys
import hello_world


class TestHelloWorld(unittest.TestCase):
    def test_print_hello_world(self):
        self.assertEqual(hello_world.print_hello_world(), "hello world")

    def test_main_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        hello_world.main()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "hello world\n")


if __name__ == "__main__":
    unittest.main()
