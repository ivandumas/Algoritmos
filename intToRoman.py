import sys, re

class intToRoman:

    roman_re = re.compile("""^
    ([M]{0,9})   # thousands
    ([DCM]*)     # hundreds
    ([XLC]*)     # tens
    ([IVX]*)     # units
    $""", re.VERBOSE)

    d2r_table = []

    def __init__(self):
        for i in range (5):
            aux = []
            for j in range (10):
                aux.append(intToRoman.roman(i*(j*10)))
        intToRoman.d2r_table.append(aux)

    def roman(V):
        value =  [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000, 4000, 5000, 9000, 10000]
        roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M", "MV̅", "V̅", "V̅X̅", "X̅"]
        n = len(value)
        
        ans = []
        res = ""
    
        i = n - 1
        while(i >= 0):
            
            # Find valueminations
            while (V >= value[i]):
                V -= value[i]
                ans.append(roman[i])
    
            i -= 1
    
        for i in range(len(ans)):
            res += ans[i]
        return res

    def romanToInt(roman):

        roman = roman.upper()
        match = intToRoman.roman_re.match(roman)

        if not match:
            raise ValueError

        thousands, hundreds, tens, units = match.groups()
        result = 1000 * len(thousands)
        result += intToRoman.d2r_table[2].index(hundreds) * 100
        result += intToRoman.d2r_table[1].index(tens) * 10
        result += intToRoman.d2r_table[0].index(units)

        return result
  
# Driver Code
if __name__ == '__main__':
    n = int(sys.argv[1])
    print("Following is minimal number",
          "of change for", n, ": ", end = "")
    intToRoman.roman(n)