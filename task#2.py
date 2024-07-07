from collections import deque

def is_palindrome(value):
    value = ''.join(filter(str.isalnum, value)).lower()
    
    char_deque = deque(value)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

print(is_palindrome("A man a plan a canal Panama"))  
print(is_palindrome("No lemon, no melon"))            
print(is_palindrome("Hello, world!"))                 
print(is_palindrome("Racecar"))                       
print(is_palindrome("Was it a car or a cat I saw"))   
print(is_palindrome("125849754")) 
print(is_palindrome("12588521")) 
print(is_palindrome("1258521")) 
