# Faça um Programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#
#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores
#     para cima, isto é, considere latas cheias.

area = float(input("Digite a quantos metros quadrados você precisa pintar: "))

lata = 18
galao = 3.6
litros = area / 6
perda = 1.1

qtdl = litros*perda / lata
qtdg = litros*perda / galao
# mista = litros

m1 = round(qtdl % litros+0.5)
m2 = round(qtdg % litros+0.5)
value1 = 80.00
value2 = 25.00
# value3 = mista
resto1 = round(litros / lata-0.5)
lit_sobra = litros - lata*resto1
resto2 = round(lit_sobra / galao+0.5)

price18 = m1 * value1
price36 = m2 * value2
price3 = resto1*value1 + resto2*value2

print(lit_sobra)
print(f"Comprar apenas latas de 18 litros = {m1} latas no valor de {price18} R$")
print(f'Comprar apenas galões de 3,6 litros = {m2} galões no valor de {price36} R$')
print(f'Misturar latas e galões, de forma que o preço seja o menor teremos {resto1} latas e {resto2}'
      f' galoes no valor de {price3} R$')


