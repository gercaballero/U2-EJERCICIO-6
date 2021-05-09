from claseFechaHora import FechaHora
import os

def test():                         #TEST DE FECHAS CON OPERACIONES
    f1=[31,12,2020,20,30,30]
    f2=[10,1,2,5,30,15]
    os.system('cls')
    print('---EJEMPLO 1---\n')                            
    fecha1=FechaHora(f1[0],f1[1],f1[2],f1[3],f1[4],f1[5])
    print('FECHA 1 ---------> {}'.format(fecha1))
    fecha2=FechaHora(f2[0],f2[1],f2[2],f2[3],f2[4],f2[5])
    print('FECHA 2 ---------> {}\n'.format(fecha2))
    input()
    print('FECHA 1 + FECHA 2 = {}\n'.format(fecha1+fecha2))
    print('FECHA 1 - FECHA 2 = {} segundos\n'.format(fecha1-fecha2))
    comp1=fecha1>fecha2
    if comp1==1:
        print('LA FECHA 1 ES MAYOR QUE LA FECHA 2')
    elif comp1==0:
        print('LA FECHA 1 ES IGUAL A LA FECHA 2')
    elif comp1==2:
        print('LA FECHA 2 ES MAYOR QUE LA FECHA 1')
    input()
    f3=[31,12,2020,20,30,30]
    f4=[31,12,2020,20,30,30]
    os.system('cls')
    print('---EJEMPLO 2---\n')                      #EJEMPLO 2 CON FECHAS IGUALES
    fecha3=FechaHora(f3[0],f3[1],f3[2],f3[3],f3[4],f3[5])
    print('FECHA 3 ---------> {}'.format(fecha3))
    fecha4=FechaHora(f4[0],f4[1],f4[2],f4[3],f4[4],f4[5])
    print('FECHA 4 ---------> {}'.format(fecha4))
    input()
    print('FECHA 3 + FECHA 4 = {}\n'.format(fecha3+fecha4))
    print('FECHA 3 - FECHA 4 = {} segundos\n'.format(fecha3-fecha4))
    comp2=fecha3>fecha4
    if comp2==1:
        print('LA FECHA 3 ES MAYOR QUE LA FECHA 4')
    elif comp2==0:
        print('LA FECHA 3 ES IGUAL A LA FECHA 4')
    elif comp2==2:
        print('LA FECHA 3 ES MAYOR QUE LA FECHA 4')
    
if __name__ == '__main__':
    t=str(input('DESEA PROBAR EL TEST (S/N) : '))
    if t.lower()=='s':
        test()
        input()
    os.system('cls')
    print('~~~~~~FECHA 1~~~~~~')
    d=int(input("Ingrese Dia: "))
    mes=int(input("Ingrese Mes: "))
    a=int(input("Ingrese Año: "))
    h=int(input("Ingrese Hora: "))
    m=int(input("Ingrese Minutos: "))
    s=int(input("Ingrese Segundos: "))
    f1 = FechaHora(d,mes,a,h,m,s)
    f1.Mostrar()
    input()
    os.system('cls')
    print('~~~~~~FECHA 2~~~~~~')
    d1=int(input("Ingrese Dia: "))
    mes1=int(input("Ingrese Mes: "))
    a1=int(input("Ingrese Año: "))
    h1=int(input("Ingrese Hora: "))
    m1=int(input("Ingrese Minutos: "))
    s1=int(input("Ingrese Segundos: "))
    f2 = FechaHora(d1,mes1,a1,h1,m1,s1)
    f2.Mostrar()
    input()
    os.system('cls')
    print('~~~~~ F1 + F2 ~~~~~')
    f3=f1+f2
    print('[{}]     +    [{}]    =      {}'.format(f1,f2,f3))
    input()
    os.system('cls')
    print('~~~~~ F1 - F2 ~~~~~')
    f4=f1-f2
    print('[{}]     -    [{}]    =      {} segundos'.format(f1,f2,f4))
    input()
    os.system('cls')
    print('~~~~~ ¿F1 > F2? ~~~~~')
    comp=f1>f2
    if comp:
        print('LA FECHA 1 ES MAYOR QUE LA FECHA 2')
    elif comp==None:
        print('')
    else:
        print('LA FECHA 2 ES MAYOR QUE LA FECHA 1')

