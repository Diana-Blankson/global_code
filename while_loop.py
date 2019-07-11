#while loop
print('first - while loop')
i = 0
while(i < 10):
    i = i + 1
    print(i)

#while loop that prints the number from 7 to 19
print('third - while loop')
i = 6
while(i < 20):
    i = i + 1
    print(i)

#even numbers between 12 and 20
print('fourth while loop')
i = 10
while(i < 21):
    i = (i + 2)
    print(i)
#a function that takes two numbers and prints all the even numbers
def evens():
	print('fifth while loop')
	num1 = int(input('Enter the first number '))
	num2 = int(input('Enter the second number '))
	for i in range(num1,num2):
		if i % 2 == 0:
                   print(i,"is even")
evens()

def reverse_evens():
    print('sixth while loop')
    num1 = int(input('Enter the first number'))
    num2 = int(input('Enter the second number'))
    for n in reversed(range(num1,num2)):
        if n % 2 == 0:
           print(n,"is even")
reverse_evens() 
