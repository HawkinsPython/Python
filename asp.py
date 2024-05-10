## 1
## Try this example, which plots a 2 Hz wave and a 25 Hz wave.
## Notice that we're only plotting the sum of the waves.
## Can you still distinguish the two separate frequencies?
import matplotlib.pyplot as plt
from pcdr import makeWave

seconds = 2
samp_rate = 300
timestamps, wave1 = makeWave(samp_rate, 2, "real", seconds=seconds)
timestamps, wave2 = makeWave(samp_rate, 25, "real", seconds=seconds)
added =  wave1 + wave2
plt.plot(timestamps, added, "*-", markersize=5)
plt.show()


## 2
## Copy and modify the previous example.
## Change the first wave's frequency to 3 Hz.
## Can you still distinguish the two waves?


## 3
## Copy and modify the previous example.
## Change the first wave's frequency to 11 Hz.
## Notice that distinguishing the two waves is more difficult.