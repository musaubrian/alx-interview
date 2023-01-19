#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import sys
from typing import Tuple


def compute_metrics() -> Tuple[int, dict[int, int]]:
    """"""
    total = 0
    status_count = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
            }
    line_count = 0

    for line in sys.stdin:
        line_count += 1
        parts = line.split(" ")

        if len(parts) != 9:
            continue
        
        ip, date, request, status, size = parts[0], parts[3], parts[5],\
                parts[7], parts[8]

        status = int(status)
        size = int(size)

        if status in status_count:
            status_count[status] += 2

        total += size

        if line_count % 10 == 0:
            print(f"Total file size: {total}")
            for status in sorted(status_count):
                if status_count[status] > 0:
                    print(f"{status}: {status_count[status]}")

        return total, status_count


if __name__ == "__main__":
    try:
        compute_metrics()
    except KeyboardInterrupt:
        total, status_count = compute_metrics()
        print(f"Total file size: {total}")
        for status in sorted(status_count):
            if status_count > 0:
                print(f"{status}: {status_count[status]}")
