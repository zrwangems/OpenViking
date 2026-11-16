---
type: simulink-block
title: 'To Instrument'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: 'Direct Interface Communication in Simulink'
documentation_page: 'toinstrument'
documentation_source_path: 'toinstrument.html'
language: en
---

# To Instrument

## Ports

Not documented in R2025b.

## Parameters

**Block sample time**
:   The Block sample time parameter is the only setting outside of the
    dialog box tabs. The default value of `-1` sets the
    block to inherit timing. A positive value is used as the sample
    period.

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
:   The total number of bytes that can be stored in the software
    output buffer during a read operation.

**Interface**
:   Select the type of hardware interface to the instrument. Your
    options are those interfaces supported by the Instrument Control Toolbox™ software. The previous figure shows a configuration
    for a serial port interface.

**Logical address**
:   The logical address of the VXI instrument. Used for VISA VXI and
    VISA VXI-GPIB interface types.

**Manufacturer ID**
:   The manufacturer ID of the VISA USB instrument defined as a
    character vector. See ManufacturerID
    property for more information.

**Model code**
:   The model code of the VISA USB instrument defined as a character
    vector. See ModelCode
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
:   Time in seconds, allowed to complete the query operation.

**VISA vendor**
:   The vendor of the VISA instrument used for any of the VISA
    interface types. Your choices are Keysight (formerly Agilent), National Instruments, and Tektronix®.

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

### Send Tab

The **Send** tab is where you define the optional
command sent to the instrument and the format of the sent data.

**Command**
:   This is the command that is sent to the instrument with the
    Simulink data. *This command is
    optional*—if you leave this field blank, the
    Simulink data is sent to the instrument without any prefix or
    additional formatting.

**Output format**
:   Your options are `ASCII`,
    `Binary`, or `Binblock`
    (binary block — the `binblock` format is
    described in the `binblockwrite`
    function reference page).

**ASCII format string**
:   Available only when the format is ASCII, this defines the format
    string for the data. For a list of formats, see the `fprintf`
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

**Tip**

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

The Query Instrument and To Instrument blocks
will be removed in a future release.

## Description

(To be removed) Send simulation data to instrument

The To Instrument block configures and opens an interface to an instrument,
initializes the instrument, and sends data to the instrument. The configuration and
initialization happen at the start of the model execution. The block sends data to
the instrument during model run time.

The block has no output ports. The block has one input port corresponding to the
data sent to the instrument. This data type must be double precision.

**Note**

The To Instrument block can be used with these interfaces: VISA, GPIB, Serial,
TCP/IP, and UDP. It is not supported on these interfaces: SPI, I2C, and
Bluetooth.

### Other Supported Features

- This block supports the use of accelerator mode, but not Rapid
  Accelerator or code generation.
- The block supports the use of model referencing, so that your model
  can include other Simulink® models as modular components.

For more information on these features, see the Simulink documentation.
