#!/usr/bin/env python3
#--
# Author: Marcos Alves
#++
#
# 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#    Calcule e mostre o total do seu salário no referido mês. 
#
ganho = float(input("Digite quanto você ganha por hora: "))
hora = int(input("Digite o número de horas trabalhadas no mês: "))
salario = ganho * hora * 30
print("Seu salário referente ao mês é: R$ %.2f" %salario)