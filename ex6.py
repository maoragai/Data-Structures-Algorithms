#Maor Agai
#305544546
def countingsort(num_array, dev10):
    num_of_dig=10
    #building an empty array to store the sorted array in
    sorted_array = [0] * len(num_array)
    #creating an counting  array
    count_array = [0] * num_of_dig
    #counting the occurrences of the numbers
    for i in range(0, len(num_array)):
        element = int(num_array[i] / dev10)
        count_array[int(element % 10)] += 1
    #accunulation array
    for i in range(1, 10):
        count_array[i] += count_array[i - 1]
    # sort the elements
    i = len(num_array) - 1
    while i >= 0:
        index = num_array[i] / dev10
        sorted_array[count_array[int(index) % 10] - 1] = num_array[i]
        count_array[int(index) % 10] -= 1
        i -= 1
    return sorted_array
    
def radix(num_array):
    # find the number of digits(by finding the max of the array)
    arrmax = max(num_array)
    # apply counting sort by digits (right to left)
    dev10 = 1
    while arrmax / dev10 > 0:
        num_array=countingsort(num_array, dev10)
        # moving one digit to the left
        dev10 *= 10
    return num_array

def main():
    # pre-processing
    num_array=input().strip()
    num_array=num_array.split(" ")
    num_array=[int(x) for x in num_array]
    #apply radix sort algorithm
    num_array=radix(num_array)
    #print the sorted array
    print(*num_array)

main()