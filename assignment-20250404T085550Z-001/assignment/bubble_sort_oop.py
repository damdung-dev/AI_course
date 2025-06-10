import random
class BubbleSort:
    list_number=[]
    def __init__(self, data):
        self.data=data
    def create_list(self):
        BubbleSort.list_number.append(self.data)
        print(BubbleSort.list_number)
    def find_and_sort(self):
        while True:
            swapped = False
            for i in range(0, len(BubbleSort.list_number) - 1):
                if BubbleSort.list_number[i] > BubbleSort.list_number[i + 1]:
                    # print(list_number[i], list_number[i + 1])
                    temp = BubbleSort.list_number[i + 1]
                    BubbleSort.list_number[i + 1] = BubbleSort.list_number[i]
                    BubbleSort.list_number[i] = temp
                    swapped = True
                else:
                    continue
            if not swapped:
                break
        return BubbleSort.list_number

user=int(input("Nhập vào 1 số: "))
for i1 in range(0,user):
    newdata=BubbleSort(random.randint(1,100))
    newdata.create_list()
print(f"Dãy ban đầu: {BubbleSort.list_number}")
newdata.find_and_sort()
print(f"Dãy số sau khi sắp xếp: {BubbleSort.list_number}", end="")