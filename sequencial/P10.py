#!/usr/bin/env python3
#--
# Author: Marcos Alves
#++
#
# 9.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.  
# 
# Lembrando que: F = ((9*C)/5) + 32 
# 
celsius = float(input("Digite a temperatura em Celsius: "))
farenheit = ((9*celsius)/5) + 32 
print("A temperatura em graus Farenheit é: %.2f F" %farenheit)