# Ex03: Ler um valor em metros e mostrar sua conversão em quilômetros, centímetros e milímetros
m = int(input('Welcome to the measurement converter, enter your value in meters: '))
# Converte para os respectivos valores
km = m / 1000
cm = m * 100
mm = m * 1000
print('Your value of {} meters results in: \n'
      '{} kilometers, {} centimeters and {} millimeters'.format(m, km, cm, mm))
