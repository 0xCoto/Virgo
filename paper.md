---
title: 'Virgo: A Versatile Spectrometer for Radio Astronomy'
tags:
  - Python
  - astronomy
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
  - name: E.P. Boven
    affiliation: 3
affiliations:
 - name: Department of Informatics, University of Piraeus, Greece
   index: 1
 - name: Dunlap Institute for Astronomy and Astrophysics, University of Toronto, 50 St. George Street, Toronto, ON M5S 3H4, Canada
   index: 2
 - name: C.A. Muller Radioastronomie Station, Dwingeloo, the Netherlands
   index: 3
date: 1 October 2020
bibliography: paper.bib

---

# Introduction

For the past few decades, radio astronomy has been a rapidly developing area of
observational astronomy. This is due to the fact that a variety of celestial objects emit
electromagnetic radiation at radio wavelengths, which has led to the
development of radio telescopes capable of revealing the otherwise-hidden
astrophysical properties of the universe. An important requirement that makes radio
astronomy observations and analysis possible is an appropriate software pipeline
compatible with the spectrometers with which radio observatories are equipped. In
this work, we present `Virgo`: a versatile software solution for radio telescopes.

# Statement of Need

`Virgo` is a Python package for the acquisition, processing and analysis of
data from radio telescopes. It is an easy-to-use open-source spectrometer and
radiometer based on the GNU Radio framework (https://www.gnuradio.org), and is conveniently
applicable to any radio telescope working with a GNU Radio-supported software-defined
radio (SDR; a radio receiver architecture where some conventional hardware-based
steps are replicated in software, @Dillinger:2003).

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

![Observation of galactic clouds of neutral hydrogen toward the constellation of Cygnus ($\alpha = 20^{\mathrm{h}}$, $\delta = 40^{\circ}$, $l = 77^{\circ}$, $b = 3^{\circ}$), observed by the TLM-18 Telescope in New Jersey, U.S. with `Virgo`. The average spectrum (top left), the calibrated spectrum (top center), the dynamic spectrum (top right) and the time series along with the total power distribution (bottom) are all plotted by the software automatically.\label{fig:example}](example.pdf)

# Features

One of the key features of `Virgo` is that it is a four-tap weighted overlap-add (WOLA) Fourier transform (FT)
spectrometer, offering a significant reduction in spectral leakage compared to
a simple FT filterbank spectrometer that does not make use of the WOLA method, with a minimal
increase in computational requirements [@Crochiere1996]\footnote{The package also supports
a plain FT filterbank pipeline for observatories with limited computational resources.}. In addition to
its data-acquisition functionality that performs data reduction by time-averaging
spectra in real time, `Virgo` also carries out automated analysis of the recorded
samples. The time-averaged spectrum, the calibrated spectrum, the dynamic spectrum
(waterfall), the time series (power vs time) and the total power distribution of the
observation are all automatically computed and plotted with the help of the `Numpy`
[@Harris2020] and `Matplotlib` [@Hunter:2007] packages.

Because of the nature of RF instrumentation radio telescopes are equipped with, the spectra acquired by SDRs
have an unwanted frequency-dependant sensitivity, also known as the bandpass shape.
In general, this frequency response makes it difficult to distinguish true signals,
originating from the sky, from instrumentation artifacts. For that reason, `Virgo`
performs bandpass calibration by taking the ratio of the observed spectrum over
the calibration spectrum. However, because this ratio is arbitrarily scaled (due to
the difference in the noise floor levels), the power axis is automatically rescaled
to units of signal-to-noise ratio. In case the resulted spectrum has an unwanted
slope due to e.g. inconsistent conditions between the calibration and the observation,
the software can also automatically correct poorly-calibrated spectra using linear
regression.

Furthermore, `Virgo` supports optional median operations, both
in the frequency and time domain, for the suppression of narrowband and/or
short-duration radio frequency interference (RFI), while allowing the user to export
the raw observation data as a FITS/csv-formatted file. Frequencies contaminated
with RFI may also be stamped out with the software's built-in channel masking
capability.

Lastly, the package may also be used for the detection of giant pulses (irregularly intense
bursts of radio emission by pulsars). Due to the frequency-dependent dispersion
introduced by plasma distributions in the interstellar medium (ISM), observed pulses
naturally appear smeared, depending on the dispersion measure (integrated column density of
free electrons from the observer to the source). To prevent implied degradations of
the signal-to-noise ratio, incoherent dedispersion is optionally applied to dynamic spectra
of pulsar observations, compensating for the unwanted dispersive effects of the ISM.

By additionally providing the observer with an important set of utilities, `Virgo` also
makes for a great tool for planning (radio) observations. This includes the ability to
compute the position of astronomical sources in the sky for a given date (see \autoref{fig:predict}),
estimate the right ascension and declination given the observer's coordinates along with
the altitude and azimuth the telescope is pointing to and convert equatorial to galactic
coordinates with the help of the `Astropy` package [@astropy:2013; @astropy:2018].

![Example prediction of the location of the Cygnus A radio galaxy (3C 405) in the celestial sphere of the observer.\label{fig:predict}](predict.pdf)

Likewise, the software provides a handy tool for simulating HI profiles based on the
Leiden/Argentine/Bonn (LAB) Survey of Galactic HI [@Kalberla2005], whose spectra (see \autoref{fig:profile}
for an example) can be associated with the integrated 21 cm all-sky map previewer shown
in \autoref{fig:map}.

![Sample HI profile ($\alpha = 20^{\mathrm{h}}30^{\mathrm{m}}$, $\delta = 45^{\circ}$) obtained with the package's `virgo.simulate()` function.\label{fig:profile}](profile.pdf)

![21 cm all-sky map rendered by the software. The red dot indicates the position of the telescope's beam in the sky, provided by the user.\label{fig:map}](map.pdf)

Moreover, the package comes with an integrated frequency-domain RFI measurement pipeline,
allowing observers to rapidly carry out a survey outlining the compatibility of the
telescope's environment with radio observation standards.

Last but not least, the software's modularity allows users to effortlessly integrate
`Virgo`'s functionalities into other pipelines, permitting a variety of automation
applications invloving the acquisition and/or processing of telescope data.

# Example Usage

`Virgo` can either be called directly as a Python script using e.g.,

`python virgo.py -rf 10 -if 20 -bb 20 -f 1420e6 -b 5e6 -c 2048 -t 1 -d 60 -s 10 -n 20 -m 35 -r 1420.4057517667e6 -C calibration.dat -W obs.fits`,

or imported and used as a package:
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

# Future Work

As `Virgo` gets adopted by more and more radio telescopes, the need for expanding the
software's capabilities grow. Additional features that have been proposed include but
are not limited to a more robust and intelligent system for the detection and
mitigation of RFI, and the support for a data acquisition/analysis pipeline for
pulsar astronomy, both of which offer the potential of appealing to a broader user
audience.

# References
