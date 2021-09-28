salario_horas= float( input('Quanto voce ganha por hora ?\n '))
horas = float(input('E quantas horas trabalhou no mes ?\n'))
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
print ('Esses sao todos os descontos que fazemos no seu salario:\n','Porcentagem do sindicato: ',sindicato,'%',', que seria em reais: R$',calculo_sindicato,'\n'
'Porcentagem do FGTS: ', FGTS,'%',', que seria em reais: R$',calculo_fgts,'\n','Porcentagem do Imposto de Renda: ', IR,'%',', que seria em reais: R$',calculo_ir,'\n')
print ('Seu salario liquido eh em torno de: R$', salario)