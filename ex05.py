# Ex05: Ler o salário de um funcionário e imprimir seu novo salário + 15% de aumento
salary = float(input('Good morning! Tell me what your salary is: US$'))
# Faz o acréssimo de 15%
newsalary = salary + (salary*0.15)
print('Congratulations! Your new salary is US${:.2f}'.format(newsalary))
