import numpy as np

def leftrotation(arr, d):
    for i in range(0, d):
        first = arr[0]

        for j in range(0, len(arr)-1):
            arr[j] = arr[j + 1]

        arr[len(arr)-1] = first

    return arr
        

def rightrotation(arr, d):
    for i in range(0, d):
        last = arr[len(arr)-1]

        for j in range(len(arr)-1,-1,-1):
            arr[j] = arr[j - 1]

        arr[0] = last

    return arr

#Gets the length of the array and fills it with random numbers
alen = int(input("Enter array length: "))
arr = np.random.randint(0, 10, alen)

print(arr)

direction = input("Would you like to rotate the array to the right or left?: ").lower()
pos = int(input("Enter the number of positions to shift: "))

if direction == "left":
    arr = leftrotation(arr, pos)
elif direction == "right":
    arr = rightrotation(arr, pos)
else:
    direction = input("Choose a direction to rotate the array: ")

print(arr)
    
