#!/usr/bin/env python3

import random, sys
from binascii import unhexlify

def long_to_bytes (val, endianness='big'):
    """
    Use :ref:`string formatting` and :func:`~binascii.unhexlify` to
    convert ``val``, a :func:`long`, to a byte :func:`str`.

    :param long val: The value to pack

    :param str endianness: The endianness of the result. ``'big'`` for
      big-endian, ``'little'`` for little-endian.

    If you want byte- and word-ordering to differ, you're on your own.

    Using :ref:`string formatting` lets us use Python's C innards.
    """

    # one (1) hex digit per four (4) bits
    width = val.bit_length()

    # unhexlify wants an even multiple of eight (8) bits, but we don't
    # want more digits than we need (hence the ternary-ish 'or')
    width += 8 - ((width % 8) or 8)

    # format width specifier: four (4) bits per hex digit
    fmt = '%%0%dx' % (width // 4)

    # prepend zero (0) to the width, to zero-pad the output
    s = unhexlify(fmt % val)

    if endianness == 'little':
        # see http://stackoverflow.com/a/931095/309233
        s = s[::-1]

    return s

def bxor(ba1,ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

bits = 128
shares = 35

poly = [random.getrandbits(bits) for _ in range(shares)]
flag = open("flag.txt","rb").read()

random.seed(poly[0])
print(bxor(flag, long_to_bytes(random.getrandbits(len(flag)*8))).hex())

try:
    x = int(input('Take a sum of shares... BUT ONLY ONE. \n'))
except:
    sys.exit(1)
if  x< 1:
    print('No way')
else:
    print(sum(map(lambda i: poly[i] * pow(x, i), range(len(poly)))))




