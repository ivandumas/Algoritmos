# Recibes una string conteniendo solo () y []
# Crea un algoritmos para validar que la sintaxis de los corchetes es correcta:
# Ejemplos validos:
# '()'
# '()()()()()()()()()'
# '([])[]()'
# Ejemplos no validos:
# ')'
# '()['
# '(([))]'
# '(((((((((((((((((((((((((((((((((('

def bracketSyntax(str):
    stack = [] #stack with list
 
    # Traversing the Expression
    for char in str:
        if char in ["(", "["]:
 
            stack.append(char) #if the character is opening, then its pushed to the stack
        else:
            if not stack: #if there's nth in the stack it means there's no opening characters
                return False
            lastChar = stack.pop() #gets the most recent stacked character
            if lastChar == '(':
                if char != ")": return False        #most recent character must meet its closing one at this point, otherwise it's wrong
            if lastChar == '[':
                if char != "]": return False

    if stack: #at this point if there's sth in the stack it means there are not enough closing characters, so it's wrong
        return False
    return True #if there's nothing left in the stack, then and only then is the solution correct
 
if __name__ == "__main__":
    str = "()()()()()()()()()"
 
    if bracketSyntax(str):
        print("Valido")
    else:
        print("No Valido")