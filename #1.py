pi = 3.14

"""1"""


def num1():
    a = 4
    p = 4 * a
    print("1--- ", p)


num1()

"""2"""


def num2():
    a = 6
    S = a**2
    print("2--- ", S)


num2()

"""3"""


def num3():
    a = 5
    b = 6
    S = 5 * 6
    P = 2 * (a + b)
    print(f"3.1--- S = {S}\n3.2--- P = {P}")


num3()

"""4"""
# from math import pi


def num4():
    d = 6
    L = d * pi
    print(f"4--- {L}")


num4()

"""5"""


def num5():
    a = 3
    V = a**3
    S = 6 * a**2
    print(f"5.1--- V = {V}\n5.2--- S = {S}")


num5()

"""6"""


def num6():
    a = 5
    b = 3
    c = 6
    V = a * b * c
    S = 2 * (a * b + b * c + a * c)
    print(f"6.1--- V = {V}\n6.2--- S = {S}")


num6()

"""7"""


def num7():
    r = 8
    s = pi * r**2
    l = 2 * pi * r
    print(f"7.1--- S = {s}\n7.2--- L = {l}")


num7()

"""8"""


def num8():
    a = 6
    b = 8
    print(f"8--- {(a+b)/2}")


num8()

'''9'''
from math import sqrt
def num9():
    a = 3
    b = 3
    print(f'9--- {(a*b)**0.1}')

num9()

'''10'''

def num10():
    a = 3
    b = 5
    print(f'10.1--- a**2 + b**2 = {a**2 + b**2}')
    print(f'10.2--- a**2 - b**2 = {a**2 - b**2}')
    print(f'10.3--- a**2 * b**2 = {a**2 * b**2}')
    print(f'10.4--- a**2 / b**2 = {a**2 / b**2}')    

num10()

'''11'''

def num11():
    a = -3
    b = -5
    print(f'11.1--- |a|**2 + |b|**2 = {abs(a)**2 + abs(b)**2}')
    print(f'11.2--- |a|**2 - |b|**2 = {abs(a)**2 - abs(b)**2}')
    print(f'11.3--- |a|**2 * |b|**2 = {abs(a)**2 * abs(b)**2}')
    print(f'11.4--- |a|**2 / |b|**2 = {abs(a)**2 / abs(b)**2}')    

num11()

"""12"""

def num12():
    a = 3
    b = 4
    c = sqrt(a**2 + b**2)
    print(f'12.1--- c = {sqrt(a**2 + b**2)}\n12.2--- P = {a+b+c}')



num12()

"""13"""

def num13():
    r1 = 6
    r2 = 4
    s1 = pi*(r1)**2
    s2 = pi*(r2)
    s3 = s1 - s2
    print(f'13.1--- {s1}\n13.2--- {s2}\n13.3--- {s3}')


num13()

"""14"""

def num14():
    l = 20
    r = l/2*pi
    s = pi*r**2
    print(f'14.1--- {r}\n14.2--- {s}')    



num14()

"""15"""

def num15():
    s = 50
    r = sqrt(s/pi)
    d = r*2
    l = 2*pi*r
    print(f'15.1--- {d}\n15.2--- {l}')



num15()

"""16"""

def num16():
    x1 = -234
    x2 = 6575
    a = abs(x1-x2)
    print(f'16--- {a}')



num16()

'''17'''

def num17():
    a = -3
    b = -2
    c = 11
    print(f'17.1--- {abs(a-c)}\n17.2--- {abs(b-c)}\n17.3--- {abs(b-c) + abs(a-c)}')



num17()

"""18"""

def num18():
    a = -2
    c = 3
    b = 6
    if c>a and c<b:
        print(f'18--- {abs(a-c) * abs(c-b)}')



num18()

"""19"""

def num19():
    x1,y1 = 2,1
    x2,y2 = 5,6
    p = (abs(2-5) + abs(1-6))*2
    s = abs(2-5) * abs(1-6)
    print(f'19.1--- {p}\n19.2--- {s}')



num19()

"""20"""

def num20():
    x1, y1 = 3, 6
    x2, y2 = 5, 8
    a = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f'20--- {a}')


num20()

"""21"""

def num21():
    x1, y1 = 3, 6
    x2, y2 = 5, 2
    x3, y3 = 1, 2
    a = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    b = sqrt((x3 - x1)**2 + (y3 - y1)**2)
    c = sqrt((x3 - x2)**2 + (y3 - y2)**2)
    P = a + b + c
    p = P/2
    S = sqrt(p * (p-a) * (p-b) * (p-c))
    print(f'21.1--- {P}\n21.2--- {S}')



num21()

"""22"""

def num22():
    a, b = 5,6
    a, b = b, a
    print(f'22--- {a,b}')



num22()

"""23"""

def num23():
    a, b, c = 1,2,3
    a, b, c = b, c, a
    print(f'23--- {a,b,c}')



num23()

"""24"""

def num24():
    a, b, c = 1,2,3
    a, b, c = c, a, b
    print(f'24--- {a,b,c}')



num24()

"""25"""

def num25():
    x = 10
    y = 3 * x ** 6 - 6 * x ** 2 - 7
    print(f'25--- {y}')



num25()

"""26"""

def num26():
    x = 6
    y = 4 * (x - 3)**6 - 7 * (x - 3) ** 3 + 2
    print(f'26--- {y}')



num26()

"""27"""

def num27():
    a = 2
    a2 = a*a
    a4 = a2*a2
    a8 = a4*a4
    print(f'27--- {a2,a4,a8}')



num27()

"""28"""

def num28():
    A = 2
    x = A*A
    print(f"28.1--- A^2 = {x}")
    A = x*A
    print(f"28.2--- A^3 = {A}")
    A = x*A
    print(f"28.3--- A^5 = {A}")
    x = A*A
    print(f"28.4--- A^10 = {x}")
    A = x*A
    print(f"28.5--- A^15 = {A}")
    a = 2
    a2 = a*a
    a3 = a2*a
    a5 = a3*a2
    a10 = a5*a5
    a15 = a10*a5
    print(f'28--- {a2,a3,a5,a10,a15}')



num28()

"""29"""
Pi = 180
def num29():
    a = 191
    if 0<a<360:
        x = a * pi/180
        print(f'29--- {x}')



num29()

"""30"""

def num30():
    a = 1.5708
    if 0<a<2*Pi:
        x = a * 180/pi
        print(f'30--- {x}')



num30()

"""31"""

def num31():
    tf = 158
    tc = (tf-32)*5/9
    print(f'31--- {tc}')



num31()

"""32"""

def num32():
    tc = 70
    tf = 9 * tc / 5 + 32
    print(f'32--- {tf}')



num32()

"""33"""

def num33():
    x = 2 #kg
    a = 200 #tg
    cost = a/x #стоимось 1 кг продукта
    y = 3 #kg
    s = y*cost # стоимость y кг продукта
    print(f'33--- {cost,s}')



num33()

"""34"""

def num34():
    x = 3 #kg
    a = 600 #tg
    y = 5 #kg
    b = 500 #tg
    costx = a/x #tg
    costy = b/y #tg
    print(f'34.1--- {costx,costy}\n34.2--- {abs(costx-costy)}')



num34()

"""35"""

def num35():
    v = 12 # скорость лодки при стоячей воде
    u = 4 # скорость течения реки
    t1 = 2 # время потраченное на озере
    s1 = v * t1
    t2 = s1/(v-u) # время потраченное на реке(против течения)
    s2 = t2 * (v-u)
    print(f'35--- {s1,s2}')



num35()

"""36"""

def num36():
    
    print()



num36()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

# """2"""

# def num2():
    
#     print()



# num2()

