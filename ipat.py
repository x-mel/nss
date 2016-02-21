# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 00:33:00 2016

@author: mel
"""
from numpy import *
from fractions import Fraction
import rational

# difference of differences has a pattern of +6 -2
ex1=[2, 3, 10, 15, 26, 35, 50]

# difference of differences have a patter of +6
ex2=[8, 27, 64, 125, 216]

# difference of differences or difference (answer 2.7)
ex3=[0.7, 1.2, 1.2, 2.2, 1.7, 3.2, 2.2, 4.2]

# difference pattern of 6 and -7
ex4=[11, 17, -6, -13, 24, 30, -19, -26, 20]

# rounding each element
ex5=[41.45, 41.5, 42, 18.23, 18.2, 18, 73.09]

# difference 3.75
ex6= [7/2, 29/4, 11, ((14*4)+3)/4, 37/2]

# division of differences
ex7=[44, 4.4, 0.88, 0.264, 0.1056]

# differences related to multiple of 3 (- => pair and + => odd)
ex8= [9, 3, 6, 21, 9, 12, 33, 15, 18]

# differences of diffrences
ex9=[5, 17, 37, 65]

# this one is actually tricky, once it's 1/3 and another time it's -3 (div and then diff)
ex10=[18, 6, 3, 33, 11, 8, 45, 15, 12, 72]

#### Part 2
# division of differences was 3, so each difference is multiplied by 3 to get
# the next one
ex11=[11.5, 17.5, 35.5, 89.5]

# This one is not easy, each 4 elements form a row, and each row is incremented
# or decremented by an amount
ex12=[56, 89, 33, 21, 57, 88, 35, 19, 60, 85, 39, 15]

# This one is annoying, it's the difference of the difference of the difference.
# Answer is 7.5
ex13=[5, 6, 6.5, 6.5, 8, 7, 9.5]

# differences that are not adjacent incremented by -5. Answer 421
ex14=[9, 4, 16, 6, 36, 21, 441]

# division by 1/5 each 3 iterations asnwer 280
ex15=[7.2, 2.2, 3.2, 16, 11, 12, 60, 55, 56]

# very hard one, it's the division between the 3rd term and the first one is 5
# not in a regular way (Divis (3-1)). answer (155*5=775))
ex16=[5, 10, 25, 15, 30, 75, 150, 80, 155, 400]

# Differences of differences are incremented by 1
ex17=[115, 100, 86, 74, 65, 60]

# Difference are multiplied by 8 next answer is 4684
ex18=[3, 4, 12, 76, 588]

# each 3 numbers are added to give the 4th one. Answer=28
ex19=[7, 0, 1, 8, 5, 12, 9, 26, 3, 23, 2]

# the 3 element is the square of the product of the previous two. Answer is
# (3.2*2)^2=40.96
ex20=[4, 3, 144, 1.5, 2, 9, 5, 0.3, 2.25, 3.2, 2]

# divided by a row of 4 numbers. First number divided by the scond number gives
# the third, and first number times the second gives the 4th. Answer= 1.2
ex21=[8, 0.5, 16, 4, 15, 0.3, 50, 4.5, 6, 0.2, 30]

# so each 3 numbers are added to give the 4th one. Answer=9
ex22=[8, 16, 3, 27, 4, 8, 7, 19, 2, 0, 7]

# very hard, most probably, distance (4-1) as it have a regular pattern, so next
# one would be (2-0=2)
ex23=[3, 2, 1, 4, 5, 4, 5, 1, 0, 6, 3]

# Pattern in division, each row of 4 numbers, 2nd number is 1/2 of the first
# and 4th number is 1/5 of the 3rd. Answer 40.
ex24=[48, 24, 35, 7, 16, 8, 75, 15, 80]

# Pattern of diifference between the first and fifth number. dist (5-1).
# the answer is 3+1=4
ex25=[1, 1, 1, 2, 2, 2, 3, 4, 3, 3, 5, 6]


n=len(o)


def diff(a):
    dif=[]
    n=len(a)
    for i in arange(n-1):
        dif.append(a[i+1]-a[i])
    return dif

def dist(a):
    dif=[]
    n=len(a)
    for j in arange(round(n-1)):
        dif.append([a[i+j+1]-a[i] for i in arange(n-1-j)])
    return dif

def divdist(a):
    dif=[]
    n=len(a)
    for j in arange(round(n-1)):
        try:
            dif.append([str(Fraction(a[i+j+1]/a[i]).limit_denominator()) for i in arange(n-1-j)])
        except ZeroDivisionError:
            print("   DB0   ")
            dif.append("DB0")
    return dif


def adiff(a):
    dif=[]
    n=len(a)
    for i in arange(n-1):
        dif.append(abs( abs(a[i+1])-abs(a[i])))
    return dif

def divis(a):
    div=[]
    n=len(a)
    for i in arange(n):
        try:
            div.append(str(Fraction(a[i]).limit_denominator()))
        except ZeroDivisionError:
            print("  DB0  ", end=' ')
        return div

def difdiv(a):
    div=[]
    n=len(a)
    for i in arange(n-1):
        try:
            div.append(str(Fraction(a[i]/a[i+1]).limit_denominator()))
        except ZeroDivisionError:
            print("  DB0  ", end=' ')
    return div

def prod(a):
    pr=[]
    n=len(a)
    for i in arange(n-1):
        pr.append(a[i+1]*a[i])
    return pr

def denom(a):
    div=[]
    n=len(a)
    for i in arange(n):
        div.append(Fraction(a[i]).denominator)
    return div

def nom(a):
    div=[]
    n=len(a)
    for i in arange(n):
        div.append(Fraction(a[i]).numerator)
    return div


###########################
## Operation on Original
###########################
a=o
print('---------------- Size= %d ---------------' %n)
print('Original   :', end="")
for elem in a:
    print('%6.2f' % elem, end=' '.ljust(4))

print(' ')
print('Difference :', end=' '.ljust(5))
for elem in diff(a):
    print( '%6.2f' % elem, end=' '.ljust(4))

#print(' ')
#print('Absol Diff :', end=' '.ljust(5))
#for elem in adiff(a):
#    print( '%6.2f' % elem, end=' '.ljust(4))

print(' ')
print('Dif of Dif :', end=' '.ljust(10))
for elem in diff(diff(a)):
    print( '%6.2f' % elem, end=' '.ljust(4))

print(' ')
print('Dif Dif Dif:', end=' '.ljust(15))
for elem in diff(diff(diff(a))):
    print( '%6.2f' % elem, end=' '.ljust(4))

print(' ')
print('Div of Dif :', end=' '.ljust(10))
for elem in difdiv(diff(a)):
    print( '  %s ' % elem, end=' '.ljust(5))

print(' ')
print('Division   :', end=' '.ljust(5))
for elem in difdiv(a):
    print( '   %s' % elem, end=' '.ljust(4))

print('\n'*2,"--------"*9)

###########################
## Distances
###########################
a= dist(o)

print('Original   :', end="")
for elem in o:
    print('%6.2f' % elem, end=' '.ljust(4))

for u in arange(round(n-1)):
    print(' ')
    print('Dist (%d-1) :' %(u+2), end=' '.ljust(5*(u+1)))
    for elem in a[u]:
        print( '%6.1f' % elem, end=' '.ljust(4))

print('\n'*2,"--------"*9)

###########################
## Division Distances
###########################
a= divdist(o)

print('Original   :', end="")
for elem in o:
    print('%6.2f' % elem, end=' '.ljust(4))

for u in arange(round(n-1)):
    print(' ')
    print('Divs (%d-1) :' %(u+2), end=' '.ljust(6*(u+1)))
    if 'DB0' not in a[u]:
        for elem in a[u]:
            print( ' %s' % elem, end=' '.ljust(5))

print('\n'*2,"--------"*9)

###########################
## Operation on denominator
###########################
a=denom(o)

print('Denominator :', end="")
for elem in a:
    print('%6.2f' % elem, end=' '.ljust(4))

print(' ')
print('Difference  :', end=' '.ljust(5))
for elem in diff(a):
    print( '%6.2f' % elem, end=' '.ljust(4))

print(' ')
print('Dif of Dif  :', end=' '.ljust(10))
for elem in diff(diff(a)):
    print( '%6.2f' % elem, end=' '.ljust(4))

print('\n'*2,"--------"*9)

###########################
## Operation on Numerator
###########################
a=nom(o)

print('Numerator   :', end="")
for elem in a:
    print('%6.2f' % elem, end=' '.ljust(4))

print(' ')
print('Difference :', end=' '.ljust(5))
for elem in diff(a):
    print( '%6.2f' % elem, end=' '.ljust(4))

print(' ')
print('Dif of Dif :', end=' '.ljust(10))
for elem in diff(diff(a)):
    print( '%6.2f' % elem, end=' '.ljust(4))

print('\n'*2,"--------"*9)
###########################
## Operation on Mixed
###########################
an=nom(o)
ad=denom(o)
frac=vstack((an,ad))
a=[rational.Rational(frac[0][i], frac[1][i]).mixedp() for i in arange(n)]
al=[rational.Rational(frac[0][i], frac[1][i]).mixed() for i in arange(n)]

print('Num Fract  :', end="")
for elem in a:
    print('  %s' % elem, end=' '.ljust(7))


a=[al[i][0] for i in arange(n)]
print(' ')
print('Whole-Whole:', end=' '.ljust(7))
for elem in diff(a):
    print( '%3.f' % elem, end=' '.ljust(8))


a=[al[i][1] for i in arange(n)]
print(' ')
print('Num-Num rel:', end=' '.ljust(7))
for elem in diff(a):
    print( '%3.f' % elem, end=' '.ljust(8))

a=[al[i][2] for i in arange(n)]
print(' ')
print('Dom-Dom rel:', end=' '.ljust(7))
for elem in diff(a):
    print( '%3.f' % elem, end=' '.ljust(8))
print("\n")

