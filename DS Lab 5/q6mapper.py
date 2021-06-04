import fileinput
import sys


def main():
    for line in sys.stdin:
        line = line.strip()
        data = line.split()
        if len(data) >= 64:
            print(f'{data[1]}\t{data[31]}')


if __name__ == '__main__':
    main()
