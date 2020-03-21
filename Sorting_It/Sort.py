def Bubble_Sorting():
    passes = 0
    n = int(input("Enter the length of your array :- "))
    if n < 1:
        raise ValueError("The number entered must be greater than +1")
    if n == 1:
        raise StopIteration("The array is already sorted.")
    # We are using list comprehension to get the input as a list from the user.
    arr = [int(input("Enter the {}th element of your array - ".format(i+1)))
           for i in range(n)]
    for x in range(1, n):
        flag = 0
        passes = x
        for i in range(n-x):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag += 1
        print("After pass {} the array is :- {}".format(x, arr))
        # We are using 'flag' avoid any redundant passes in the loop.
        # For an already sorted algorithm we will get the result in a single pass.
        if flag == 0:
            break
    print("The new sorted Array using bubble sort is :- {}".format(arr))
    print("Your array was sorted in {} number of passes".format(passes))


def Merge_Sorting():
    n = int(input("Enter the length of your array :- "))
    if n < 1:
        raise ValueError("The number entered must be greater than +1")
    if n == 1:
        raise StopIteration("The array is already sorted.")
    # We are using list comprehension to get the input as a list from the user.
    arr = [int(input("Enter the {}th element of your array - ".format(i + 1)))
           for i in range(n)]

    def merge(l, ri, arr):
        nl = len(l)
        nr = len(ri)
        i, j, k = 0, 0, 0
        while i < nl and j < nr:
            if l[i] <= ri[j]:
                arr[k] = l[i]
                i += 1
                k += 1
            else:
                arr[k] = ri[j]
                j += 1
                k += 1
        while i < nl:
            arr[k] = l[i]
            i += 1
            k += 1
        while j < nr:
            arr[k] = ri[j]
            j += 1
            k += 1

    def merge_sort(arr):
        len_arr = len(arr)
        if len_arr < 2:
            return arr
        # We are splitting the arrays into two parts i.e., left and right.
        left = arr[:n / 2]
        right = arr[n / 2:]
        # Recursive call to merge_sort
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)

    merge_sort(arr)
    print("The sorted list is :- {}".format(arr))
