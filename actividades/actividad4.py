print('*****************************************************************************************************')
meses=['enero','febrero','marzo','abril','mayo','junio','julio']

print()
print("El mes de abril se encuentra en la posicion numero {}".format(meses.index('abril')))
print()
print("El valor de la lista en el indice 6 es {} y en la posicion 3 es {} ".format(meses[6],meses[3]))

mes=('agosto','septiembre','octubre','noviembre','diciembre')
for m in mes:
        meses.append(m)
print()
print(",".join(meses))
print('*****************************************************************************************************')
edades=[24,25,27,36,35,32,27,30,39]
print()
print('La edad mas alta en la lista es {}'.format(max(edades)))
print()
print('La edad menor en la lista es {}'.format(min(edades)))
print('*****************************************************************************************************')
print('El promedio de las edades de la lista es {}'.format(sum(edades)//len(edades)))
print('*****************************************************************************************************')



print()
print('*********************cajero electronico  virtual****************************')
print()

data = [123, 456, 789, 321, 654, 987]
vigilante = True
saldo = 0
nombre = str(input('Bienvenido Ingrese su nombre: '))
id = int(input('ingrese su numero de documento: '))
print()

while vigilante:
   
        if id in data:

            print()
            print(f'{nombre}' ' Digite la operacion que deseas realizar')
            print()
            op = int(
                input(' 1->Consignar \n 2->Retirar \n 3->Consultar saldo \n 0->salir \n \n'))

            if op == 1:
                monto = (int(input('ingrese la cantidad de dinero a consignar $')))
                saldo = saldo+monto
                print(f'su nuevo saldo es $ {saldo}')
                print()

            elif op == 2:

                dinero = [100000, 50000, 20000, 10000]
                monto = int(input('Cuanto dinero desea retirar $'))

                if saldo > monto:
                    retiro = monto

                    for i in dinero:

                        b = retiro//i
                        v = retiro % i

                        if b > 0 or v == 0:
                            if i == 10000:
                                print(f'{b} billetes de $ {i} ')
                                retiro = retiro-(b*i)

                            else:
                                b = b-1

                                print(f'{b} billetes de $ {i} ')
                                retiro = retiro-(b*i)

                    saldo = saldo-monto
                    print(f'su nuevo saldo es $ {saldo}')
                    print()
                   

                else:
                    print('No tienes fondos suficientes para realizar la operacion')
                    print()
                    break

            elif op == 3:
                print('Su saldo es $', saldo)
                print()

           
       
  
            elif op == 0:
                print('Gracias por utilizar nuestro servicio')
                vigilante = False

        else:
            print(f'el documento {id} no se encuentra registrado en el sistema')
            print()
            break
            

