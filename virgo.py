import os
import sys
import datetime
import numpy as np
from time import sleep

#matplotlib.use('Agg') # If you run into display/rendering errors, please try uncommenting this line

def observe(dev_args='', frequency=1420e6, bandwidth=2e6, rf_gain=10, if_gain=20, bb_gain=20, channels=1024, duration=60, t_sample=1, out_file='observation.dat', start_in=0):
	from run_observation import run_observation

	# Schedule observation
	if start_in != 0:
		print('[*] The observation will begin in '+str(start_in)+' sec automatically. Please wait...\n')
	sleep(t_sample)

	# Delete pre-existing observation file
	try:
		os.remove(out_file)
	except OSError:
		pass

	# Note current datetime
	currentDT = datetime.datetime.now()
	obsDT = currentDT.strftime('%Y-%m-%d %H:%M:%S')
	print('\n[+] Starting observation at ' + obsDT + ' (local machine time)...\n')

	# Run observation
	observation = run_observation(dev_args=dev_args, frequency=frequency, bandwidth=bandwidth, rf_gain=rf_gain,
                                  if_gain=if_gain, bb_gain=bb_gain, channels=channels,
								  duration=duration, t_sample=t_sample, out_file=out_file)
	observation.start()
	observation.wait()
	print('\n[!] Data acquisition complete. Observation saved as: '+out_file)

def plot(frequency, bandwidth, channels, t_sample, n=0, m=0, f_rest=0, dB=False, in_file='observation.dat', cal_file='', plot_file='plot.png'):
	import matplotlib
	import matplotlib.pyplot as plt
	from matplotlib.gridspec import GridSpec

	plt.rcParams['legend.fontsize'] = 14
	plt.rcParams['axes.labelsize'] = 14
	plt.rcParams['axes.titlesize'] = 18
	plt.rcParams['xtick.labelsize'] = 12
	plt.rcParams['ytick.labelsize'] = 12

	def SNR(spectrum, mask=np.array([])):
		"""Signal-to-Noise Ratio estimator, with optional masking.
		If mask not given, then all channels will be used to estimate noise
		(will drastically underestimate S:N - not robust to outliers!)"""

		if mask.size == 0:
			mask = np.zeros_like(spectrum)

		noise = np.std((spectrum[2:]-spectrum[:-2])[mask[1:-1] == 0])/np.sqrt(2)
		background = np.nanmean(spectrum[mask == 0])

		return (spectrum-background)/noise

	def decibel(x):
		if dB: return 10.0*np.log10(x)
		return x

	left_velocity_edge = -299792.458*(bandwidth-2*frequency+2*f_rest)/(bandwidth-2*frequency)
	right_velocity_edge = 299792.458*(-bandwidth-2*frequency+2*f_rest)/(bandwidth+2*frequency)

	# Transform sampling time to number of bins
	bins = int(t_sample*bandwidth/channels)

	# Load observation & calibration data
	offset = 10000
	waterfall = offset*np.fromfile(in_file, dtype='float32').reshape(-1, channels)/bins

	if cal_file != '': waterfall_cal = offset*np.fromfile(cal_file, dtype='float32').reshape(-1, channels)/bins

	# Compute average specta
	avg_spectrum = decibel(np.mean(waterfall, axis=0))
	if cal_file != '': avg_spectrum_cal = decibel(np.nanmean(waterfall_cal, axis=0))

	# Define array for Time Series plot
	power = decibel(np.mean(waterfall, axis=1))

	# Number of sub-integrations
	subs = waterfall.shape[0]

	# Compute Time axis
	t = t_sample*np.arange(subs)

	# Compute Frequency axis; convert Hz to MHz
	frequency = np.linspace(frequency-0.5*bandwidth, frequency+0.5*bandwidth, channels, endpoint=False)*1e-6

	# Apply Mask
	mask = np.zeros_like(avg_spectrum)
	mask[np.logical_and(frequency > f_rest*1e-6-0.2, frequency < f_rest*1e-6+0.8)] = 1 # Margins OK for galactic HI

	# Define text offset for axvline text label
	text_offset = 0

	# Calibrate Spectrum
	if cal_file != '':
		if dB:
			spectrum = 10**((avg_spectrum-avg_spectrum_cal)/10)
		else:
			spectrum = avg_spectrum/avg_spectrum_cal

		# Mitigate RFI (Frequency Domain)
		if n != 0:
			spectrum_clean = SNR(spectrum.copy(), mask)
			for i in range(0, int(channels)):
				spectrum_clean[i] = np.median(spectrum_clean[i:i+n])

		# Apply offset for the Spectral Line label
		text_offset = 70

	# Mitigate RFI (Time Domain)
	if m != 0:
		power_clean = power.copy()
		for i in range(0, int(subs)):
			power_clean[i] = np.median(power_clean[i:i+m])

	# Initialize plot
	if cal_file != '':
		fig = plt.figure(figsize=(27,15))
		gs = GridSpec(2,3)
	else:
		fig = plt.figure(figsize=(21,15))
		gs = GridSpec(2,2)

	# Plot Average Spectrum
	ax1 = fig.add_subplot(gs[0,0])
	ax1.plot(frequency, avg_spectrum)
	ax1.set_xlim(np.min(frequency), np.max(frequency))
	ax1.ticklabel_format(useOffset=False)
	ax1.set_xlabel('Frequency (MHz)')
	if dB:
		ax1.set_ylabel('Relative Power (dB)')
	else:
		ax1.set_ylabel('Relative Power')
	if f_rest != 0:
		ax1.set_title('Average Spectrum\n')
	else:
		ax1.set_title('Average Spectrum')
	ax1.grid()

	if f_rest != 0:
		# Add secondary axis for Relative Velocity
		ax1_secondary = ax1.twiny()
		ax1_secondary.set_xlabel('Relative Velocity (km/s)', labelpad=5)
		ax1_secondary.axvline(x=0, color='brown', linestyle='--', linewidth=2, zorder=0)
		ax1_secondary.annotate('Spectral Line\nRest Frequency', xy=(470-text_offset, 5), xycoords='axes points', size=14, ha='left', va='bottom', color='brown')
		ax1_secondary.set_xlim(left_velocity_edge, right_velocity_edge)
		ax1_secondary.tick_params(axis='x', direction='in', pad=-22)

	#Plot Calibrated Spectrum
	if cal_file != '':
		ax2 = fig.add_subplot(gs[0,1])
		ax2.plot(frequency, SNR(spectrum, mask), label='Raw Spectrum')
		if n != 0:
			ax2.plot(frequency, spectrum_clean, label='Median (n = '+str(n)+')')
		ax2.set_xlim(np.min(frequency), np.max(frequency))
		ax2.ticklabel_format(useOffset=False)
		ax2.set_xlabel('Frequency (MHz)')
		ax2.set_ylabel('Signal-to-Noise Ratio (S/N)')
		if f_rest != 0:
			ax2.set_title('Calibrated Spectrum\n')
		else:
			ax2.set_title('Calibrated Spectrum')
		if n != 0:
			ax2.legend(bbox_to_anchor=(0.002, 0.96), loc='upper left')
		ax2.grid()

		if f_rest != 0:
			# Add secondary axis for Relative Velocity
			ax2_secondary = ax2.twiny()
			ax2_secondary.set_xlabel('Relative Velocity (km/s)', labelpad=5)
			ax2_secondary.axvline(x=0, color='brown', linestyle='--', linewidth=2, zorder=0)
			ax2_secondary.annotate('Spectral Line\nRest Frequency', xy=(400, 5), xycoords='axes points', size=14, ha='left', va='bottom', color='brown')
			ax2_secondary.set_xlim(left_velocity_edge, right_velocity_edge)
			ax2_secondary.tick_params(axis='x', direction='in', pad=-22)

	# Plot Dynamic Spectrum
	if cal_file != '':
		ax3 = fig.add_subplot(gs[0,2])
	else:
		ax3 = fig.add_subplot(gs[0,1])
	ax3.imshow(decibel(waterfall), origin='lower', interpolation='None', aspect='auto',
               extent=[np.min(frequency), np.max(frequency), np.min(t), np.max(t)])
	ax3.ticklabel_format(useOffset=False)
	ax3.set_xlabel('Frequency (MHz)')
	ax3.set_ylabel('Time (s)')
	ax3.set_title('Dynamic Spectrum (Waterfall)')

	# Adjust Subplot Width Ratio
	if cal_file != '':
		gs = GridSpec(2, 3, width_ratios=[16.5, 1, 1]) ###17.7
	else:
		gs = GridSpec(2, 2, width_ratios=[7.6, 1])

	# Plot Time Series (Power vs Time)
	ax4 = fig.add_subplot(gs[1,0])
	ax4.plot(t, power, label='Raw Time Series')
	if m != 0:
		ax4.plot(t, power_clean, label='Median (n = '+str(m)+')')
	ax4.set_xlim(0, np.max(t))
	ax4.set_xlabel('Time (s)')
	if dB:
		ax4.set_ylabel('Relative Power (dB)')
	else:
		ax4.set_ylabel('Relative Power')
	ax4.set_title('Average Power vs Time')
	if m != 0:
		ax4.legend(bbox_to_anchor=(1,1), loc='upper right')
	ax4.grid()

	# Plot Time Series Histogram
	if cal_file != '':
		gs = GridSpec(2, 3, width_ratios=[7.83, 1.5, -0.325])
	else:
		gs = GridSpec(2, 2, width_ratios=[8.8, 1.5])

	ax5 = fig.add_subplot(gs[1,1])

	n, bins, patches = ax5.hist(power, np.size(power)/10, density=1, alpha=0.75, orientation='horizontal', zorder=10)

	# Compute Gaussian Fit
	avg = np.mean(power)
	var = np.var(power)

	gaussian_fit_x = np.linspace(np.min(power),np.max(power),100)
	gaussian_fit_y = 1.0/np.sqrt(2*np.pi*var)*np.exp(-0.5*(gaussian_fit_x-avg)**2/var)

	ax5.plot(gaussian_fit_y, gaussian_fit_x, 'r--', label='Best fit', zorder=20)
	ax5.get_shared_x_axes().join(ax5, ax4)
	ax5.set_yticklabels([])
	ax5.set_xlabel('Probability Density')
	ax5.set_title('Total Power Distribution')
	ax5.legend(bbox_to_anchor=(1,1), loc='upper right')
	ax5.grid()

	plt.tight_layout()
	plt.savefig(plot_file)
