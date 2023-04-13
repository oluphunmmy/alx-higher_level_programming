#!/usr/bin/python3
"""
This module reads stdin line by line and computes metrics
Input format: <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>
Every 10 lines or on keyboard interrupt, prints:
- Total file size: <total size>
- Number of lines by status code in ascending order (if seen):
  - <status>: <number>
"""
import sys



file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
i = 0
try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            a = i
            if tokens[-2] in status_tally:
                status_tally[tokens[-2]] += 1
                i += 1
            try:
                file_size += int(tokens[-1])
                if a == i:
                    i += 1
            except FileNotFoundError:
                if a == i:
                    continue
        if i % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(status_tally.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
