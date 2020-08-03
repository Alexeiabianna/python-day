# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# # acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor
# a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

option_fuel = input("Escolha o tipo de combustível: Álcool[A] Gasolina[G]---> ")
litres = float(input("Digite a quantidade de litros: "))

price_g: float = 2.50
price_a: float = 1.90

# tax discount to alcohol
discount_3 = 0.97
discount_5 = 0.95
# tax discount to gás
discount_4 = 0.96
discount_6 = 0.94

# Calculate to Alcohol
if option_fuel == 'A':
    if litres <= 20.00:
        value = (litres * price_a) * discount_3
        print(f"O valor a ser pago será de {value} R$")
    elif litres > 20.00:
        value = (litres * price_a) * discount_5
        print(f"O valor a ser pago será de {value} R$")
elif option_fuel == 'a':
    if litres <= 20.00:
        value = (litres * price_a) * discount_3
        print(f"O valor a ser pago será de {value} R$")
    elif litres > 20.00:
        value = (litres * price_a) * discount_5
        print(f"O valor a ser pago será de {value} R$")

# Calculate to Gás
if option_fuel == 'G':
    if litres <= 20.00:
        value = (litres * price_g) * discount_4
        print(f"O valor a ser pago será de {value} R$")
    elif litres > 20.00:
        value = (litres * price_g) * discount_6
        print(f"O valor a ser pago será de {value} R$")
elif option_fuel == 'g':
    if litres <= 20.00:
        value = (litres * price_g) * discount_4
        print(f"O valor a ser pago será de {value} R$")
    elif litres > 20.00:
        value = (litres * price_g) * discount_6
        print(f"O valor a ser pago será de {value} R$")
