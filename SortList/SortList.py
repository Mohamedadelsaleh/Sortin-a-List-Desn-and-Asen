myList = []
while True:
    numOfEle = input("Please Enter Number of List Elements : ")
    if numOfEle.isnumeric():
        numOfEle = int(numOfEle)
        break

for ln in range(0, numOfEle):
    while True:
        ele = input("Please enter an Integer Value : ")
        if ele.isnumeric():
            ele = int(ele)
            myList.append(ele)
            break
        else:
            print("You Enter not Integer value, please try again")

print(myList)
myList.sort()
print(myList)
myList.sort(reverse=True)
print(myList)