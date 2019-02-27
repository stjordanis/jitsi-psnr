#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
import sys

# This is assumed to be the *capture* frame rate, so each frame duration is
# 1/FRAMERATE.

FRAMERATE = 30/1000
DURATION = 1/FRAMERATE

df = pd.read_csv(sys.stdin, index_col='frameno')

time = 0
times = []
durations = []

for i in range(len(df)):
    times.append(time)
    time += DURATION

    if i < 1 or df.loc[i, 'seqno'] != df.loc[i + 1, 'seqno']:
        durations.append(DURATION)
    else:
        durations.append(durations[i-1] + DURATION)

df['time'] = times
df['duration'] = durations

print(df.describe())
df.plot(x='time',y=['psnr', 'duration'], subplots=True)
plt.show()
