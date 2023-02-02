# EX04: Leia quanto dinheiro o usuário possuí e converta em doláres
brl = float(input('Hey! I will convert your money! \n'
                'How much do you own? R$'))
# Faz a conversão na cotação 5.08
usd = brl / 5.08
print('Your money, R${:.2f}, is converted in to quotation 5.08 \n'
      'For the value US${:.2f}'.format(brl, usd))
