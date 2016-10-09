#!/usr/bin/env python3
#--
# Author: Marcos Alves
#++
#
# 11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#    a. o produto do dobro do primeiro com metade do segundo .
#    b. a soma do triplo do primeiro com o terceiro.
#    c. o terceiro elevado ao cubo.   
# 
numero_1 = int(input("Digite o 1º número (inteiro): "))
numero_2 = int(input("Digite o 2º número (inteiro): "))
numero_3 = float(input("Digite o 3º número (real): "))

a = (numero_1 * 2) * (numero_2/2)
b = (numero_1 * 3) + numero_3
c = numero_3 * numero_3 * numero_3

print("A =", a, " B =", b, " C =", c)