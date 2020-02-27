# Maor Agai
# 305544546
# ex10a
import random


def main():
    # get probability from the user
    p = float(input())
    #   length of data to generate
    length = 10000
    f = open("tocompress.txt", "w+")
    f.write(createrandomsequance(p, length))
    f.close()

    f = open("tocompress.txt", "r")
    data = ""
    for line in f.readlines():
        data = data + line.strip()
    # create the lempel-ziv decoder
    lzencoder = lz()
    # compressed = lzencoder.copmress("0110001110100110101010100") # for testing purpuses
    compressed = lzencoder.copmress(data)
    f.close()
    # export to file
    f2 = open("compressed.txt", "w+")
    f2.write(compressed)
    f2.close()
    # export to terminal
    # print(compressed)
    # print(len(compressed.split(",")))


class lz():
    # dictionary to hold the mapping table
    indexes = dict()

    def __init__(self):
        pass

    def copmress(self, data):
        # for the 0110001110100110101010100 input sequence
        # this algo got the '01105344282129' compressed sequence and got the same results as
        # the instructor got in the tirgul
        compressed = ""
        self.indexes['0'] = 0
        self.indexes['1'] = 1
        indexcounter = 1
        offset = 0
        b = data[0]
        while offset < len(data) - 1:
            nextbit = data[offset + 1]
            st = b + nextbit
            # בcheck if current string and next bit are in the dictiona
            if b + nextbit in self.indexes.keys():
                b = b + nextbit
                offset += 1
            else:
                compressed = compressed + str(self.indexes[b]) + ","
                indexcounter += 1
                self.indexes[b + nextbit] = indexcounter
                offset += 1
                b = data[offset]
        if st in self.indexes.keys():
            compressed = compressed + str(self.indexes[b])
        else:
            self.indexes[b] = indexcounter
            compressed = compressed + str(self.indexes[b])
        return compressed


def createrandomsequance(probability, length):
    seq = ''
    for i in range(length):
        rnd = random.random()
        if rnd <= probability:
            seq = seq + '0'
        else:
            seq = seq + '1'
    return seq


main()
