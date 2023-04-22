#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""

from sys import stdin

if __name__ == "__main__":
    file_size = 0
    status_codes = {}
    status_codes_list = [
        "200", "301", "400", "401", "403", "404", "405", "500"]
    for status in status_codes_list:
        status_codes[status] = 0
    count = 0
    try:
        for line in stdin:
            try:
                line_args = line.split(" ")
                if len(line_args) != 9:
                    pass
                if line_args[-2] in status_codes_list:
                    status_codes[line_args[-2]] += 1
                if line_args[-1][-1] == '\n':
                    line_args[-1][:-1]
                file_size += int(line_args[-1])
            except:
                pass
            count += 1
            if count % 10 == 0:
                print("File size: {}".format(file_size))
                for status in sorted(status_codes.keys()):
                    if status_codes[status] != 0:
                        print("{}: {}".format(
                            status, status_codes[status]))
        print("File size: {}".format(file_size))
        for status in sorted(status_codes.keys()):
            if status_codes[status] != 0:
                print("{}: {}".format(status, status_codes[status]))
    except KeyboardInterrupt as err:
        print("File size: {}".format(file_size))
        for status in sorted(status_codes.keys()):
            if status_codes[status] != 0:
                print("{}: {}".format(status, status_codes[status]))
        raise
