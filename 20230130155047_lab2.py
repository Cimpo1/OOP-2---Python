def my_abs(x):
    '''Take the absolute value of 'x'.'''
    return -x if x<0 else x
assert my_abs(-2) == 2
assert my_abs(3.9) == 3.9
assert my_abs(-301) == 301

def is_palindrome(x):
    '''Return True if iterable x is symmetric (a palindrome).'''
    return True if len(x) <= 1 else x[0] == x[-1] and is_palindrome(x[1:-1])

assert is_palindrome('radar')
assert is_palindrome(())
assert not is_palindrome([1,2,3,1])
assert is_palindrome((6, 1, 2, 2, 1, 6))

def power(x, y):
    '''Given iterable 'x' and number 'y', construct a new list
    such that each element of 'x' is raised to the power 'y'.'''
    result = [value**y for value in x]
    return result
    
assert power([3, -2, 4], 2) == [9, 4, 16]
assert power([-1, 3, -5], 3) == [-1, 27, -125]

def zeroes(m, n):
    '''Construct a matrix with 'm' rows and 'n' columns, initially
    set to zero.'''
    result = [[0 for c in range(n)] for r in range(m)]
    return result

assert zeroes(2, 2) == [[0,0],[0,0]]
assert zeroes(2, 3) == [[0,0,0],[0,0,0]]
assert zeroes(3, 2) == [[0,0],[0,0],[0,0]]

factorial = lambda x: 1 if x==0 else x*factorial(x-1)
    
assert factorial(0) == 1
assert factorial(3) == 6
assert factorial(15) == 1307674368000

add_vectors = lambda x, y: [a+b for a, b in zip(x,y)]

assert add_vectors([1, 1, 1], (2, 1, -2)) == [3, 2, -1]
assert add_vectors([5, 4, 2], [-2, 8]) == [3, 12]

all_even = lambda x: (len([v for v in x if v%2 == 0]) == len(x))

assert all_even([2, 98, 102, 44])
assert not all_even({2, 98, 103, 46})

s = set()
for n in range(1, 10+1):
    s.add(sum(range(1, n+1)))

t = { sum(range(1, n+1)) for n in range(1, 10+1) }

assert t == s

n = 10
r = [(i, j) for i in range(n) for j in range(i + 1, n)]

y = []
for i in range(n):
    for j in range(i+1,n):
        d = [i, j]
        h = tuple(d)
        y.append(h)

assert y == r

print ('All tests passed')

p = 101
q = 19
r = 0

def simple_function():
    global r
    r = (r + p) % q
    return r

xi = 0
while xi != 5:
    print(simple_function())
    xi += 1
print(p, q, r)

# a) An unbound local error happens with the variable r
# b) we get that the first value printed is a 6 and it works
# c) 6
#    12
#    18
#    5
#    11
#    101 19 11
#  The value of r is changing with each iteration by adding it with p and reminder with q
#
#Part 2
#
# b)
#
# Number of calls: 4
# 6
# Number of calls: 1
# 7
# Number of calls: 4
# 2
# Number of calls: 5
# 15
# Number of calls: 5
# -1
# Number of calls: 5
# -1
# Number of calls: 6
# -1
#
# c)
#
# Traceback (most recent call last):
#   File "C:\Users\david\OneDrive - Marianopolis College\Programing 2\Lab 2\binary_search.py", line 33, in <module>
#     print(binary_search(x, v))
#   File "C:\Users\david\OneDrive - Marianopolis College\Programing 2\Lab 2\binary_search.py", line 24, in binary_search
#     result = helper(0, len(ls) - 1)
#   File "C:\Users\david\OneDrive - Marianopolis College\Programing 2\Lab 2\binary_search.py", line 12, in helper
#     calls +=1
# UnboundLocalError: local variable 'calls' referenced before assignment
#
#An error happens clearly stating it has an unbound local variable 'calls' that has been called before assignment
#
#d)
#
# Traceback (most recent call last):
#   File "C:\Users\david\OneDrive - Marianopolis College\Programing 2\Lab 2\binary_search.py", line 34, in <module>
#     print(binary_search(x, v))
#   File "C:\Users\david\OneDrive - Marianopolis College\Programing 2\Lab 2\binary_search.py", line 25, in binary_search
#     result = helper(0, len(ls) - 1)
#   File "C:\Users\david\OneDrive - Marianopolis College\Programing 2\Lab 2\binary_search.py", line 13, in helper
#     calls +=1
# NameError: name 'calls' is not defined
#
#It does not know the name 'calls' because it simply has not been defined before the global call

print('\nPart 3 from now on')

f1 = open('set1.txt')
f2 = open('set2.txt')

s1 = set([int(v) for v in f1.read().split()])
s2 = set([int(v) for v in f2.read().split()])

ls = s1 & s2
print(ls)