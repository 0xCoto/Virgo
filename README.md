# Virgo: A Versatile Spectrometer for Radio Astronomy
<p align="center">
  <img src="https://i.imgur.com/lH2OOTd.png?raw=true" alt="Virgo Spectrometer"/>
</p>

<p align="center">
  <a href="https://joss.theoj.org/papers/612c2634c1dd83749e95a93449740861"><img src="https://joss.theoj.org/papers/612c2634c1dd83749e95a93449740861/status.svg"></a>
  <img src="https://img.shields.io/badge/python-2.7%20%7C%203.x-green"/>
  <img src="https://img.shields.io/pypi/v/astro-virgo"/>
  <img src="http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat"/>
  <img src="https://img.shields.io/github/license/0xCoto/Virgo?color=yellow"/>
</p>


## About Virgo
**Virgo** is an easy-to-use **open-source** spectrometer and radiometer based on [Python](https://www.python.org) and [GNU Radio](https://wiki.gnuradio.org) (GR) that is conveniently applicable to any radio telescope working with a GR-supported software-defined radio (SDR). In addition to data acquisition, Virgo also carries out automated analysis of the recorded samples, producing an **averaged spectrum**, a **calibrated spectrum**, a **dynamic spectrum (waterfall)**, a **time series (power vs time)** and a **total power distribution** plot.

A list of GR-supported SDRs can be found [here](https://wiki.gnuradio.org/index.php/Hardware).

### Key Features

- 4-tap weighted overlap-add (WOLA) Fourier transform spectrometer
- - Reduced FFT sidelobes
- - Plain FT filterbank pipeline also supported for observatories with limited computational resources
- Adjustable SDR parameters
- - Device arguments
- - RF/IF/BB Gain
- Header file
- - Observation parameters automatically passed to corresponding `.header` file
- - Includes logged MJD (at observation *t<sub>0</sub>*)
- Spectral line support
- - Spectrum calibration
- - - *y* axis is automatically rescaled to S:N units with line masking
- - - Optional automatic slope correction (based on linear regression) for poorly-calibrated spectra
- - Supports median operation for RFI mitigation on the frequency-domain (adjustable *n*-factor)
- - RFI channel masking
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
- Pulsars
- - Incoherent dedispersion support for giant pulse search (and FRB follow-up, assuming DM is known)
- Dynamic spectrum (waterfall)
- - Optionally saved as a `FITS` file for further advanced/custom analysis
- Decibel support
- - Power units optionally displayed in dB
- Observation planning toolkit
- - Predict source altitude & azimuth vs time
- - Quickly convert galactic to equatorial and Alt/Az to RA/Dec
- - Plot telescope position on the 21 cm all-sky survey
- - Simulate 21 cm profiles based on the LAB HI survey
- Basic calculation toolkit for system sensitivity & performance. Computes:
- - Antenna gain (in dBi, linear or K/Jy)
- - Effective aperture
- - Half-power beamwidth
- - Noise figure to noise temperature and vice versa
- - Antenna gain-to-noise-temperature (G/T)
- - System equivalent flux density (SEFD)
- - Radiometer equation (S:N estimation)
- Built-in tool for conducting rapid RFI surveys
- Argument-parsing support
- Works directly from the command line (`virgo -h`), or as a Python module

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

### Example Observation
<p align="center">
  <img src="https://i.imgur.com/ROPPWza.png" alt="Example Observation"/>
</p>
Observation of galactic clouds of neutral hydrogen toward the constellation of Cygnus (α = 20h, δ = 40° , l = 77° , b = 3°), observed by the TLM-18 Telescope in New Jersey, U.S. with Virgo. The average spectrum (top left), the calibrated spectrum (top center), the dynamic spectrum (top right) and the time series along with the total power distribution (bottom) are all plotted by the software automatically.

### Example Source Location Prediction
<p align="center">
  <img src="https://i.imgur.com/jnGJEvQ.png" alt=""/>
</p>

### Example HI Profile Retrieval
<p align="center">
  <img src="https://i.imgur.com/HHSkDJM.png" alt="Example HI Profile Retrieval"/>
</p>

### Example HI Map
<p align="center">
  <img src="https://i.imgur.com/bvg4r4c.png" alt="Example HI map plot"/>
</p>
The red dot indicates the position of the telescope's beam in the sky.

## Data Acquisition Flowgraph
**Virgo** is a **four-tap WOLA Fourier transform** spectrometer. The raw I/Q samples are processed in real time using GNU Radio, with the amount of data stored to file being drastically reduced for further analysis. The following flowgraph handles the acquisition and early-stage processing of the data:

![alt text](https://i.imgur.com/5tR7WjL.png "Data Acquisition Flowgraph")

### Example radio map acquired and processed with the help of Virgo (PICTOR Northern HI Survey)
![alt text](https://i.imgur.com/pYgMAhW.png "PICTOR HI Survey")

## Installation
To use **Virgo**, make sure **[Python](https://www.python.org/)** and **[GNU Radio](https://wiki.gnuradio.org/index.php/InstallingGR)** (with **[gr-osmosdr](https://osmocom.org/projects/gr-osmosdr/wiki)**) are installed on your machine.

Once Python and GNU Radio are installed on your system, run

```
pip install astro-virgo
```

## Documentation
To learn how to use Virgo, please read through the documentation **[here](https://virgo.readthedocs.io/en/latest/)**.

If you believe something is not clarified in the documentation page, you are encouraged to **[create an issue](https://github.com/0xCoto/Virgo/issues/new)** (or send me an [e-mail](mailto:0xcoto@protonmail.com) and I'll be happy to help.

## Contributing
If you wish to contribute to the package (either with code, ideas or further documentation), please read through the **[Contributor Guidelines](https://github.com/0xCoto/Virgo/blob/master/docs/contributing.md)**.

## Credits
**Virgo** was created by **[Apostolos Spanakis-Misirlis](https://www.github.com/0xCoto/)**.

**Contact:** [0xcoto@protonmail.com](mailto:0xcoto@protonmail.com)

---

Special thanks to **Dr. Cameron Van Eck**, **Paul Boven** and **Dr. Cees Bassa** for their valuable contributions.
