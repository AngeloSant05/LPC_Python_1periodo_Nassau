import openpyxl

book = openpyxl.Workbook()
Sheet = book['Sheet']
Sheet.title = 'Entrada_Saida'
fluxo = book['Entrada_Saida']
'''
# Entradas
qtd_meses = 0
meses = ['','',]
val_total = ['','Total',]
a_vista = ['','A vista',]
porc_avista = 0
d30 = ['','D+30',]
porc_d30 = 0
d60 = ['','D+60',]
porc_d60 = 0
recebiveis = ['','Agnd Rec',]

# Saídas
salario = []
repo_estoque = []
telefonia = []
internet = ['','Internet']
agua = ['','Água',]
energia = ['','Energia',]
aluguel = ['','Aluguel',]
vt = ['','VT',]
vr = ['', 'VR',]
investimentos = ['', 'Investimentos',]
saida_total = ['','Total Saída',]

# Saldo Final
saldo_final = []

# Inserindo os meses
qtd_meses = int(input("Quantos meses digita fazer o fluxo de caixa: "))
for x in range(qtd_meses):
    mes = input("Digite o mês (3 digitos): ")
    meses.append(mes)
fluxo.append(meses)

# Inserindo as entradas

# Definindo os valores totais
fluxo.append(['Entrada'])
for x in range(2, len(meses)):
    total = float(input(f"Digite o valor total recebido em {meses[x]}: "))
    val_total.append(total)
fluxo.append(val_total)

# Definindo as porcentagens
porc_avista = float(input("Quanto porcento dessas vendas foram a vista? "))
porc_avista /= 100
porc_d30 = float(input("Quanto porcento dessas vendas foram parceladas em 1x? "))
porc_d30 /= 100
porc_d60 = float(input("Quanto porcento dessas vendas foram parceladas em 2x? "))
porc_d60 /= 100

# Agenda de recebíveis
for x in range(2, len(meses)):
    tot_vist = val_total[x] * porc_avista
    a_vista.append(tot_vist)
fluxo.append(a_vista)

for x in range(2, len(meses)):
    if x < 3:
        d30.append(0)
    else:
        tot_d30 = val_total[x-1] * porc_d30
        d30.append(tot_d30)
fluxo.append(d30)

for x in range(2, len(meses)):
    if x < 4:
        d60.append(0)
    else:
        tot_d60 = val_total[x-2] * porc_d60
        d60.append(tot_d60)
fluxo.append(d60)

fluxo.append([''])

for x in range(2, len(meses)):
    tot_rec = a_vista[x] + d30[x] + d60[x]
    recebiveis.append(tot_rec)
fluxo.append(recebiveis)




'''
nome = input("Digite o nome que quer dar ao arquivo: ")
# Salvando arquivo
book.save(nome+'.xlsx')
