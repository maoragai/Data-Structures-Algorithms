# Maor Agai

# EX4
class ufheap:
    conarray=[] # this array will be of n+1 size and neglect the 0 place
    def __init__(self,number_of_elements):
        self.conarray = [1]*number_of_elements
        for i in range(number_of_elements):
            self.conarray[i]=i

    def union(self,p, q):
        # this union method will be responsible to change all
        # the new group members to point to the new root
        # this way there will be no trees for a specific root
        # algo complexity:
        # group size calc = O(n)
        # group unify= O(n)
        pcounter=0
        qcounter=0
        group_of_p=self.conarray[p]
        group_of_q=self.conarray[q]
        #we want to see which group is bigger
        for i in range(len(self.conarray)):
            if self.conarray[i]==group_of_p:
                pcounter+=1
            if self.conarray[i]==group_of_q:
                qcounter+=1
        if pcounter>qcounter:
            self.change_father(group_of_q,group_of_p)
        elif pcounter<qcounter:
            self.change_father(group_of_p,group_of_q)
        else:
            if p<q:
                self.change_father(group_of_p, group_of_q)
            if q<=p:
                self.change_father(group_of_q, group_of_p)

    def change_father(self,old_father,new_father):
        # algo complexity: O(n)
        for i in range(len(self.conarray)):
            if self.conarray[i]==old_father:
                self.conarray[i] = new_father

def main():
    #will ask for the number of nodes from the user
    num_of_elements=int(input())
    uf=ufheap(int(num_of_elements)+1)

    while 1:
        user_input = int(input())

        # if the user chose 1 get a number as input and print the group this number belongs to
        if user_input==1:
            find_num=int(input())
            print(uf.conarray[find_num])

        # unify the two groups
        if user_input==2:
            elements_to_unify=[int(x) for x in input().split()]
            uf.union(elements_to_unify[0],elements_to_unify[1])

        #end process
        if user_input==0:break


main()
