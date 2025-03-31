def countdown(max):
    if max == 0:
        print("Blastoff")
        return max
    print(max)
    return countdown(max - 1)

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1)


def reverse_string(word):
    if len(word) == 0:
        return ""
    
    return reverse_string(word[1:len(word)]) + word[0:1]

def is_palindrome(word):
    if len(word) == 0:
        return True
    if word[0:1] != word[len(word) - 1: len(word)]:
        return False
    
    return is_palindrome(word[1:len(word) - 1])



def calc_exp(base, exp):
    if exp == 0:
        return 1
    return base * calc_exp(base, exp - 1)

# def digit1(num):
#     if num == 0:
#         return 0
#     num_1s = 0
#     for i in str(num):
#         if num == 1:
#             return digit1(num - 1) + num_1s + 1
        
#         if num % 10 == 1:
#             num_1s += 1
    

#     return digit1(num - 1)

# print(digit1(13))


def gcd(num1, num2):
    min = 0
    if num1 > num2:
        min = num2
        max = num1
    else:
        min = num1
        max = num2
    if max % min == 0:
        return min
    else:
        return gcd(min - 1, max - 1)
    


