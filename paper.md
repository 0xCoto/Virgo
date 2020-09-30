---
title: 'Virgo: A Versatile Spectrometer for Radio Astronomy'
tags:
  - Python
  - radio astronomy
  - digital signal processing
  - astrophysics
authors:
  - name: Apostolos Spanakis-Misirlis
    orcid: 0000-0001-6928-6877
    affiliation: 1
  - name: TBA
    affiliation: 2
  - name: TBA
    affiliation: 3
affiliations:
 - name: University of Piraeus
   index: 1
 - name: TBA (Institution Name)
   index: 2
 - name: TBA (Institution Name)
   index: 3
date: 16 September 2020
bibliography: paper.bib

---

# Introduction

For the last decades, radio astronomy has been among the most fundamental
branches of astrophysics. This is due to the fact that a variety of
celestial objects emit electromagnetic radiation at radio wavelengths,
which has led to the development of radio telescopes, capable of
revealing the otherwise-hidden astrophysical properties of the universe. An
important requirement that makes radio astronomy observations and analyses
possible is an appropriate software pipeline compatible with the
spectrometers with which radio observatories are equipped.

# Statement of Need

`Virgo` is a Python package for the acquisition, processing and analysis of
data from radio telescopes. It is an easy-to-use open-source spectrometer and
radiometer based on the GNU Radio framework [@gnuradio], and is conveniently
applicable to any radio telescope working with a GNU Radio-supported software-defined
radio (i.e. a radio receiver architecture which applies certain functionalities on an
embedded system/computer by means of software).

`%Comment: Wikipedia cites the parentheses statement with 'Markus Dillinger, Kambiz Madani, Nancy Alonistioti (2003). Software Defined Radio: Architectures, Systems and Functions. Wiley & Sons. p. xxxiii. ISBN 0-470-85164-3'. Should I do the same?`

`%Comment [to Paul]: How do you suggest we cite GNU Radio?`

Designed to be used by students, educators and amateurs in the field of radio
astronomy, `Virgo` has already been adopted by a number of small and
large-aperture radio telescopes, permitting both spectral and continuum
observations with great success. These instruments include the ISEC TLM-18 (18m),
the ACRO RT-320 (3.2m), the JRT (1.9m), the PICTOR Telescope (1.5m), among others.

Although the hardware aspect of a radio telescope is generally handled by newcomers
with relative ease, the skill set needed to integrate a complete software pipeline to
support observations is not something most users are equipped with. `Virgo` tackles
this problem by providing non-experts with a tool to collect and interpret data from
radio telescopes, without requiring expertise in digital signal  processing and
software engineering.

An example observation of the 21-cm hydrogen line acquired and processed with
`Virgo` is shown in \autoref{fig:example}.

`%Self-comment: TBA (most likely within a few days, once I get a chance to implement
the S/W): Allen Telescope Array (42x 6.1m)`

![Clouds of neutral hydrogen/the 21-cm hydrogen line at (Source name/RA=hh:mm:ss, Dec=dd:mm:ss), observed by the (TBA) Telescope with `Virgo`. The average spectrum (top left), the calibrated spectrum (top center), the dynamic spectrum (top right) and the time series along with the total power distribution (bottom) are all plotted by the software automatically.\label{fig:example}](example.pdf)

`%Self-comment: Add example observation (use .pdf instead of .png for optimal quality)`

# Use Cases

TBA

# Features

One of the key features of `Virgo` is that it is a polyphase filterbank
spectrometer, offering a  significant reduction in spectral leakage compared to
the more traditional Fourier transform filterbank spectrometers, with a minimal
increase in computational requirements, as described in greater detail by
@Price:2021. In addition to its data-acquisition functionality, `Virgo` carries
out automated analysis of the recorded samples, producing the time-averaged spectrum,
the calibrated spectrum, the dynamic spectrum (waterfall), the time series (power
vs time) and the total power distribution plot of the observation, with the help
of the NumPy [@Harris2020] and Matplotlib [@Hunter:2007] packages.

Furthermore, `Virgo` supports optional median operations, both
in the frequency and time domain, for the suppression of narrowband and/or
short-duration radio frequency interference (RFI), while allowing the user to export
the raw observation data as a FITS/csv-formatted file.

# Example Usage
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

# Begin data acquisition in 10 seconds
virgo.observe(obs_parameters=observation, obs_file='observation.dat',
              start_in=10)

# Analyze data, mitigate RFI and export the data as a FITS file
virgo.plot(obs_parameters=observation, n=20, m=35, f_rest=1420.4057517667e6,
           obs_file='observation.dat', cal_file='calibration.dat',
           waterfall_fits='obs.fits', plot_file='plot.png')
```

# Future Work

As `Virgo` gets adopted by more and more radio telescopes, the need for expanding the
software's capabilities grow. Additional features that have been proposed include but
are not limited to a more robust and intelligent system for the detection and
mitigation of RFI, and the support for a data acquisition/analysis pipeline for
pulsar astronomy, both of which offer the potential of appealing to a broader user
audience.

# References
