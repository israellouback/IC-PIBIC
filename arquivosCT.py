import pandas as pd
import os

     #Obtencao da Carga termica Atual e Carga Termica Atual nos hórarios de Pico.


def path_files(diretorio_atual,lista_arquivos):
    for root, dirs, files in os.walk(diretorio_atual):
        for filename in files:
            if filename.endswith(".csv"):
                file_path = os.path.join(root, filename)
                # Ler o arquivo em um DataFrame
                lista_arquivos .append(file_path)  #adiciona todos os arquivos csv do diretório numa lista
def calculo_ct(dados): #Cálculo da Carga Térmica Total (Resfriamento e Aquecimento) de todos os cômodos
    ct_atual = dados['DORM1 IDEAL LOADS AIR SYSTEM:Zone Ideal Loads Zone Total Cooling Energy [J](Hourly)'].sum() + \
               dados['DORM2 IDEAL LOADS AIR SYSTEM:Zone Ideal Loads Zone Total Cooling Energy [J](Hourly)'].sum() + \
               dados['DORM1 IDEAL LOADS AIR SYSTEM:Zone Ideal Loads Zone Total Heating Energy [J](Hourly)'].sum() + \
               dados['DORM2 IDEAL LOADS AIR SYSTEM:Zone Ideal Loads Zone Total Heating Energy [J](Hourly)'].sum() + \
               dados['SALA IDEAL LOADS AIR SYSTEM:Zone Ideal Loads Zone Total Cooling Energy [J](Hourly) '].sum() + \
               dados['SALA IDEAL LOADS AIR SYSTEM:Zone Ideal Loads Zone Total Heating Energy [J](Hourly)'].sum()
    ct_atual = ct_atual * 2.77778e-7  # Conversao J para KWh

    return ct_atual
def ct_atual(lista_arquivos): #Carga termica atual
    for arquivos in lista_arquivos:
        # print(arquivos)
        dados = pd.read_csv(arquivos)
        ct_atual = calculo_ct(dados)
        with open('adrianoCT.txt', 'a') as arq:
            arq.write(str(ct_atual) + ' ')
            arq.write(arquivos + '\n')
def ct_pico_atual(lista_arquivos): #Carga termica atual nos hórarios de pico.
    for arquivos in lista_arquivos:
       dados= pd.read_csv(arquivos)
       dados[['Date','Time']] = dados['Date/Time'].str.split('  ',n=1,expand=True)
       dados = dados.drop('Date/Time',axis=1)
       # horario de pico (17-21)
       novos_dados = dados[(dados['Time'] == '17:00:00') | (dados['Time'] == '18:00:00') | (dados['Time'] == '19:00:00') | (dados['Time'] == '20:00:00') | (dados['Time'] == '21:00:00')]
       ct_atual = calculo_ct(novos_dados)
       with open('adrianoCT_pico_atual', 'a') as arq:
         arq.write(str(ct_atual) + ' ')
         arq.write(arquivos + '\n')

diretorio_atual = 'D:\IC\prototipo16000\Adriano CT\csvs'
lista_arquivos = []
path_files(diretorio_atual,lista_arquivos)
ct_atual(lista_arquivos)
ct_pico_atual(lista_arquivos)