import logging
import sys
import os


logger = logging.getLogger("mikes_app")


def mikes_add(x, y):
    logger.debug("Inside mikes_add() function in mikes_util module")
    return x + y

def mikes_subtract(x, y):
    logger.debug("Inside mikes_subtract() function in mikes_util module")
    return x - y

def mikes_mult(x, y):
    logger.debug("Inside mikes_mult() function in mikes_util module")
    return x * y   


def main() -> None:
    # No logger here. This code only runs if executed directly.
    # Recall the logger is a singleton invoked by running main.py
    print("Inside main() of mikes_util.py")
    print("Calling mikes_add() function...")
    print("Passing 2 + 2 in as parameters.")
    result = mikes_add(2,2)
    print(f"Guess what MFer?  The result was:  {result}")
    #print(f"We have {count} even numbers.")

if __name__ == "__main__":
    main()
