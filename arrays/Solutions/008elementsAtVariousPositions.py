input1 = input("Enter some numbers and separate them with comas:  ")
list1 = []
list1.append(input1)

try:
    a = list1[0]
    b = list1[4]
except IndexError:
    print("Boo")