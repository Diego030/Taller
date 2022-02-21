pi=3.1416
R=float(input("Ingresa el radio:" ))
h=float(input("Ingresa la altura del cilindro: "))
V=R**2
volumen=(pi*V)*h
A=R*(h+R)
area=(2*pi)*A
print("El volumen del cilindro es: ", volumen)
print("El area del cilindro es: ", area)