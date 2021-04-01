.. Virgo documentation master file

.. |joss| image:: https://joss.theoj.org/papers/612c2634c1dd83749e95a93449740861/status.svg
   :target: https://joss.theoj.org/papers/612c2634c1dd83749e95a93449740861

.. |python| image:: https://img.shields.io/badge/python-2.7%20%7C%203.x-green
   :target: https://www.python.org/

.. |pypi| image:: https://img.shields.io/pypi/v/astro-virgo
   :target: https://pypi.python.org/pypi/astro-virgo

.. |astropy| image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
   :target: https://www.astropy.org/

.. |license| image:: https://img.shields.io/github/license/0xCoto/Virgo?color=yellow
   :target: https://github.com/0xCoto/Virgo/blob/master/LICENSE

.. |last-commit| image:: https://img.shields.io/github/last-commit/0xCoto/Virgo.svg?colorB=e6c000
   :target: https://github.com/0xCoto/Virgo

.. |issues| image:: https://img.shields.io/github/issues/fpavogt/fcmaker.svg?colorB=b4001e   
   :target: https://github.com/0xCoto/Virgo/issues

.. |stars| image:: https://img.shields.io/github/stars/0xCoto/Virgo.svg?style=social&label=Stars
   :target: https://github.com/0xCoto/Virgo

.. |github| image:: https://img.shields.io/github/release/0xCoto/Virgo.svg
   :target: https://github.com/0xCoto/Virgo/releases   


.. figure:: https://camo.githubusercontent.com/6a51d3998787aecfa34154eb524fea7462fe9bad882a31121ae6ef26de2858da/68747470733a2f2f692e696d6775722e636f6d2f6c48324f4f54642e706e673f7261773d74727565
    :align: center
    :alt: Virgo Spectrometer

    |joss| |python| |pypi| |astropy| |license|


About
-----

``Virgo`` is an easy-to-use **open-source** spectrometer and radiometer based on `Python <https://www.python.org>`_ and
`GNU Radio <https://wiki.gnuradio.org>`_ (GR) that is conveniently applicable to any radio telescope working with a
GR-supported software-defined radio (SDR). In addition to data acquisition, ``Virgo`` also carries out automated analysis
of the recorded samples, producing an averaged spectrum,a calibrated spectrum, a dynamic spectrum (waterfall),
a time series (power vs time) and a total power distribution plot.

Lastly, an important set of utilities is provided to observers, making the package for a great tool for planning (radio)
observations, estimating the system sensitivity of an instrument, and many more.


Key Features
^^^^^^^^^^^^


- 4-tap weighted overlap-add (WOLA) Fourier transform spectrometer
- - Reduced FFT sidelobes
- - Plain FT filterbank pipeline also supported for observatories with limited computational resources
- Adjustable SDR parameters
- - Device arguments
- - RF/IF/BB Gain
- Header file
- - Observation parameters automatically passed to corresponding ``.header`` file
- - Includes logged MJD (at observation *t*\ :sub:`0`)
- Spectral line support
- - Spectrum calibration
- - - *y* axis is automatically rescaled to S:N units with line masking
- - - Optional automatic slope correction (based on linear regression) for poorly-calibrated spectra
- - Supports median operation for RFI mitigation on the frequency-domain (adjustable *n*-factor)
- - RFI channel masking
- - Adjustable *f*\ :sub:`rest` for the observation of any spectral line (not just HI)
- - Secondary axes for relative velocity automatically adjusted accordingly
- - Prevention against strong narrowband RFI rescaling subplot
- - The average spectra, calibration spectra and calibrated spectra are optionally saved as a ``csv`` file for further analysis
- Continuum support
- - Supports median operation for time-varying RFI mitigation (adjustable *n*-factor)
- - Total power distribution (histogram) displayed, both for raw and clean data
- - - Best Gaussian fits computed automatically
- - Prevention against strong short-duration RFI rescaling subplot
- - Time series optionally saved as a ``csv`` file for further analysis
- Pulsars
- - Incoherent dedispersion support for giant pulse search (and FRB follow-up, assuming DM is known)
- Dynamic spectrum (waterfall)
- - Optionally saved as a ``FITS`` file for further advanced/custom analysis
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
- Works directly via ``python virgo.py``, or as a module (see Usage)

Contents
---------
.. toctree::
   :maxdepth: 1
   
   About <self>
   installation
   usage
   examples
   reference
   license
   GitHub <https://github.com/0xCoto/Virgo>
