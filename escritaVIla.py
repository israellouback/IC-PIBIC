import os

    #Escrita no arquivo configurado para Vila

def path_files(diretorio_atual,lista_arquivos):
    for root, dirs, files in os.walk(diretorio_atual):
        for filename in files:
            if filename.endswith(".idf"):
                file_path = os.path.join(root, filename)
                # Ler o arquivo em um DataFrame
                lista_arquivos .append(file_path)  #adiciona todos os arquivos csv do diretório numa lista

def escrita_arquivos(lista_arquivos,lista_pisos,lista_cob,lista_paredes_ext,lista_paredes_int,setup_porta,setup_janela):
    linha_i = "!-   ===========  ALL OBJECTS IN CLASS: CONSTRUCTION ==========="
    linha_f = "!-   ===========  ALL OBJECTS IN CLASS: GLOBALGEOMETRYRULES ==========="
    a = 0
    j = 0
    k = 0
    contador = 0
    for arquivos in lista_arquivos:  # para cada arquivo pertencente a lista de arquivos
        with open(arquivos, "r+") as arq:  # abre o arquivo modo leitura/escrita
            linhas = arq.readlines()  # armazena todas as linhas do arquivo
            for i, linha in enumerate(linhas):  # pegar linha inicial e final do campo que queremos alterar
                if linha_i in linha:
                    ind_i = i
                if linha_f in linha:
                    ind_f = i
            # manipula as os campos que queremos alterar
            linhas[ind_i + 1] = lista_cob[j]
            linhas[ind_i + 2] = setup_janela
            linhas[ind_i + 3] = lista_pisos[k]
            linhas[ind_i + 4] = lista_paredes_int[a]
            linhas[ind_i + 5] = lista_paredes_ext[a]
            linhas[ind_i + 6] = lista_lajes[j]
            linhas[ind_i + 7] = setup_porta
            linhas[ind_i + 8] = linha_f
            for l in range(ind_i + 9, ind_f + 1):
                linhas[l] = ' ' + '\n'
            # verifica o valor de alguns indices para manter o controle das instancias
            if a == len(lista_paredes_int) - 1 and j == len(lista_cob) - 1 and k == len(lista_pisos) - 1:
                break;
            elif k == len(lista_pisos) - 1 and j == len(lista_cob) - 1:
                a += 1
                k = 0
                j = 0
            elif k == len(lista_cob) - 1:
                k = 0
                j += 1
            else:
                k += 1
            # reabre o arquivo para  escrever todos o conteudo com os campos alterados
            with open(arquivos, "w") as arq:
                arq.writelines(linhas)
               # os.rename(arquivos, 'instancia' + str(contador) + ".idf")
                contador += 1

    #INTERNAS
parede_1 = ('Construction,' +'\n'
                'Paredeinterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'Reboco1,                 !- Layer 2'+'\n'
                'BlocoCeramico1e2,        !- Layer 3'+'\n'
                'Reboco1,                 !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_2 =('Construction,' +'\n'
                'Paredeinterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'Reboco2e10e14,           !- Layer 2'+'\n'
                'BlocoCeramico1e2,        !- Layer 3'+'\n'
                'Reboco2e10e14,           !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_10 =('Construction,' +'\n'
                'Paredeinterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'Reboco2e10e14,           !- Layer 2'+'\n'
                'BlocoCeramico10e11e34,   !- Layer 3'+'\n'
                'Reboco2e10e14,           !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_11 =('Construction,' +'\n'
                'Paredeinterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'Reboco11,                !- Layer 2'+'\n'
                'BlocoCeramico10e11e34,   !- Layer 3'+'\n'
                'Reboco11,                !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_14 =('Construction,' +'\n'
                'Paredeinterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'Reboco2e10e14,           !- Layer 2'+'\n'
                'BlocoCeramico14,         !- Layer 3'+'\n'
                'Reboco2e10e14,           !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_28 =('Construction,' +'\n'
                'Paredeinterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'Reboco28,                !- Layer 2'+'\n'
                'BlocoConcreto28,         !- Layer 3'+'\n'
                'Reboco28,                !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_33 =('Construction,' +'\n'
                'Paredeinterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'BlocoCeramico33,         !- Layer 2'+'\n'
                'Pintura branca;          !- Layer 3'+'\n'+'\n')

parede_34 =('Construction,' +'\n'
                'Paredeinterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'BlocoCeramico10e11e34,   !- Layer 2'+'\n'
                'Pintura branca;          !- Layer 3'+'\n'+'\n')

parede_36int =('Construction,' +'\n'
                'Paredeinterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'PainelGesso36,           !- Layer 2'+'\n'
                'ref_camara_ar_cob,       !- Layer 3'+'\n'
                'PainelGesso36,           !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_39int =('Construction,' +'\n'
                'Paredeinterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'OBS,                     !- Layer 2'+'\n'
                'LaVidro,                 !- Layer 3'+'\n'
                'OBS,                     !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')


#EXTERNAS
parede_1ext = ('Construction,' +'\n'
                'Paredeexterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'Reboco1,                 !- Layer 2'+'\n'
                'BlocoCeramico1e2,        !- Layer 3'+'\n'
                'Reboco1,                 !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_2ext =('Construction,' +'\n'
                'Paredeexterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'Reboco2e10e14,           !- Layer 2'+'\n'
                'BlocoCeramico1e2,        !- Layer 3'+'\n'
                'Reboco2e10e14,           !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_10ext =('Construction,' +'\n'
                'Paredeexterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'Reboco2e10e14,           !- Layer 2'+'\n'
                'BlocoCeramico10e11e34,   !- Layer 3'+'\n'
                'Reboco2e10e14,           !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_11ext =('Construction,' +'\n'
                'Paredeexterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'Reboco11,                !- Layer 2'+'\n'
                'BlocoCeramico10e11e34,   !- Layer 3'+'\n'
                'Reboco11,                !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_14ext =('Construction,' +'\n'
                'Paredeexterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'Reboco2e10e14,           !- Layer 2'+'\n'
                'BlocoCeramico14,         !- Layer 3'+'\n'
                'Reboco2e10e14,           !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_28ext =('Construction,' +'\n'
                'Paredeexterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'Reboco28,                !- Layer 2'+'\n'
                'BlocoConcreto28,         !- Layer 3'+'\n'
                'Reboco28,                !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_33ext =('Construction,' +'\n'
                'Paredeexterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'BlocoCeramico33,         !- Layer 2'+'\n'
                'Pintura branca;          !- Layer 3'+'\n'+'\n')

parede_34ext =('Construction,' +'\n'
                'Paredeexterna,           !- Name'+'\n'
                'Pintura branca,          !- Outside Layer'+'\n'
                'BlocoCeramico10e11e34,   !- Layer 2'+'\n'
                'Pintura branca;          !- Layer 3'+'\n'+'\n')
parede_36ext =('Construction,' +'\n'
                'Paredeexterna,           !- Name'+'\n'
                'Pintura externa,         !- Outside Layer'+'\n'
                'Placa36e39,              !- Layer 2'+'\n'
                'ref_camara_ar_cob,       !- Layer 3'+'\n'
                'PainelGesso36,           !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')

parede_39ext =('Construction,' +'\n'
                'Paredeexterna,           !- Name'+'\n'
                'Pintura externa,         !- Outside Layer'+'\n'
                'Placa36e39,              !- Layer 2'+'\n'
                'LaVidro,                 !- Layer 3'+'\n'
                'OBS,                     !- Layer 4'+'\n'
                'Pintura branca;          !- Layer 5'+'\n'+'\n')
        #Telhados

cob_1 =('Construction,' +'\n'
           'Telhado,                !- Name'+'\n'
           'RebocoCob,              !- Outside Layer'+'\n'
           'LajeConcreto,           !- Layer 2'+'\n'
           'Impermeabilizante;      !- Layer 3'+'\n'+'\n')

cob_2 =('Construction,' +'\n'
           'Telhado,                !- Name'+'\n'
           'RebocoCob,              !- Outside Layer'+'\n'
           'LajeTrelicada2e5,       !- Layer 2'+'\n'
           'Impermeabilizante;      !- Layer 3'+'\n'+'\n')

cob_3 =('Construction,' +'\n'
           'Telhado,                !- Name'+'\n'
           'RebocoCob,              !- Outside Layer'+'\n'
           'LajeTrelicada3,         !- Layer 2'+'\n'
           'Impermeabilizante;      !- Layer 3'+'\n'+'\n')

cob_4 =('Construction,' +'\n'
           'Telhado,                !- Name'+'\n'
           'RebocoCob,              !- Outside Layer'+'\n'
           'LajeConcreto,           !- Layer 2'+'\n'
           'ref_camara_ar_cob,      !- Layer 3'+'\n'
           'TelhaCeramica;          !- Layer 4'+'\n'+'\n')

cob_5 =('Construction,' +'\n'
           'Telhado,                !- Name'+'\n'
           'RebocoCob,              !- Outside Layer'+'\n'
           'LajeTrelicada2e5,       !- Layer 2'+'\n'
           'ref_camara_ar_cob,      !- Layer 3'+'\n'
           'TelhaCeramica;          !- Layer 4'+'\n'+'\n')

cob_101 =('Construction,' +'\n'
           'Telhado,                !- Name'+'\n'
           'ForroMadeira,           !- Outside Layer'+'\n'
           'ref_camara_ar_cob,      !- Layer 2'+'\n'
           'TelhaConcreto;          !- Layer 3'+'\n'+'\n')

cob_102 =('Construction,' +'\n'
           'Telhado,                !- Name'+'\n'
           'ForroMadeira,           !- Outside Layer'+'\n'
           'ref_camara_ar_cob,      !- Layer 2'+'\n'
           'TelhaFibrocimento;      !- Layer 3'+'\n'+'\n')

cob_103 =('Construction,' +'\n'
           'Telhado,                !- Name'+'\n'
           'ForroMadeira,           !- Outside Layer'+'\n'
           'ref_camara_ar_cob,      !- Layer 2'+'\n'
           'MantaTermAcCob,         !- Layer 3'+'\n'
           'TelhaCeramica;          !- Layer 4'+'\n'+'\n')

cob_104 =('Construction,' +'\n'
           'Telhado,                !- Name'+'\n'
           'ForroMadeira,           !- Outside Layer'+'\n'
           'ref_camara_ar_cob,      !- Layer 2'+'\n'
           'MantaTermAcCob,         !- Layer 3'+'\n'
           'TelhaConcreto;          !- Layer 4'+'\n'+'\n')

cob_105 =('Construction,' +'\n'
           'Telhado,                !- Name'+'\n'
           'ForroMadeira,           !- Outside Layer'+'\n'
           'ref_camara_ar_cob,      !- Layer 2'+'\n'
           'MantaTermAcCob,         !- Layer 3'+'\n'
           'TelhaFibrocimento;      !- Layer 4'+'\n'+'\n')

# Lajes
laje_1 =('Construction,' +'\n'
          'Laje,                    !- Name'+'\n'
           'RebocoCob,              !- Outside Layer'+'\n'
           'LajeConcreto,           !- Layer 2'+'\n'
           'Impermeabilizante;      !- Layer 3'+'\n'+'\n')

laje_2 =('Construction,' +'\n'
          'Laje,                    !- Name'+'\n'
           'RebocoCob,              !- Outside Layer'+'\n'
           'LajeTrelicada2e5,       !- Layer 2'+'\n'
           'Impermeabilizante;      !- Layer 3'+'\n'+'\n')

laje_3 =('Construction,' +'\n'
          'Laje,                    !- Name'+'\n'
           'RebocoCob,              !- Outside Layer'+'\n'
           'LajeTrelicada3,         !- Layer 2'+'\n'
           'Impermeabilizante;      !- Layer 3'+'\n'+'\n')

laje_4 =('Construction,' +'\n'
          'Laje,                    !- Name'+'\n'
           'RebocoCob,              !- Outside Layer'+'\n'
           'LajeConcreto,           !- Layer 2'+'\n'
           'ref_camara_ar_cob,      !- Layer 3'+'\n'
           'TelhaCeramica;          !- Layer 4'+'\n'+'\n')

laje_5 =('Construction,' +'\n'
          'Laje,                    !- Name'+'\n'
           'RebocoCob,              !- Outside Layer'+'\n'
           'LajeTrelicada2e5,       !- Layer 2'+'\n'
           'ref_camara_ar_cob,      !- Layer 3'+'\n'
           'TelhaCeramica;          !- Layer 4'+'\n'+'\n')

laje_101 =('Construction,' +'\n'
          'Laje,                    !- Name'+'\n'
           'ForroMadeira,           !- Outside Layer'+'\n'
           'ref_camara_ar_cob,      !- Layer 2'+'\n'
           'TelhaConcreto;          !- Layer 3'+'\n'+'\n')

laje_102 =('Construction,' +'\n'
          'Laje,                    !- Name'+'\n'
           'ForroMadeira,           !- Outside Layer'+'\n'
           'ref_camara_ar_cob,      !- Layer 2'+'\n'
           'TelhaFibrocimento;      !- Layer 3'+'\n'+'\n')

laje_103 =('Construction,' +'\n'
          'Laje,                    !- Name'+'\n'
           'ForroMadeira,           !- Outside Layer'+'\n'
           'ref_camara_ar_cob,      !- Layer 2'+'\n'
           'MantaTermAcCob,         !- Layer 3'+'\n'
           'TelhaCeramica;          !- Layer 4'+'\n'+'\n')

laje_104 =('Construction,' +'\n'
          'Laje,                    !- Name'+'\n'
           'ForroMadeira,           !- Outside Layer'+'\n'
           'ref_camara_ar_cob,      !- Layer 2'+'\n'
           'MantaTermAcCob,         !- Layer 3'+'\n'
           'TelhaConcreto;          !- Layer 4'+'\n'+'\n')

laje_105 =('Construction,' +'\n'
          'Laje,                    !- Name'+'\n'
           'ForroMadeira,           !- Outside Layer'+'\n'
           'ref_camara_ar_cob,      !- Layer 2'+'\n'
           'MantaTermAcCob,         !- Layer 3'+'\n'
           'TelhaFibrocimento;      !- Layer 4'+'\n'+'\n')

        #Pisos

piso_2 =('Construction,' +'\n'
                'Piso,                    !- Name'+'\n'
                'Contrapiso,              !- Outside Layer'+'\n'
                'TacoMadeira;             !- Layer 2'+'\n'+'\n' )

piso_5 =('Construction,' +'\n'
                'Piso,                    !- Name'+'\n'
                'Contrapiso,              !- Outside Layer'+'\n'
                'MadeiraLaminada;         !- Layer 2'+'\n'+'\n' )

piso_7 =('Construction,' +'\n'
                'Piso,                    !- Name'+'\n'
                'Contrapiso,              !- Outside Layer'+'\n'
                'Carpete;                 !- Layer 2'+'\n'+'\n' )

piso_10 =('Construction,' +'\n'
                'Piso,                    !- Name'+'\n'
                'Laje,                    !- Outside Layer'+'\n'
                'Contrapiso,              !- Layer 2'+'\n'
                'Vinil;                   !- Layer 3'+'\n'+'\n' )

piso_14 =('Construction,' +'\n'
               'Piso,                    !- Name'+'\n'
                'Laje,                    !- Outside Layer'+'\n'
                'Contrapiso,              !- Layer 2'+'\n'
                'Carpete;                 !- Layer 3'+'\n'+'\n' )

piso_16 =('Construction,' +'\n'
                'Piso,                    !- Name'+'\n'
                'Laje,                    !- Outside Layer'+'\n'
                'MantaTermAcPiso,         !- Layer 2'+'\n'
                'Contrapiso,              !- Layer 3'+'\n'
                'TacoMadeira;             !- Layer 4'+'\n'+'\n')

piso_18 =('Construction,' +'\n'
                'Piso,                    !- Name'+'\n'
                'Laje,                    !- Outside Layer'+'\n'
                'MantaTermAcPiso,         !- Layer 2'+'\n'
                'Contrapiso,              !- Layer 3'+'\n'
                'Cimento;                 !- Layer 4'+'\n'+'\n')

piso_19 =('Construction,' +'\n'
                'Piso,                    !- Name'+'\n'
                'Laje,                    !- Outside Layer'+'\n'
                'MantaTermAcPiso,         !- Layer 2'+'\n'
                'Contrapiso,              !- Layer 3'+'\n'
                'MadeiraLaminada;         !- Layer 4'+'\n'+'\n')

piso_20 =('Construction,' +'\n'
                'Piso,                    !- Name'+'\n'
                'Laje,                    !- Outside Layer'+'\n'
                'MantaTermAcPiso,         !- Layer 2'+'\n'
                'Contrapiso,              !- Layer 3'+'\n'
                'ArgamassaPiso            !- Layer 4'+'\n'
                'Granito;                 !- Layer 5'+'\n'+'\n')

piso_21 =('Construction,' +'\n'
                'Piso,                    !- Name'+'\n'
                'Laje,                    !- Outside Layer'+'\n'
                'MantaTermAcPiso,         !- Layer 2'+'\n'
                'Contrapiso,              !- Layer 3'+'\n'
                'Carpete;                 !- Layer 4'+'\n'+'\n')

      # Setup janela
setup_janela = ('Construction,' +'\n'
                'Janela,                  !- Name'+'\n'
                'ref_vidro;               !- Outside Layer'+'\n'+'\n')

        # Setup porta
setup_porta = ('Construction,' +'\n'
            'Porta,                   !- Name'+'\n'
            'Compensado;              !- Outside Layer'+'\n'+'\n' )

# Listas
lista_paredes_int = [parede_1,parede_2,parede_10,parede_11,parede_14,parede_28,parede_33,parede_34,parede_36int,parede_39int]
lista_paredes_ext =[parede_1ext,parede_2ext,parede_10ext,parede_11ext,parede_14ext,parede_28ext,parede_33ext,parede_34ext,parede_36ext,parede_39ext]
lista_pisos = [piso_2,piso_5,piso_7,piso_10,piso_14,piso_16,piso_18,piso_19,piso_20,piso_21]
lista_cob = [cob_1,cob_2,cob_3,cob_4,cob_5,cob_101,cob_102,cob_103,cob_104,cob_105]
lista_lajes = [laje_1,laje_2,laje_3,laje_4,laje_5,laje_101,laje_102,laje_103,laje_104,laje_105]

diretorio_atual = 'D:\IC\prototipo16000\Vila GH\Teste' #trocar diretorio
lista_arquivos = []

path_files(diretorio_atual, lista_arquivos)
escrita_arquivos(lista_arquivos, lista_pisos, lista_cob, lista_paredes_ext, lista_paredes_int, setup_porta, setup_janela)