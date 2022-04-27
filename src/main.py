# lib imports
import numpy as np
import statistics as sts
import pandas as pd

# file imports
import menus




# global variables

activity_labels = ["WALKING", "WALKING_UPSTAIRS", "WALKING_DOWNSTRAIRS", "SITTING", "STANDING", "LAYING",
                "STAND_TO_SIT", "SIT_TO_STAND", "SIT_TO_LIE", "LIE_TO_SIT", "STAND_TO_LIE", "LIE_TO_STAND"]
dynamic_activity_labels = ["WALKING", "WALKING_UPSTAIRS", "WALKING_DOWNSTRAIRS"]
static_activity_labels = ["SITTING", "STANDING", "LAYING"]
transition_activity_labels = ["STAND_TO_SIT", "SIT_TO_STAND", "SIT_TO_LIE", "LIE_TO_SIT", "STAND_TO_LIE", "LIE_TO_STAND"]


path_exp_data = "HAPT_Data_Set/RawData"
path_labels = "HAPT_Data_Set/RawData/labels.txt"

exp_data_files = ["acc_exp01_user01.txt", "acc_exp02_user01.txt", "acc_exp03_user02.txt", "acc_exp04_user02.txt",
            "acc_exp05_user03.txt", "acc_exp06_user03.txt", "acc_exp07_user04.txt", "acc_exp08_user04.txt"]



def main():

    print("Obtaiing data from txt files...")
    

    while True:

        menus.main_menu()
        option = int(input())

        if option == 1:
            print("\nPlotting all experiences...")

        elif option == 2:
            print("\nRecalculating all experiences...")

            

    return




def data(file):
    user_ex = []
    while True:
        file_line = file.readline()
        if not file_line:
            break
        array = file_line.rstrip().split(' ')
        user_ex.append(array)



user1, user2, user3, user4 = [], [], [], []

exemple = open(exp_data_files[0], "r")
user1.append(data(exemple))
exemple = open(exp_data_files[1], "r")
user1.append(data(exemple))
exemple = open(exp_data_files[2], "r")
user2.append(data(exemple))
exemple = open(exp_data_files[3], "r")
user2.append(data(exemple))
exemple = open(exp_data_files[4], "r")
user3.append(data(exemple))
exemple = open(exp_data_files[5], "r")
user3.append(data(exemple))
exemple = open(exp_data_files[6], "r")
user4.append(data(exemple))
exemple = open(exp_data_files[7], "r")
user4.append(data(exemple))
