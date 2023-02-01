# Ex02: Ler um número e imprimir respecticamente seu dobro, triplo  e raíz quadrada
num = int(input('Olá! Preciso fazer cálculos! Me diga um número: '))
# Realiza os cálculos
dob = num * 2
tri = num * 3
# Potencializa o valor 0.5 para forçar uma raíz quadrada
raiz = num ** (1/2)
print('Quanto ao número {} posso dizer que... \n'
      'O valor do seu dobro é {} \n'
      'Seu triplo resulta em {} \n'
      'E sua raíz quadrada é {} \n'.format(num, dob, tri, raiz))
