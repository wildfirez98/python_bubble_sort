# Practice implementing a bubble sort algorithm that repeadtedly swaps adjacent elements if they are not in the correct order
# Sorting a list in ascending order

def bubble_sort(list):  # Function "bubble_sort" that takes in a parameter we will call "list"
    for i in range(len(list)-1): # Outer 'for' loop, will run for as many times are there are elements in the list
        swapped = False # Variable to determine if the items in the list have been swapped
        print(f"Iteration ") # Show when a new loop iteration is beginning
        for j in range(len(list) - 1): # Inner 'for' loop to compare all the value in the list for each pass
            print(f"Comparing {list [j], list[j+1]}") # Print each iteration of the outer and inner loop
            if list[j] > list[j+1]: # Conditional statement that checks if the element on the left is greater than the element on the right. If it is, switch the order of the elements
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True # Set swapped variable equal to True if elements were swapped during a pass of the inner loop. If a swap occurs, set the variable to true
        if not swapped:
            return

    return list # return the value of the list after its been sorted

sample_list = [4, 2, 9, 13, 46, 29, 7, 10, 36, 12, 5, 123, 1233, 204, 230, 759]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")
