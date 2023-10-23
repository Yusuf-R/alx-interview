#!/usr/bin/env python3

import sys
from collections import defaultdict


def search_items(line, status_codes):
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
    return 0


def print_statistics(total_size, status_codes):
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


def main():
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


if __name__ == "__main__":
    main()
