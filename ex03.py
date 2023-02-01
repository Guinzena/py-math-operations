# Ex03: Ler um valor em metros e mostrar sua conversão em quilômetros, centímetros e milímetros
m = int(input('Bem-vindo(a) ao conversor de medidas, digite seu valor em metros: '))
# Converte para os respectivos valores
km = m / 1000
cm = m * 100
mm = m * 1000
print('O seu valor de {} metros resulta em: \n'
      '{} quilômetros, {} centímetros, {} milímetros'.format(m, km, cm, mm))
