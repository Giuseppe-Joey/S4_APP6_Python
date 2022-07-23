

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from zplane import zplane
from code_exemple_guide_etudiant import code_exemple_guide_etudiant

import time

def probleme_1(fe: float):
    """
    ProblÃ¨me 1: Filtre IIR elliptique
    """

    # Filter specifications
    fc_low: float = 900
    fc_high: float = 1100
    filter_order: int = 2
    pass_band_ripple_db: float = 1
    stop_band_attn_db: float = 40

    # Filter coefficients
    [b, a] = signal.ellip(
        N=filter_order,
        rp=pass_band_ripple_db,
        rs=stop_band_attn_db,
        Wn=[fc_low, fc_high],
        fs=fe,
        btype="bandpass",
        output="ba",
    )

    # Frequency response
    [w, h_dft] = signal.freqz(b, a, worN=10000, fs=fe)
    plt.figure()
    plt.semilogx(w, 20 * np.log10(np.abs(h_dft)))
    plt.title(f"RÃ©ponse en frÃ©quence du filtre elliptique (ordre {filter_order})")
    plt.xlabel("FrÃ©quence [Hz]")
    plt.ylabel("Gain [dB]")
    plt.grid(which="both", axis="both")
    plt.tight_layout()
    # plt.show()



    # probleme 2
    # plt.figure()
    # zplane(b,a)
    # plt.show()

    # probleme 3
    N = 1000

    # plt.figure()
    # imp = signal.unit_impulse(N)
    # plt.title("impulsion de dirac")
    # plt.plot(imp)
    # plt.show()



    # filter = signal.lfilter(b,a,imp)

    # plt.figure()
    # plt.title("reponse impulsionnelle")
    # plt.plot(filter)
    # plt.show()


    # --------------------
    # BON POUR LA PROBLEMATIQUE
    # --------------------
    #on commence par multiplier par 2 a la y
    # puis on arrondi
    # on devra re diviser par 2 a la y pour SOSfreqZ


    # plt.figure()
    #code_exemple_guide_etudiant()
    # plt.show()



    # probleme 4
    # Filter coefficients
    # Filter coefficients
    sos = signal.ellip(
        N=filter_order,
        rp=pass_band_ripple_db,
        rs=stop_band_attn_db,
        Wn=[fc_low, fc_high],
        fs=fe,
        btype="bandpass",
        output="sos",
    )

    # Frequency response
    [w, h_dft] = signal.sosfreqz(sos, worN=10000, fs=fe)
    [w1, h_dft1] = signal.sosfreqz(np.round(sos * (2 ** 13)) / (2 ** 13), worN=10000, fs=fe)
    # [w2, h_dft2] = signal.sosfreqz(np.round(b * (2 ** 13)) / (2 ** 13), np.round(a * (2 ** 13)) / (2 ** 13), worN=10000, fs=fe)

    plt.figure()
    plt.semilogx(w, 20 * np.log10(np.abs(h_dft)))
    plt.semilogx(w1, 20 * np.log10(np.abs(h_dft1)))
    plt.title(f"RÃ©ponse en frÃ©quence du filtre elliptique (ordre {filter_order})")
    plt.xlabel("FrÃ©quence [Hz]")
    plt.ylabel("Gain [dB]")
    plt.grid(which="both", axis="both")
    plt.tight_layout()
    plt.show()






    # probleme 5













def laboratoire():
    # plt.ion()  # Comment out if using scientific mode!

    fe = 20000

    probleme_1(fe)
    print("Done!")







if __name__ == "__main__":

    laboratoire()


