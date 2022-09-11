print()
print('************************Los meses del año************************************')
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
        "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

for mes in meses:

        print(mes, end=("-"))

x=",".join(meses)
print('\n')
print("La cantidad de meses que terminan en 'bre' son: ",x.count("bre"))
print("La cantidad de meses que terminan en 'ero' son: ",x.count("ero"))
print()


print('*************************Dias de la semana*********************************')
dias = ["lunes", "martes", "miercoles", "jueves", "viernes","sabado","domingo"]

for dia in dias:

       print(dia, end=("-"))

d=",".join(dias)
print('\n')
print("Los dias que terminan en 'es' son: ",d.count("es"))
print("Los dias que terminan en 'o' son: ",d.count("o"))
print()

print('*************************Rango de Numeros primos*********************************')


def numerosPrimos(inicial,final):
   

    for n in range(inicial,final+1):
            contador=0
            
            for i in range(1, n+1):
                if n % i == 0:
                    contador +=1
            if contador==2:
                print(f'El numero {n} es primo')

a = int(input('Ingrese un numero inicial '))
b = int(input('Ingrese un numero final '))
numerosPrimos(a,b)
print()

print('*************************Los 100 primeros Numeros primos*********************************')


def numerosPrimos(cantidad):

    contador = 1
    n = 2

    while contador <= cantidad:

        for i in range(2, n):
            if n % i == 0:
                break

        else:
            print(f'{contador}-> El numero {n} es primo')
            contador += 1

        n += 1


a = int(input('Ingrese la cantidad de numeros primos que quieres visualizar: '))
numerosPrimos(a)
print()
import random
print('*************************Adivina que numero soy**************************************')
print()


def juego(intentos):
    y = 1
    b = intentos

    x = random.randint(1, 100)
    print(f'El numero misterioso es {x}')

    while y <= intentos:

        print()
        n = int(input(f'{y}-> Ingrese un numero tienes {b} intentos :'))

        if n == x:
            print(
                f'¡Felicitaciones! lo lograste el numero es {x} y lo adivinaste en el intento No.{y}')
            print()
            d = input('Desea continuar Jugando digite si/no?: ')
            print()
            if d == 'si':
                juego(int(input('Ingrese la cantidad de intentos para jugar: ')))

            elif d == 'no':
                print('Nos vemos que tengas un buen dia')
                break

        elif n > x:
            print('El numero que ingresaste es mayor que el numero misterioso ')

        elif n < x:
            print('El numero que ingresaste es menor que el numero misterioso')

        y += 1
        b -= 1


a = int(input('Ingrese la cantidad de intentos para jugar: '))

juego(a)
