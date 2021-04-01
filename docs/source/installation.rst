Installation
============

Although Virgo has been tested successfully on both Windows and Mac OS, the required
dependencies are most easily installed on Linux distributions (recommended OS).

Dependencies
^^^^^^^^^^^^

.. note::
   The following two dependencies are only required for **acquiring data with the necessary
   hardware** (software-defined radio). They are not required for planning observations,
   analyzing data, running calculations or any other functionalities provided by the package.

- `GNU Radio <https://wiki.gnuradio.org/index.php/InstallingGR>`_: An open radio framework for digital signal processing
- `gr-osmosdr <https://osmocom.org/projects/gr-osmosdr/wiki>`_: Fundamental I/O GNU Radio blocks supporting most SDRs

For Debian/Ubuntu and derivates, the installation is straightforward:

.. code-block:: bash

   sudo apt install gnuradio gr-osmosdr

If you wish to verify the installation has succeeded, run:

.. code-block:: bash

   gnuradio-companion

Once the graphical interface opens up, check the right-hand side (**Library** panel)
for a block named ``osmocom Source``. If this block shows up, GNU Radio and ``gr-osmosdr``
have been installed on your system successfully.


Installing Virgo
^^^^^^^^^^^^^^^^

Virgo runs on Python 2.7/3.x. To install the package, you can get it directly
from `PyPI <https://pypi.org/project/astro-virgo/>`_ using ``pip``:

.. code-block:: bash

   pip install astro-virgo

By obtaining ``Virgo``, the following packages are installed *automatically*:

* `numpy <https://numpy.org/>`_
* `matplotlib <https://matplotlib.org/>`_
* `astropy <https://www.astropy.org/>`_

You can finally verify the installation by running:

.. code-block:: bash

    python -c "import virgo"

No output indicates a successful installation.


Troubleshooting
^^^^^^^^^^^^^^^^

In certain systems, this command may give an error like this:

.. code-block:: bash

    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    ImportError: No module named virgo

This is a common error when installing Python packages, and it is often
due to a mismatch between the Python versions the ``pip`` and ``python`` commands
refer to.

You can diagnose this with ``pip -V`` and ``python -V``, or you can simply run:

.. code-block:: bash

   python -m pip install astro-virgo

This should load the exact ``pip`` version associated with ``python``.