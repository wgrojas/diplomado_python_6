print()

impares=[]
for n in range(50,100):
   
    if n%2 !=0:

       impares.append(n)

print('numeros impares del 51 al 100: ',impares)
print()



def nombre(n):
    print(f'hola {n} bienvenido')
    while n !=0:
        nombre=input('Cual es tu nombre? ')
        if nombre=='0':
            n=int(nombre)
        else:
            print(f'hola {nombre}')
        
    print(f'hasta pronto')

a=input('Cual es tu nombre? ')
nombre(a)
print()


n=input('Cual es tu nombre? ')
print(f'hola {n} bienvenido')
while n !='0':
    n=input('Cual es tu nombre? ')
    if n!='0':
        print(f'hola {n}')
print(f'hasta pronto')


d=int(input('Cuanto dinero en efectivo tienes: $'))
if d>0:
    print('Listo te ayudare con los gastos ')

    while d>0:
        print()
        gasto=int(input('Cuanto gastaste: $'))
        d=d-gasto

        if d>0:
            print(f'Te queda un saldo de ${d}')
        else:
            print('Te quedaste sin saldo vuelve a retirar dinero')

       






        



