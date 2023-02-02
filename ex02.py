# Ex02: Ler um número e imprimir respecticamente seu dobro, triplo  e raíz quadrada
num = int(input('Hi! I need to do operations! Tell me a number: '))
# Realiza os cálculos
doub = num * 2
tri = num * 3
# Potencializa o valor 0.5 para forçar uma raíz quadrada
root = num ** (1/2)
print('About your number {} i can say... \n'
      'The value of its double is {} \n'
      'Its triple results in {} \n'
      'And its square root is {} \n'.format(num, doub, tri, root))
