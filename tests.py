from intToRoman import roman

def intToRoman_test(num):
    for i in range(num):
        roman(i+1)

def test():
    d2r_table = []
    for i in range (5):
        aux = []
        for j in range (10):
            aux.append(roman(i*(j*10)))
        d2r_table.append(aux)
    return(d2r_table)


if __name__ == '__main__':
    print(test())