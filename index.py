first = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, ]


#Fibonacci series
#the sum of two elements defines the next
a, b = 0, 1
while a < 10 :
    print(a)
    a, b = b, a+b


#statements

#if statements
x = int(input("Enter a given integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('single')
else:
    print('more')

    #elif = else if
    
y = int(input("Ahmed is of what age: "))
if y < 15:
    print('Ahmed is more than that')
elif y == 16:
    print('Correct')
elif y == 15:
    print('Ahmed is a year more than that')
else:
    print('Incorrect')


#for statements
word = ['cat', 'window', 'deferenstate'] #lists in python
for w in word:
    print(w, len(w))

counter = str(input('Enter the word you want to count: '))
print(counter, len(counter))


# range built in function
for i in range(5):
    print(i)

glob = list(range(0, 150, 20))

print(glob)

action = ['Mary', 'had', 'a', 'little', 'lamp']
for i in range(len(action)):
    print(i, action[i])

