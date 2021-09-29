def geron(a, b, c):
    p = (a+b+c)/2
    print ('Полупериметр =', p )
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print ('Площадь =',s, '\n')
    return s



def y_n(qwes):
    ch = input(qwes)
    while ch.lower() not in ('y', 'n'):
        ch = input("выберете y/n\n")
    return ch.lower()



def test(a,b,c):
    ttt = (a, b, c)
    sor = sorted(ttt)
    if sor[2] >= sor[0]+sor[1]:
        print('Это не треугольник')
        main()
    else:
        geron(a, b, c)


def main():
    abc = input('Введите длины сторон треугольника через пробел\n').split()
    for i in range(len(abc)):
        abc[i] = int(abc[i])
    if len(abc) != 3:
        print('У треугольника 3 стороны ;)')
        main()
    a = abc[0]
    b = abc[1]
    c = abc[2]
    test(a, b, c)
    ans = y_n('Посчитать еще один треугольник? Напишите y или n\n')
    if ans == 'y':
        main()
    elif ans == 'n':
        print('Удачи!')
        exit(0)
main()