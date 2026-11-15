---
type: simulink-block
title: 'SDRu Transmitter'
family: 'wireless-testbench'
product_id: 'wireless-testbench'
product_name: 'Wireless Testbench'
documentation_release: R2025b
official_category: 'Live Data I/O / Radio I/O'
documentation_page: 'sdrutransmitter'
documentation_source_path: 'ref/sdrutransmitter.html'
language: en
---

# SDRu Transmitter

## Ports

### Input

### **data** — Input data column vector | matrix

Input data sent to the radio hardware, specified as a column vector or
matrix. For a single channel radio, **data** is a
column vector. For a multichannel radio, **data** is a
matrix, where each column contains a channel of data. The range of
values for **data** are `[-1 1]` for
`double` or `single` precision
data and `[-32768, 32767]` for `int16`
data.

#### Dependencies

To specify the output data type, use the **Output data
type** parameter.

**Data Types:** `int16` | `single` | `double`
**Complex Number Support:** Yes

### **fc** — Center frequency setting positive scalar

Center frequency setting in Hz, specified as a positive scalar.

**Example:**
`88.9e6` tunes the transmitter to a center frequency of
88.9 MHz.

#### Dependencies

To enable this port, set **Source of center
frequency** parameter to `Input
Port`.

**Data Types:** `double`

### **LO offset** — Local oscillator offset scalar

Local oscillator (LO) offset in Hz, specified as a scalar.

**Example:**
`10` sets the LO offset to 10 Hz.

#### Dependencies

To enable this port, set **Source of LO offset**
parameter to `Input Port`.

**Data Types:** `double`

### **gain** — Transmitter gain setting scalar | vector

Transmitter gain setting in dB, specified as a scalar or vector. The
valid range of this gain depends on the RF daughterboard of the
USRP device.

Transmitter gain setting accounts combined analog and digital
transmitter gains of the USRP hardware.

- For a single channel, specify the value for the gain as a
  scalar in dB.
- For multiple channels that use the same gain value, specify
  the gain as a scalar in dB. The gain is set by scalar
  expansion.
- For multiple channels that use different gains, specify the
  values in a vector, for example, `[5 12]`. The
  *N*th element of the vector is applied to
  the *N*th channel specified by **Channel mapping**.

**Example:**
`10` sets the transmitter gain level to 10
dB.

#### Dependencies

To enable this port, set **Source of gain**
parameter to `Input Port`.

**Data Types:** `double`
### Output

### **underrun** — Data discontinuity flag `0` | `1`

Data discontinuity flag, returned as one of these values.

- `0` — Data samples are not lost.
- `1` — Data samples are lost.

Use this port as a diagnostic tool to determine real-time
operation of the SDRu Transmitter block. If your model is not running in real
time, you can adjust parameters that reduce the number of transported
samples. To approach or achieve real-time performance, you can increase
the interpolation factor.

#### Dependencies

To enable this port, select **Enable overrun output
port**.

### **refLocked** — Lock status of USRP radio to 10 MHz clock signal `0` | `1`

Lock status of the USRP radio to the 10 MHz clock signal, returned as one of these
Boolean values.

- `0` — The USRP radio is not locked to the 10 MHz clock signal
  of an external clock source or a global positioning system
  disciplined oscillator (GPSDO).
- `1` — The USRP radio is locked to the 10 MHz clock signal of
  an external clock source or a GPSDO.

#### Dependencies

To enable this port, select the **Enable ref\_locked output
port** parameter.

**Data Types:** `Boolean`

### **gpsLocked** — Lock status of GPSDO to GPS constellation `0` | `1`

Lock status of the GPSDO to the GPS constellation, returned as one of
these Boolean values.

- `0` — The GPSDO is not locked to the GPS
  constellation.
- `1` — The GPSDO is locked to the GPS
  constellation.

#### Dependencies

To enable this port, select the **Enable gps\_locked output
port** parameter.

**Data Types:** `Boolean`

## Parameters

When you set block
parameter values, the SDRu Transmitter block first checks that the values have the correct data
types. Even if the values pass those checks, the values can still be out of range for the
radio hardware. In that case, the radio hardware sets the actual value as close to the
specified value as possible. When you next synchronize the block with the radio hardware by
clicking **Info**, a dialog box open to display the actual values along
with other radio information.

If a parameter is listed as tunable, then you can change its value during simulation.

### Radio Connection

### **Platform** — Radio to configure `E320` | `N300` | `N310` | `N320/N321` | `X300` | `X310` | `X410`

Radio to configure, specified as one of these options.

- `E320` — A
  connected USRP E320 radio. *(since R2025a)*
- `N300` — A connected USRP N300 radio.
- `N310` — A connected USRP N310 radio.
- `N320/N321` — A connected USRP N320 or USRP N321 radio.
- `X300` — A connected USRP X300 radio.
- `X310` — A connected USRP X310 radio.
- `X410` — A
  connected USRP X410 radio. *(since R2025a)*

### **IP address** — IP address of radio hardware `192.168.10.2` (default) | dotted quad expression

IP address of the radio hardware, specified as a dotted quad expression.

This parameter must match the physical IP address of the radio hardware assigned when you
set up your radio using the Radio Setup
wizard. If you
configure the radio hardware with an IP address other than the default, update
**IP address** accordingly.

The **IP address** list displays IP addresses for USRP devices attached to the host computer. To specify another known dotted quad IP address, enter it directly into this field.

### **Refresh Device List** — Refresh the list of connected devices button

Refresh the list of all connected devices to update the **IP
address** list. The updated list retains the value in focus before
**Refresh Device List** is selected, even if the device with that
setting was disconnected.

### **Info** — Provides information about device button

Provides information about
the **Platform** of the radio associated with **IP
address**. When you select the **Info** button, a new
dialog box opens with information about the specified device.

### Radio Properties

### **Channel mapping** — Channel output mapping for radio or bundled radios `1` (default) | integer | vector

Channel output mapping for radio or bundled radios, specified as a
positive integer scalar or vector. This table shows valid values for
various radio platforms.

| Platform Value | **Channel mapping** Value |
| --- | --- |
| `E320` *(since R2025a)* | - When **IP address**   includes one IP address, specify this parameter as   `1`, `2`, or   `[1 2]`. - When **IP address**   includes *N* IP addresses,   specify this parameter as   1-by-2*N* row vector. |
| `N300` | - When **IP address**   includes one IP address, specify this parameter as   `1`, `2`, or   `[1 2]`. - When **IP address**   includes *N* IP addresses,   specify this parameter as   1-by-2*N* row vector. |
| `N310` | - When **IP address**   includes one IP address, specify this parameter as   1-, 2-, 3-, or 4-element row vector of channel   numbers from the set {1, 2, 3, 4} - When **IP address**   includes *N* IP addresses,   specify this parameter as   1-by-4*N* row vector. |
| `N320/N321` | - When **IP address**   includes one IP address, specify this parameter as   `1`, `2`, or   `[1 2]`. - When **IP address**   includes *N* IP addresses,   specify this parameter as   1-by-2*N* row vector. |
| `X300` or `X310` | - When **IP address**   includes one IP address, specify this parameter as   `1`, `2`, or   `[1 2]`. - When **IP address**   includes *N* IP addresses,   specify this parameter as   1-by-2*N* row vector. |
| `X410` *(since R2025a)* | - When **IP address**   includes one IP address, specify this parameter as   1-, 2-, 3-, or 4-element row vector of channel   numbers from the set {1, 2, 3, 4} - When **IP address**   includes *N* IP addresses,   specify this parameter as   1-by-4*N* row vector. |

When **Channel Mapping** is a scalar,
`1`, or `2`, the radio operates in
single input single output (SISO) mode. When **Channel
Mapping** is a vector, the radio operates in multiple input
multiple output (MIMO) mode.

When **IP Address** contains multiple IP addresses,
the channels defined by **Channel Mapping** are ordered
first by the order in which the IP addresses appear in the list and then
by the channel order within the same radio.

For example, if **Platform** is
`"X300"` and **IP Address** is
`"192.168.20.2, 192.168.10.3"`, then the
**Channel Mapping** must be `[1 2 3
4]`. Channels 1 and 2 of the bundled radio refer to
channels 1 and 2 of the radio with IP address 192.168.20.2,
respectively. Channels 3 and 4 of the bundled radio refer to channels 1
and 2 of the radio with IP address 192.168.10.3, respectively.

**Data Types:** `double`

### **Source of center frequency** — Select source of center frequency `Dialog` (default) | `Input port`

Select source of center frequency, specified as:

- `Dialog` — Set the center frequency using the **Center frequency (Hz)** parameter.
- `Input port` — Set the center frequency using the **fc** input port.

### **Center frequency (Hz)** — RF center frequency `2.45e9` (default) | nonnegative finite scalar | vector of nonnegative finite scalars

RF center frequency in Hz, specified as a nonnegative finite scalar or
vector of nonnegative finite scalars. The valid range of this parameter
depends on the RF daughterboard of the USRP device.

- For a single channel (SISO), specify the value for the center
  frequency as a scalar.
- For multiple channels (MIMO) that use the same center
  frequency, specify the center frequency value as a scalar. The
  center frequency is set by scalar expansion.
- For multiple channels (MIMO) that use different center
  frequencies, specify the values in a vector. The
  *i*th element of the vector is applied to
  the *i*th channel specified by **Channel mapping**.

**Note**

- The channels corresponding to the same RF daughterboard of a USRP N300 or N310 radio must have the same center frequency.
- For a MIMO scenario, the center frequency for a USRP N300 radio must be a scalar. You cannot specify the frequencies as a vector.

#### Dependencies

To enable this parameter, set the **Source of center
frequency** to
`Dialog`.

**Data Types:** `double`

### **Source of LO offset** — Select source of LO offset `Dialog` (default) | `Input port`

Select source of LO offset, specified as:

- `Dialog` — Set the LO offset using the **LO offset (Hz)** parameter.
- `Input port` — Set the LO offset using the **LO offset** input port.

### **LO offset (Hz)** — Offset frequency for local oscillator `0` (default) | scalar | vector

Offset frequency for the local oscillator, specified as a scalar or
vector. The valid range of this parameter depends on the RF
daughterboard of the USRP device.

This figure shows that the local oscillator offset affects the
intermediate center frequency in the USRP hardware. It does not affect the transmitted center
frequency.

- *f*LO offset is the
  local oscillator offset frequency.
- *f*center represents
  the center frequency specified by the block.

To move the center frequency away from interference or harmonics
generated by the USRP hardware, use the LO offset.

- For a single channel (SISO), specify the value for the LO
  offset as a scalar.
- For multiple channels (MIMO), the LO offset must be zero. This
  restriction is due to a UHD limitation. You can specify the LO
  offset as a scalar or as a vector.

#### Dependencies

To enable this parameter, set **Source of LO
offset** to `Dialog`.

### **Source of gain** — Select source of gain `Dialog` (default) | `Input port`

Select source of gain, specified as:

- `Dialog` — Specify the gain using the **Gain (dB)** parameter.
- `Input port` — Specify the gain using the **gain** input port.

### **Gain (dB)** — Transmitter gain `8` (default) | scalar | vector

Transmitter gain in dB, specified as a scalar or vector. The valid
range of this gain depends on the RF daughterboard of the USRP device.

Set the value of gain based on the **Channel
Mapping** configuration:

- For a single channel (SISO), specify the gain as a
  scalar.
- For multiple channels (MIMO) that use the same gain value,
  specify the gain as a scalar. The gain is set by scalar
  expansion.
- For multiple channels (MIMO) that use different gains,
  specify the values in a row vector. The
  *i*th element of the vector is applied to
  the *i*th channel specified by
  **Channel Mapping**.

#### Dependencies

To enable this parameter, set **Source of gain**
to `Dialog`.

**Data Types:** `double`

### **PPS source** — PPS signal source `Internal` (default) | `External` | `GPSDO`

Pulse per second (PPS) signal source, specified as one of these values.

- `Internal` — Use the internal PPS signal of the
  USRP radio.
- `External` — Use the PPS signal from an external
  signal generator.
- `GPSDO` — Use the PPS signal from a GPSDO.

To synchronize the time for all channels of the bundled radios, you can:

- Provide a common external PPS signal to all of the bundled radios and set
  this parameter to `External`.
- Use the PPS signal from the GPSDO that is available on the USRP radio by
  setting this parameter to `GPSDO`.

To synchronize the USRP time to the valid GPS time, set this parameter to
`GPSDO`. You must also enable the **Ensure sync GPS
time** parameter if the GPSDO is not locked to the GPS constellation at the
start of the simulation.

### **Enable gps\_locked output port** — Option to enable lock status of GPSDO to GPS constellation `off` (default) | `on`

Select this parameter to enable the **gpsLocked** output port, which
indicates the lock status of the GPSDO to the GPS constellation.

#### Dependencies

To enable this parameter, set the **PPS source** parameter to
`GPDSO`.

### **Ensure sync GPS time** — Option to ensure GPS time synchronization `off` (default) | `on`

Select this parameter to ensure that the USRP radio time is synchronized to the valid GPS
time.

When you select this parameter, the block checks the lock status of the GPSDO. When the GPSDO
is locked to the GPS constellation, the block sets the USRP radio time to the valid GPS
time.

#### Dependencies

To enable this parameter, set the **PPS source** parameter to
`GPSDO`.

### **Clock source** — Clock source `Internal` (default) | `External` | `GPSDO`

Clock source, specified as one of these values.

- `Internal` — Use the internal clock signal of the
  USRP radio.
- `External` — Use the 10 MHz clock signal from an
  external clock generator.
- `GPSDO` — Use the 10 MHz clock signal from a
  GPSDO.

The external clock port is labeled *REF IN*.

To synchronize the frequency for all channels of the bundled radios, you can:

- Provide a common external 10 MHz clock signal to all of the bundled radios
  and set this parameter to `External`.
- Provide a 10 MHz clock signal from each GPSDO to the corresponding radio
  and set this parameter to `GPSDO`.

### **Enable ref\_locked output port** — Option to enable lock status of USRP radio to 10 MHz clock signal `off` (default) | `on`

Select this parameter to enable the **refLocked** output port, which
indicates the lock status of the USPR radio to the 10 MHz clock signal.

#### Dependencies

To enable this parameter, set the **Clock source** parameter to
`External` or `GPDSO`.

### **Master clock rate (Hz)** — Master clock rate scalar

Master clock rate, specified as a scalar in Hz. The
master clock rate is the A/D and D/A clock rate. The valid range of values for this
property depends on the radio platform that is connected.

| Platform Value | Supported **Master clock rate (Hz)** Values |
| --- | --- |
| `E320` *(since R2025a)* | Scalar in the range from `200e3` to `61.44e6`.  When you use a USRP E320 radio with two transmit channels or two receive channels, the clock rate must be less than or equal to 30.72e6. This restriction is a hardware limitation for two-channel operations on USRP E320 radios.  The default value is `30.72e6`. |
| `N300` or `N310` | `122.88e6`, `125e6` (default), or `153.6e6` |
| `N320/N321` | `200e6` (default), `245.76e6`, or `250e6`. |
| `X300` or `X310` | `184.32e6` or `200e6` (default).  `200e6` — When TwinRX daughterboard is selected. |
| `X410` *(since R2025a)* | `245.76e6` or `250e6` (default). |

**Data Types:** `double`

### **Interpolation factor** — Interpolation factor for SDRu Transmitter `512` (default) | integer

Interpolation factor for the SDRu transmitter, specified as an integer in the range
`[1,1024]` with restrictions that depend on the radio you use.

| Radio Device | Supported Interpolation Factors |
| --- | --- |
| USRP E320 *(since R2025a)*  USRP N300  USRP N310  USRP N320  USRP N321  USRP X410 *(since R2025a)* | 1 |
| 2 |
| 3 |
| Even integer in the range from 4 to 256 |
| Multiple of 4 in the range from 256 to 512 |
| Multiple of 8 in the range from 512 to 1016 |
| USRP X300  USRP X310 | Integer in the range from 1 to 128 |
| Even integer in the range from 128 to 256 |
| Multiple of 4 in the range from 256 to 512 |
| Multiple of 8 in the range from 512 to 1016 |

The radio uses the interpolation factor when it upconverts the complex
baseband signal to an intermediate frequency (IF) signal.

### **Enable time trigger** — Option to enable timed transmission and reception off (default) | on

Option to enable timed transmission and reception. To enable the radio
to transmit or receive data after a specified time, select **Enable time
trigger**.

When you select **Enable time trigger** parameter,
you can:

- Transmit or receive after the time specified in the **Trigger
  time** parameter.
- Transmit or receive at the specified GPS time in the **Trigger
  time** parameter if you set the **PPSSource** parameter to
  `GPSDO`.
- Simultaneously transmit and receive after the time specified in the
  **Trigger time** parameter.

### **Trigger time** — Trigger time in seconds `5` (default) | nonnegative scalar

Trigger time in seconds, specified as a nonnegative scalar. Specify the trigger time after
which you want the radio to transmit or receive data. The **Trigger
time** value must be greater than the current USRP radio time.

When you set the **PPS Source** parameter to
`GPSDO`, specify the **Trigger time** parameter
as the exact GPS time in seconds at which the radio transmits and receives data.

**Note**

For AD936x-based
N3xx
USRP radios, you can expect a consistent delay between the specified
trigger time and the start of transmission or reception.

#### Dependencies

To enable this parameter, select the **Enable trigger time** parameter.

### Data

### **Baseband sample rate (Hz)** — Baseband sample rate of output signal scalar

This parameter is read-only.

Baseband sample rate of output signal, in Hz, specified as a
scalar.

This parameter displays the computed baseband sample rate derived from
the **Master clock rate
(Hz)** and **Interpolation factor**
parameter values. This computation uses the formula, **Baseband
sample rate** = Master clock
rate/Interpolation factor. If you change the **Interpolation
factor** during simulation, then the block changes hardware
data rate, but does not change the Simulink sample time.

To get more information on sample time, see What Is Sample Time? (Simulink).

**Data Types:** `double`

### **Transport data type** — Transport data type `int16` (default) | `int8`

Transport data type, specified as:

- `int16` — Uses 16-bit transport. Achieves higher precision than 8-bit transport.
- `int8` — Uses 8-bit transport. Uses a quantization step 256 times larger and achieves approximately two times faster transport data rate than 16-bit transport.

Specifying transport data rate data type as `int16`, assigns 16 bits for the in-phase component and 16 bits for the quadrature component, resulting in 32 bits for each complex sample of transport data.

### **Enable underrun output port** — Option to enable underrun output port off (default) | on

To measure the number of samples lost during transmission, select this
parameter.

If your model is not running in real time, you can adjust parameters
that reduce the number of transported samples. To approach or achieve
real-time performance, you can increase the interpolation factor.

### **Enable burst mode** — Option to enable burst mode off (default) | on

Option to enable burst mode. To produce a set of contiguous frames without an overrun or underrun to the radio, select **Enable burst mode**. Enabling burst mode helps you simulate models that cannot run in real time.

When burst mode is enabled, specify the desired amount of contiguous data using the **Number of frames in burst** parameter.

### **Number of frames in burst** — Number of frames in contiguous burst `100` (default) | nonnegative integer

Number of frames in a contiguous burst, specified as a nonnegative integer.

#### Dependencies

To enable this parameter, select **Enable burst mode**.

**Data Types:** `double`

## Libraries

Wireless Testbench Support Package for NI USRP Radios

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011b**

### R2025a: Support for USRP E320 and X410 radios

You can now use the SDRu Transmitter block to transmit data using
USRP E320 and X410 radios.

### R2024a: Support for N3xx and X3xx series radio devices moved to Wireless Testbench

Support for NI
USRP N3xx and X3xx series radio devices has moved from Communications Toolbox Support Package for USRP Radio to Wireless Testbench Support Package for NI
USRP Radios.

### R2023b: Enhanced support for time triggering in SDRu Blocks

You can now specify trigger time to enable transmission and reception of data at a
specified time for a USRP radio. This property is available in the SDRu Transmitter and SDRu Receiver
Simulink blocks.

### R2020a: interp input port has been removed

Starting in R2020a, the SDRu Transmitter block removed the
**interp** input port. You can not set the interpolation factor
value for this block by using an input port. Instead use the **Interpolation
factor** parameter.

### R2020a: Sample time parameter has been removed

Starting in R2020a, the SDRu Transmitter block removed the **Sample
time** parameter. Use the read-only **Baseband sample rate
(Hz)** parameter instead. This parameter displays the computed baseband
sample rate derived from the **Master clock
rate (Hz)** and **Interpolation factor**
parameters.

### R2020a: X3xx series radios no longer support 120 MHz master clock rate

Beginning with Ettus Research UHD version 003.014.000.000, X3xx series radios do not support a
master clock rate value of 120 MHz. Consequently,
starting in R2020a, which supports UHD version 003.015.000.000, Communications Toolbox Support Package for USRP Radio does not support a master clock
rate value of 120 MHz for X3xx series radios.

For the SDRu Transmitter and SDRu Receiver blocks,
when you select an X3xx series radio for the **Platform**
parameter, you can no longer set the **Master
clock rate (Hz)** parameter to `120e6`.

## Description

Send data to USRP device

The SDRu Transmitter block supports communication between Simulink® and a Universal Software Radio Peripheral (USRP™) device, enabling simulation and development for various software-defined
radio applications. The SDRu Transmitter block and the USRP board must be on the same Ethernet subnetwork.

The SDRu Transmitter block accepts a column vector or matrix input signal from Simulink and transmits signal and control data to a USRP board using the Universal Hardware Driver (UHD™) from Ettus Research™. The SDRu Transmitter block is a Simulink sink that takes data from a model and sends it to a USRP board. The first call to this block can contain transient values, in this
case the resulting packets contain undefined data.

This block diagram illustrates how Simulink, SDRu Transmitter and Receiver blocks, and USRP hardware interface.

For transmitting a radio signal over the air, pass the signal generated in Simulink to an SDRu transmitter block. The transmitter block forwards the signal to the radio hardware. For receiving a radio signal over the air, use an SDRu receiver block. The receiver block forwards the signal received from the radio hardware for post processing in Simulink.

If your computer is not connected to any USRP hardware, you can still use this block to develop a model that propagates
sample time and data type information. To propagate this information, select
**Simulation** >> **Update diagram**.

For information about the USRP hardware products that interface with this block, see Supported Radio Devices.

This icon shows all ports, including optional ones: SDRu transmitter block with all the ports

**Note**

Starting in R2024a, the MathWorks® products and support packages you require to use this Simulink block depend on your radio device.

| Radio Device | Required MathWorks Products | Support Package Installation |
| --- | --- | --- |
| USRP2™  USRP N200, N210  USRP B200, B210 | - Communications Toolbox™ Support Package for USRP Radio | Install Communications Toolbox Support Package for USRP Radio |
| USRP E320 *(since R2025a)*  USRP N300, N310, N320, N321  USRP X300, X310  USRP X410 *(since R2025a)* | - Wireless Testbench™ - Wireless Testbench Support Package for NI™   USRP Radios | Install Support Package for NI USRP Radios |

For details on how to use this Simulink block with a radio device supported by Communications Toolbox Support Package for USRP Radio, see SDRu Transmitter.
