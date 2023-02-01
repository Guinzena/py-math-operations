# ex08: Receba duas notas de um aluno e calcule sua média
nome = str(input('Bom dia! \n'
                    'Digite o nome do aluno(a): '))
nota1 = float(input('Agora digite a sua 1° nota: '))
nota2 = float(input('E agora a 2° nota: '))
# Faz o cálculo da média
media = (nota1 + nota2) / 2
# Utilizando o \033 para alterar as coresdo terminal
print('\033[32mBoletim de {}\033[m \n'
      '1° Prova: \033[32m{}\033[m \n'
      '2° Prova: \033[32m{}\033[m \n'
      'Média: \033[32m{}\033[m'.format(nome, nota1, nota2, media))
