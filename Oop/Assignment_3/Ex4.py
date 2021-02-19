# Merge Sort
def merge(L, R):
    result = []

    while len(L) > 0 and len(R) > 0:
        if L[0] > R[0]:
            result.append(R[0])
            del R[0]

        else:
            result.append(L[0])
            del L[0]

    while len(L) > 0:
        result.append(L[0])
        del L[0]

    while len(R) > 0:
        result.append(R[0])
        del R[0]

    return result

def mergeSort(arr):
    if len(arr) > 1: # [3 1]
        mid = len(arr)//2 # Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        R = arr[mid:] # into 2 halves

        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half

        # Write code here!
        result = []

        while len(L) > 0 and len(R) > 0:
            if L[0] > R[0]:
                result.append(R[0])
                del R[0]

            else:
                result.append(L[0])
                del L[0]

        while len(L) > 0:
            result.append(L[0])
            del L[0]

        while len(R) > 0:
            result.append(R[0])
            del R[0]

        arr.clear()     # arr을 비우고 새로 요소를 넣음
        for i in range(0, len(result)) :
            arr.append(result[i])

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end =" ")
    print()


if __name__ == '__main__':
	arr = [5,3,1,4,7,0]
	print ("Input Array:")
	printList(arr)
	mergeSort(arr)
	print("Sorted Array:")
	printList(arr)

