#   Agai Maor

#   ex1a

# queue implementation as a class
class Queue:
    def __init__(self):
        self.arr = []

    def isempty(self):
        return bool(len(self.arr) == 0)

    def enqueue(self, q):
        if self.isempty():
            self.arr.append(q)
        else:
            self.arr.append([])
            for i in range(len(self.arr) - 1, 0, -1):
                self.arr[i] = self.arr[i - 1]
            self.arr[0] = q

    def dequeue(self):
        self.arr.remove(self.arr[len(self.arr) - 1])

    def size(self):
        return self.arr.__len__

# function that maps neighbors of a certain point in the matrix and enqueue them into the queue
def mapneighbors(matrix, p, q):
    # assuming the input is legit
    i = p[0]  # line index
    j = p[1]  # column index
    layernodesc = 0
    # checking upper neighbor
    if isinbounds(matrix, [i - 1, j]) and matrix[i - 1][j] == 1:
        q.enqueue([i - 1, j])
        layernodesc = layernodesc + 1
    # checking bottom neighbor
    if isinbounds(matrix, [i + 1, j]) and matrix[i + 1][j] == 1:
        q.enqueue([i + 1, j])
        layernodesc = layernodesc + 1
    # checking left neighbor
    if isinbounds(matrix, [i, j - 1]) and matrix[i][j - 1] == 1:
        q.enqueue([i, j - 1])
        layernodesc = layernodesc + 1
    # checking right neighbor
    if isinbounds(matrix, [i, j + 1]) and matrix[i][j + 1] == 1:
        q.enqueue([i, j + 1])
        layernodesc = layernodesc + 1

    # zero-ing the current point so we wont step it again
    matrix[i][j] = 0
    # dequeue-ing the current point from the queue
    q.dequeue()
    # returning the amount of nodes we added to the queue
    return layernodesc

# checks if the point is legit in terms of matrix bound
def isinbounds(matrix, p):
    lines = len(matrix)
    cols = len(matrix[0])
    if p[0] >= 0 and p[0] <= (lines - 1) and p[1] >= 0 and p[1] <= (cols - 1):
        return True
    else:
        return False

# function for getting the user inputs
def inputvector():
    sizev = [int(x) for x in input().split()]
    matrix = []
    for i in range(sizev[0]):
        matrix.append([int(x) for x in input().split()])
    startv = [int(x) for x in input().split()]
    stopv = [int(x) for x in input().split()]
    return sizev, matrix, startv, stopv

def main():
    # first arguments are the size of the matrix
    siz, matrix, startv, stopv = inputvector()
    linsize = siz[0]
    colsiz = siz[1]
    minmatrix = []
    # the binary matrix itself
    for i in range(linsize):
        minmatrix.append(matrix[i].copy())
    # initialize the min matrix with -1
    # this matrix won't include all matrix items for the algorithm only
    # goes threw the minimal steps to the destination
    for i in range(linsize):
        for j in range(colsiz):
            if minmatrix[i][j] == 1: minmatrix[i][j] = -1
    # beginning point
    startp = startv
    # destination point
    endp = stopv
    # boolean variable to determine if the
    achieveddest = False
    # define a new queue
    q = Queue()
    # inserting the start point to the queue
    q.enqueue(startp)
    currentp = startp
    nodesinlayer = 1
    # if the start point isn't containing a 1
    if matrix[startp[0]][startp[1]] != 1:
        print(-1)
        return
    # layers counter
    layerc = 0

    # we will run this loop as long as the queue isn't empty
    while not q.isempty() and not achieveddest:
        for i in range(nodesinlayer):
            l = currentp[0]
            k = currentp[1]
            if minmatrix[l][k] == -1: minmatrix[l][k] = layerc
            if currentp[0] == endp[0] and currentp[1] == endp[1]:
                achieveddest = True
                break
            # map neighbors and put them inside q and zeroing the current point
            nodesinlayer = nodesinlayer + mapneighbors(matrix, currentp, q)
            if not q.isempty(): currentp = q.arr[len(q.arr) - 1]
            # if minmatrix[l][k] == -1: minmatrix[l][k]=layerc
        layerc = layerc + 1
        nodesinlayer = len(q.arr)
    for i in range(linsize):
        for j in range(colsiz):
            if minmatrix[i][j] <= 0: minmatrix[i][j] = -1
    # output handling
    if achieveddest:
        print(layerc - 1)
        return
    elif q.isempty():
        print(-1)
        return

main()
