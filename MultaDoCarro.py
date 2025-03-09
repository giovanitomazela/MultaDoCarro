vel = float(input('Digite a velocidade do carro: '))

print('A velocidade foi de {} km/h'.format(vel))

if vel > 80:
    print('Você foi multado!')
    multa = (vel - 80) * 7
    print('Sua multa é de R${}'.format(multa))
else:
    print('Parabéns, continue assim!')
