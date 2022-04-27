def main_menu():
	print("Choose an option:\n"
	      "1. Plot all experiences\n"
	      "2. Re-calculate all experiences' DFT\n"
	      "3. Re-calculate single experience DFT\n"
	      "4. Plot single experience DFT\n"
	      "5. Get important features\n"
	      "6. Step calculation - frequency with biggest magnitude\n"
	      "7. Sensibility and specificity\n"
	      "8. Calculate STFT\n"
	      "9. Exit\n")


def single_dft_menu():
	print("input: <n_exp> <n_user> <label> <window>")


def all_dft_menu():
	print("input: <window>")


def experience_menu():
	print("input: <experience> (between 26 and 33)")


def feature_model_menu():
	print("1: Get features by single activity\n2: Get features by type\n")