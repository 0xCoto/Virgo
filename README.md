# VIRGO: An open-source Spectrometer for Radio Astronomy
<p align="center">
  <img src="https://i.imgur.com/lH2OOTd.png?raw=true" alt="VIRGO Spectrometer"/>
</p>

## About VIRGO
**VIRGO** is an easy-to-use **open-source** spectrometer and radiometer based on [Python](https://www.python.org) and [GNU Radio Companion](https://wiki.gnuradio.org/index.php/GNURadioCompanion) (GRC) that is conveniently applicable to any radio telescope working with a GRC-supported software-defined radio (SDR). In addition to data acquisition, VIRGO also carries out automated analysis of the recorded samples, producing an **averaged spectrum**, a **calibrated spectrum**, a **dynamic spectrum (waterfall)** and a **time series (power vs time)** plot.

A list of GRC-supported SDRs can be found [here](https://wiki.gnuradio.org/index.php/Hardware).

![alt text](https://i.imgur.com/zS5ZjK0.png)

## Telescopes based on the VIRGO Spectrometer
- ISEC TLM-18 Telescope (18m)
- SALSA Vale Telescope (2.3m)
- SALSA Brage Telescope (2.3m)
- PICTOR Telescope (1.5m)
- NanoRT Telescope (15cm)
- and others!

## Example Observation
![alt text](https://i.imgur.com/K8g0wVd.png "Example Observation")

## GRC Data Acquisition Flowgraph
**VIRGO** is a [**polyphase filterbank** spectrometer](https://arxiv.org/abs/1607.03579). The raw I/Q samples are processed in real time using GNU Radio, with the amount of data stored to file being drastically reduced for further analysis. The following flowgraph handles the acquisition and early-stage processing of the data:

![alt text](https://i.imgur.com/2Xp8qnZ.png "Data Acquisition Flowgraph")

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

#### If you do not use an RTL-SDR
Once the repository has been cloned, open `pfb.grc` using GNU Radio Companion and replace the `RTL-SDR Source` block with the  source block of your SDR (e.g. `UHD: USRP Source`). After modifying the properties of the new SDR Source block (optional), click the little button next to the **Play** button to generate the new and updated version of `top_block.py` that is compatible with your SDR:

![alt text](https://i.imgur.com/F16haLm.png)

(You only need to do this once.)

## Usage
Once **VIRGO** is downloaded on your system and the SDR Source block has been replaced (unless you use an RTL-SDR where you shouldn't need to change anything), you can begin observing with **VIRGO** by running:

```
python observe.py
```

From there, the interactive software should ask you for the parameters of your observation, which you can simple enter in and let **VIRGO** do its magic! Once the observation is finished, your data will be processed, analyzed and saved as `plot.png` (in the same directory as `observe.py`).

## To do
- [x] Add list of radio telescopes using software based on **VIRGO**
- [ ] Implement additional horizontal axis on the calibrated spectrum to display relative velocity (derived from Δf = f<sub>rest</sub> − f<sub>obs</sub>)
- [ ] Improve the UI by adding **bold text** and *colors*

## Credits
**VIRGO** was created by **[Apostolos Spanakis-Misirlis](https://www.github.com/0xCoto/)**.

**Contact:** [0xcoto@protonmail.com](mailto:0xcoto@protonmail.com)

---

Special thanks to **Dr. Cees Bassa** and **Dr. Cameron Van Eck** for their valuable contributions.
