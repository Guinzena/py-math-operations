# ex08: Receba duas notas de um aluno e calcule sua média
name = str(input('Good morning! \n'
                    'Enter the students name: '))
grade1 = float(input('Now enter the 1st grade: '))
grade2 = float(input('And now 2nd grade: '))
# Faz o cálculo da média
average = (grade1 + grade2) / 2
# Utilizando o \033 para alterar as cores do terminal
print('\033[32mBulletin of {}\033[m \n'
      '1st Test: \033[32m{}\033[m \n'
      '2nd Test: \033[32m{}\033[m \n'
      'Average: \033[32m{:.1f}\033[m'.format(name, grade1, grade2, average))
