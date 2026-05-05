
valor_compra = float(input("Digite o valor total da compra: R$ "))
if valor_compra > 250.00: 
    desconto = valor_compra * 0.16
    valor_final = valor_compra - desconto
    print(f"Desconto de 16% incluido!")
    print(f"O valor final da compra é: R$ {valor_final:}")
else:
    print(f"Sem desconto para este valor.")
    print(f"O valor normal da compra é: R$ {valor_compra:}")





