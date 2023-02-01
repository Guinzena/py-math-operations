# EX04: Leia quanto dinheiro o usuário possuí e converta em doláres
brl = float(input('Olá! Irei converter seu dinheiro! \n'
                'Quanto você possuí? R$ '))
# Faz a conversão na cotação 5.08
usd = brl / 5.08
print('Seu dinheiro, R${:.2f}, é convertido na cotação 5.08 \n'
      'Para o valor de US${:.2f}'.format(brl, usd))
