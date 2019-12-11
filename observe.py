import os
import sys
import datetime
from time import sleep

print('\n======================================================================================')
sleep(0.3)
print('VIRGO: An easy-to-use spectrometer & radiometer for Radio Astronomy based on GNU Radio')
sleep(0.3)
print('======================================================================================\n')
sleep(1)
print('[*] Please enter your desired observation parameters...\n')
sleep(0.5)

#Input observation parameters
f_center = str(input('Center frequency [MHz]: '))
f_center = str(float(f_center)*10**6)
bandwidth = str(input('Bandwidth [MHz]: '))
bandwidth = str(float(bandwidth)*10**6)
channels = str(input('Number of channels (FFT size): '))
t_int = str(input('Integration time per FFT sample [sec]: '))
nbins = str(int(float(t_int) * float(bandwidth)/float(channels)))
duration = str(input('Observing duration [sec]: '))

#Calibration option
cal = str(raw_input('\nWould you like to produce a calibrated spectrum at the end of your observation (requires off_nchan.dat calibration reference file in directory)? [y/N]: '))
yes = {'y', 'ye', 'yes'}
if cal.lower() in yes:
    cal = True
else:
    cal = False

#Delete pre-existing observation.dat & plot.png files
try:
    os.remove('observation.dat')
    os.remove('plot.png')
except OSError:
    pass

#Note current datetime
currentDT = datetime.datetime.now()
obsDT = currentDT.strftime('%Y-%m-%d %H:%M:%S')
print('\n[+] Starting observation at ' + obsDT + ' (local computer time)...')

#Execute top_block.py with parameters
sys.argv = ['top_block.py', '--c-freq='+f_center, '--samp-rate='+bandwidth, '--nchan='+channels, '--nbin='+nbins, '--obs-time='+duration]
execfile('top_block.py')

print('[!] Observation finished! Plotting data...')

#Execute plotter
if cal:
    sys.argv = ['plot_cal.py', 'freq='+f_center, 'samp_rate='+bandwidth, 'nchan='+channels, 'nbin='+nbins]
    execfile('plot_hi.py')
else:
    sys.argv = ['plot.py', 'freq='+f_center, 'samp_rate='+bandwidth, 'nchan='+channels, 'nbin='+nbins]
    execfile('plot.py')

print('\n======================================================================================')
print('[+] The observation data has been plotted and saved as plot.png.')
print('======================================================================================')
