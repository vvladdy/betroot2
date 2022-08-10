print('Task 1')

# from typing import Optional
#def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:

def to_power(x: int|float, exp: int) -> int|float:

	if exp < 0:
		raise ValueError('This function works only with exp > 0')
	if exp == 0:
		return 1
	return x*to_power(x, exp-1)

print(to_power(3.5, 2))
print(to_power(2, 3))
#print(to_power(2, -1))


print('\nTask 2')
"""
Checks if input string is Palindrome
is_palindrome('mom') - True
is_palindrome('sassas')  - True
is_palindrome('o') - True
"""

def is_palindrome(looking_str: str, index: int = 0) -> bool:
	if looking_str[:] == looking_str[::-1]:
		return True
	else:    return False

def is_palindrome_rec(looking_str: str, index: int = 0) -> bool:
	if len(looking_str) <= 1:
		return True
	if looking_str[0] == looking_str[-1]:
		return is_palindrome_rec(looking_str[1:-1])
	else:
		return False


print(is_palindrome_rec('mom'))
print(is_palindrome_rec('sassas'))
print(is_palindrome_rec('ou'))

print('Task 3')
"""
This function works only with positive integers

>>> mult(2, 4) == 8
True

>>> mult(2, 0) == 0
True

>>> mult(2, -4)
ValueError("This function works only with postive integers")
"""


def mult(a: int, n: int) -> int:
	if a < 0 or n < 0:
		raise ValueError('This function works only with postive integers')
	#print(a)
	if n == 0:
		return 0

	return a+mult(a, n-1) # прибавлять а+а+а+...+а (n раз)


print(mult(2, 4))
print(mult(2, 7))
#print(mult(2, -4))


print('\nTask 4')

"""
Function returns reversed input string
>>> reverse("hello") == "olleh"
True
>>> reverse("o") == "o"
True
"""


def reverse(input_str: str) -> str:
	if len(input_str) == 1:
		return input_str
	else:
		return reverse((input_str[1:])) + (input_str[0])

print(reverse('hello'))
print(reverse('o'))


print('\nTask 5')

"""
>>> sum_of_digits('26') == 8
True

>>> sum_of_digits('test')
ValueError("input string must be digit string")
"""


def sum_of_digits(digit_string: str) -> int:
	if digit_string.isdigit() and len(digit_string) == 1:
		return int(digit_string)
	if digit_string.isdigit():
		return int(sum_of_digits(digit_string[1:])) + int(digit_string[0])

print(sum_of_digits('26') == 8)
print(sum_of_digits('26464'))