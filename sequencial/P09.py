#!/usr/bin/env python3
#--
# Author: Marcos Alves
#++
#
# 9.Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em 
#   graus Celsius. 
# 
# Lembrando que: C = (5 * (F-32) / 9). 
# 
farenheit = float(input("Digite a temperatura em Farenheit (F): "))
celsius = (5 * (farenheit - 32)/9)
print("A temperatura em graus Celsius é: %.2f" %celsius)