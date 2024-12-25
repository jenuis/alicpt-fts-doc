.. inlab

In-lab Test
===================

For the in-lab test, only the main FTS part is used and the output is directedly measured by **Power Meter** or low-temperature millimeter wave dectector for RF source and black-body source, respectively. In this sense, the following steps are required to perform the in-lab test:

.. note::
    Follow necessary steps in :ref:`Hardware Preparation` before starting the in-lab test.

- Open the application ``FTS.exe``.
- Select and set ``SM Controller``.
- Select ``Stepping`` mode.
- Set ``Loop Number``.
- Set ``Min Pos`` and ``Max Pos`` to adjust the spectra resolution.
- Set ``Step`` and ``Pause Time``.
- Confirm ``Linear Encoder Name`` is valid and with ``ctr0`` selected.
- Make sure ``On Site Switch`` is switched off.
- Leave ``Trigger Source`` empty.
- Select and set the chopper signal in the first element of ``DAQmx Channels`` (``Saving Name`` can be **chopper**).
- Select and set the detector signal in the second element of ``DAQmx Channels`` (``Saving Name`` can be **detector**).
- Fill ``Data File Suffix`` and ``Comments`` on needs.
- Click ``Start``.
