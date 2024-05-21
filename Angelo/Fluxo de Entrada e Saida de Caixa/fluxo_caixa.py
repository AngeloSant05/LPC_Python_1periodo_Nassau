import openpyxl

book = openpyxl.Workbook()
Sheet = book['Sheet']
Sheet.title = 'Entrada_Saida'
fluxo = book['Entrada_Saida']

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
salario = ['','Salário',]
repo_estoque = ['','Repo Estoq',]
telefonia = ['','Telefonia',]
internet = ['','Internet',]
agua = ['','Água',]
energia = ['','Energia',]
aluguel = ['','Aluguel',]
vt = ['','VT',]
vr = ['', 'VR',]
investimentos = ['', 'Investimentos',]
saida_total = ['','Total Saída',]

# Saldo Final
saldo_final = ['','Saldo Final',]

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

# Declarando as compras a vista
for x in range(2, len(meses)):
    tot_vist = val_total[x] * porc_avista
    a_vista.append(tot_vist)
fluxo.append(a_vista)

# Declarando as compras parceladas em 1x
for x in range(2, len(meses)):
    if x < 3:
        d30.append(0)
    else:
        tot_d30 = val_total[x-1] * porc_d30
        d30.append(tot_d30)
fluxo.append(d30)

# Declarando as compras parceladas em 2x
for x in range(2, len(meses)):
    if x < 4:
        d60.append(0)
    else:
        tot_d60 = val_total[x-2] * porc_d60
        d60.append(tot_d60)
fluxo.append(d60)

fluxo.append([''])

# Somando o total para a agenda de recebíveis
for x in range(2, len(meses)):
    tot_rec = a_vista[x] + d30[x] + d60[x]
    recebiveis.append(tot_rec)
fluxo.append(recebiveis)


# Inserindo as saídas

fluxo.append([''])

# Declarando o valor do salário
for x in range(2, len(meses)):
    total = float(input(f"Digite qual o valor gasto com salários no mês de {meses[x]}: "))
    salario.append(total)
fluxo.append(salario)

# Declarando da reposição de estoque
for x in range(2, len(meses)):
    total = float(input(f"Digite qual o valor gasto com reposição de estoque no mês de {meses[x]}: "))
    repo_estoque.append(total)
fluxo.append(repo_estoque)

# Declarando o valor da telefonia
for x in range(2, len(meses)):
    total = float(input(f"Digite qual o valor gasto com telefonia no mês de {meses[x]}: "))
    telefonia.append(total)
fluxo.append(telefonia)

# Declarando o valor da internet
for x in range(2, len(meses)):
    total = float(input(f"Digite qual o valor gasto com internet no mês de {meses[x]}: "))
    internet.append(total)
fluxo.append(internet)

# Declarando o valor da água
for x in range(2, len(meses)):
    total = float(input(f"Digite qual o valor gasto com água no mês de {meses[x]}: "))
    agua.append(total)
fluxo.append(agua)

# Declarando o valor da energia
for x in range(2, len(meses)):
    total = float(input(f"Digite qual o valor gasto com energia no mês de {meses[x]}: "))
    energia.append(total)
fluxo.append(energia)

# Declarando o valor do aluguel
for x in range(2, len(meses)):
    total = float(input(f"Digite qual o valor gasto com aluguel no mês de {meses[x]}: "))
    aluguel.append(total)
fluxo.append(aluguel)

# Declarando o valor do VT
for x in range(2, len(meses)):
    total = float(input(f"Digite qual o valor gasto com VT no mês de {meses[x]}: "))
    vt.append(total)
fluxo.append(vt)

# Declarando o valor do VR
for x in range(2, len(meses)):
    total = float(input(f"Digite qual o valor gasto com VR no mês de {meses[x]}: "))
    vr.append(total)
fluxo.append(vr)

# Declarando o valor dos investimentos
for x in range(2, len(meses)):
    total = float(input(f"Digite qual o valor gasto com investimentos no mês de {meses[x]}: "))
    investimentos.append(total)
fluxo.append(investimentos)

# Somando o total de gastos
for x in range(2, len(meses)):
    total = (salario[x] + repo_estoque[x] + telefonia[x] + internet[x] + agua[x] + energia[x] + aluguel[x] +\
vt[x] + vr[x] + investimentos[x]) * -1
    saida_total.append(total)
fluxo.append(saida_total)

fluxo.append([''])

# Calculando o saldo final
for x in range(2, len(meses)):
    total = recebiveis[x] + saida_total[x]
    saldo_final.append(total)
fluxo.append(saldo_final)


# Salvando arquivo
book.save('Fluxo de caixa.xlsx')

# nome = input("Digite o nome que quer dar ao arquivo: ")
# book.save(nome+'.xlsx')
