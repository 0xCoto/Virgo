Usage
=====

Module import
^^^^^^^^^^^^^

``Virgo`` can be imported and used as a module (traditional method):

.. code-block:: python

    # Load package
    import virgo
    
    # Example functions
    virgo.observe(...)
    virgo.plot(...)

Script method
^^^^^^^^^^^^^

Alternatively, it can be called directly as a Python script using:

.. code-block:: bash

    python virgo.py [arguments]

The latter method is typically preferred for quick hardware-verification tests etc.,
although using ``Virgo`` as a module offers much more versatility.

You can view the full list of arguments by running:

.. code-block:: bash

    python virgo.py -h

The following parameters are more thoroughly described in section **Functions**:

.. code-block:: none

    usage: virgo.py [-h] [-da DEV_ARGS] [-rf RF_GAIN] [-if IF_GAIN] [-bb BB_GAIN]
                    -f FREQUENCY -b BANDWIDTH -c CHANNELS -t T_SAMPLE
                    [-d DURATION] [-s START_IN] [-o OBS_FILE] [-C CAL_FILE] [-db]
                    [-n N] [-m M] [-r F_REST] [-W WATERFALL_FITS] [-S SPECTRA_CSV]
                    [-P POWER_CSV] [-p PLOT_FILE]
    
    optional arguments:
      -h, --help            show this help message and exit
      -da DEV_ARGS, --dev_args DEV_ARGS
                            SDR Device Arguments (osmocom Source)
      -rf RF_GAIN, --rf_gain RF_GAIN
                            SDR RF Gain (dB)
      -if IF_GAIN, --if_gain IF_GAIN
                            SDR IF Gain (dB)
      -bb BB_GAIN, --bb_gain BB_GAIN
                            SDR BB Gain (dB)
      -f FREQUENCY, --frequency FREQUENCY
                            Center Frequency (Hz)
      -b BANDWIDTH, --bandwidth BANDWIDTH
                            Bandwidth (Hz)
      -c CHANNELS, --channels CHANNELS
                            Number of Channels (FFT Size)
      -t T_SAMPLE, --t_sample T_SAMPLE
                            FFT Sample Time (s)
      -d DURATION, --duration DURATION
                            Observing Duration (s)
      -s START_IN, --start_in START_IN
                            Schedule Observation (s)
      -o OBS_FILE, --obs_file OBS_FILE
                            Observation Filename
      -C CAL_FILE, --cal_file CAL_FILE
                            Calibration Filename
      -db, --db             Use dB-scaled Power values
      -n N, --median_frequency N
                            Median Factor (Frequency Domain)
      -m M, --median_time M
                            Median Factor (Time Domain)
      -r F_REST, --rest_frequency F_REST
                            Spectral Line Rest Frequency (Hz)
      -W WATERFALL_FITS, --waterfall_fits WATERFALL_FITS
                            Filename for FITS Waterfall File
      -S SPECTRA_CSV, --spectra_csv SPECTRA_CSV
                            Filename for Spectra csv File
      -P POWER_CSV, --power_csv POWER_CSV
                            Filename for Spectra csv File
      -p PLOT_FILE, --plot_file PLOT_FILE
                            Plot Filename