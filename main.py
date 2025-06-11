#a=5
#b=1
#print(a,'+',b,'=',a+b)
#print(f'{a} + {b} = {a+b}')
#rint(f'{a} - {b} = {a-b}')
#print(f'{a} * {b} = {a*b}')
#print(f'{a} / {b} = {a/b}')

#a=int(input('yakum adad'))
#b=int(input('duyum adad'))
#print(f'{a} + {b} = {a+b}')
#print(f'{a} - {b} = {a-b}')
#print(f'{a} * {b} = {a*b}')
#print(f'{a} / {b} = {a/b}')
#print(f'{a} // {b} = {a//b}')

# import math
# a=int(input())
# b=int(input())
# c=math.sqrt (a**2+b**2)
# print(c)


# a=int(input())
# n0=a//10000
# n1=a//1000%10
# n2=a//100%10
# n3=a//10%10
# n4=a%10
# print(n1+n2+n3+n4+n0)


# a=int(input())
# b=int(input())
# c=int(input())
# x=a+b+c
# print(f'{x//100}s {x%100}d')


# a=int(input())
# n1=a//3600%24
# n2=a//60%60
# n3=a%60
# print(f'{n1}:{n2//10}{n2%10}:{n3//10}{n3%10}')

# a=int(input())
# t=a*45+(a//2)*5+((a-1)//2)*15
# print(((t//60)+9),(t%60))



# a=int(input())
# b=int(input())
# c=int(input())
# t=(a*100)+b
# m=t*c
# print((m//100),(m%100))

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# e=int(input())
# f=int(input())
# m1=(a*60)*60+b*60+c
# n1=(d*60)*60+e*60+f
# print(n1-m1)

# a=int(input())
# b=int(input())
# x1=b%a
# print((a-x1)%a)




# n=int(input())
# if n%5==0 and n%3==0:
#     print('Hello World')
# elif n%5==0:
#     print('World')
# elif n%3==0:
#     print('Hello')


# a=int(input())
# sym=input()
# b=int(input())
# if sym=="+":
#     print(f'{a}{sym}{b}={a+b}')
# elif sym=='-':
#     print(f'{a}{sym}{b}={a-b}')
# elif sym=='*':
#     print(f'{a}{sym}{b}={a*b}')
# elif sym=='/':
#     print(f'{a}{sym}{b}={a//b}')
# elif sym=='%':
#     print(f'{a}{sym}{b}={a%b}')


# a=int(input())
# b=int(input())
# c=int(input())
# pos=0
# neg=0
# zero=0
# if a > 0:
#     pos+=1
# elif a < 0:
#     neg+=1
# else :
#     zero+=1
# if b > 0 :
#     pos+=1
# elif b < 0 :
#     neg+=1
# else :
#     zero+=1
# if c > 0 :
#     pos +=1
# elif c < 0 :
#     neg+=1
# else :
#     zero+=1
# print(f'Positive={pos}')
# print(f'Negative={neg}')
# print(f'Zero={zero}')


# a=int(input())
# match a:
#     case 1:
#         print('is a number')
#     case 2:
#         print('is a number')
#     case 3:
#         print('is a number')
#     case 4:
#         print('is a number')
#     case 5:
#         print('is a number')
#     case 6:
#         print('is a number')
#     case 7:
#         print('is a number')
#     case 8:
#         print('is a number')
#     case 9:
#         print('is a number')
#     case 10:
#         print('is a number')
#     case 0:
#         print('is a number')




# n=int(input())
# m=int(input())
# if (n > m):
#     print(1)
# elif (n < m):
#     print(2)
# else:
#     print(0)



# a=int(input())
# if a > 0:
#     print('Positive')
# elif a < 0:
#     print('Negative')
# else:
#     print('Zero')



# a=int(input())
# maxx=a+1
# if maxx % 2 == 0 :
#     maxx+=1
# minn=a-1
# if minn % 2 == 0 :
#     minn-=1
# print(f'The next odd number after the number {a} is {maxx}')
# print(f'The previous odd number before the number {a} is {minn}')


# a=int(input())
# if a > 0:
#     a = -a
# elif a < 0:
#     a = -a
# else:
#     a = 0
# print(a)

# a=int(input())
# b=int(input())
# if a % b == 0:
#     print(a // b)
# elif b % a == 0:
#     print(b//a)
# else :
#     print('None of them is divisible by other!')


# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if b == c and c == d :
#     print(1)
# elif a == c and c == d :
#     print (2)
# elif a == b and b == d :
#     print(3)
# else :
#     print(4)

# a=int(input())
# b=int(input())
# c=int(input())
# if a == b and b == c and c == a :
#     print(3)
# elif a == b or a == c  or b == c:
#     print (2)
# else :
#     print(0)

# a=int(input())
# if a % 2 != 0 :
#     print('Odd')
# else :
#     print('Even')

# a=int(input())
# if a == 1 :
#     print('NO')
# elif a == 2 :
#     print('NO')
# elif a == 4 :
#     print('NO')
# elif a == 7 :
#     print('NO')
# else :
#     print('YES')

# A = int(input())
# B = int(input())
# C = int(input())
# even = (A % 2 == 0) or (B % 2 == 0) or (C % 2 == 0)
# odd = (A % 2 != 0) or (B % 2 != 0) or (C % 2 != 0)

# if even and odd:
#     print("YES")
# else:
#     print("NO")


# a=int(input())
# b=int(input())
# if a != b :
#     print('The given numbers are not equal')
# elif a == b :
#     print('The given numbers are equal')
# else :
#     print(0)



# a = input()
# if a.isalpha():
#     print(f"{a} is alphabet")
# else:
#     print(f"{a} is a number")


# a=int(input())
# if a >= 18 :
#     print('You are eligible to vote')
# else :
#     print ('You are not eligible to vote yet')


# a=int(input())
# if a <= 12 :
#     print('You are a child')
# elif a <= 19 :
#     print ('You are a teenager')
# else :
#     print('You are an adult')


# a=int(input())
# if a < 12 :
#     print('$5')
# elif a >= 12 and a < 60 :
#     print('$10')
# else :
#     print('$7')


# a=int(input())
# if a > 0 :
#     a+=1
#     print(a)
# elif a < 0 :
#     a-=2
#     print(a)
# else :
#     print(10)


# a=int(input())
# b=int(input())
# c=int(input())
# pos=0
# if a > 0:
#     pos+=1
# if b > 0:
#     pos+=1
# if c > 0:
#     pos+=1
# print(pos)


# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# e=int(input())
# f=int(input())
# g=int(input())
# h=int(input())
# tim1=a+c+e+g
# tim2=b+d+f+h
# if tim1 > tim2 :
#     print('1')
# elif tim2 > tim1 :
#     print('2')
# else :
#     print('0')


# a=int(input())
# b=int(input())
# if a == b :
#     print('It is a square')
# else :
#     print('It is not a square')



# a=int(input())
# n=a//100000
# n1=a//10000%10
# n2=a//1000%10
# n3=a//100%10
# n4=a//10%10
# n5=a%10
# sum1=n+n1+n2
# sum2=n3+n4+n5
# if sum1 == sum2 :
#     print('YES')
# else :
#     print ('NO')


# a=int(input())
# b=int(input())
# c=a+b
# if a == 10 or b == 10 or c == 10 :
#     print('True')
# else :
#     print('False')


a=int(input())
n2=a//1000%10
n3=a//100%10
n4=a//10%10
n5=a%10
if n2 == n5 and n3 == n4 :
    print('YES')
else :
    print('NO')
