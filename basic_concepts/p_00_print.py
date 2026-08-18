#Print methods with format and f-string

a,b,c,d,e = 10,20,30,40,50

f = a+b+c+d+e
print('sum of a,b,c,d,e is ', f) #sum of a,b,c,d,e is  150
print('a={}, b={}, c={}, d={}, e={} sum of is f={}'.format(a,b,c,d,e,f))   # a=10, b=20, c=30, d=40, e=50 sum of is f=150
print('a={0}, b={1}, c={2}, d={3}, e={4}'.format(a, b, c, d, e)) #a=10, b=20, c=30, d=40, e=50
print(f'a={a}, b={b}, c={c}, d={d}, e={e}') #a=10, b=20, c=30, d=40, e=50

print(a,b,c,d,e,f, sep="/") #With / Seperator 10/20/30/40/50/150
print(a,b,c,d,e,f, sep="-") #With - Seperator 10-20-30-40-50-150

print(a)
print(b, end="-")
print(c)
print(d, end="-")
print(e)
print(f) 
# 10
# 20-30
# 40-50
# 150

 #using input() to take user input
num1 = input('Enter a number: ') #20
num2 = input('Enter a number: ') #30

print('You Entered:', num1 , num2) #20 ,30

print('Sum is:', num1 + num2) #2030
 #using input() With data type
num1 = int(input('Enter a number: ')) #20
num2 = int(input('Enter a number: ')) #30

print('You Entered:', num1 , num2) #20, 30

print('Sum is:', num1 + num2) #50