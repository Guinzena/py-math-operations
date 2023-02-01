# Ex05: Ler o salário de um funcionário e imprimir seu novo salário + 15% de aumento
salario = float(input('Bom dia! Nos diga qual é o valor de seu salário: R$'))
# Faz o acréssimo de 15%
novosal = salario + (salario*0.15)
print('Parabéns! O seu novo salário é R${:.2f}'.format(novosal))