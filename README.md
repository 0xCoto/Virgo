# VIRGO: A Versatile Spectrometer for Radio Astronomy
<p align="center">
  <img src="https://i.imgur.com/lH2OOTd.png?raw=true" alt="VIRGO Spectrometer"/>
</p>

## About VIRGO
**VIRGO** is an easy-to-use **open-source** spectrometer and radiometer based on [Python](https://www.python.org) and [GNU Radio Companion](https://wiki.gnuradio.org/index.php/GNURadioCompanion) (GRC) that is conveniently applicable to any radio telescope working with a GRC-supported software-defined radio (SDR). In addition to data acquisition, VIRGO also carries out automated analysis of the recorded samples, producing an **averaged spectrum**, a **calibrated spectrum**, a **dynamic spectrum (waterfall)** and a **time series (power vs time)** plot.

A list of GRC-supported SDRs can be found [here](https://wiki.gnuradio.org/index.php/Hardware).

### Key Features

- Polyphase filterbank-based data acquisition
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
observation = {
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

# Data acquisition
virgo.observe(obs_parameters=observation, obs_file='observation.dat', start_in=0)

# Data analysis
virgo.plot(obs_parameters=observation, n=10, m=25, f_rest=1420.4057517667e6,
           dB=False, obs_file='observation.dat', cal_file='calibration.dat', waterfall_fits='obs.fits',
           spectra_csv='spectra.csv', power_csv='pwr.csv', plot_file='plot.png')
```

## Telescopes based on the VIRGO Spectrometer
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
  <img src="https://i.imgur.com/VBxFBs6.png" alt="Example Observation"/>
</p>                                                                     

## GRC Data Acquisition Flowgraph
**VIRGO** is a [**polyphase filterbank** spectrometer](https://arxiv.org/abs/1607.03579). The raw I/Q samples are processed in real time using GNU Radio, with the amount of data stored to file being drastically reduced for further analysis. The following flowgraph handles the acquisition and early-stage processing of the data:

![alt text](https://i.imgur.com/5tR7WjL.png "Data Acquisition Flowgraph")

## Spectral leakage: a comparison between ACS, FTF and PFB spectrometers
The noteworthy advantage of polyphase filterbanks is **reduced spectral leakage**, with a slight increase in computational requirements. The following figure compares the spectral leakage produced by an autocorrelation spectrometer (ACS), a Fourier transform filterbank spectrometer (FTF) and a polyphase filterbank spectrometer (PFB) with a Hann FFT window:
![alt text](https://i.imgur.com/e5TwE3w.png "Spectrometer comparison regarding spectral leakage")
Source: [Danny C. Price (2018)](https://arxiv.org/abs/1607.03579)

## A graphical representation of a polyphase filterbank
![alt text](https://i.imgur.com/HUFTmTh.png)
Source: [Danny C. Price (2018)](https://arxiv.org/abs/1607.03579)

## Data Analysis
Once a submitted observation is finished and the data has been acquired and stored to `observation.dat`, the FFT samples (interpreted as a [numpy array](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html) in `plot.py` and `plot_hi.py`) constitute the **dynamic spectrum (waterfall)**, from which the **averaged spectrum** and **time series (power vs time)** of the observation can be derived.

We can mathematically interpret the dynamic spectrum as a two-dimensional matrix with ***m*** rows and ***2<sup>n</sup>*** columns, where *m* ∈ ℕ\* is the total number of FFT samples (integrations) and *2<sup>n</sup>*, *n* ∈ ℕ is the number of frequency channels (FFT size).

In `plot.py` and `plot_hi.py`, this matrix is defined as a 2D numpy array at [line 29](https://github.com/0xCoto/VIRGO/blob/master/plot.py#L29) and [line 58](https://github.com/0xCoto/VIRGO/blob/master/plot_hi.py#L58) respectively.

![alt text](https://i.imgur.com/JksgAav.png)

### Time Series Derivation
If we take the average of this matrix with respect to time (`w = np.mean(a=z, axis=1)`), we get a new *m* × *1* **column matrix** (or **column vector**), which is the <ins>time series (power vs time)</ins> of the observation. This is defined at [line 33](https://github.com/0xCoto/VIRGO/blob/master/plot.py#L33) and [line 88](https://github.com/0xCoto/VIRGO/blob/master/plot_hi.py#L88) of `plot.py` and `plot_hi.py` respectively.

### Averaged Spectrum Derivation
Similarly, if we average with respect to the frequency channels (`zmean = np.mean(a=z, axis=0)`), we get a new *1* × *2<sup>n</sup>* **row matrix** (or **row vector**), which is the <ins>averaged spectrum</ins> of the observation. This is defined at [line 39](https://github.com/0xCoto/VIRGO/blob/master/plot.py#L39) and [line 64](https://github.com/0xCoto/VIRGO/blob/master/plot_hi.py#L64) of `plot.py` and `plot_hi.py` respectively.

### Calibrated Spectrum Derivation
To get the <ins>calibrated spectrum</ins>, we could simply subtract the ***OFF*** spectrum (obtained from an observation of e.g. the cold sky) from the ***ON*** spectrum (Z<sub>ON<sub>mean</sub></sub> − Z<sub>OFF<sub>mean</sub></sub>). However, because the system temperature of a radio telescope (T<sub>sys</sub>) is generally variable with time and temperature, the noise floor will not be at a constant level. For this reason, it is more appropriate to choose division over subtraction (Z<sub>ON<sub>mean</sub></sub> / Z<sub>OFF<sub>mean</sub></sub>), in order to account for the variability of thse noise floor. The calibrated spectrum is computed at [line 85](https://github.com/0xCoto/VIRGO/blob/master/plot_hi.py#L85) of `plot_hi.py`.

## Installation
To use **VIRGO**, make sure **[Python](https://www.python.org/) (Version 2.7)** and **[GNU Radio](https://wiki.gnuradio.org/index.php/InstallingGR)** (with **[gr-osmosdr](https://osmocom.org/projects/gr-osmosdr/wiki)**) are installed on your machine.

Once Python and GNU Radio are installed on your system, navigate to a directory of your choice (e.g. `cd Desktop`) and run:

```
git clone https://github.com/0xCoto/VIRGO
```

#### If you do not use an osmocom-supported SDR (unlikely)
Once the repository has been cloned, open `pfb.grc` using GNU Radio Companion and replace the `osmocom Source` block with the source block of your SDR (e.g. `UHD: USRP Source`). After modifying the properties of the new SDR Source block (optional), click the little button next to the **Play** button to generate the new and updated version of `run_observation.py` that is compatible with your SDR:

![alt text](https://i.imgur.com/F16haLm.png)

(You only need to do this once.)

## Usage
Once **VIRGO** is downloaded on your system and the SDR Source block has been replaced (unless you use an osmocom-supported SDR where you shouldn't need to change anything), you can begin observing with **VIRGO** by running:

```
python virgo.py [arguments]
```

(Run `python virgo.py -h` to see all the available arguments)

Alternatively, you can import **VIRGO** as a Python module (see **Example Usage** section above).

## Credits
**VIRGO** was created by **[Apostolos Spanakis-Misirlis](https://www.github.com/0xCoto/)**.

**Contact:** [0xcoto@protonmail.com](mailto:0xcoto@protonmail.com)

---

Special thanks to **Dr. Cameron Van Eck** and **Dr. Cees Bassa** for their valuable contributions.
