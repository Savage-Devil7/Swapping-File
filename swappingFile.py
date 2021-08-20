def swapFileData():
    fileName1 = input("Enter the file name of first file -> ")
    fileName2 = input("Enter the file name of the second file -> ")

    with open(fileName1,'r') as a:
        data_a = a.read()

    with open(fileName2,'r') as b:
        data_b = b.read()

    with open(fileName1,'w') as a:
        a.write(data_b)
        print(data_a)
    
    with open(fileName2,'w') as b:
        b.write(data_a)
        print(data_b)

swapFileData()