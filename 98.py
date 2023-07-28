def countnumberofwords():
    filename = input("Enter The File Name: ")
    nwords = 0
    file = open(filename,'r')
    for line in file:
        words = line.split()
        nwords = nwords + len(words)
    print("Number of Words")
    print(nwords)
countnumberofwords()