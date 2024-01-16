import pandas as pd
import os

    # Obtencao do Graus-Hora Atual e Graus-Hora nas semanas críticas de verão e inverno.

def path_files(diretorio_atual,lista_arquivos):
    for root, dirs, files in os.walk(diretorio_atual):
        for filename in files:
            if filename.endswith(".csv"):
                file_path = os.path.join(root, filename)
                # Ler o arquivo em um DataFrame
                lista_arquivos .append(file_path)  #adiciona todos os arquivos csv do diretório numa lista
def interval_setpoint(gh,valores_gh): #Calcula diferenca de temperatura para o setpoint
  if(gh < 18):
    gh = 18 - gh
  elif(gh > 26):
    gh = gh - 26
  valores_gh.append(gh)

def loopGH(gh_room,):
  valores_gh = []
  res = 0
  for i in gh_room:
    interval_setpoint(i,valores_gh)
    res = sum(valores_gh)
  return res

def gh_atual(lista_arquivos):
  for arquivos in lista_arquivos:
    #leitura dos arquivos
    dados= pd.read_csv(arquivos)
    #Cálculo de graus-horas para cada comodo
    ghZ1_sala = (dados['ZONA1:Zone Operative Temperature [C](Hourly)'] < 18 ) | (dados['ZONA1:Zone Operative Temperature [C](Hourly)'] > 26)
    ghZ2_quarto1 =(dados['ZONA2:Zone Operative Temperature [C](Hourly)']< 18) | (dados['ZONA2:Zone Operative Temperature [C](Hourly)']> 26)
    ghZ3_quarto2 = (dados['ZONA3:Zone Operative Temperature [C](Hourly)']< 18)| (dados['ZONA3:Zone Operative Temperature [C](Hourly)'] > 26)
    gh_sala=dados.loc[ghZ1_sala,'ZONA1:Zone Operative Temperature [C](Hourly)']
    gh_q1=dados.loc[ghZ2_quarto1,'ZONA2:Zone Operative Temperature [C](Hourly)']
    gh_q2=dados.loc[ghZ3_quarto2,'ZONA3:Zone Operative Temperature [C](Hourly)']

    sala=loopGH(gh_sala)
    quarto1=loopGH(gh_q1)
    quarto2=loopGH(gh_q2)

    #Pegar o maximo (critico) entre os 3 comodos
    ghFinal = max(sala,quarto1,quarto2)
    with open('vilaGH.txt','a') as arq:
        arq.write(str(ghFinal) + ' ')
        arq.write(arquivos + '\n')

diretorio_atual = 'D:\IC\prototipo16000\Vila GH\lstima'
lista_arquivos = []
path_files(diretorio_atual,lista_arquivos)
gh_atual(lista_arquivos)