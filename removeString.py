def toString(List):
    return ' '.join(List)

def removeDuplicate(string):
    copy=[]
    words = []
    string = string.split(" ")
    for elem in string: copy.append(elem)
    length=len(string)

    for i in range(length):
        #print(copy[i])
        if copy[i] in words:
            string.remove(copy[i])
        else:
            words.append(copy[i])
        #print(copy)

    return toString(string)

if __name__=="__main__":
    print(removeDuplicate('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))