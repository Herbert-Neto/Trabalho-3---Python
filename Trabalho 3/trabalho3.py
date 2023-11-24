import csv
import pandas as pd
import matplotlib.pyplot as plt

diabeticos = []

def carrega_dados():
    with open('diabetes.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            diabeticos.append(linha)

def titulo(msg, traco="-"):
    print()
    print(msg)
    print(traco*40)

def resumo():
    titulo("Resumo dos Dados")

    dados = pd.read_csv('diabetes.csv')

    num = len(diabeticos)
    num_m_diabeticas = 0
    num_sem_diabetes = 0

    idade = dados['Age']

    idade_minima = idade.min()
    idade_maxima = idade.max()

    for diabete in diabeticos:
        if diabete ["Outcome"]:
            diabetico = int(diabete["Outcome"])
            if diabetico > 0:
                num_m_diabeticas += 1
            else:
                num_sem_diabetes += 1
    
    print(f"\nNº Mulheres: {num}")
    print(f"\n Nº Mulheres Diabéticas: {num_m_diabeticas}")
    print(f"\n Nº Mulheres Sem Diabetes: {num_sem_diabetes}")
    print(f"\n Faixa Etaria das Mulheres: {idade_minima} até {idade_maxima} anos")

def grafico_gestação():
    titulo("Gráfico Comparativo de Diabéticas por Gestação")
    
    ate2 = []
    entre3_5 = []
    entre6_8 = []
    acima8 = []
    

    for diabete in diabeticos:
        if diabete ["Outcome"] and diabete["Pregnancies"]:
            diabetico = int(diabete["Outcome"])
            gestação = int(diabete["Pregnancies"])
            if diabetico == 1 and gestação <= 2:
                ate2.append(gestação)
            elif diabetico == 1 and gestação >= 3 and gestação <= 5:
                entre3_5.append(gestação)
            elif diabetico == 1 and gestação >= 6 and gestação <= 8:
                entre6_8.append(gestação)
            else:
                acima8.append(gestação)

    dados = [len(ate2), len(entre3_5), len(entre6_8), len(acima8)]
    categorias = ['Até 2 gestações', 'Entre 3 e 5 gestações', 'Entre 6 e 8 gestações', 'Acima de 8 gestações']


    plt.pie(dados, labels=categorias, autopct='%1.1f%%', startangle=90)
    plt.title("Gráfico Comparativo de Diabéticas por Gestação")
    plt.show()


def grafico_taxa():
    titulo("Gráfico Comparativo de Taxas de Glicose")
    plt.title("Gráfico Comparativo de Taxas de Glicose")

    sem_até_99 = []
    com_até_99 = []

    sem_entre_100_130 = []
    com_entre_100_130 = []

    sem_entre_131_160 = []
    com_entre_131_160 = []
    
    sem_acima_160 = []
    com_acima_160 = []

    for diabete in diabeticos:
        if diabete ["Outcome"] and diabete["Glucose"]:
            diabetico = int(diabete["Outcome"])
            glicose = int(diabete["Glucose"])
            if diabetico == 0 and glicose <= 99:
                sem_até_99.append(glicose)
            elif diabetico == 0 and glicose >= 100 and glicose <= 130 :
                sem_entre_100_130.append(glicose)
            elif diabetico == 0 and glicose >= 131 and glicose <= 160:
                sem_entre_131_160.append(glicose)
            elif diabetico == 0 and glicose >= 161:
                sem_acima_160.append(glicose)
    for diabete in diabeticos:
        if diabete ["Outcome"] and diabete["Glucose"]:
            diabetico = int(diabete["Outcome"])
            glicose = int(diabete["Glucose"])
            if diabetico == 1 and glicose <= 99:
                com_até_99.append(glicose)
            elif diabetico == 1 and glicose >= 100 and glicose <= 130 :
                com_entre_100_130.append(glicose)
            elif diabetico == 1 and glicose >= 131 and glicose <= 160:
                com_entre_131_160.append(glicose)
            elif diabetico == 1 and glicose >= 161:
                com_acima_160.append(glicose)

    categorias = ['Até 99', 'Entre 100 e 130', 'Entre 131 e 160', 'Acima de 160']
    bar_width = 0.35
    r1 = range(len(categorias))
    r2 = [x + bar_width for x in r1]

    plt.bar(r1, [len(sem_até_99), len(sem_entre_100_130), len(sem_entre_131_160), len(sem_acima_160)],
            color='b', width=bar_width, edgecolor='grey', label='Não Diabéticas')
    plt.bar(r2, [len(com_até_99), len(com_entre_100_130), len(com_entre_131_160), len(com_acima_160)],
            color='g', width=bar_width, edgecolor='grey', label='Diabéticas')
    
    plt.xlabel('Taxa de Glicose')
    plt.ylabel('Número de Pessoas')
    plt.xticks([r + bar_width/2 for r in range(len(categorias))], categorias)

    plt.legend()
    plt.show()









carrega_dados()

while True:
    titulo("Estatisticas sobre Mulheres Diabeticas")
    print("1. Resumo dos Dados")
    print("2. Gráfico Comparativo de Diabéticas por Gestação")
    print("3. Gráfico Comparativo de Taxas de Glicose")
    print("4. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        resumo()
    elif opcao == 2:
        grafico_gestação()
    elif opcao == 3:
        grafico_taxa()
    else:
        break