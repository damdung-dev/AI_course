import random
list_number=[]
def bubbleSort():
    while True:
        swapped=False
        for i in range(0,len(list_number)-1):
            if list_number[i]>list_number[i+1]:
                #print(list_number[i], list_number[i + 1])
                temp = list_number[i+1]
                list_number[i+1] = list_number[i]
                list_number[i] = temp
                swapped=True
            else:
                continue
        if not swapped:
            break
    return list_number

user=int(input("Nhập vào 1 số: "))
for i1 in range(0,user):
    list_number.append(random.randint(1,100))
print(f"Dãy ban đầu: {list_number}")

print(f"Dãy số sau khi sắp xếp: {bubbleSort()}", end="")
