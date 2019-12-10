# VIRGO: An open-source spectrometer for radio astronomy
![alt text](https://i.imgur.com/PR2wpse.png "VIRGO Spectrometer")

## About VIRGO
**VIRGO** is an easy-to-use **open-source** spectrometer and radiometer based on [Python](https://www.python.org) and [GNU Radio Companion](https://wiki.gnuradio.org/index.php/GNURadioCompanion) (GRC) that is conveniently applicable to any radio telescope working with a GRC-supported software-defined radio (SDR).

A list of GRC-supported SDRs can be found [here](https://wiki.gnuradio.org/index.php/Hardware).

## GRC Data Acquisition Flowgraph
**VIRGO** is a [**polyphase filterbank** spectrometer](https://arxiv.org/abs/1607.03579). The raw I/Q samples are processed in real time using GNU Radio, with the amount of data stored to file being drastically reduced for further analysis. The following flowgraph handles the acquisition and early-stage processing of the data:
![alt text](https://i.imgur.com/2Xp8qnZ.png "Data Acquisition Flowgraph")

One of the advantages of polyphase filterbanks is reduced spectral leakage. The following figure is a comparison between ACS (dotted line), FTF (dashed line) and H PFB with a Hann FFT window (solid line):
![alt text](https://i.imgur.com/e5TwE3w.png "Spectrometer comparison regarding spectral leakage")
