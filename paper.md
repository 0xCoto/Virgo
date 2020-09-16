---
title: 'VIRGO: A Versatile Spectrometer for Radio Astronomy'
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

# Summary

For the last decades, radio astronomy has been undoubtedly among the most
fundamental branches of astrophysics. This is due to the fact that a variety of
celestial objects tend to emit electromagnetic radiation at radio wavelengths,
which has lead to the development of competent radio telescopes, capable of
revealing the otherwise-hidden astrophysical properties of the universe. An
important requirement that deems radio astronomy observations and analyses
possible, is of course an appropriate software pipeline compatible with the
spectrometers with which radio observatories are equipped.

`%Comment: should 'competent' be changed to a different word?`

`%Comment: is 'astrophysical' redundant/obvious since I'm referring to 'universe' anyway?`

The forces on stars, galaxies, and dark matter under external gravitational
fields lead to the dynamical evolution of structures in the universe. The orbits
of these bodies are therefore key to understanding the formation, history, and
future state of galaxies. The field of "galactic dynamics," which aims to model
the gravitating components of galaxies to study their structure and evolution,
is now well-established, commonly taught, and frequently used in astronomy.
Aside from toy problems and demonstrations, the majority of problems require
efficient numerical tools, many of which require the same base code (e.g., for
performing numerical orbit integration).

# Statement of need

`VIRGO` is a Python package for the acquisition, processing and analysis of
data from radio telescopes. It is an easy-to-use open-source spectrometer and
radiometer based on the `GNU Radio` framework, and is conveniently applicable
to any radio telescope working with a GR-supported software-defined radio (SDR).
In addition to its data acquisition functionality, `VIRGO` carries out automated
analysis of the recorded samples, producing the average spectrum, the calibrated
spectrum, the dynamic spectrum (waterfall), the time series (power vs time) and
the total power distribution plot of the observation, with the help of the `numpy`
and `matplotlib` packages.

`%Comment: Should I cite gnu radio/numpy/matplotlib?`

`%Comment: Should "with the help of numpy/matplotlib" be rephrased a bit differently?`

Designed to be used by both researchers and students in the field of radio
astronomy, `VIRGO` has already been adapted in a number of small and
large-aperture radio telescopes, permitting both spectral and continuum
observations with great success. These instruments include the ISEC TLM-18 (18m),
the ACRO RT-320 (3.2m), the JRT (1.9m), the PICTOR Telescope (1.5m), among others.
An example observation of the 21-cm hydrogen line acquired and processed with
`VIRGO` is shown in \autoref{fig:example}.

`%Comment: "with great success" - is this inappropriately subjective? Would a
different phrase be more suitable?`

`%Comment: Do the telescopes require some sort of a reference? What if not quite
applicable (i.e. telescope doesn't have an official website etc.)?`

`%Comment: Maybe I can ask Paul to try VIRGO out with the Dwingeloo 25m to add
another large-aperture antenna to the list?`

`%Comment: TBA (most likely within a few days, once I get a chance to implement
the S/W): Allen Telescope Array (42x 6.1m)`

![Clouds of neutral hydrogen/the 21-cm hydrogen line at (Source name/RA=hh:mm:ss, Dec=dd:mm:ss), observed by the (TBA) Telescope with `VIRGO`. The average spectrum (top left), the calibrated spectrum (top center), the dynamic spectrum (top right) and the time series, along with the total power distribution (bottom right) are all plotted by the software automatically.\label{fig:example}](example.pdf)

`%Comment: Add example observation (use .pdf instead of .png for optimal quality)`

# Features

One of the key features of `VIRGO` is that it is a polyphase filterbank
spectrometer, offering a  significant reduction in spectral leakage compared to
the more traditional Fourier transform filterbank spectrometers, with a minimal
increase in computational requirements, as described in greater detail by Danny
C. Price (2018). Furthermore, `VIRGO` supports optional median operations, both
in the frequency and time domain, for the suppression of narrowband and/or
short-duration radio frequency interference, while allowing the user to export
the raw observation data as a FITS/csv-formatted file for further manual
intervention analysis.

`%Comment: Must cite Price according to his comment about rev. 2: https://arxiv.org/abs/1607.03579`

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
virgo.observe(obs_parameters=observation, obs_file='observation.dat', start_in=10)

# Analyze data, mitigate RFI and export the data as a FITS file
virgo.plot(obs_parameters=observation, n=20, m=35, f_rest=1420.4057517667e6,
           obs_file='observation.dat', cal_file='calibration.dat',
           waterfall_fits='obs.fits', plot_file='plot.png')
```	


# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Fenced code blocks are rendered with syntax highlighting:
```python
for n in range(10):
    yield f(n)
```	

# References
