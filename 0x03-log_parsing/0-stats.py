#!/usr/bin/python3
"""Log Analyzer"""
import sys


if __name__ == '__main__':
    file_sizes = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    def print_statistics():
        """Print the statistics"""
        print('File size: {}'.format(file_sizes[0]))
        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                print('{}: {}'.format(key, status_codes[key]))

    def parse_log_line(line):
        """Check each log line"""
        try:
            line = line[:-1]
            words = line.split(' ')
            # File size is the last parameter in the log line
            file_sizes[0] += int(words[-1])
            # Status code comes before file size
            status_code = int(words[-2])
            # Move through dictionary of status codes
            if status_code in status_codes:
                status_codes[status_code] += 1
        except BaseException:
            pass

    line_number = 1
    try:
        for line in sys.stdin:
            parse_log_line(line)
            """Print statistics after every 10 log lines"""
            if line_number % 10 == 0:
                print_statistics()
            line_number += 1
    except KeyboardInterrupt:
        print_statistics()
        raise
    print_statistics()
