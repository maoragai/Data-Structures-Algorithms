# Maor Agai
# 305544546
# ex10b

class hashtabl():
    n = 0
    arraylen = 0
    dictarray = []
    primers = []
    def __init__(self, n, lengthofarray):
        # this function takes the length of the substring to check and the length of the whole string
        self.n = n
        self.arraylen = lengthofarray
        # creating an array of polynomial prime number
        self.primers = [7 ** i for i in range(n)]
        # initializing the dictionary array
        self.dictarray = [0] * self.arraylen
        for i in range(self.arraylen - 1):
            self.dictarray[i] = []

    def inedex(self, key):
        # wiil return the location for a given key
        return self.hashfun(key) % self.arraylen

    def hashfun(self, key):
        # holds the hash function
        sum = 0
        # get the text and the string length
        for i in range(len(key)):
            sum += ord(key[i]) * self.primers[i]
        return sum

    def insert(self, key, value):
        # for a given key this method will increase the value in location [index] by 1
        place = self.inedex(key)
        # nestedlist=self.dictarray[place]
        # nestedlist.append(key)
        self.dictarray[place].append(key)

    def getvalue(self, key):
        numofapearences = 0
        for string in self.dictarray[self.inedex(key)]:
            if string == key:
                numofapearences += 1
        return numofapearences


def main():
    # get the text and the string length
    text = input().split(" ")
    n = int(text[1])
    text = text[0]
    # number for test # n = 3
    # text for test # text = "the_rain_in_spain_stays_mainly_on_the_drain"
    hush = hashtabl(n, 5 * len(text))
    for str in searchstring(n, text, hush):
        print(str)


def searchstring(n, text, hasht):
    apeartwice = set()
    for i in range(len(text)):
        str = text[i:i + n]
        hasht.insert(str, 1)
    for i in range(len(text)):
        str = text[i:i + n]
        if hasht.getvalue(str) == 2:
            apeartwice.add(str)
    return sorted(apeartwice)


main()
