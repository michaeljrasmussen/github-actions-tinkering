import logging
import pytest
import sys
import os
from src.tinkering.mikes_util import mikes_add, mikes_mult, mikes_subtract


# Uncomment below to run this module directly. Otherwise, get
# 'can't find module exception'. You don't really want to run this
# directly anyway. Want to use "python3 -m pytest ./tests/test_mikes_util.py"
# from the venv CLI to run tests in this file.

# abs_file_path = os.path.abspath(__file__)
# sys.path.append(os.path.dirname(os.path.dirname(abs_file_path)))
# from src.tinkering.mikes_util import mikes_add


def test_mikes_add():
    assert mikes_add(5,5) == 10


def test_mikes_subtract():
    assert mikes_subtract(10,5) == 5   


def test_mikes_mult():
    assert mikes_mult(5,5) == 25


def main() -> None:
    test_mikes_add()
    print()
    print("test_mikes_add() called from test_mikes_util.py")
    print()


if __name__ == "__main__":
    main()