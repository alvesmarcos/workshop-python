#!/usr/bin/env python3
#--
# Author: Marcos Alves
#++
#
# 11. Tendo como dados de entrada a altura de uma pessoa, construa um 
#     algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
#     (72.7*altura) - 58 
#
altura = float(input("Digite sua altura (m): "))
peso_ideal = (72.7*altura) - 58 
print("O pesoal ideal é: %.2f kg" %peso_ideal)