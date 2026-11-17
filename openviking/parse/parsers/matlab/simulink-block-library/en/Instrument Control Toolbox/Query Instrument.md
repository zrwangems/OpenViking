---
type: simulink-block
title: 'Query Instrument'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'queryinstrument'
documentation_source_path: 'queryinstrument.html'
language: en
---

# Query Instrument

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

**Block sample time**
:   The Block sample time parameter is the only setting outside of the
    dialog box tabs. The default value is `1`. Setting the
    value to `-1` sets the block to inherit timing. A
    positive value is used as the sample period.

### Hardware Configuration Tab

The **Hardware Configuration** tab is where you
define the settings for communications with your instrument. You have two
choices about establishing an interface:

- Specify a new hardware configuration.
- Use an interface object from the MATLAB® workspace.

The following figure shows the **Hardware
Configuration** tab set to specify a new hardware configuration
using a serial port interface.

Because some parameters apply to multiple interface types, they appear here in
alphabetical order.

**Baudrate**
:   The rate at which bits are transmitted for the serial or VISA
    serial interface.

**Board index**
:   The index of the board used for GPIB, VISA GPIB, VISA TCPIP, or
    VISA USB interface to the instrument.

**Board vendor**
:   The vendor of the GPIB board used for the interface to the
    instrument. Your choices are Keysight® (formerly Agilent®), ICS Electronics™, Measurement Computing™ (MCC), and National Instruments™.

**Chassis index**
:   The index number of the VXI chassis. Used for VISA VXI and VISA
    VXI-GPIB interface types.

**Buffer size**
:   The total number of bytes that can be stored in the software input
    buffer during a read operation.

**Interface**
:   Select the type of hardware interface to the instrument. Your
    options are those interfaces supported by the Instrument Control Toolbox™ software. The previous figure shows a configuration
    for a serial port interface.

**Logical address**
:   The logical address of the VXI instrument. Used for VISA VXI and
    VISA VXI-GPIB interface types.

**Manufacturer ID**
:   The manufacturer ID of the VISA USB instrument. See ManufacturerID
    property for more information.

**Model code**
:   The model code of the VISA USB instrument. See ModelCode
    property for more information.

**Port**
:   The port for the serial interface: COM1, COM2, etc.

**Primary address**
:   The primary address of the instrument on the GPIB.

**Remote host**
:   The host name or IP address of the instrument. Used for UDP,
    TCPIP, or VISA TCPIP interface types.

**Remote port**
:   The port on the instrument or remote host used for communication.
    Used for UDP, TCPIP, or VISA TCPIP interface types.

**Secondary address**
:   The secondary address of the instrument on the GPIB.

**Serial number**
:   The serial number of the VISA USB instrument defined as a
    character vector. See SerialNumber
    property for more information.

**Timeout**
:   Time in seconds allowed to complete the query operation.

**VISA vendor**
:   The vendor of the VISA used for any of the VISA interface types.
    Your choices are Keysight (formerly Agilent), National Instruments, and Tektronix®.

**Use interface object from MATLAB workspace**
:   Select this option to use an interface object from the MATLAB workspace.

**Workspace object**
:   Enter the object name that you want to use from the MATLAB workspace.

### Instrument Initialization Tab

The **Instrument Initialization** tab is where
you define what happens when you first open your connection to the
instrument.

**None**
:   The default initialization option is none.

**Send string**
:   A string sent to the instrument as an instrument command to
    initialize the instrument or set it up in a known state.

**Execute function**
:   Any function that has as its only argument the interface object
    representing the instrument. You can write this function to include
    several instrument commands and initialization data.

### Query Tab

The **Query** tab is where you define the
optional query command, set the format for the response, and define what the
block does after the initial instrument response.

**Query command**
:   This is the query command that is sent to the instrument. It is
    usually a request for instrument status or data. *This
    command is optional* — if you are retrieving
    information or data from the instrument and no query command is
    necessary to do that, you can leave this field blank.

**Data format**
:   Your options are `ASCII`,
    `Binary`, or `Binblock`
    (binary block — the `binblock` format is
    described in the `binblockwrite`
    function reference page).

**ASCII format string**
:   Available only when the format is `ASCII`, this
    defines the format string for the data. For a list of formats, see
    the `fscanf`
    function.

**Precision**
:   Used for binary or binblock format. Your options are:

    - `8-bit integer` (default)
    - `16-bit integer`
    - `32-bit integer`
    - `8-bit unsigned integer`
    - `16-bit unsigned integer`
    - `32-bit unsigned integer`
    - `32-bit float`
    - `64-bit float`

**Byte order**
:   When using binary or binblock format with more than 8 bits, you
    can specify the instrument's byte order for the data. Your options
    are `Big Endian` or
    `Little Endian`.

**Binary values to read**
:   Used for binary format. Specify the number of binary values to
    read from the instrument.

**Remove additional bytes from input buffer**
:   Select this option if you want to remove any additional bytes from
    the input buffer before querying.

**After initial response**
:   This defines the action to take after the first response from the
    instrument. Your options are Repeat query for new data, Recycle
    original data, Hold final value, Output zero, or Stop simulation.

**Enable frame output**
:   A frame is a sequence of samples combined into a single vector. In
    frame-based processing all the samples in a frame are processed
    simultaneously. In sample-based processing, samples are processed
    one at a time. The advantage of frame-based processing is that it
    can greatly increase the speed of a simulation. For example, you
    might use frames if you are reading a waveform from your instrument
    rather than a single-point measurement.

**Frame size**
:   Frame size determines the number of samples in a frame.

**Note**

Hardware information shown in the dialog box is determined and cached when
you first open the dialog box. To refresh the display with new values,
restart MATLAB.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

### R2024b: Errors

This block throws an error when added to a model. Opening any existing model
with this block causes an error. The model cannot be simulated because of this
error. You can still open the block parameter dialog and see the parameter
values.

Use the interface-specific blocks instead:

- Serial
  Configuration
- Serial Receive
- Serial Send
- TCP/IP
  Receive
- TCP/IP Send
- UDP Receive
- UDP Send
- VISA

These interface-specific blocks all support additional properties
and have improved performance compared to Query Instrument and
To Instrument.

### R2023b: To be removed

The Query Instrument and To Instrument
Simulink blocks will be removed.

## Description

(To be removed) Query or read instrument data

The Query Instrument block configures and opens an interface to an instrument,
initializes the instrument, and queries the instrument for data. The configuration
and initialization happen at the start of the model execution. The block queries the
instrument for data during model run time.

The block has no input ports. The block has one output port corresponding to the
data received from the instrument.

### Other Supported Features

- This block supports the use of accelerator mode, but not Rapid
  Accelerator or code generation.
- The block supports the use of model referencing, so that your model
  can include other Simulink® models as modular components.

For more information on these features, see the Simulink documentation.
