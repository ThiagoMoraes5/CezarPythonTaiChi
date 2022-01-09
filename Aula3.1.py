from random import randit
pc = randit(0,5)
print('-=-'*20)
print('Vou Pensar em um numero de 0 a 5 tente adivinhar')
print('-=-'*20)
jogador = int(input('Digite um numero'))
if jogador == pc:
    print('Parabens voce ganhou')
else:
    print('Voce perdeu o numero foi {}'.format(pc))
