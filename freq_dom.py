## 4
import matplotlib.pyplot as plt
from pcdr import makeWave, make_fft_positive_freqs_only

maxTime = 2
samp_rate = 300 
timestamps, wave = makeWave(samp_rate, 10, "real", seconds=maxTime)
sample_freqs, fft_mag = make_fft_positive_freqs_only(wave, samp_rate)
plt.subplot(2, 1, 1, title="Time Domain")
plt.plot(timestamps, wave, "*-", markersize=5)
plt.subplot(2, 1, 2, title="Frequency Domain")
plt.plot(sample_freqs, fft_mag, '.g-')
plt.show()