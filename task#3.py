def check_brackets(expression):
    brackets = {')': '(', ']': '[', '}': '{'}

    stack = []

    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack == [] or brackets[char] != stack.pop():
                return "Несиметрично"
    
    return "Симетрично" if not stack else "Несиметрично"

print(check_brackets("( ){[ 1 ]( 1 + 3 )( ){ }}")) 
print(check_brackets("( 23 ( 2 - 3);"))            
print(check_brackets("( 11 }"))                     
