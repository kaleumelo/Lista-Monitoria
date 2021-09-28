salario_horas= float( input('Quanto voce ganha por hora ?: '))
horas = float(input('E quantas horas trabalhou no mes ?: '))
salario_bruto = salario_horas * horas
sindicato = 3
calculo_sindicato = salario_bruto * (sindicato/100)
FGTS = 11
calculo_fgts= salario_bruto * (FGTS/100)

if(salario_bruto <= 900):
    salario = salario_bruto - (calculo_sindicato + calculo_fgts)

elif(salario_bruto <= 1500):
    IR = 5 
    calculo_ir = salario_bruto * (IR/100)
    salario = salario_bruto - (calculo_ir + calculo_sindicato + calculo_fgts)

elif(salario_bruto <= 2500):
    IR = 10 
    calculo_ir = salario_bruto * (IR/100)
    salario = salario_bruto - (calculo_ir + calculo_sindicato + calculo_fgts)

else:
    salario_bruto > 2500
    IR = 20 
    calculo_ir = salario_bruto * (IR/100)
    salario = salario_bruto - (calculo_ir + calculo_sindicato + calculo_fgts)


print ('Seu salario bruto eh: R$', salario_bruto)
print ('Esses sao todos os descontos que fazemos no seu salario:\n','Porcentagem do sindicato: ',sindicato,'%\n'
'Porcentagem do sindicato: ', FGTS,'%\n','Porcentagem do sindicato: ', IR,'%\n')
print ('Seu salario liquido eh: R$', salario)
print ('')