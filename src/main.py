import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.signal import spectrogram
from scipy.fftpack import fft, fftshift

atividades = ["WALKING", "WALKING_UPSTAIRS", "WALKING_DOWNSTRAIRS", "SITTING", "STANDING", "LAYING",
			  "STAND_TO_SIT", "SIT_TO_STAND", "SIT_TO_LIE", "LIE_TO_SIT", "STAND_TO_LIE", "LIE_TO_STAND"]
atividades_dinamicas = ["WALKING", "WALKING_UPSTAIRS", "WALKING_DOWNSTRAIRS"]
atividades_estaticas = ["SITTING", "STANDING", "LAYING"]
atividades_transicao = ["STAND_TO_SIT", "SIT_TO_STAND", "SIT_TO_LIE", "LIE_TO_SIT", "STAND_TO_LIE", "LIE_TO_STAND"]


def normalize(arr, t_min, t_max):
	norm_arr = []
	diff = t_max - t_min
	diff_arr = max(arr) - min(arr)
	for i in arr:
		temp = (((i - min(arr)) * diff) / diff_arr) + t_min
		norm_arr.append(temp)
	print("normalize done")
	return norm_arr


def plot(matrix):
	arr = np.array([])
	fig, axs = plt.subplots(3)
	fig.suptitle('Signals')
	plt.figure(figsize=(200, 200))

	for i in matrix:
		arr = np.append(arr, i[0])
	stop = int((1 / 50) * arr.size)
	nelements = arr.size
	x = np.linspace(0, stop, nelements)
	y = normalize(arr, -1, 1)
	axs[0].plot(x, y, "red")
	axs[0].set_xlabel('time(min)')
	axs[0].set_ylabel('ACC_x')
	print("plot x done")

	for i in matrix:
		arr = np.append(arr, i[1])
	stop = int((1 / 50) * arr.size)
	nelements = arr.size
	x = np.linspace(0, stop, nelements)
	y = normalize(arr, -1, 1)
	axs[1].plot(x, y, "blue")
	axs[1].set_xlabel('time(min)')
	axs[1].set_ylabel('ACC_y')
	print("plot y done")

	for i in matrix:
		arr = np.append(arr, i[2])
	stop = int((1 / 50) * arr.size)
	nelements = arr.size
	x = np.linspace(0, stop, nelements)
	y = normalize(arr, -1, 1)
	axs[2].plot(x, y, "green")
	axs[2].set_xlabel('time(min)')
	axs[2].set_ylabel('ACC_z')
	print("plot z done")

	plt.show()


"----------------------------------------------------------------------------------------------------------------------"


def data(path_to_labels, path_to_exp):
	info_users = []
	info_labels = np.genfromtxt(path_to_labels, dtype=int)
	n_exp = 1
	n_user = 1
	for i in range(8):
		info_users.append(np.genfromtxt(path_to_exp + "0" + str(n_exp) + "_user" + "0" + str(n_user) + ".txt", dtype='float'))
		n_exp += 1
		if i % 2 == 1:
			n_user += 1
	return info_users, info_labels


def calculate_dft(segment, axis_x, axis_y, axis_z, size):
	window = signal.windows.boxcar(size)
	axis_x_detrended = signal.detrend(axis_x[segment[3]:segment[4]], type="constant")
	axis_y_detrended = signal.detrend(axis_y[segment[3]:segment[4]], type="constant")
	axis_z_detrended = signal.detrend(axis_z[segment[3]:segment[4]], type="constant")
	y = axis_x_detrended
	axis_x_fft_w = abs(fftshift(fft(np.multiply(y, window))))
	y = axis_y_detrended
	axis_y_fft_w = abs(fftshift(fft(np.multiply(y, window))))
	y = axis_z_detrended
	axis_z_fft_w = abs(fftshift(fft(np.multiply(y, window))))
	return axis_x_fft_w, axis_y_fft_w, axis_z_fft_w



def fourier_single(info_labels, label, info_user, n_exp, n_user):
	single_experience = []
	segment = []
	for lab in info_labels:
		if int(lab[0]) == n_exp and int(lab[1]) == n_user and int(lab[2]) - 1 == atividades.index(label):
			segment += [lab[0], lab[1], lab[2], lab[3], lab[4]]

			axis = list(zip(*info_user))
			axis_x, axis_y, axis_z = axis[0], axis[1], axis[2]

			fftx, ffty, fftz = calculate_dft(segment, axis_x, axis_y, axis_z, segment[4]-segment[3])

			segment += [fftx, ffty, fftz]
		single_experience += [segment]
	return single_experience


def plot_activity(experience):
	print(f"Plotting all activities of {experience[0][0]}_{experience[0][1]}")
	for i in range(len(experience)):
		fig, axs = plt.subplots(3)
		plt.figure()
		fig.set_figheight(5)
		fig.set_figwidth(10)
		fig.suptitle("DFT - " + atividades[experience[i][2] - 1] + "(" + str(experience[i][0]) + "_" + str(
			experience[i][1]) + ")")

		x = np.linspace(-25, 25, experience[i][4] - experience[i][3])

		axs[0].plot(x, experience[i][5], 'blue')
		axs[0].set_ylabel('axis_x')
		axs[0].set_xlim([0, 25])

		axs[1].plot(x, experience[i][6], 'orange')
		axs[1].set_ylabel('axis_y')
		axs[1].set_xlim([0, 25])

		axs[2].plot(x, experience[i][7], 'green')
		axs[2].set_xlabel('Frequency (Hz)')
		axs[2].set_ylabel('axis_z')
		axs[2].set_xlim([0, 25])

		plt.show()
	print("Plot successful!\n")



def get_window(option, size):
	if option.lower() == "rect":
		window_signal = signal.windows.boxcar(size)
	elif option.lower() == "triang":
		window_signal = signal.windows.triang(size)
	elif option.lower() == "gauss (size/5)":
		window_signal = signal.windows.gaussian(size, std=size / 5)
	elif option.lower() == "gauss (size/10)":
		window_signal = signal.windows.gaussian(size, std=size / 10)
	elif option.lower() == "gauss (size/2)":
		window_signal = signal.windows.gaussian(size, std=size / 2)
	elif option.lower() == "hamming":
		window_signal = signal.windows.hamming(size)
	else:
		window_signal = signal.windows.gaussian(size, std=size / 5)
		print("Wrong input: default value set")
	return window_signal



# Ve a tua função de calcular pq acho que da pra usar so esta e passar 
# a window_option como "rect" e tens a mesma função que ja tinhas e tens 
# opções
def calculate_dft(segment, axis_x, axis_y, axis_z, window_option):
	window = get_window(window_option, segment[4] - segment[3])
	
	axis_x_detrended = signal.detrend(axis_x[segment[3]:segment[4]], type="constant")
	axis_y_detrended = signal.detrend(axis_y[segment[3]:segment[4]], type="constant")
	axis_z_detrended = signal.detrend(axis_z[segment[3]:segment[4]], type="constant")
	
	y = axis_x_detrended
	axis_x_fft_w = abs(fftshift(fft(np.multiply(y, window))))
	y = axis_y_detrended
	axis_y_fft_w = abs(fftshift(fft(np.multiply(y, window))))
	y = axis_z_detrended
	axis_z_fft_w = abs(fftshift(fft(np.multiply(y, window))))
	return axis_x_fft_w, axis_y_fft_w, axis_z_fft_w



def calc_stft(info_user, n_exp, window_signal):
	if n_exp % 2 == 0:
		n_user = n_exp - 13
	else:
		n_user = n_exp - 13 - 1
	
	axis = list(zip(*info_user))
	axis_z = np.array(axis[2])
	fs = 50
	Tframe = 1.5
	Toverlap = 0.1
	Nframe = int(np.round(Tframe * fs))
	Noverlap = int(np.round(Toverlap * fs))


	f, t, Sxx = spectrogram(axis_z, fs, window=window_signal, nperseg=Nframe, noverlap=Noverlap, detrend='constant', mode='magnitude')
	plt.figure(figsize=(30, 8))
	plt.pcolormesh(t, f, Sxx, shading='gouraud', cmap='plasma')
	plt.colorbar()
	plt.ylabel('f [Hz]', fontweight="bold")
	plt.xlabel('t [s]', fontweight="bold")
	plt.title("acc_exp" + str(n_exp) + "_user" + str(n_user) + "\nno window", fontweight="bold")
	plt.show()





def main():

	# sacar a window certa
	window_signal = get_window(option, segment[4] - segment[3])
	
	# o dft nao muda nada mas eles querem , entao e so por os argumentos certos
	calculate_dft()

	# calcular o stft com o sinal que ja sacamos
	calc_stft(info_users[0], n_exp, window_signal)



users, labels = data("C:/Users/narig/OneDrive/Ambiente de Trabalho/ATD/ATD20212022-Projeto/Projeto Python/labels.txt", "C:/Users/narig/OneDrive/Ambiente de Trabalho/ATD/ATD20212022-Projeto/Projeto Python/acc_exp")
plot(list(zip(*users)))
"""
n_exp = 1
n_user = 1
label = "STANDING"
experience = fourier_single(info_labels, label, info_users[0], n_exp, n_user)
plot_activity(experience)
"""