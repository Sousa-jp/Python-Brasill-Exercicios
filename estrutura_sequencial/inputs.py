import numpy as np

''' Faça um Programa que mostre a message "Alo mundo" na tela. '''
# print('Alo mundo')

'''Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].'''
# numero = int(input('Digite um numero:\n'))
# print(f'O numero informado foi {numero}')

'''Faça um Programa que peça dois números e imprima a soma'''
# numero1 = int(input('Numero 1:\n'))
# numero2 = int(input('Numero 2:\n'))
# print(numero1 + numero2)

'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''
# Nota1 = int(input('Nota 1\n:'))
# Nota2 = int(input('Nota 2\n:'))
# Nota3 = int(input('Nota 3\n:'))
# Nota4 = int(input('Nota 4\n:'))
# media = (Nota1 + Nota4 + Nota3 + Nota2) / 4
# print(f' a media foi {media}')

'''Faça um Programa que converta metros para centímetros.'''
# numero_em_metros = float(input('Digite o numero para converter:\n'))
# numero_em_cm = numero_em_metros*100
#
# print(numero_em_cm, 'cm')

"""Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""
# raio_do_circulo = float(input('Digite o raio do circulo:\n'))
#
# area = (raio_do_circulo**2)*3.14
# print(f'Area do circulo: {area} m')

'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.'''
# lado = float(input('Lado do quadrado:\n'))
# area = lado**2
# x2_area = area * 2
# print(f'dobro da area é {x2_area}')

'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''
# salario_por_hora = float(input('Quanto ganhas por hora:\n'))
# horas_trabalhadas = float(input('Quantas horas trabalhadas:\n'))
# salario = horas_trabalhadas*salario_por_hora
# print(f'Salario do mes: {salario} R$')

'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.'''
'''C = 5 * ((F-32) / 9).'''
# temperatura_fahrenheint = float(input('Temperatura em F:\n'))
# C = 5 * ((temperatura_fahrenheint - 32) / 9)
# print(C, 'graus C')

'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:'''
'''1. o produto do dobro do primeiro com metade do segundo .
2. a soma do triplo do primeiro com o terceiro.
3. o terceiro elevado ao cubo.'''
# numeroint1 = int(input('digite numero inteiro 1:\n'))
# numeroint2 = int(input('digite numero inteiro 2:\n'))
# numeroreal = float(input('digite numero real:\n'))
#
# primeiro = (2*numeroint1) * (numeroint2/2)
# print(primeiro)
#
# segundo = (3*numeroint1) + numeroreal
# print(segundo)
#
# terceiro = numeroreal**3
# print(terceiro)

'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58'''
# altura = float(input('digite sua altura\n'))
# peso_ideal = (72.7*altura) - 58
# print(peso_ideal)

'''  Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    1. Para homens: (72.7*h) - 58
    2. Para mulheres: (62.1*h) - 44.7 '''
#
# altura = float(input('Digite sua altura:\n'))
# sexo = input('h ou m?\n')
#
# if sexo == 'h':
#     peso_ideal = (72.7 * altura) - 58
#     print(peso_ideal)
# elif sexo == 'm':
#     peso_ideal = (62.1 * altura) - 44.7
#     print(peso_ideal)
# else:
#     print('nao sei')

'João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.' \
' Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo ' \
'(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.'
'João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na v' \
'ariável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar' \
'. Imprima os dados do programa com as mensagens adequadas.'

# peso = float(input('Peso de peixes:\n'))
# excesso = 0
# if peso > 50 :
#     excesso = peso - 50
#
# multa = excesso*4
#
# print(f'Peso de peixes: {peso} Kg')
#
# print(f'excessp: {excesso} Kg')
#
# print(f'multa: {multa} R$')

'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
1. salário bruto.
2. quanto pagou ao INSS.
3. quanto pagou ao sindicato.
4. o salário líquido.
5. calcule os descontos e o salário líquido, conforme a tabela abaixo: Obs.: Salário Bruto - Descontos = Salário Líquido.

    ```
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
    ```
'''

# ganho_por_hora = float(input('Quanto vc ganha por hora:\n'))
# horas_trabalhadas = float(input('Horas trabalhadas:\n'))
#
# salario = ganho_por_hora*horas_trabalhadas
#
# descontos = salario*0.11 + salario*0.08 + salario*0.05
# salario_liquido = salario - descontos
#
# print(f'Salario bruto: {salario} R$')
# print(f'Imposto INSS: {salario*0.08} R$')
# print(f'Imporsto sindicato: {salario*0.05} R$')
# print(f'Salario liquido: {salario_liquido} R$')
#
'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 
 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

# area_a_pintar = float(input('Tamanho da area em m2: '))
#
# litros_totais = area_a_pintar / 3
# print(f' litros totais: {litros_totais} L')
# quantidade_de_latas = np.ceil(litros_totais / 18)
# print(f'quantidade de latas : {quantidade_de_latas} unidades')
# valor_total = quantidade_de_latas*80
# print(f'valor total: {valor_total} R$')

'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.'''

area_a_pintar = float(input('Tamanho da area em m2: '))

litros_totais = area_a_pintar / 6
print(f' litros totais: {litros_totais} L')
quantidade_de_latas = np.ceil(litros_totais / 18)
print(f'quantidade de latas : {quantidade_de_latas} unidades')
quantidade_de_galoes = np.ceil(litros_totais / 3.6)
valor_total_galao = quantidade_de_galoes * 25
valor_total_lata = quantidade_de_latas * 80

print(f'valor total lata: {valor_total_lata} R$')
print(f'valor total galao: {valor_total_galao} R$')

while (litros_totais % 18 < 3.6):
    quantidade_de_latas = np.ceil(litros_totais / 18)

quantidade_de_galoes = litros_totais
