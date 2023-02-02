# Ex01: Imprimir o sucessor e antecessor de um número inteiro
num = int(input('Hi! Tell me any integer number: '))
# Dá valor ao sucessor e antecessor
suces = num + 1
predec = num - 1
print('Analyzing your number {}, we can say that...\n'
      'The sucessor is {} \n'
      'And the predecessor is {}' .format(num, suces, predec))
