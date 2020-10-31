#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Run Observation
# GNU Radio version: 3.7.13.5
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy as np
import osmosdr
import time


class run_observation(gr.top_block):

    def __init__(self, bandwidth=2e6, bb_gain=20, channels=1024, dev_args='', duration=60, frequency=1420e6, if_gain=20, obs_file='observation.dat', rf_gain=30, t_sample=1):
        gr.top_block.__init__(self, "Run Observation")

        ##################################################
        # Parameters
        ##################################################
        self.bandwidth = bandwidth
        self.bb_gain = bb_gain
        self.channels = channels
        self.dev_args = dev_args
        self.duration = duration
        self.frequency = frequency
        self.if_gain = if_gain
        self.obs_file = obs_file
        self.rf_gain = rf_gain
        self.t_sample = t_sample

        ##################################################
        # Variables
        ##################################################
        self.sinc_sample_locations = sinc_sample_locations = np.arange(-np.pi*4/2.0, np.pi*4/2.0, np.pi/channels)
        self.sinc = sinc = np.sinc(sinc_sample_locations/np.pi)
        self.custom_window = custom_window = sinc*np.hamming(4*channels)

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + dev_args )
        self.osmosdr_source_0.set_sample_rate(bandwidth)
        self.osmosdr_source_0.set_center_freq(frequency, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(rf_gain, 0)
        self.osmosdr_source_0.set_if_gain(if_gain, 0)
        self.osmosdr_source_0.set_bb_gain(bb_gain, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.fft_vxx_0 = fft.fft_vcc(channels, True, (window.blackmanharris(channels)), True, 1)
        self.blocks_stream_to_vector_0_2 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, channels)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, channels)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, channels)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, channels)
        self.blocks_multiply_const_vxx_0_0_0_0 = blocks.multiply_const_vcc((custom_window[0:channels]))
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vcc((custom_window[channels:2*channels]))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((custom_window[2*channels:3*channels]))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((custom_window[-channels:]))
        self.blocks_integrate_xx_0 = blocks.integrate_ff(int(t_sample*bandwidth/channels), channels)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, int(duration*bandwidth))
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*channels, obs_file, True)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_gr_complex*1, channels)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, channels*2)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, channels*3)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(channels)
        self.blocks_add_xx_0 = blocks.add_vcc(channels)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_integrate_xx_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_vector_0_2, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_stream_to_vector_0_1, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_integrate_xx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_2, 0), (self.blocks_multiply_const_vxx_0_0_0_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_head_0, 0))

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self.osmosdr_source_0.set_sample_rate(self.bandwidth)
        self.blocks_head_0.set_length(int(self.duration*self.bandwidth))

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self.osmosdr_source_0.set_bb_gain(self.bb_gain, 0)

    def get_channels(self):
        return self.channels

    def set_channels(self, channels):
        self.channels = channels
        self.set_custom_window(self.sinc*np.hamming(4*self.channels))
        self.set_sinc_sample_locations(np.arange(-np.pi*4/2.0, np.pi*4/2.0, np.pi/self.channels))
        self.blocks_multiply_const_vxx_0_0_0_0.set_k((self.custom_window[0:self.channels]))
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.custom_window[self.channels:2*self.channels]))
        self.blocks_multiply_const_vxx_0_0.set_k((self.custom_window[2*self.channels:3*self.channels]))
        self.blocks_multiply_const_vxx_0.set_k((self.custom_window[-self.channels:]))
        self.blocks_delay_0_1.set_dly(self.channels)
        self.blocks_delay_0_0.set_dly(self.channels*2)
        self.blocks_delay_0.set_dly(self.channels*3)

    def get_dev_args(self):
        return self.dev_args

    def set_dev_args(self, dev_args):
        self.dev_args = dev_args

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration
        self.blocks_head_0.set_length(int(self.duration*self.bandwidth))

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.osmosdr_source_0.set_center_freq(self.frequency, 0)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self.osmosdr_source_0.set_if_gain(self.if_gain, 0)

    def get_obs_file(self):
        return self.obs_file

    def set_obs_file(self, obs_file):
        self.obs_file = obs_file
        self.blocks_file_sink_0.open(self.obs_file)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.osmosdr_source_0.set_gain(self.rf_gain, 0)

    def get_t_sample(self):
        return self.t_sample

    def set_t_sample(self, t_sample):
        self.t_sample = t_sample

    def get_sinc_sample_locations(self):
        return self.sinc_sample_locations

    def set_sinc_sample_locations(self, sinc_sample_locations):
        self.sinc_sample_locations = sinc_sample_locations
        self.set_sinc(np.sinc(self.sinc_sample_locations/np.pi))

    def get_sinc(self):
        return self.sinc

    def set_sinc(self, sinc):
        self.sinc = sinc
        self.set_custom_window(self.sinc*np.hamming(4*self.channels))
        self.set_sinc(np.sinc(self.sinc_sample_locations/np.pi))

    def get_custom_window(self):
        return self.custom_window

    def set_custom_window(self, custom_window):
        self.custom_window = custom_window
        self.blocks_multiply_const_vxx_0_0_0_0.set_k((self.custom_window[0:self.channels]))
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.custom_window[self.channels:2*self.channels]))
        self.blocks_multiply_const_vxx_0_0.set_k((self.custom_window[2*self.channels:3*self.channels]))
        self.blocks_multiply_const_vxx_0.set_k((self.custom_window[-self.channels:]))


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--bandwidth", dest="bandwidth", type="eng_float", default=eng_notation.num_to_str(2e6),
        help="Set bandwidth [default=%default]")
    parser.add_option(
        "", "--bb-gain", dest="bb_gain", type="eng_float", default=eng_notation.num_to_str(20),
        help="Set bb_gain [default=%default]")
    parser.add_option(
        "", "--channels", dest="channels", type="intx", default=1024,
        help="Set channels [default=%default]")
    parser.add_option(
        "", "--dev-args", dest="dev_args", type="string", default='',
        help="Set dev_args [default=%default]")
    parser.add_option(
        "", "--duration", dest="duration", type="eng_float", default=eng_notation.num_to_str(60),
        help="Set duration [default=%default]")
    parser.add_option(
        "", "--frequency", dest="frequency", type="eng_float", default=eng_notation.num_to_str(1420e6),
        help="Set frequency [default=%default]")
    parser.add_option(
        "", "--if-gain", dest="if_gain", type="eng_float", default=eng_notation.num_to_str(20),
        help="Set if_gain [default=%default]")
    parser.add_option(
        "", "--obs-file", dest="obs_file", type="string", default='observation.dat',
        help="Set obs_file [default=%default]")
    parser.add_option(
        "", "--rf-gain", dest="rf_gain", type="eng_float", default=eng_notation.num_to_str(30),
        help="Set rf_gain [default=%default]")
    parser.add_option(
        "", "--t-sample", dest="t_sample", type="intx", default=1,
        help="Set t_sample [default=%default]")
    return parser


def main(top_block_cls=run_observation, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(bandwidth=options.bandwidth, bb_gain=options.bb_gain, channels=options.channels, dev_args=options.dev_args, duration=options.duration, frequency=options.frequency, if_gain=options.if_gain, obs_file=options.obs_file, rf_gain=options.rf_gain, t_sample=options.t_sample)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
