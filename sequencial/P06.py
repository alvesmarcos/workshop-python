#!/usr/bin/env python3
#--
# Author: Marcos Alves
#++
#
# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 
#
# Lembrando que: Area = pi*r*r
# 
import math

raio = int(input("Digite o valor do raio: "))
area = math.pi * raio * raio
print("Área do círculo é: %.2f" %area)