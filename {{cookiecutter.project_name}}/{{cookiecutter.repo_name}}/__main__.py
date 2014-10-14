#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


class Main(object):
    def __call__(self, args):
        return True


def main():
    main = Main()
    value = main(sys.argv[1:])
    if isinstance(value, bool):
        value = int(not value)
    elif value is None:
        value = 0

    sys.exit(value)

if __name__ == '__main__':
    main()
