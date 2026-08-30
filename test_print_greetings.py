import io
import sys
from print_greetings import print_hello


def test_print_hello():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_hello()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "hello world\n"
