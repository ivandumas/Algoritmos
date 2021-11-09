def funcion(nums,n):
    print(nums)
    res = []

    for i in range(len(nums)):
        suma = 0
        aux = []
        suma += nums[i]
        for j in range(i+1,len(nums)):
            print(i,j)
            if suma + nums[j] == n:
                aux.append(nums[i])
                aux.append(nums[j])
                res.append(aux)
            else:
                pass
    return res

def main():
    print(funcion([1,2,3,4,5,6,7,-1],6))


main()