salario_colaborador =float(input('Qual o seu salario atual ?'))
if(salario_colaborador <= 280):
    percentual = 20

elif(280 > salario_colaborador <= 700):
    percentual = 15
    
elif( 700 > salario_colaborador <= 1500):
    percentual = 10

else:
    
    percentual = 5

percentual_aplicado = percentual/100
valor_do_aumento= salario_colaborador * percentual_aplicado
reajuste_salario = salario_colaborador + valor_do_aumento

print ('Seu salario antes do reajuste era: R$', salario_colaborador)
print ('O percentual de aumento aplicado foi : ', percentual, '%')
print ('O valor do aumento eh de : R$', valor_do_aumento)
print ('O seu novo salario apos o reajuste eh : R$',reajuste_salario)
print ('Tenha uma boa tarde!')
