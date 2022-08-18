import  random
print('Task 1')

# A bubble sort can be modified to “bubble” in both directions. The first
# pass  moves “up” the list and the second pass moves “down.” This
# alternating pattern continues until no more passes are necessary.
# Implement this variation and describe under what circumstances it might be
# appropriate.

def bubbleSortUp(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSortUp(alist)
print('UP: ', alist)


def bubbleSortUpDown(alis):
    for i in range(len(alis)):
        for j in range (i, len(alis) - 1 - i):
            if alis[j] > alis[j + 1]:
                alis[j], alis[j +1] = alis[j + 1], alis[j]
        for j in range(len(alis) - 2 - i, i - 1, -1):
            if alis[j] > alis[j + 1]:
                alis[j], alis[j + 1] = alis[j + 1], alis[j]

    return alis

al = [random.randint(1,40) for i in range (30)]
print('UPDOWN: ', bubbleSortUpDown(al))

print('Task 2')

# Implement the mergeSort function without using the slice operator.

def merge_sort(lefthalf, righthalf):
    i, j = 0, 0
    rezult = []
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] <= righthalf[j]:
            rezult.append(lefthalf[i])
            i += 1
        else:
            rezult.append(righthalf[j])
            j += 1


    rezult += [lefthalf[it] for it in range(i, len(lefthalf))] + \
              [righthalf[it] for it in range(j, len(lefthalf))]
    return rezult


def merge(alist):
    if len(alist) < 2:
        return alist
    middle = len(alist) // 2
    leftarr = [alist[i] for i in range(middle)]
    righarr = [alist[i] for i in range(middle, len(alist))]

    print(leftarr, righarr)

    return merge_sort((merge(leftarr)), (merge(righarr)))

alist = 54,26,93,17,77,31,44,55,20
print(merge(alist))



print('Task 3')

# One way to improve the quicksort is to use an insertion sort on lists  that
# are small in length (call it the “partition limit”). Why does this make
# sense? Re-implement the quicksort and use it to sort a random list of
# integers. Perform analysis using different list sizes for the partition limit


def insertionSort(alist):

   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)