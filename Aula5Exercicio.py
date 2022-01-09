a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
if a > b and a > c:
    print('O maior numero foi o', a)
if b > a and b > c:
    print('O maior numero foi o', b)
else:
    print('O maior numero foi o', c)
print('A soma de todos os 3 numeros é:', (a+b+c))
