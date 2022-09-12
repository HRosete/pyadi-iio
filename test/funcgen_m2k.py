import matplotlib
import numpy as np
import wave, math

from matplotlib import pyplot as plt
# Variables
freq = 20000 # frequency of first sine wave
sRate = 2*freq # sample rate in Hertz
amplitude1 = 1 # amplitude of first wave
numPeriods = 1 # number of periods of the sine waves
numSamples = sRate * numPeriods # total number of samples

# Graphing helper function
def setup_graph(title='', x_label='', y_label='', fig_size=None):
    fig = plt.figure()
    if fig_size != None:
        fig.set_size_inches(fig_size[0], fig_size[1])
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
# Create the x axis from 0 to numPeriods, divided into numSamples samples.
x = np.linspace(0, numPeriods, numSamples)
print(len(x))

f1 = lambda x: amplitude1*np.sin(freq*2*np.pi*x)
sampled_f1 = [f1(i) for i in x]
print(len(sampled_f1))

fig = plt.figure()
fig.set_size_inches(12,6)
plt.subplots_adjust(hspace=1)

plt.subplot(311)
plt.plot(x, sampled_f1)
plt.title('Sine wave 50Hz')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude [arbitrary]')
plt.xlim(0, 1)
plt.ylim(-15, 15)
plt.show()

fft_output = np.fft.rfft(sampled_f1)
magnitude = [np.sqrt(i.real**2+i.imag**2)/len(fft_output) for i in fft_output]
frequencies = [(i*1.0/numSamples)*sRate for i in range(numSamples//2+1)]

setup_graph(x_label='frequency [Hz]', y_label='amplitude [arbitrary]', 
            title='Frequency Domain', fig_size=(12,6))
plt.xlim(40,60)
plt.plot(frequencies, magnitude, 'r')
plt.show()

len(sampled_f1)
len(magnitude)
len(frequencies)

