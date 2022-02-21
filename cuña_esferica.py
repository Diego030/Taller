pi=3.1416
R=float(input("Ingresa el radio: "))
n=float(input("Introduce los grados"))
v=4*pi
v1=R**3*n
v2=3*360
volumen=(v*v1)/v2
a=R**2*n
area=(v*a)/360
print("El volumen del Huso: Cuña esferica es: ", volumen)
print("El area del Huso: Cuña esferica es: ", area)