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
           dB=True, plot_file='plot.png')

### Extended function examples/tests ###

# Display all-sky HI survey (marker at RA = 21h, Dec. = 40 deg)
virgo.map_hi(ra=21, dec=40)

# Estimate telescope half-power beamwidth (FWHM)
hpbw = virgo.beamwidth(D=1.5, f=1420e6)
hpbw = round(hpbw, 2)
print(hpbw)

# Convert Equatorial coordinates to Galactic
l, b = virgo.galactic(21, 40)
print(l,b)

# Simulate 21 cm profile based on the LAB HI survey
virgo.simulate(l=l, b=b, beamwidth=hpbw, v_min=-150, v_max=320)

# Check source position
virgo.predict(lat=39.83, lon=-74.87, source='Cas A', date='2020-12-26')

# Takes observer’s location and Alt/Az as input and return RA/Dec for current time
ra, dec = virgo.equatorial(alt=54, az=23, lat=39.83, lon=-74.87)
print(ra, dec)

# Convert wavelength to frequency
freq = virgo.frequency(wavelength=0.21)
print(freq)

# Convert frequency to wavelength
lamda = virgo.wavelength(frequency=1420e6)
print(lamda)

# Transform antenna gain to effective aperture
e_aperture = A_e(gain=40, f=1420e6)
print(e_aperture)

# Estimate antenna gain
ant_gain = virgo.gain(D=20, f=1420e6, e=0.7, u='K/Jy')
print(ant_gain)

# Convert noise temperature [K] to noise figure [dB]
noise_fig = NF(T_noise=35, T_ref=290)
print(noise_fig)

# Convert noise fiugre [dB] to noise temperature [K]
T_noise(NF=2, T_ref=290)
print(T_noise)

# Compute antenna gain-to-noise-temperature (G/T)
G_T(gain=40, T_sys=85)
print(G_T)

# Compute system equivalent flux density [Jy]
SEFD(A_e=300, T_sys=73)
print(SEFD)

# Estimate the obtained signal-to-noise ratio of an observation (radiometer equation)
snr(S=1100, sefd=1320, t=3600, bw=100e6)
print(snr)
