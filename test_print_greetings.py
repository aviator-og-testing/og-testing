import io
import sys
from print_greetings import print_hello, print_bye


def test_print_hello():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_hello()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "hello world\n"


def test_print_bye():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_bye()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "bye world\n"


def test_print_both():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_hello()
    print_bye()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "hello world\nbye world\n"
