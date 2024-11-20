array = [6, 5, 33, 55, 73, 22, 85, 79, 30, 46]
print("toto je pole pred serazenim", array)

sorted_array = sorted(array)
print ("toto je pole po serazenim", sorted_array)

def bubble_sort():
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                print(array)
    return array

print(bubble_sort())