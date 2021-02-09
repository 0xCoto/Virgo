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
