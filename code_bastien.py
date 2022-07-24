import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

#données pour les 5 filtres FIR
fe = 20000
N = 256

#Filtre passe-bas
fc_pb = 500

#Filtres passe-bande
fc1 = 500
fc2 = 1500
fc3 = 2500
fc4 = 4500

#Filtre passe-haut
fc_ph = 4490

# calculating the X axis range
rangeXaxis = np.arange(N)
Xaxis = (rangeXaxis*fe/N)-fe/2


h1 = signal.firwin(N, fc_pb, window='blackman', fs=fe, pass_zero='lowpass')
H1 = np.fft.fft(h1)
print(H1)

h2 = signal.firwin(N, [fc1, fc2], window='blackman', fs=fe, pass_zero='bandpass')
H2 = np.fft.fft(h2)

h3 = signal.firwin(N, [fc2, fc3], window='blackman', fs=fe, pass_zero='bandpass')
H3 = np.fft.fft(h3)

h4 = signal.firwin(N, [fc3, fc4], window='blackman', fs=fe, pass_zero='bandpass')
H4 = np.fft.fft(h4)

# h5 = signal.firwin(N, [fc_ph, fe/2-1], window='blackman', fs=fe, pass_zero='bandpass')
# H5 = np.fft.fft(h5)

h5 = signal.firwin(N, [fc_ph,(fe/2)-1], window='blackman', fs=fe, pass_zero=False)
H5 = np.fft.fft(h5)




plt.figure()
plt.title("Filtres")
plt.xlabel("Fréquence(Hz)")
plt.ylabel("Amplitude (linéaire)")
plt.plot(Xaxis, np.fft.fftshift(np.abs(H1)), label='H1')
plt.plot(Xaxis, np.fft.fftshift(np.abs(H2)), label='H2')
plt.plot(Xaxis, np.fft.fftshift(np.abs(H3)), label='H3')
plt.plot(Xaxis, np.fft.fftshift(np.abs(H4)), label='H4')
plt.plot(Xaxis, np.fft.fftshift(np.abs(H5)), label='H5')

plt.legend()
# plt.show()









plt.figure()
plt.title("Sommes des Filtres")
plt.xlabel("Fréquence(Hz)")
plt.ylabel("Amplitude (linéaire)")
H_somme = H1 + H2 + H3 + H4 + H5
# plt.plot(Xaxis, np.fft.fftshift(H_somme), label='H_somme')
plt.plot(Xaxis, np.fft.fftshift(np.abs(H_somme)), label='H_somme')
plt.show()






#
# plt.figure()
# plt.title("Filtres")
# plt.xlabel("Fréquence(Hz)")
# plt.ylabel("Amplitude (linéaire)")
# plt.subplot(2,1,1)
# Xaxis = np.arange(fe/2)
# plt.plot(Xaxis, np.fft.fftshift(np.abs(H1)), label='H1')
# plt.plot(Xaxis, np.fft.fftshift(np.abs(H2)), label='H2')
# plt.plot(Xaxis, np.fft.fftshift(np.abs(H3)), label='H3')
# plt.plot(Xaxis, np.fft.fftshift(np.abs(H4)), label='H4')
# plt.plot(Xaxis, np.fft.fftshift(np.abs(H5)), label='H5')
# plt.legend()
# plt.show()




