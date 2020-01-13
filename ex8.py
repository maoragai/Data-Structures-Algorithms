# Maor Agai
# 305544546
# ex8

class ufheap:
    # this is the union find class implementation from ex4
    # but in order for it to adapt to any node representation (letters/integers as requested) i changed it to use
    # a dictionary instead of an array, this change shouldn't have any effect on the efficiency
    conarray = dict()  # this array will be of n+1 size and neglect the 0 place

    def __init__(self, nodes):
        # create a dictionary which in which the keys are the nodes of the graph
        for i in nodes:
            self.conarray[i] = int(i)

    def union(self, p, q):
        # this union method will be responsible to change all
        # the new group members to point to the new root
        # this way there will be no trees for a specific root
        # algo complexity:
        # group size calc = O(n)
        # group unify= O(n)
        pcounter = 0
        qcounter = 0
        group_of_p = self.conarray[p]
        group_of_q = self.conarray[q]
        # we want to see which group is bigger by counting occurrences
        for i in self.conarray.keys():
            if self.conarray[i] == group_of_p:
                pcounter += 1
            if self.conarray[i] == group_of_q:
                qcounter += 1
        if pcounter > qcounter:
            self.change_father(group_of_q, group_of_p)
        elif pcounter < qcounter:
            self.change_father(group_of_p, group_of_q)
        else:
            if p < q:
                self.change_father(group_of_p, group_of_q)
            if q <= p:
                self.change_father(group_of_q, group_of_p)

    def change_father(self, old_father, new_father):
        # algo complexity: O(n)
        for i in self.conarray.keys():
            if self.conarray[i] == old_father:
                self.conarray[i] = new_father


def todict(liseddb):
    # this data structure will hold the dictionary in dictionary as requested by the staff
    db = dict()
    vertexset = set()
    for item in liseddb:
        vertex1 = item[0]
        vertex2 = item[1]
        weight = item[2]
        # just to ease some things ill create the set of all the vertexes
        vertexset.update([vertex1, vertex2])
        # checks if vertex1 is already in the db
        # if not initialize
        if vertex1 not in db:
            db[vertex1] = {vertex2: weight}
        else:
            if vertex2 not in db[vertex1]:
                db[vertex1][vertex2] = weight
            # we want the weight to update only if its a new minimum
            if db[vertex1][vertex2] > weight:
                db[vertex1][vertex2] = weight
        if vertex2 not in db:
            db[vertex2] = {vertex1: weight}
        else:
            if vertex1 not in db[vertex2]:
                db[vertex2][vertex1] = weight
            # we want the weight to update only if its a new minimum
            if db[vertex2][vertex1] > weight:
                db[vertex2][vertex1] = weight
    return db, vertexset


def sortdB(filename):
    # takes the input file
    # returns a listed [vertex,vertex,weight]
    file = open(filename)
    lines = file.readlines()
    db = []
    for line in lines:
        currentlinelist = line.strip().split(" ")
        currentlinelist[2] = int(currentlinelist[2])
        db.append(currentlinelist)
    # i am familiar with lambda programming and its an embedded python technique
    # so i hope i wont get points reduction for that. of course this is just for sorting purposes.
    db.sort(key=lambda x: x[2])
    return db


def createMST(uf, vertexlist):
    weightsum = 0
    for item in vertexlist:
        vertex1 = item[0]
        vertex2 = item[1]
        weight = item[2]
        # the list is already sorted therefor the edges is the shortest on top and will be first
        # if the nodes arent part of the same minimal tree that means we can add them to the same tree with the new edge
        if uf.conarray[vertex1] != uf.conarray[vertex2]:
            uf.union(vertex1, vertex2)
            weightsum += weight
    return weightsum


def main():
    # read the file (currently hardcoded)
    filename = "input.txt"
    #filename=input()#this option didnt work on submit
    listeddb = sortdB(filename)
    becausepolinaaskeddB, versexset = todict(listeddb)
    numberofnodes = len(versexset)
    unionfind = ufheap(versexset)
    weightsum = createMST(unionfind, listeddb)
    print(weightsum)


main()
