Examples
========

Example snippet
^^^^^^^^^^^^^^^

Here's an example code snippet you can try out with ``Virgo`` to acquire data
using a low-cost RTL-SDR receiver:

.. code-block:: python

    import virgo
    
    # Define observation parameters
    obs = {
        'dev_args': '',
        'rf_gain': 30,
        'if_gain': 25,
        'bb_gain': 18,
        'frequency': 1420e6,
        'bandwidth': 2.4e6,
        'channels': 2048,
        't_sample': 1,
        'duration': 60
    }
    
    # Check source position
    virgo.predict(lat=39.8, lon=-74.9, source='Cas A', date='2020-12-26')
    
    # Begin data acquisition
    virgo.observe(obs_parameters=obs, obs_file='observation.dat')
    
    # Analyze data, mitigate RFI and export the data as a CSV file
    virgo.plot(obs_parameters=obs, n=20, m=35, f_rest=1420.4057517667e6,
               obs_file='observation.dat', rfi=[1419.2e6, 1419.3e6],
               dB=True, spectra_csv='spectrum.csv', plot_file='plot.png')

The above script will plot the position of the supernova remnant Cassiopeia A
in the celestial sphere of the observer and configure the device by tuning the
receiver to the given observing parameters and acquire data.

Once the observation is complete (60 sec in this case), the data will be
automatically processed and analyzed, applying a median filter to both the time
series and the frequency domain, and masking a channel range, ultimately supressing
radio-frequency interference. In this example, dB scaling is used, enabling
the plot to support a wide dynamic range.

Lastly, the data is plotted as a PNG file and the
discrete spectrum datapoints are exported as a CSV document for further manual
analysis (optional).

Example observation
^^^^^^^^^^^^^^^^^^^

.. figure:: https://camo.githubusercontent.com/56847be7590a8f4f3bbeb507b6a2f09f002b4a0b717a60abfd99a292dafa8311/68747470733a2f2f692e696d6775722e636f6d2f524f5050577a612e706e67
    :align: center
    :alt: Example observation
    
    *Fig: Observation of galactic clouds of neutral hydrogen toward the constellation of Cygnus
    (α = 20h, δ = 40° , l = 77° , b = 3°), observed by the TLM-18 Telescope in New Jersey, U.S.
    with Virgo. The average spectrum (top left), the calibrated spectrum (top center), the dynamic
    spectrum (top right) and the time series along with the total power distribution (bottom) are all
    plotted by the software automatically.*

Example source prediction
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: https://camo.githubusercontent.com/aa5999c1430f15397f89f47309eab9da55a1bbf3377af94aedd3145281fa49ca/68747470733a2f2f692e696d6775722e636f6d2f6a6e474a4576512e706e67
    :align: center
    :alt: Example source prediction
    
    *Fig: Example prediction of the position of the Cygnus A radio galaxy (3C 405) in the celestial
    sphere of the observer obtained via* ``virgo.predict()``.

Example source prediction
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: https://camo.githubusercontent.com/263822450db159b0d1012b4b7cb60a642457eed276f394c7e4130a30d5e01c15/68747470733a2f2f692e696d6775722e636f6d2f4848536b444a4d2e706e67
    :align: center
    :alt: Example HI profile retrieval
    
    *Fig: Sample HI profile (α = 20h30m, δ = 45°) obtained with the package's* ``virgo.simulate()`` *function.*

Offline experiments
^^^^^^^^^^^^^^^^^^^

For users who wish to experiment with the package's data acquisition, processing and analysis
pipelines, but do not have any supported hardware at hand, an example observation file
is included in the repository of the software on `GitHub <https://github.com/0xCoto/Virgo/tree/master/joss_example>`_.

This folder includes three files, which can be used to test the software without any access to equipment:

- ``observation.dat``: ON-source observation
- ``calibration.dat``: OFF-source observation (reference calibration)
- ``joss_example.py``: Example script for (spectrum) calibration and data visualization