# Ex06: Calcule a área de uma parede e responda quantos litros de tinta serão necessários
# Cada litro de tinta pinta 2m² de parede
height = float(input('Welcome! Lets calculate how many liters of ink will be necessary \n'
                  'What is the height(m) of the wall? '))
width = float(input('And what is the width(m)? '))
# Faz o cálculo da área e em seguida do núemro de litros necessários
area = height * width
liters = area / 2
print('With the respective values({}, {}), your wall has an area of {}m² \n'
      'Being necessary {}l of ink to paint it.'.format(height, width, area, liters))
