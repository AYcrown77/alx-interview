#!/usr/bin/python3
"""Log Parser function"""
import sys


if __name__ == '__main__':
    size = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    def stats_output():
        """ Function that prints the stats """
        print('File size: {}'.format(size[0]))
        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                print('{}: {}'.format(key, status_codes[key]))

    def parse_line(line):
        """ Function that checks the line for matches """
        try:
            line = line[:-1]
            word = line.split(' ')
            size[0] += int(word[-1])
            status_code = int(word[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except BaseException:
            pass

    line_num = 1
    try:
        for line in sys.stdin:
            parse_line(line)
            if line_num % 10 == 0:
                print_stats()
            line_num += 1
    except KeyboardInterrupt:
        stats_output()
        raise
    stats_output()
