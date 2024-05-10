## 6
## Try this.
import matplotlib.pyplot as plt
from pcdr import makeWave, make_fft_positive_freqs_only

maxTime = 2
samp_rate = 300
timestamps, wave1 = makeWave(samp_rate, 2, "real", seconds=maxTime)
timestamps, wave2 = makeWave(samp_rate, 25, "real", seconds=maxTime)
added = wave1 + wave2
sample_freqs, fft_mag = make_fft_positive_freqs_only(added, samp_rate)
plt.subplot(2, 1, 1, title="Time Domain")
plt.plot(timestamps, added, "*-", markersize=5)
plt.subplot(2, 1, 2, title="Frequency Domain")
plt.plot(sample_freqs, fft_mag, '.g-')
plt.tight_layout()
plt.show()