def bubble_sort():
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


def merge_sort():
    arr = [9,5,1,4,6,3,5,7,2,8]
    pass
