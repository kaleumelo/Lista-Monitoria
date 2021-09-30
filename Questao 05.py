lista_prestacao = []
lista_valor_pago = []
prestacoes_pagas = 0
def valorpagamento(valor_prestacao, numero_dias):
    Vpm = valor_prestacao * 1.03
    valor_com_taxa = round(Vpm *((1 + 0.001) ** numero_dias), 2)
    lista_valor_pago.append(valor_com_taxa)
    print('Valor corrigido:', valor_com_taxa)
    global prestacoes_pagas
    prestacoes_pagas += 1
    lista_prestacao.append(prestacoes_pagas)

while True:
    valor_prestacao = float(input('Digite o valor da prestação: (0 para sair)\n '))
    if valor_prestacao == 0:
       break
    numero_dias = int(input('Quantos dias que está em atraso: '))
    valorpagamento(valor_prestacao, numero_dias)
print('Quantidade de prestações pagas: ', prestacoes_pagas)
print('Valor total de prestações pagas no dia: R$', round(sum(lista_valor_pago)), 2)