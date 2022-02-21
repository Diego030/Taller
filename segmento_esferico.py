pi=3.1416
R=float(input("Ingresa el radio superior: "))
r=float(input("Ingresa el radio inferior: "))
h=float(input("Ingresa la altura: "))
v=3*R**2
v1=3*r**2
v2=v+v1
v3=h**2+v2
v4=pi*h
volumen=(v4*v3)/6
a=2*pi
a1=R*h
area=a*a1
print("El volumen de la zona o segmento esferico es: ", volumen)
print("El area de la zona o segmento esferico es: ", area)