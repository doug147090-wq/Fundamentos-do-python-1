import random

print('JOGO DA ALEATORIDADE')
print()
print('TENTE ACERTAR O NÚMERO DE 1 A 10... ')
print('VALENDO R$5.000,00')

numero_maquina = random.randint(1,10)
tentativas  =  3
for n in range(tentativas):
    numero_usuario = int(input('SEU CHUTE VALENDO 5K!>>>> '))
    tentativas =  tentativas - 1
    if numero_usuario == numero_maquina:
        print('Você é o grande vencedor(a)')
        print('LEVE SEU 5K!!!! ;)')
    else:
        print('ERROU FEIO!! PERDEDOR(A)!!')
        
        print('tentativas', tentativas)
        if tentativas  == 0:
            print('o numero da maquina é ', numero_maquina)
else:
    print('Tentaivas esgotadas!!! ;P ')


 

 

 


 






 

 
