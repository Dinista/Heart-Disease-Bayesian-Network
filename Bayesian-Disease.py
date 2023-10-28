import pandas as pd
import numpy as np
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination


    
def Menu(model, dataset):
    
    visited = []
    op = "s"
    querysel = []
    evidence = None
    
    # Cenarios
    
    print("\nDefina o cenário a partir de uma ou mais evidencias:")
    
    options = [ "Dor no peito (cp)",
                "Frequencia cardica (thalach)",
                "Pico do eletrocardiograma (slope)",
                "Resultados eletrocardiograficos em repouso (Restecgn)", 
                "Calcular probabilidade"]

    while op == 's' or op == 'S':
        for (i, item) in enumerate(options, start=1):
            if i in visited:
                continue
            print(" ",i,": ",item)
        
        sel = int(input())
        if sel in visited:
            sel = 0

        # ---------- CP selecionado ---------

        if sel == 1:
            evidence = "cp"
            print("\nSelecione o tipo de dor no peito:\n",
            "1: angina típica\n",
            "2: angina atípica\n",
            "3: dor não anginosa\n",
            "4: assintomático\n")
            
            cptype = int(input())
            
            if cptype in dataset.cp.unique():
                visited.append(sel)
                querysel.append([evidence,cptype])
            else:
                print("Entrada inválida.")

        # ---------- Thalach selecionado ---------
        
        elif sel == 2:
            evidence = "thalach"
            print("\nAVISO: O sistema depende da base de dados, caso o valor não exista na base,",
            "não é possível calcular a propabilidade.\nVerifique os valores disponíveis.")
            input("\nPressione enter para continuar...\n")
            print("\n Dados disponíveis: ", dataset.thalach.unique(),"\n")
            print("Indique a frequência cardíaca máxima alcançada pelo paciente:")
            
            maxim = int(input())
            if maxim in dataset.thalach.unique():
                visited.append(sel)
                querysel.append([evidence,maxim])
            else:
                print("Frequencia não encontrada na base de dados.")
        
        # ---------- Slope selecionado ---------

        elif sel == 3:
            evidence = "slope"
            print("\nSelecione a inclinação do pico do eletrocardiograma:\n",
            "1: ascendente\n",
            "2: plano\n",
            "3: descendente\n")
            slopval = int(input())
            
            if slopval in dataset.slope.unique():
                visited.append(sel)
                querysel.append([evidence,slopval])
            else:
                print("Entrada inválida.")
        
        # ---------- Restecg selecionado ---------

        elif sel == 4:
            evidence = "restecg"
            print("\nSelecione o resultado eletrocardiográficos de repouso:\n", 
            "0: normal\n",
            "1: Anormalidade nas ondas do exame.\n",
            "2: Mostrando provável hipertrofia ventricular\n")
            restval = int(input())
            if restval in dataset.restecg.unique():
                visited.append(4)
                querysel.append([evidence,restval])
            else:
                print("Entrada inválida.")

        elif sel == 5:

            if (evidence == None):
                print("Nenhuma evidencia foi fornecida para o calculo de probabilidade.\n A probabilidade será calculada de acordo com a base de dados")
                # input("\nPressione enter para continuar...\n")
            else:
                print("\nCALCULANDO PROBABILIDADE:\n")
                tabela(model, querysel)
                return

         # ---------- Erro ---------

        else:
            print("Entrada inválida.")
        
        print("\nContinuar? (s/n) Selecione (n) para calcular a probabilidade.")
        op = input()
        
        if not(op == 's' or op == "S"):
            print("\nCALCULANDO PROBABILIDADE:\n")
            tabela(model, querysel, dataset)

# Aplicando o modelo e criando e mostrando a tabela de probabilidade

def tabela(model, vals, dataset):
    prob_Doenca = VariableElimination(model)
    mostra_cenario(vals)
    print("\n")
    size = len(vals)
    flag = ['doencaCardiaca']
    if size == 1:
        mostra_tabela(model, flag, {vals[0][0]: vals[0][1]}, vals, dataset)
    elif size == 2:
        mostra_tabela(model, flag, {vals[0][0]: vals[0][1], vals[1][0]: vals[1][1]}, vals, dataset)
    elif size == 3:
        mostra_tabela(model, flag, {vals[0][0]: vals[0][1], vals[1][0]: vals[1][1], vals[2][0]: vals[2][1]}, vals, dataset)
    elif size == 4:
        mostra_tabela(model, flag, {vals[0][0]: vals[0][1], vals[1][0]: vals[1][1], vals[2][0]: vals[2][1], vals[3][0]: vals[3][1]}, vals, dataset)
    else:        
        mostra_tabela(model, flag, {}, vals, dataset)
        
        

def mostra_tabela(model, flag, evidencia, vals, dataset):
    if evidencia != {}:
        mostra_info(vals, dataset)
    else:
        acaso_n_cardioca = (dataset['doencaCardiaca'] == 0).sum()
        acaso_cardioca = (dataset['doencaCardiaca'] == 1).sum()
        
        print("Base de dados, doençaCardiaca = 0: " + str(acaso_n_cardioca))
        print("Base de dados, doençaCardiaca = 1: " + str(acaso_cardioca))
        print("Base de dados, Total: " + str(acaso_n_cardioca + acaso_cardioca))

        
    prob_Doenca = VariableElimination(model)    
    print(prob_Doenca.query(flag, evidence=evidencia, show_progress=False))

def mostra_info(vals, dataset):
    tamanho = len(vals)
    if tamanho == 1:    
        satisfaz_doenca = ((dataset[vals[0][0]] == vals[0][1]) & (dataset['doencaCardiaca'] == 1)).sum()
        n_satisfaz_doenca = ((dataset[vals[0][0]] == vals[0][1]) & (dataset['doencaCardiaca'] == 0)).sum()        
    elif tamanho == 2: 
        satisfaz_doenca = ((dataset[vals[0][0]] == vals[0][1]) & (dataset[vals[1][0]] == vals[1][1]) & (dataset['doencaCardiaca'] == 1)).sum()
        n_satisfaz_doenca = ((dataset[vals[0][0]] == vals[0][1]) & (dataset[vals[1][0]] == vals[1][1]) & (dataset['doencaCardiaca'] == 0)).sum()
    
    elif tamanho == 3: 
        satisfaz_doenca = ((dataset[vals[0][0]] == vals[0][1]) & (dataset[vals[1][0]] == vals[1][1]) & (dataset[vals[2][0]] == vals[2][1]) &  (dataset['doencaCardiaca'] == 1)).sum()
        n_satisfaz_doenca = ((dataset[vals[0][0]] == vals[0][1]) & (dataset[vals[1][0]] == vals[1][1]) & (dataset[vals[2][0]] == vals[2][1]) &  (dataset['doencaCardiaca'] == 0)).sum()
    else:
        satisfaz_doenca = ((dataset[vals[0][0]] == vals[0][1]) & (dataset[vals[1][0]] == vals[1][1]) & (dataset[vals[2][0]] == vals[2][1]) & (dataset[vals[3][0]] == vals[3][1]) & (dataset['doencaCardiaca'] == 1)).sum()
        n_satisfaz_doenca = ((dataset[vals[0][0]] == vals[0][1]) & (dataset[vals[1][0]] == vals[1][1]) & (dataset[vals[2][0]] == vals[2][1]) & (dataset[vals[3][0]] == vals[3][1]) & (dataset['doencaCardiaca'] == 0)).sum()

    total_doenca = satisfaz_doenca + n_satisfaz_doenca

    print("Base de dados, doençaCardiaca = 0: " + str(n_satisfaz_doenca))
    print("Base de dados, doençaCardiaca = 1: " + str(satisfaz_doenca))
    print("Base de dados, Total: " + str(total_doenca))

def mostra_cenario(vals):
    
    print('Considerando:\n')
    
    if vals == []:
        print('Nenhuma evidencia foi fornecida!')        
    else:
        for (a, b) in vals:
            if a == 'cp':
                if b == 1:
                    print('- Dor no peito angina típica.')
                if b == 2:
                    print('- Dor no peito angina atípica.')
                if b == 3:
                    print('- Dor no peito não anginosa.')
                if b == 4:
                    print('- Paciente assintomático.')
            
            if a == 'thalach':
                print('- Frequência cardíaca máxima de', b,'.')
            
            if a == 'slope':
                if b == 1:
                    print("- Inclinação ascendente do pico do eletrocardiograma.")
                if b == 2:
                    print("- Inclinação plana do pico do eletrocardiograma.")
                if b == 3:
                    print("- Inclinação descendente do pico do eletrocardiograma")
            
            if a == 'restecg':
                if b == 0:
                    print ("- Eletrocardiográficos de repouso normais.")
                if b == 1:
                    print('- Eletrocardiográficos de repouso com ondas anormais.')
                if b == 2:
                    print('- Eletrocardiográficos de repouso mostrando hipertrofia ventricular.')
                


def main():
    #   Cabecalho
    print("\nREDE BAYESIANA - DOENÇAS CARDÍACAS")
    
    #   Carregando dataset
    dataset = pd.read_csv("heart-die.csv", encoding='utf-8')

    #   Criando cenario
    cenario = [('doencaCardiaca','cp'),('doencaCardiaca','thalach'),
    ('doencaCardiaca','slope'),('doencaCardiaca','restecg')]

    #   Criando modelo bayesiano
    model = BayesianNetwork(cenario)
    model.fit(dataset, estimator=BayesianEstimator)


    #   Menu
    op = 'n'
    
    while op == 'n' or op == 'N':
        Menu(model, dataset)
        print("\nSair? (s/n)\n")
        op = input()

    print("\nSaindo...\n")


if __name__ == "__main__":
    main()
