Reference
=========

This reference page details the functions included in Virgo, describing their roles and what they do.

simulate
""""""""

.. function:: simulate(l, b, beamwidth=0.6, v_min=-400, v_max=400, plot_file='')

   Simulate 21 cm profiles based on the LAB HI Survey.

   :param l: Target galactic longitude [deg]
   :type l: float
   :param b: Target galactic latitude [deg]
   :type b: float
   :param beamwidth: Telescope half-power beamwidth (approx. equal to 0.7 * lambda/D) [deg]
   :type beamwidth: float
   :param v_min: Minimum radial velocity (xlim) [km/s]
   :type v_min: float
   :param v_max: Maximum radial velocity (xlim) [km/s]
   :type v_max: float

predict
"""""""

.. function:: predict(lat, lon, height=0, source='', date='', plot_sun=True, plot_file='')

   Plots source Alt/Az given the observer's Earth coordinates.

   :param lat: Observer latitude [deg]
   :type lat: float
   :param lon: Obesrver longitude [deg]
   :type lon: float
   :param height: Observer elevation [m]
   :type height: float
   :param source: Date in YYYY-MM-DD format. If no date is given, it defaults to today's system date.
   :type source: string
   :param plot_sun: Also plot Sun position for reference
   :type plot_sun: bool
   :param plot_file: Output plot filename
   :type plot_file: string

equatorial
""""""""""

.. function:: equatorial(alt, az, lat, lon, height=0)

   Takes observer's location and Alt/Az as input and returns RA/Dec as a tuple.

   :param alt: Altitude [deg]
   :type alt: float
   :param az: Azimuth [deg]
   :type az: float
   :param lat: Observer latitude [deg]
   :type lat: float
   :param lon: Observer longitude [deg]
   :type lon: float
   :param height: Observer elevation [m]
   :type height: float

galactic
""""""""

.. function:: galactic(ra, dec)

   Converts RA/Dec. to galactic coordinates, returning galactic longitude and latitude (tuple).

   :param ra: Right ascension [deg]
   :type ra: float
   :param dec: Declination [deg]
   :type dec: float

frequency
"""""""""

.. function:: frequency(wavelength)

   Transform wavelength to frequency.

   :param wavelength: Wavelength [m]
   :type wavelength: float

wavelength
""""""""""

.. function:: wavelength(frequency)

   Transform frequency to wavelength.

   :param frequency: Wave frequency [Hz]
   :type frequency: float

gain
""""

.. function:: gain(D, f, e=0.7, u='dBi')

   Estimate parabolic antenna gain.

   :param D: Antenna diameter [m]
   :type D: float
   :param f: Frequency [Hz]
   :type f: float
   :param e: Aperture efficiency (0 >= e >= 1)
   :type e: float
   :param u: Output gain unit ('dBi', 'linear' or 'K/Jy')
   :type u: string

A_e
"""

.. function:: A_e(gain, f)

   Transform antenna gain to effective aperture [m^2].

   :param gain: Antenna gain [dBi]
   :type gain: float
   :param f: Frequency [Hz]
   :type f: float

beamwidth
"""""""""

.. function:: beamwidth(D, f)

   Estimate parabolic antenna half-power beamwidth (FWHM).

   :param D: Antenna diameter [m]
   :type D: float
   :param f: Frequency [Hz]
   :type f: float

NF
""

.. function:: NF(T_noise, T_ref=290)

   Convert noise temperature to noise figure [dB].

   :param T_noise: Noise temperature [K]
   :type T_noise: float
   :param T_ref: Reference temperature [K]
   :type T_ref: float

T_noise
"""""""

.. function:: T_noise(NF, T_ref=290)

   Convert noise figure to noise temperature [K].

   :param NF: Noise figure [dB]
   :type NF: float
   :param T_ref: Reference temperature [K]
   :type T_ref: float

G_T
"""

.. function:: G_T(gain, T_sys)

   Compute antenna gain-to-noise-temperature (G/T).

   :param gain: Antenna gain [dBi]
   :type gain: float
   :param T_sys: System noise temperature [K]
   :type T_sys: float

SEFD
""""

.. function:: SEFD(A_e, T_sys)

   Compute system equivalent flux density [Jy].

   :param A_e: Effective antenna aperture [m^2]
   :type A_e: float
   :param T_sys: System noise temperature [K]
   :type T_sys: float

snr
"""

.. function:: snr(S, sefd, t, bw)

   Estimate the obtained signal-to-noise ratio of an observation (radiometer equation).

   :param S: Source flux density [Jy]
   :type S: float
   :param sefd: Instrument's system equivalent flux density [Jy]
   :type sefd: float
   :param t: Total on-source integration time [sec]
   :type t: float
   :param bw: Acquisition bandwidth [Hz]
   :type bw: float

map_hi
""""""

.. function:: map_hi(ra=None, dec=None, plot_file='')

   Plots the all-sky 21 cm map (LAB HI survey). Setting RA/Dec (optional args) will add a red dot indicating where the telescope is pointing to.

   :param ra: Right ascension [deg]
   :type ra: float
   :param dec: Declination [deg]
   :type dec: float
   :param plot_file: Output plot filename
   :type plot_file: string

observe
"""""""

.. function:: observe(obs_parameters, spectrometer='wola', obs_file='observation.dat', start_in=0)

   Begin data acquisition (requires SDR connected to the machine).

   :param obs_parameters: Observation parameters
   :type obs_parameters: dict
   :param spectrometer: Spectrometer flowchart/pipeline ('WOLA'/'FTF')
   :type spectrometer: string
   :param obs_file: Output data filename
   :type obs_file: string
   :param start_in: Schedule observation start [sec]
   :type start_in: float

Arguments for ``obs_parameters``:

.. attribute:: obs_parameters

   :param dev_args: Device arguments (gr-osmosdr)
   :type dev_args: string
   :param rf_gain: RF gain
   :type rf_gain: float
   :param if_gain: IF gain
   :type if_gain: float
   :param bb_gain: Baseband gain
   :type bb_gain: float
   :param frequency: Center frequency [Hz]
   :type frequency: float
   :param bandwidth: Instantaneous bandwidth [Hz]
   :type bandwidth: float
   :param channels: Number of frequency channels (FFT size)
   :type channels: int
   :param t_sample: Integration time per FFT sample
   :type t_sample: float
   :param duration: Total observing duration [sec]
   :type duration: float

plot
""""

.. function:: plot(obs_parameters='', n=0, m=0, f_rest=0, slope_correction=False, dB=False, rfi=[0,0], xlim=[0,0], ylim=[0,0], dm=0, obs_file='observation.dat', cal_file='', waterfall_fits='', spectra_csv='', power_csv='', plot_file='plot.png')

   Process, analyze and plot data.

   :param obs_parameters: Observation parameters
   :type obs_parameters: dict
   :param n: Median filter factor (spectrum)
   :type n: int
   :param m: Median filter factor (time series)
   :type m: int
   :param f_rest: Spectral line reference frequency used for radial velocity (Doppler shift) calculations [Hz]
   :type f_rest: float
   :param slope_correction: Correct slope in poorly-calibrated spectra using linear regression
   :type slope_correction: bool
   :param dB: Display data in decibel scaling
   :type dB: bool
   :param rfi: Blank frequency channels contaminated with RFI ([low_frequency, high_frequency]) [Hz]
   :type rfi: list
   :param xlim: x-axis limits ([low_frequency, high_frequency]) [Hz]
   :type xlim: list
   :param ylim: y-axis limits ([start_time, end_time]) [Hz]
   :type ylim: list
   :param dm: Dispersion measure for dedispersion [pc/cm^3]
   :type dm: float
   :param obs_file: Input observation filename (generated with virgo.observe)
   :type obs_file: string
   :param cal_file: Input calibration filename (generated with virgo.observe)
   :type cal_file: string
   :param waterfall_fits: Output FITS filename
   :type waterfall_fits: string
   :param spectra_csv: Output CSV filename (spectra)
   :type spectra_csv: string
   :param power_csv: Output CSV filename (time series)
   :type power_csv: string
   :param plot_file: Output plot filename
   :type plot_file: string

Arguments for ``obs_parameters``:

.. attribute:: obs_parameters

   :param dev_args: Device arguments (gr-osmosdr)
   :type dev_args: string
   :param rf_gain: RF gain
   :type rf_gain: float
   :param if_gain: IF gain
   :type if_gain: float
   :param bb_gain: Baseband gain
   :type bb_gain: float
   :param frequency: Center frequency [Hz]
   :type frequency: float
   :param bandwidth: Instantaneous bandwidth [Hz]
   :type bandwidth: float
   :param channels: Number of frequency channels (FFT size)
   :type channels: int
   :param t_sample: Integration time per FFT sample
   :type t_sample: float
   :param duration: Total observing duration [sec]
   :type duration: float

plot_rfi
""""""""

.. function:: plot_rfi(rfi_parameters, data='rfi_data', dB=True, plot_file='plot.png')

   Plots wideband RFI survey spectrum.

   :param rfi_parameters: Identical to obs_parameters, but also including 'f_lo': f_lo
   :type rfi_parameters: dict
   :param data: Survey data directory containing individual observations
   :type data: string
   :param dB: Display data in decibel scaling
   :type dB: bool
   :param plot_file: Output plot filename
   :type plot_file: string

monitor_rfi
"""""""""""

.. function:: monitor_rfi(f_lo, f_hi, obs_parameters, data='rfi_data')

   Begin data acquisition (wideband RFI survey).

   :param obs_parameters: Observation parameters (identical to parameters used to acquire data)
   :type obs_parameters: dict
   :param f_lo: Start frequency [Hz]
   :type f_lo: float
   :param f_hi: End frequency [Hz]
   :type f_hi: float
   :param data: Survey data directory to output individual observations to
   :type data: string

Arguments for ``obs_parameters``:

.. attribute:: obs_parameters

   :param dev_args: Device arguments (gr-osmosdr)
   :type dev_args: string
   :param rf_gain: RF gain
   :type rf_gain: float
   :param if_gain: IF gain
   :type if_gain: float
   :param bb_gain: Baseband gain
   :type bb_gain: float
   :param frequency: Center frequency [Hz]
   :type frequency: float
   :param bandwidth: Instantaneous bandwidth [Hz]
   :type bandwidth: float
   :param channels: Number of frequency channels (FFT size)
   :type channels: int
   :param t_sample: Integration time per FFT sample
   :type t_sample: float
   :param duration: Total observing duration [sec]
   :type duration: float







