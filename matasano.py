import string
import base64
import pprint as p

english = {"E":12.02,
            "T":9.10,
            "A":8.12,
            "O":7.68,
            "I":7.31,
            "N":6.95,
            "S":6.28,
            "R":6.02,
            "H":5.92,
            "D":4.32,
            "L":3.98,
            "U":2.88,
            "C":2.71,
            "M":2.61,
            "F":2.30,
            "Y":2.11,
            "W":2.09,
            "G":2.03,
            "P":1.82,
            "B":1.49,
            "V":1.11,
            "K":0.69,
            "X":0.17,
            "Q":0.11,
            "J":0.10,
            "Z":0.07}

def challenge1():
    chalstring = bytearray([0x49,0x27,0x6d,0x20,0x6b,0x69,0x6c,0x6c,0x69,0x6e,0x67,0x20,0x79,0x6f,0x75,0x72,0x20,0x62,0x72,0x61,0x69,0x6e,0x20,0x6c,0x69,0x6b,0x65,0x20,0x61,0x20,0x70,0x6f,0x69,0x73,0x6f,0x6e,0x6f,0x75,0x73,0x20,0x6d,0x75,0x73,0x68,0x72,0x6f,0x6f,0x6d])
    print(base64.b64encode(chalstring))

def challenge2():
    chalstring = "1c0111001f010100061a024b53535009181c"
    xorstring = "686974207468652062756c6c277320657965"
    chalhex = bytearray.fromhex(chalstring)
    xorhex = bytearray.fromhex(xorstring)
    output = bytearray()
    for x in range(len(chalhex)):
        output.append(chalhex[x] ^ xorhex[x])
    return output

def challenge3():
    chalstring = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    chalhex = bytearray.fromhex(chalstring)
    f = get_freq(chalhex)
    print_freqs(f)

def xor(barr1, barr2):
    output = bytearray()
    if (len(barr1) == len(barr2)):
        """ one time pad xor """
        for x in range(len(barr1)):
            output.append(barr1[x] ^ barr2[x])
    elif(type(barr2) == type(byetarray())):
        """ repeating byte arrays xor """
        for x in range(len(barr1)):
            output.append(barr1[x] ^ barr2[(x % len(barr2))])
    elif(type(barr2) == type(0x1)):
        """ single value xor """
        for x in range(len(barr1)):
            output.append(barr1[x] ^ barr2)
    else:
        """ ERROR """
        raise(TypeError("xor takes in either a byet array or an int"))
    return output

def get_freq(barr):
    length = len(barr)
    freqs = {}
    for x in range(length):
        freqs[barr[x]] = freqs.setdefault(barr[x], 0) + 1
    return freqs

def print_freqs(f):
    for x in f:
        print("freq of {} is {:.2%}".format(x, int(f[x])/len(f)))



challenge1()
print(repr(challenge2()))
challenge3()
