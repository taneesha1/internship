list1 = [8, 6, 8, 10, 8, 20, 10, 8, 8]

def countx(list1, x):

    count = 0
    for element in list1:
        if (element == x):
            count = count + 1
    return count
 

x = 8
print("8 has occured", countx(list1, x),"times")
