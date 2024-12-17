.. file

File
===================

There are three types of file for the FTS application: the data file (``.tdms`` format), the configuration file (``.ini`` format) and the log file (``.txt`` format).

Data File
-------------------
The data file utilizes LabVIEW™'s `TDMS file format <https://www.ni.com/en/support/documentation/supplemental/06/the-ni-tdms-file-format.html>`_, where the data is classifed by groups and channels. There are two groups of the data file, i.e., ``Linear Encoder`` and ``DAQmx``. Attributes are also supported in TDMS file. For each tree (group) and leaf (channel), attributes can be attached. Currently, ``Comments`` is attached in the root and ``Sampling_Rate`` is attached for the ``Linear Encoder`` and ``DAQmx`` groups. The hierarchy of a typical calibration data file is shown below.

- FTS_test_2024-12-17_17-00-22.tdms (Attributes: ``Comments`` = "This is a test file")
    - ``Linear Encoder`` (Attributes: ``Sampling_Rate`` = 100000)
        - ``Untitled``: [-99.99, -99.80, -99.70, ..., -0.10, 0.00]
    - ``DAQmx`` (Attributes: ``Sampling_Rate`` = 1000)
        - ``Second Pulse``: [0.0, 0.0, 2.5, 5.0, 5.0, 5.0, 2.5, 0.0, ..., 0.0]

.. note:: 
    TDMS file can be quickly viewed by Excel.

Config File
-------------------
The configuration file named ``FTS.ini`` should be put under the same directory as ``FTS.exe``. The config file is automatically loaded after the initialization of the ``FTS.exe``. Once loaded, the corresponding panel values are changed or the corresponding commands will be sent to the instruments. All the settings should be put under the ``FTS`` section. Currently, only the ``Data Saving Folder`` is configured by key ``DataFolder``.

.. code-block:: ini
    
    [FTS]
    ; Change the value of "Data Saving Folder"
    DataFolder="E:"

Log File
-------------------
The log file simply records the messages outputted from the **Log Panel** in the FTS application. Log file is important to trace the application errors. If an unexpected error is reported, one should send the lastest log file along with the screen shot of the error message to the developer (see :ref:`Contact`) for help.

.. note::
    The location of the log file is in the same directory as the data file, i.e., under ``Data Saving Folder`` specified in the FTS application. 