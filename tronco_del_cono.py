pi=3.1416
r=float(input("Introduce el radio de la base superior: "))
R=float(input("Introduce el radio de labase inferior: "))
h=float(input("Introduce la altura: "))
g=float(input("Introduce el valor de la generatriz: "))
V=R*r
v=R**2+r**2
v1=v+V
v2=pi*h
volumen=(v2*v1)/3
A=(R+r)*g
a=A+v
area=pi*a
print("El volumen del tronco de cono es: ", volumen)
print("El area del tronco de cono es: ", area)