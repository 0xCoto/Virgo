# Virgo: A Versatile Spectrometer for Radio Astronomy
<p align="center">
  <img src="https://i.imgur.com/lH2OOTd.png?raw=true" alt="Virgo Spectrometer"/>
</p>

## About Virgo
**Virgo** is an easy-to-use **open-source** spectrometer and radiometer based on [Python](https://www.python.org) and [GNU Radio](https://wiki.gnuradio.org) (GR) that is conveniently applicable to any radio telescope working with a GR-supported software-defined radio (SDR). In addition to data acquisition, Virgo also carries out automated analysis of the recorded samples, producing an **averaged spectrum**, a **calibrated spectrum**, a **dynamic spectrum (waterfall)**, a **time series (power vs time)** and a **total power distribution** plot.

A list of GR-supported SDRs can be found [here](https://wiki.gnuradio.org/index.php/Hardware).

### Key Features

- 4-tap weighted overlap-add (WOLA) Fourier transform spectrometer
- - Reduced FFT sidelobes
- Adjustable SDR parameters
- - Device arguments
- - RF Gain
- - IF Gain
- - BB Gain
- Header file
- - Observation parameters automatically passed to corresponding `.header` file
- - Includes logged MJD (at observation *t<sub>0</sub>*)
- Spectral line support
- - Spectrum calibration
- - - *y* axis is automatically transformed to S:N units with line masking
- - Supports median operation for RFI mitigation on the frequency-domain (adjustable *n*-factor)
- - Adjustable *f*<sub>rest</sub> for observation of any spectral line (not just HI)
- - Secondary axes for relative velocity automatically adjusted accordingly
- - Prevention against strong narrowband RFI rescaling subplot
- - The average spectra, calibration spectra and calibrated spectra are optionally saved as a `csv` file for further analysis
- Continuum support
- - Supports median operation for time-varying RFI mitigation (adjustable *n*-factor)
- - Total power distribution (histogram) displayed, both for raw and clean data
- - - Best Gaussian fits computed automatically
- - Prevention against strong short-duration RFI rescaling subplot
- - Time series optionally saved as a `csv` file for further analysis
- Dynamic spectrum (waterfall)
- - Optionally saved as a `FITS` file for further advanced/custom analysis
- Decibel support
- - Power units optionally displayed in dB
- Argument-parsing support
- Works directly via `python virgo.py`, or as a module (see below)

## Example Usage

```python
import virgo

# Define observation parameters
obs = {
    'dev_args': '',
    'rf_gain': 10,
    'if_gain': 20,
    'bb_gain': 20,
    'frequency': 1420e6,
    'bandwidth': 5e6,
    'channels': 2048,
    't_sample': 1,
    'duration': 60
}

# Check source position
virgo.predict(lat=39.83, lon=-74.87, source='Cas A', date='2020-12-26')

# Begin data acquisition in 10 sec
virgo.observe(obs_parameters=obs, obs_file='observation.dat', start_in=10)

# Analyze data, mitigate RFI and export the data as a FITS file
virgo.plot(obs_parameters=obs, n=20, m=35, f_rest=1420.4057517667e6,
           obs_file='observation.dat', cal_file='calibration.dat',
           rfi=[1419.2e6, 1419.3e6], waterfall_fits='obs.fits',
           slope_correction=True, plot_file='plot.png')
```

---

### Function definitions
```python
# Schedules observation for start_in seconds. Spectrometer defaults to WOLA unless 'ftf' is specified.
observe(obs_parameters, spectrometer='wola', obs_file='observation.dat', start_in=0)

# Plots data. n and m are median in the spectrum and time series respectively, f_rest is used for frequency -> velocity transformation, slope_correction used to correct poor spectra (linear regression), dB to display data values in decibels, rfi to mask out contaminated data, xlim and ylim to scale frequency and time range respectively, obs_file and cal_file are the data files of the observation and calibration respectively, waterfall_fits is the output .fits filename and spectra_csv and power_cst are the output .csv files respectively.
plot(obs_parameters='', n=0, m=0, f_rest=0, slope_correction=False, dB=False, rfi=[0,0], xlim=[0,0], ylim=[0,0], dm=0,
	 obs_file='observation.dat', cal_file='', waterfall_fits='', spectra_csv='', power_csv='', plot_file='plot.png'):

# Plots source AltAz given observer's Earth coordinates. If date is not given, it defaults to today's system date.
predict(lat, lon, height=0, source='', date='', plot_sun=True, plot_file='')

# Simulates 21 cm profiles based on the LAB HI Survey. l and b are galactic longitude and latitude, beamwidth is the HPBW (beam FWHM) of the telescope and v_min/v_max is the x axis velocity limits.
simulate(l, b, beamwidth=0.6, v_min=-400, v_max=400, plot_file=''):

# Converts RA/Dec. to galactic longitude and latitude. The position is returned as a tuple, where the first element [0] is l and the second [1] is b.
galactic(ra, dec)

# Takes observer's location and AltAz as input and returns RA/Dec as a tuple.
equatorial(alt, az, lat, lon, height=0)

# Plots 21 cm map (LAB HI survey). Setting RA/Dec (optional args) will add a red dot indicating where the telescope is pointing to.
map_hi(ra=None, dec=None, plot_file='')

# Monitors RFI. f_lo and f_hi define the frequency limits in Hz and data is the directory in which the .dat RFI survey files are stored in.
monitor_rfi(f_lo, f_hi, obs_parameters, data='rfi_data')

# Plots RFI data. rfi_parameters should be the same as obs_parameters, but should also include 'f_lo': f_lo. Set dB=True for a wider dynamic range.
plot_rfi(rfi_parameters, data='rfi_data', dB=True, plot_file='plot.png')
```

---

## Telescopes based on the Virgo Spectrometer
- ISEC TLM-18 Telescope (18m)
- ACRO RT-320 (3.2m)
- SALSA Vale Telescope (2.3m) [potentially soon, but already tested]
- SALSA Brage Telescope (2.3m) [potentially soon, but already tested]
- JRT (1.9m)
- PICTOR Telescope (1.5m)
- NanoRT Telescope (15cm)
- and more!

## Example Observation
<p align="center">
  <img src="https://i.imgur.com/ROPPWza.png" alt="Example Observation"/>
</p>                                                                     
Observation of galactic clouds of neutral hydrogen toward the constellation of Cygnus (α = 20h, δ = 40° , l = 77° , b = 3°), observed by the TLM-18 Telescope in New Jersey, U.S. with Virgo. The average spectrum (top left), the calibrated spectrum (top center), the dynamic spectrum (top right) and the time series along with the total power distribution (bottom) are all plotted by the software automatically.

## Data Acquisition Flowgraph
**Virgo** is a **four-tap WOLA Fourier transform** spectrometer. The raw I/Q samples are processed in real time using GNU Radio, with the amount of data stored to file being drastically reduced for further analysis. The following flowgraph handles the acquisition and early-stage processing of the data:

![alt text](https://i.imgur.com/5tR7WjL.png "Data Acquisition Flowgraph")

## Data Analysis
Once a submitted observation is finished and the data has been acquired and stored to `observation.dat`, the FFT samples (interpreted as a [numpy array](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html) in `plot.py` and `plot_hi.py`) constitute the **dynamic spectrum (waterfall)**, from which the **averaged spectrum** and **time series (power vs time)** of the observation can be derived.

We can mathematically interpret the dynamic spectrum as a two-dimensional matrix with ***m*** rows and ***2<sup>n</sup>*** columns, where *m* ∈ ℕ\* is the total number of FFT samples (integrations) and *2<sup>n</sup>*, *n* ∈ ℕ is the number of frequency channels (FFT size).

In `__init__.py`, this matrix is defined as a 2D numpy array at [line 137](https://github.com/0xCoto/Virgo/blob/master/virgo/__init__.py#L137).

![alt text](https://i.imgur.com/JksgAav.png)

### Time Series Derivation
If we take the average of this matrix with respect to time (`power = decibel(np.mean(waterfall, axis=1))`), we get a new *m* × *1* **column matrix** (or **column vector**), which is the <ins>time series (power vs time)</ins> of the observation. This is defined in [line 146](https://github.com/0xCoto/Virgo/blob/master/virgo/__init__.py#L146).

### Averaged Spectrum Derivation
Similarly, if we average with respect to the frequency channels (`avg_spectrum = decibel(np.mean(waterfall, axis=0))`), we get a new *1* × *2<sup>n</sup>* **row matrix** (or **row vector**), which is the <ins>averaged spectrum</ins> of the observation. This is defined at [line 142](https://github.com/0xCoto/Virgo/blob/master/virgo/__init__.py#L142).

### Calibrated Spectrum Derivation
To get the <ins>calibrated spectrum</ins>, we could simply subtract the ***OFF*** spectrum (obtained from an observation of e.g. the cold sky) from the ***ON*** spectrum (X(f)<sub>ON<sub>mean</sub></sub> − X(f)<sub>OFF<sub>mean</sub></sub>). However, because the system temperature of a radio telescope (T<sub>sys</sub>) is generally variable with time and temperature, the noise floor will not be at a constant level. For this reason, it is more appropriate to choose division over subtraction (X(f)<sub>ON<sub>mean</sub></sub> / X(f)<sub>OFF<sub>mean</sub></sub>), in order to account for the variability of thse noise floor. The calibrated spectrum is computed at [line 165](https://github.com/0xCoto/Virgo/blob/master/virgo/__init__.py#L165).

## Installation
To use **Virgo**, make sure **[Python](https://www.python.org/)** and **[GNU Radio](https://wiki.gnuradio.org/index.php/InstallingGR)** (with **[gr-osmosdr](https://osmocom.org/projects/gr-osmosdr/wiki)**) are installed on your machine.

Once Python and GNU Radio are installed on your system, run

```
pip install astro-virgo
```

#### If you do not use an osmocom-supported SDR (unlikely)
Once the repository has been cloned, open `pfb.grc` using GNU Radio Companion and replace the `osmocom Source` block with the source block of your SDR (e.g. `UHD: USRP Source`). After modifying the properties of the new SDR Source block (optional), click the little button next to the **Play** button to generate the new and updated version of `run_observation.py` that is compatible with your SDR:

![alt text](https://i.imgur.com/F16haLm.png)

(You only need to do this once.)

## Usage
Once **Virgo** is downloaded on your system and the SDR Source block has been replaced (unless you use an osmocom-supported SDR where you shouldn't need to change anything), you can begin observing with **Virgo** by running:

```
python virgo.py [arguments]
```

(Run `python virgo.py -h` to see all the available arguments)

Alternatively, you can import **Virgo** as a Python module (see **Example Usage** section above).

## Credits
**Virgo** was created by **[Apostolos Spanakis-Misirlis](https://www.github.com/0xCoto/)**.

**Contact:** [0xcoto@protonmail.com](mailto:0xcoto@protonmail.com)

---

Special thanks to **Dr. Cameron Van Eck**, **Paul Boven** and **Dr. Cees Bassa** for their valuable contributions.
