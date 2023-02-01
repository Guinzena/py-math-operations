# Ex01: Imprimir o sucessor e antecessor de um número inteiro
num = int(input('Olá! Me diga qualquer número inteiro: '))
# Dá valor ao sucessor e antecessor
suces = num + 1
antec = num - 1
print('Analizando o número {}, podemos dizer que...\n'
      'O seu sucessor é {} \n'
      'E seu antecessor é {} \n' .format(num, suces, antec))
