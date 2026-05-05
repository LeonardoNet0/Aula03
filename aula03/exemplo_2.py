



idade = int(input('digite a idade:' )) #19 ###### >, < , >= <= ,== ,=!26

if idade >= 18: 
    print('voce é adulto')
else: 
    print('voce é menor') 



#classificaçao por Pontos   
 
pontos = int(input('informe os pontos:'))
if pontos >= 100:
    total = pontos + 10
    print('f excelente! Agora você tem {total} pontos') 
elif pontos >= 50:
    total = pontos + 5
    print('f Bom desempenho. voce tem {total} pontos')
else:
    print('f treine mais. Pontuaçao {pontos} pontos')

    print('Fim!')