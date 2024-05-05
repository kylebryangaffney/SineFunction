import soundfile as sf
import numpy as np
import scipy.signal as signal


A = 0.25
f = 300
f_s = 44100
phi_0 = 0

## build a numpy array for the time which creates 3 seconds of 44100 samples each -- n/f_s
t = np.arange(0, 3, 1/f_s) 

## build the new actual array 
## using the Time array as the indecies in the new array using the  
sine_wave = A * np.sin(2 * np.pi * f * t + phi_0)

## actually write the sine wave 
sf.write('sine_wave.wav', sine_wave, f_s)