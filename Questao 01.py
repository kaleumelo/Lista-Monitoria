salario= float( input('Quanto voce ganha por hora?: '))
horas = float(input('E quantas horas trabalhou no mes ?: '))

salario_bruto = salario * horas

INSS = salario_bruto * 0.08

sindicato = salario_bruto * 0.05  

salario_liquido = salario_bruto - (INSS + sindicato)

print('Seu salario bruto eh: R$ ',salario_bruto)
print('A porcentagem para o INSS eh: R$ ', INSS)
print('A porcentagem para o Sindicato eh: R$ ', sindicato)
print('Seu salario liquido eh: R$ ', salario_liquido)
