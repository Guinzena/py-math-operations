# Ex06: Calcule a área de uma parede e responda quantos litros de tinta serão necessários
# Cada litro de tinta pinta 2m² de parede
alt = float(input('Bem Vindo(a)! Vamos calcular quantos litros de tinta lhe serão necessários \n'
                  'Qual é a altura(m) da parede que você deseja pintar? '))
larg = float(input('E qual é a medida da largura(m)? '))
# Faz o cálculo da área e em seguida do núemro de litros necessários
area = alt * larg
litros = area / 2
print('Com os respectivos valores({}, {}), sua parede tem uma área de {}m² \n'
      'Sendo assim necessário {}l de tinta para pinta-la.'.format(alt, larg, area, litros))
