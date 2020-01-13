# Agai Maor
# 305544546
# ex1b

#stack class
class Stack:
    def __init__(self):
        self.arr=[]

    def isempty(self):
        return len(self.arr)==0

    def pop(self):
        leng =len(self.arr)
        if not self.isempty():
            temp= self.arr[0]
        if leng>1:
            for i in range(leng - 1):
                 self.arr[i]=self.arr[i+1]

        self.arr.remove(self.arr[leng-1])
        return temp

    def push(self, q):
        if self.isempty():
            self.arr.append(q)
        else:
            self.arr.append([])
            for i in range(len(self.arr) - 1, 0, -1):
                self.arr[i] = self.arr[i - 1]
            self.arr[0] = q

def main():
    # some test arguments
    #argv = "([4{5}6 ])"
    #argv = "{) 8"

    #accepting user input
    argv=input()
    argv= argv.replace(" ","")
    # boolean variable to determine if the string is balanced or not
    isbalanced=True
    # creating the stack object
    q = Stack()
    #going threw string chars
    for c in argv:
        #enqueue opening parenthesis
        if  c=="{" or c=="(" or c=="[":
            q.push(c)

        if (c=="}" or c==")" or c=="]" ) and (not q.isempty()):
            parenthesis = q.pop()
            if c=="}":
                if parenthesis == "{" and isbalanced: continue
                else:
                    isbalanced= False
                    break
            elif c == ")":
                if parenthesis == "("and isbalanced: continue
                else:
                    isbalanced= False
                    break
            elif c=="]":
                if parenthesis =="["and isbalanced: continue
                else:
                    isbalanced= False
                    break
        elif (c=="}" or c==")" or c=="]" ) and (q.isempty()):
            isbalanced = False
            break
    # string has been checked yet the stack isn't empty= there's an imbalance in the string
    if not q.isempty():
        isbalanced= False

    # final result output for the user
    if not isbalanced:
        print("-1")
    else:
        print ("1")


main()