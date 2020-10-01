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
  - name: Cameron L. Van Eck
    affiliation: 2
    orcid: 0000-0002-7641-9946
  - name: TBA
    affiliation: 3
affiliations:
 - name: Department of Informatics, University of Piraeus, Greece
   index: 1
 - name: Dunlap Institute for Astronomy and Astrophysics, University of Toronto, 50 St. George Street, Toronto, ON M5S 3H4, Canada
   index: 2
 - name: TBA (Institution Name)
   index: 3
date: 1 October 2020
bibliography: paper.bib

---

# Introduction

For the past few decades, radio astronomy has been among the most fundamental
branches of astrophysics. This is due to the fact that a variety of
celestial objects emit electromagnetic radiation at radio wavelengths,
which has led to the development of radio telescopes capable of revealing
the otherwise-hidden astrophysical properties of the universe. An important
requirement that makes radio astronomy observations and analyses possible
is an appropriate software pipeline compatible with the spectrometers
with which radio observatories are equipped. In this work, we present `Virgo`:
a versatile software solution for radio telescopes.

# Statement of Need

`Virgo` is a Python package for the acquisition, processing and analysis of
data from radio telescopes. It is an easy-to-use open-source spectrometer and
radiometer based on the GNU Radio framework [@gnuradio], and is conveniently
applicable to any radio telescope working with a GNU Radio-supported software-defined
radio (SDR; a radio receiver architecture where some conventional hardware-based
steps are replicated in software, @Dillinger:2003).

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
radio telescopes, without requiring expertise in digital signal processing and
software engineering. An example use case is classroom experiments in which students
build a small-aperture antenna connected to a low-noise amplifier followed by an SDR,
and with the help of `Virgo`, obtain adequate data to map out the galactic
distribution of neutral hydrogen and/or derive the rotation curve of the Milky Way.

An example observation of the 21-cm hydrogen line acquired and processed with
`Virgo` is shown in \autoref{fig:example}.

![TO-DO: CHANGE FIGURE - Clouds of neutral hydrogen/the 21-cm hydrogen line at (Source name/RA=hh:mm:ss, Dec=dd:mm:ss), observed by the (TBA) Telescope with `Virgo`. The average spectrum (top left), the calibrated spectrum (top center), the dynamic spectrum (top right) and the time series along with the total power distribution (bottom) are all plotted by the software automatically.\label{fig:example}](example.pdf)

# Features

One of the key features of `Virgo` is that it is a polyphase filterbank
spectrometer, offering a  significant reduction in spectral leakage compared to
the more traditional Fourier transform filterbank spectrometers, with a minimal
increase in computational requirements, as described by @Price:2021. In addition to
its data-acquisition functionality that performs data reduction by time-averaging
spectrum samples in real time, `Virgo` carries out automated analysis of the recorded
samples, producing the time-averaged spectrum, the calibrated spectrum, the dynamic
spectrum (waterfall), the time series (power vs time) and the total power
distribution plot of the observation, with the help of the NumPy [@Harris2020] and
Matplotlib [@Hunter:2007] packages.

Because of the nature of their late-stage architecture, the spectra acquired by SDRs
have an unwanted frequency-dependant sensitivity, also known as the bandpass shape.
In general, this frequency response makes it difficult to distinguish
true signals originating from the sky and not from instrumentation artifacts. For
that reason, `Virgo` performs bandpass calibration by taking the ratio of the
observation spectrum (ON) over the calibration spectrum (OFF).

However, because this ratio is arbitrarily scaled (due to the difference in the
noise floor levels), the power axis is automatically rescaled to units of
signal-to-noise ratio.

Furthermore, `Virgo` supports optional median operations, both
in the frequency and time domain, for the suppression of narrowband and/or
short-duration radio frequency interference (RFI), while allowing the user to export
the raw observation data as a FITS/csv-formatted file.

# Example Usage

`Virgo` can either be called directly as a Python script using e.g.,

`python virgo.py -rf 10 -if 20 -bb 20 -f 1420e6 -b 5e6 -c 2048 -t 1 -d 60 -s 10 -n 20 -m 35 -r 1420.4057517667e6 -C calibration.dat -W obs.fits`,

or imported and used as a package:
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
