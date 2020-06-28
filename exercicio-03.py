from math import pi

'''
2. Faça um programa que converta metros para milímetros.
3. Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
4. Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área
para o usuário.
5. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês.'''



'''01 Faça um programa que peça as 4 notas de atividades contínuas e mostre a média. Lembrando
que, o total de atividades contínuas consideradas para o cálculo da média será um total de sete).'''
'''
num = int(input('digite a primeira nota: '))
num1 = int(input('digite a segunda nota: '))
num2 = int(input('digite a terceira nota: '))
num3 = int(input('digite a quanta nota: '))

media = (num + num1 + num2 + num3) / 4

print(f'a media das nota são: {media}')
'''
'''#02 2. Faça um programa que converta metros para milímetros.

metro = float(input('digite a quantidade de metros: '))

milimetro = 1000

conversao = metro * milimetro 

print(f' a distancia em milimetros é: {conversao}')


#03  Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input('digite o raio: '))

area = (raio * raio) * pi

print(f'a área do círculo é: {area: .2f}')
'''
'''
#04 Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

alt= float(input('digite a altura do quadrado: '))
lar= float(float(input('digite a largura do quadrado: ')))
print(f'resuataod:{alt * lar * 2: .0f}')
'''
'''5. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês.'''

horas = int(input('quantas horas o funcionario trabalhou: '))
valor = float(input('qual é o valor da hora paga a o funcionario: '))
(salario) = horas * valor

print(f'o salario menssal do funcionario é:{salario: .0f}')


