#Rectangulo
from math import pi


print("******************************************************************************************************************************")
print("Operaciones geometricas del rectangulo")
base=int(input("Ingrese la longitud de la base: "))
altura=int(input("Ingrese la longitud de la altura: "))
ancho=int(input("Ingrese la longitud del ancho: "))
print('dimensiones: base:{}, altura: {}, ancho: {}'.format(base,altura,ancho))
print()
#perimetro
print('calculando el perimetro...')
perimetro=2*(base+altura)
print('El perimetro del rectangulo es: {}'.format(perimetro))
print()
#area
print('calculando el area...')
areaRectangulo=base*altura
print('El area del rectangulo es:{}'.format(areaRectangulo))
print()
#volumen
print('calculando el volumen de un prisma rectangulo...')
volumen=base*altura*ancho
print('El volumen delrectangulo es:{}'.format(volumen))
print()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#cuadrado
print("*********************************************************************************************************************************************")
print("Operaciones geometricas del cuadrado")
lado=int(input("Ingrese la longitud del lado: "))
print('dimensiones: lado:{}'.format(lado))
print()
#perimetro
print('calculando el perimetro...')
perimetro=4*(lado)
print('El perimetro del cuadrado es: {}'.format(perimetro))
print()
#area
print('calculando el area...')
areaCuadrado=lado**2
print('El area del cuadrado es:{}'.format(areaCuadrado))
print()
#volumen
print('calculando el volumen de un prisma cuadrado...')
volumen=lado**3
print('El volumen del prisma cuadrado es:{}'.format(volumen))
print()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#circulo y esfera
print("************************************************************************************************************************************************")
print("Operaciones geometricas del circulo")
radio=float(input("Ingrese la longitud del radio: "))
print('dimensiones: radio:{}'.format(radio))
print()
#perimetro
print('calculando el perimetro...')
perimetro=2*pi*radio
print('El perimetro del circulo es: {}'.format(perimetro))
print()
#area
print('calculando el area...')
areaCirculo=pi*radio**2
print('El area del circulo es:{}'.format(areaCirculo))
print()
#volumen
print('calculando el volumen de la esfera es...')
volumen=4/3*pi*radio**3
print('El volumen de la esfera es:{}'.format(volumen))
print()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#triangulo y piramide
print("*****************************************************************************************************************************************************")
print("Operaciones geometricas del triangulo")
base=int(input("Ingrese la longitud del lado base: "))
altura=int(input("Ingrese la longitud de la altura: "))
lado1=int(input("Ingrese la longitud del lado 1: "))
lado2=int(input("Ingrese la longitud del lado 2: "))

print('dimensiones: base:{},altura:{},lado1:{},lado2:{}'.format(base,altura,lado1,lado2))
print()

#perimetro
print('calculando el perimetro...')
perimetro=(base+lado1+lado2)
print('El perimetro del triangulo es: {}'.format(perimetro))
print()

#area
print('calculando el area...')
areaTriangulo=(base*altura)/2
print('El area del triangulo es:{}'.format(areaTriangulo))
print()

#volumen
print('calculando el volumen de un prisma triangular...')
volumen=areaTriangulo*altura
print('El volumen del prisma triangular es:{}'.format(volumen))
print()



