#!/usr/bin/python3
"""
This script reads standard input line by line and calculates metrics.
"""

from sys import stdin

if __name__ == "__main__":
    total_size = 0
    status_counts = {}
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    for code in status_codes:
        status_counts[code] = 0
    count = 0
    try:
        for line in stdin:
            try:
                fields = line.split(" ")
                if len(fields) != 9:
                    continue
                status_code = fields[-2]
                if status_code in status_codes:
                    status_counts[status_code] += 1
                if fields[-1][-1] == '\n':
                    fields[-1] = fields[-1][:-1]
                total_size += int(fields[-1])
            except Exception:
                pass
            count += 1
            if count % 10 == 0:
                print("Total size: {}".format(total_size))
                for code in sorted(status_counts.keys()):
                    if status_counts[code] != 0:
                        print("{}: {}".format(code, status_counts[code]))
        print("Total size: {}".format(total_size))
        for code in sorted(status_counts.keys()):
            if status_counts[code] != 0:
                print("{}: {}".format(code, status_counts[code]))
    except KeyboardInterrupt:
        print("Total size: {}".format(total_size))
        for code in sorted(status_counts.keys()):
            if status_counts[code] != 0:
                print("{}: {}".format(code, status_counts[code]))
        raise
