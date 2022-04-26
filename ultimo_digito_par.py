"""Problema No. 3:
Verificar si el ultimo digito de un numero es PAR"""

print("-------------------------------------")
print("--------ULTIMO DIGITO PAR------------")
print("-------------------------------------")





# input
x = int(input("Digite el valor de x: "))


# procesing
ultimo_digito_par = x % 10
r = ultimo_digito_par % 2

if r == 0:
    print("El ultimo digito de " + str(x) + " es PAR")
    