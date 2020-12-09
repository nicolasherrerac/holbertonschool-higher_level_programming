#!/usr/bin/env python3
for c in reversed(range(97, 123)):
    if c % 2 != 0:
        rest = 32
    else:
        rest = 0
    print("{}".format(chr(c - rest)), end="")
