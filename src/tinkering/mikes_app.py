import logging
import mikes_util
#import python.src.tinkering.mikes_util as mikes_util

import os
import sys


# # If having trouble importing a custom module, append src dir
# # path to the PATH, ensuring the Python interpreter finds
# # all modules in this dir.
# # Get file path for this module
# abs_file_path = os.path.abspath(__file__)
# print()
# print(abs_file_path)
# print()
# # Get dir of this file (src dir contains all your custom modules)
# sys.path.append(os.path.dirname(abs_file_path))

logger = logging.getLogger("mikes_app")


def setup_logging() -> None:
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)

    file_handler = logging.FileHandler('./logs/mikes_app.log')
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        '%(asctime)s::%(levelname)s::''%(name)s::%(funcName)s::''%(lineno)d::%(message)s')
    file_handler.setFormatter(file_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


def main() -> None:
    try:
        setup_logging()
    except Exception as e:
        print("Error setting up logging for application.")
        print(f"Exception: {e}")

    logger.debug("test log message INSIDE of main()")

    mikes_util.mikes_add(5, 5)

    logger.debug("after call to mikes_add function from mikes_app module")


if __name__ == "__main__":
    main()
