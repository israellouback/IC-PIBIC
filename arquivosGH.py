import pandas as pd
import os

    # Obtencao do Graus-Hora Atual e Graus-Hora nas semanas críticas de verão e inverno.

#Constantes para definição do setpoint
TEMP_INICIAL = 18
TEMP_FINAL = 26
def path_files(diretorio_atual,lista_arquivos):
    for root, dirs, files in os.walk(diretorio_atual):
        for filename in files:
            if filename.endswith(".csv"):
                file_path = os.path.join(root, filename)
                # Ler o arquivo em um DataFrame
                lista_arquivos .append(file_path)  #adiciona todos os arquivos csv do diretório numa lista
def interval_setpoint(gh,valores_gh): #Calcula diferenca de temperatura para o setpoint
  if(gh < TEMP_INICIAL):
    gh = TEMP_INICIAL - gh
  elif(gh > TEMP_FINAL):
    gh = gh - TEMP_FINAL
  valores_gh.append(gh)

def loopGH(gh_room):
  valores_gh = []
  res = 0
  for i in gh_room:
    interval_setpoint(i,valores_gh)
    res = sum(valores_gh)
  return res


#Obtem graus-hora das semana critica de verao / inverno
def gh_semana_critica(lista_arquivos):
    # Para
    for arquivos in lista_arquivos:
        #leitura dos arquivos
        dados= pd.read_csv(arquivos)
    #dados

        passo = 24  # Intervalo de iteração de 1 a 24
        inicio = 0  # Início da iteração
        fim = 0

        while fim < 8759:
            fim = inicio + 167   # +1 para incluir a linha atual
            #print(f"Iteração {inicio } a {fim}")
            valores = dados['Environment:Site Outdoor Air Drybulb Temperature [C](Hourly)'].iloc[inicio:fim]
            temp_total = valores.sum()
            dados.loc[inicio,'SomaTempTotal']= temp_total #preencher inicio do intervalo com a soma dos valores
            dados.loc[fim,'SomaTempTotal']= temp_total     #preencher o fim o intervalo com a soma dos valores
            inicio += passo

        for indice,row in dados.iterrows():
            maior_temp = dados['SomaTempTotal'].max()
            novos_dados = dados[dados['SomaTempTotal'] == maior_temp]
        inicio=novos_dados.iloc[0] #instancia inicial
        final=novos_dados.iloc[1] #instancia final
        first_day = novos_dados.index[novos_dados.index.get_loc(inicio.name)]
        last_day  = novos_dados.index[novos_dados.index.get_loc(final.name)]
        novos_dados = dados.iloc[first_day:last_day + 1]

        for i in dados:
          #MIN -> semana critica de inverno
          # MAX -> semana critica de verao
          a = dados['ZONA1:Zone Operative Temperature [C](Hourly)'].min()
          b=  dados['ZONA2:Zone Operative Temperature [C](Hourly)'].min()
          c=  dados['ZONA3:Zone Operative Temperature [C](Hourly)'].min()

          ghZ1_sala = (novos_dados['ZONA1:Zone Operative Temperature [C](Hourly)'] <  TEMP_INICIAL) | (novos_dados['ZONA1:Zone Operative Temperature [C](Hourly)'] >  TEMP_FINAL)
          ghZ2_quarto1 =(novos_dados['ZONA2:Zone Operative Temperature [C](Hourly)']<  TEMP_INICIAL) | (novos_dados['ZONA2:Zone Operative Temperature [C](Hourly)']>  TEMP_FINAL)
          ghZ3_quarto2 = (novos_dados['ZONA3:Zone Operative Temperature [C](Hourly)']<  TEMP_INICIAL)| (novos_dados['ZONA3:Zone Operative Temperature [C](Hourly)'] >  TEMP_FINAL)
          gh_sala=novos_dados.loc[ghZ1_sala,'ZONA1:Zone Operative Temperature [C](Hourly)']
          gh_q1=novos_dados.loc[ghZ2_quarto1,'ZONA2:Zone Operative Temperature [C](Hourly)']
          gh_q2=novos_dados.loc[ghZ3_quarto2,'ZONA3:Zone Operative Temperature [C](Hourly)']

          sala=loopGH(gh_sala)
          quarto1=loopGH(gh_q1)
          quarto2=loopGH(gh_q2)

        # Pegar o maximo (critico) entre os 3 comodos
        ghFinal = min(sala,quarto1,quarto2)
        print(ghFinal, arquivos)


def gh_atual(lista_arquivos):
  for arquivos in lista_arquivos:
    #leitura dos arquivos
    dados= pd.read_csv(arquivos)
    #Cálculo de graus-horas para cada comodo
    ghZ1_sala = (dados['ZONA1:Zone Operative Temperature [C](Hourly)'] < TEMP_INICIAL ) | (dados['ZONA1:Zone Operative Temperature [C](Hourly)'] > TEMP_FINAL)
    ghZ2_quarto1 =(dados['ZONA2:Zone Operative Temperature [C](Hourly)']< TEMP_INICIAL) | (dados['ZONA2:Zone Operative Temperature [C](Hourly)']> TEMP_FINAL)
    ghZ3_quarto2 = (dados['ZONA3:Zone Operative Temperature [C](Hourly)']< TEMP_INICIAL)| (dados['ZONA3:Zone Operative Temperature [C](Hourly)'] > TEMP_FINAL)
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
gh_semana_critica(lista_arquivos)