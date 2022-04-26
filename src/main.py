atividades = ["WALKING", "WALKING_UPSTAIRS", "WALKING_DOWNSTRAIRS", "SITTING", "STANDING", "LAYING",
              "STAND_TO_SIT", "SIT_TO_STAND", "SIT_TO_LIE", "LIE_TO_SIT", "STAND_TO_LIE", "LIE_TO_STAND"]
atividades_dinamicas = ["WALKING", "WALKING_UPSTAIRS", "WALKING_DOWNSTRAIRS"]
atividades_estaticas = ["SITTING", "STANDING", "LAYING"]
atividades_transicao = ["STAND_TO_SIT", "SIT_TO_STAND", "SIT_TO_LIE", "LIE_TO_SIT", "STAND_TO_LIE", "LIE_TO_STAND"]


def data(file):
    user_ex = []
    while True:
        file_line = file.readline()
        if not file_line:
            break
        array = file_line.rstrip().split(' ')
        user_ex.append(array)


data_dir = [
    "C:/Users/narig/OneDrive/Ambiente de Trabalho/ATD/ATD20212022-Projeto/HAPT_Data_Set/Nossos RawData/acc_exp01_user01.txt",
    "C:/Users/narig/OneDrive/Ambiente de Trabalho/ATD/ATD20212022-Projeto/HAPT_Data_Set/Nossos RawData/acc_exp01_user01.txt",
    "C:/Users/narig/OneDrive/Ambiente de Trabalho/ATD/ATD20212022-Projeto/HAPT_Data_Set/Nossos RawData/acc_exp02_user01.txt",
    "C:/Users/narig/OneDrive/Ambiente de Trabalho/ATD/ATD20212022-Projeto/HAPT_Data_Set/Nossos RawData/acc_exp02_user01.txt",
    "C:/Users/narig/OneDrive/Ambiente de Trabalho/ATD/ATD20212022-Projeto/HAPT_Data_Set/Nossos RawData/acc_exp03_user01.txt",
    "C:/Users/narig/OneDrive/Ambiente de Trabalho/ATD/ATD20212022-Projeto/HAPT_Data_Set/Nossos RawData/acc_exp03_user01.txt",
    "C:/Users/narig/OneDrive/Ambiente de Trabalho/ATD/ATD20212022-Projeto/HAPT_Data_Set/Nossos RawData/acc_exp04_user01.txt",
    "C:/Users/narig/OneDrive/Ambiente de Trabalho/ATD/ATD20212022-Projeto/HAPT_Data_Set/Nossos RawData/acc_exp04_user01.txt"]