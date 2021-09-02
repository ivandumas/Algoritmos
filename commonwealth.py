def check_pools(input_file):
    m = []
    with open(input_file, 'r') as file:
        nm = list(map(int, file.readline().split()))
        for row in file:
            m.append([int(i) for i in row.split()])
    if nm[0] > nm[1]:
        return 'yes'
    
    countries = set(sum(m, []))
    country_neighbors = {c: [i if j==c else j for i,j in m if c in [i,j]] for c in countries}
    
    pool1,pool2 = [],[]
    
    for country,neighbors in country_neighbors.items():
        if not any([neighbor in pool1 for neighbor in neighbors]):
            pool1.append(country)
        elif not any([neighbor in pool2 for neighbor in neighbors]):
            pool2.append(country)
        else:
            return 'no'
    return 'yes'

def toString(List,char):
    return char.join(List)

def highlight(input_file):
    with open(input_file, 'r') as file:
        sentence = list(map(str, file.readline().split()))
        T = int(file.readline())
        words = list(map(str, file.readline().split()))

        if T > 0 and T < 101 and T == len(words):
            for i in range(T):
                if words[i] in sentence:
                    id=sentence.index(words[i])
                    if id >= 0 and id < 100:
                        tlist=list(sentence[id])
                        tlist.insert(len(tlist),"*/")
                        tlist.insert(0,"/*")
                        sentence[id]=toString(tlist,'')
                else:
                    pass


        
    return toString(sentence,' ')



if __name__=="__main__":
    print(highlight("input.txt"))