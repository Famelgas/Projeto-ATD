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


data_dir = ["acc_exp01_user01.txt", "acc_exp01_user01.txt", "acc_exp02_user01.txt", "acc_exp02_user01.txt",
            "acc_exp03_user01.txt", "acc_exp03_user01.txt", "acc_exp04_user01.txt", "acc_exp04_user01.txt"]

user1, user2, user3, user4 = [], [], [], []

exemple = open(data_dir[0], "r")
user1.append(data(exemple))
exemple = open(data_dir[1], "r")
user1.append(data(exemple))
exemple = open(data_dir[2], "r")
user2.append(data(exemple))
exemple = open(data_dir[3], "r")
user2.append(data(exemple))
exemple = open(data_dir[4], "r")
user3.append(data(exemple))
exemple = open(data_dir[5], "r")
user3.append(data(exemple))
exemple = open(data_dir[6], "r")
user4.append(data(exemple))
exemple = open(data_dir[7], "r")
user4.append(data(exemple))