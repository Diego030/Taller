pi=3.1416
R=float(input("Introduce el radio: "))
g=float(input("introduce la generatriz: "))
h=float(input("Introduce la altura:"))
ab=pi*R**2
volumen=(ab*h)/3
asc=pi*R*g
area=ab+asc
print("El volumen del cono es: ", volumen)
print("El area del cono es: ", area)