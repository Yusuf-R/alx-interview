#!/usr/bin/python3
"""A module that performs log parsing and statistics calculations."""

import sys
from collections import defaultdict
import re


def search_items(line, status_codes):
    """
    A function that searches for items in a line and
    updates a dictionary of status codes.

    Parameters:
        line (str): The line to search for items.
        status_codes (dict): A dictionary containing
        status codes as keys and their respective counts as values.

    Returns:
        int: The size of the item found in the line,
        or 0 if no item is found.
    """
    valid_format = (re.match(r'^\S+ - \[.+\] "GET \S+ HTTP/1.1" \d{3} \d+$',
                             line))
    if valid_format:
        try:
            parts = line.split()
            if len(parts) >= 7:
                status = int(parts[-2])
                size = int(parts[-1])
                if size > 0 and status > 0:
                    status_codes[status] += 1
                    return size
        except (ValueError, IndexError):
            pass
    else:
        return None


def print_statistics(total_size, status_codes):
    """
    Prints the statistics of a file, including its total
    size and the count of each status code.

    Parameters:
        total_size (int): The total size of the file.
        status_codes (dict): A dictionary containing
        the status codes and their corresponding counts.

    Returns:
        None
    """
    if total_size > 0:
        print("File size: {:d}".format(total_size))
        for code, count in sorted(status_codes.items()):
            if count > 0:
                print("{}: {}".format(code, count))


def main():
    """
    A module that performs log parsing and statistics calculations.

    This module provides functions to search for items
    in log lines, update a dictionary of status codes,
    and print the statistics of a file,
    including its total size and the count of each status code.

    Functions:
        search_items(line, status_codes)
        print_statistics(total_size, status_codes)
        main()
    """
    status_codes = defaultdict(int)
    total_size = 0
    i = 0

    try:
        for line in sys.stdin:
            total_size += search_items(line, status_codes)

            if i != 0 and i % 9 == 0:
                print_statistics(total_size, status_codes)

            i += 1

    except KeyboardInterrupt:
        pass
    finally:
        print_statistics(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
