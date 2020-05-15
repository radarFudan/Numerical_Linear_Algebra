# I learned about this from answers on the stack overflow website
# https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex

# To use these functions interactively in python3 console, run the command `python3 -i machine-epsilon.py`

import struct
def binary(num):
    return ''.join(bin(c).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))
# It is said that the python3 do required the ord(c) since the result from struct.pack is already a number.

def binary_detailed(num):
    # Struct can provide us with the float packed into bytes. The '!' ensures that
    # it's in network byte order (big-endian) () and the 'f' says that it should be
    # packed as a float. Alternatively, for double-precision, you could use 'd'.
    # Notes from sanderwang: big-endian https://en.wikipedia.org/wiki/Endianness
    # The change from print str and % to print(str) and .format is just a change from python2 to python3
    packed = struct.pack('!f', num)
    print('Packed: {}'.format(repr(packed)))

    # For each character in the returned string, we'll turn it into its corresponding
    # integer code point
    #
    # [62, 163, 215, 10] = [ord(c) for c in '>\xa3\xd7\n']
    integers = [c for c in packed]
    print('Integers: {}'.format(integers))

    # For each integer, we'll convert it to its binary representation.
    binaries = [bin(i) for i in integers]
    print('Binaries: {}'.format(binaries))

    # Now strip off the '0b' from each of these
    stripped_binaries = [s.replace('0b', '') for s in binaries]
    print('Stripped: {}'.format(stripped_binaries))

    # Pad each byte's binary representation's with 0's to make sure it has all 8 bits:
    #
    # ['00111110', '10100011', '11010111', '00001010']
    padded = [s.rjust(8, '0') for s in stripped_binaries]
    print('Padded: {}'.format(padded))

    # At this point, we have each of the bytes for the network byte ordered float
    # in an array as binary strings. Now we just concatenate them to get the total
    # representation of the float:
    return ''.join(padded)
