print("Swap 2 files ")
first = input("Insert the name of the first file :- ")
second = input("Insert the name of the second file :- ")
def swapFileData():
    with open(first,'r') :
        data_a = first.read()
    with open(second,'r') :
        data_b = second.read()
    with open(first,'w') :
        first.write(data_b)
    with open(second,'w') :
        second.write(data_a)
swapFileData()
    


