from random import randint
list_of_elements = []
for i in range(10):
    list_of_elements.append(randint(1, 50))
print(list_of_elements)

# bubble sort_for
def bubble_sort(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array
print(bubble_sort(list_of_elements))

def binary_search(value, list_of_elements):
    first = 0
    last = len(list_of_elements) - 1
    while first <= last:
        middle = (first + last) // 2
        guess = list_of_elements[middle]
        if guess == value:
            return middle
        if guess > value:
            last = middle - 1
        else:
            first = middle + 1

    return None

print(binary_search(40, list_of_elements))
