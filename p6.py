# python program to convert an array of machine values and return the bytes representation
import array
import binascii
a = array.array('i', [1, 2, 3, 4, 5, 6])
print("ORIGINAL ARRAY:\nA1: ", a)
a2 = a.tobytes()
print("Array of bytes: ", binascii.hexlify(a2))

