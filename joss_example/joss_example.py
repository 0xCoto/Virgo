import virgo

# Set observation parameters
obs = {
    'frequency': 1420e6,
    'bandwidth': 2.4e6,
    'channels': 2048,
    't_sample': 0.085
}

# Analyze and export data as csv
virgo.plot(obs_parameters=obs, n=10, m=25, f_rest=1420.4057517667e6,
           obs_file='observation.dat', cal_file='calibration.dat',
           spectra_csv='spectrum.csv', power_csv='time_series.csv',
           dB=True, plot_file='observation.png')

### Extended function examples/tests ###

# Display all-sky HI survey (marker at RA = 21h, Dec. = 40 deg)
virgo.map_hi(ra=21, dec=40, plot_file='map.png')

# Estimate telescope half-power beamwidth (FWHM)
hpbw = virgo.beamwidth(D=1.5, f=1420e6)
hpbw = round(hpbw, 2)
print('HPBW: ' + str(hpbw))

# Convert Equatorial coordinates to Galactic
l, b = virgo.galactic(21, 40)
print('Galactic longitude: '+str(l) + ', Galactic latitude: ' + str(b))

# Simulate 21 cm profile based on the LAB HI survey
virgo.simulate(l=l, b=b, beamwidth=hpbw, v_min=-150, v_max=320, plot_file='profile.png')

# Check source position
virgo.predict(lat=39.83, lon=-74.87, source='Cas A', date='2020-12-26', plot_file='cas_a.png')

# Takes observer's location and Alt/Az as input and return RA/Dec for current time
ra, dec = virgo.equatorial(alt=54, az=23, lat=39.83, lon=-74.87)
print('RA: ' + str(ra) + ', Dec.: ' + str(dec))

# Transform antenna gain to effective aperture
e_aperture = virgo.A_e(gain=40, f=1420e6)
print('A_e: ' + str(e_aperture))

# Estimate antenna gain
ant_gain = virgo.gain(D=20, f=1420e6, e=0.7, u='K/Jy')
print('Gain: '+str(ant_gain))

# Convert noise temperature [K] to noise figure [dB]
noise_fig = virgo.NF(T_noise=35, T_ref=290)
print('NF: '+str(noise_fig))

# Convert noise fiugre [dB] to noise temperature [K]
noise_temp = virgo.T_noise(NF=2, T_ref=290)
print('T_noise: '+str(noise_temp))

# Convert wavelength to frequency
freq = virgo.frequency(wavelength=0.21)
print('Frequency: ' + str(freq))

# Convert frequency to wavelength
lamda = virgo.wavelength(frequency=1420e6)
print('Wavelength: ' + str(lamda))

# Compute system equivalent flux density [Jy]
sensitivity = virgo.SEFD(A_e=300, T_sys=73)
print('SEFD: ' + str(sensitivity))

# Estimate the obtained signal-to-noise ratio of an observation (radiometer equation)
signal_to_noise = virgo.snr(S=20, sefd=3320, t=30, bw=15e6)
print('SNR: ' + str(signal_to_noise))

# Compute antenna gain-to-noise-temperature (G/T)
g_over_t = virgo.G_T(gain=40, T_sys=85)
print('G/T: ' + str(g_over_t))
