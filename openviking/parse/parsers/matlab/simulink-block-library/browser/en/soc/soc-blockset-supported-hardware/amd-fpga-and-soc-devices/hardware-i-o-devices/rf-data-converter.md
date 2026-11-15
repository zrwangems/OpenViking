---
type: simulink-block
title: 'RF Data Converter'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'rfdataconverter'
documentation_source_path: 'ref/rfdataconverter.html'
language: en
---

# RF Data Converter

## Ports

### Input

### **adcT*`x`*Ch*`y`*** — ADC input data column vector

ADC input data, specified as a column vector.

***`x`*** indicates the ADC tile number
and ***`y`*** indicates the ADC channel
number. The **RF interface** parameter sets the number of
**adc** ports. For example, if **RF interface** is
set to `ADC & DAC 2x2 RF Interface`, the block has ports
**adcT0Ch0** and **adcT0Ch1**, that is, one input
port per ADC channel interface.

Valid values for this port depend on the simulation mode and the **Digital
interface** parameter value.

- In the **Pass-through** simulation mode, the block accepts
  inputs of `int16` and `uint16` data types. In
  this mode:

  - If you set the **Digital interface** parameter to
    `Real`, specify this value as an
    *N*-element column vector, where *N* is
    the number of samples per clock cycle that you set in the **Samples
    per clock cycle** parameter.

    Use this option to specify real-valued data. For example, consider
    *N* equal to 2 and data containing two real values
    *D*0 and
    *D*1. In this case, specify this
    port value as a vector in the form
    [*D*0
    *D*1].
  - If you set the **Digital interface** parameter to
    `I/Q`, specify this value as a
    2*N*-element column vector, where *N* is
    the number of samples per clock cycle that you set in the **Samples
    per clock cycle** parameter.

    Use this option to specify complex-valued data. For example, consider
    *N* equal to 2 and data containing two complex values with
    real parts *I*0 and
    *I*1 and imaginary parts
    *Q*0 and
    *Q*1, respectively. In this case,
    specify this port value as a vector in the form
    [*I*0
    *Q*0
    *I*1
    *Q*1].

  **Data Types:**
  `int16` | `uint16`
- In the **Behavioral** simulation mode, the block accepts
  inputs of `double` data type. Specify this value as an
  *R**N*-element column vector, where
  *R* is the decimation factor that you set in the
  **Decimation mode (xN)** parameter and *N* is
  the number of samples per clock cycle that you set in the **Samples per
  clock cycle** parameter.

  **Data Types:**
  `double`

**Data Types:** `int16` | `uint16` | `double`

### **dacT*`x`*Ch*`y`*Data** — DAC input data scalar | column vector

DAC input data, specified as a scalar or column vector with a length in the range
[1, *N*], where *N* is the number of samples per
clock cycle that you specify in the **Samples per clock cycle**
parameter.

***`x`*** indicates the DAC tile number
and ***`y`*** indicates the DAC channel
number. The **RF interface** parameter sets the number of
**dacT*`x`*Ch*`y`*Data**
ports.

For more information about the data format, see Data Format Between RF Data Converter Block and Hardware Logic.

#### Dependencies

To enable this port, set the **Digital interface** parameter to
`Real`.

**Data Types:** `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

### **dacT*`x`*Ch*`y`*IData** — Real part of DAC input scalar | column vector

Real part of the DAC input, specified as a scalar or column vector with a length
in the range [1, *N*], where *N* is the number of
samples per clock cycle that you specify in the **Samples per clock
cycle** parameter.

***`x`*** indicates the DAC tile number
and ***`y`*** indicates the DAC channel
number. The **RF interface** parameter sets the number of
**dacT*`x`*Ch*`y`*IData**
ports.

For more information about the data format, see Data Format Between RF Data Converter Block and Hardware Logic.

#### Dependencies

To enable this port, set the **Digital interface** parameter to
`I/Q`.

**Data Types:** `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

### **dacT*`x`*Ch*`y`*QData** — Imaginary part of DAC input scalar | column vector

Imaginary part of the DAC input, specified as a scalar or column vector with a
length in the range [1, *N*], where *N* is the
number of samples per clock cycle that you specify in the **Samples per clock
cycle** parameter.

***`x`*** indicates the DAC tile number
and ***`y`*** indicates the DAC channel
number. The **RF interface** parameter sets the number of
**dacT*`x`*Ch*`y`*QData**
ports.

For more information about the data format, see Data Format Between RF Data Converter Block and Hardware Logic.

#### Dependencies

To enable this port, set the **Digital interface** parameter to
`I/Q`.

**Data Types:** `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

### **dacT*`x`*Ch*`y`*Valid** — Indication of valid DAC input data `Boolean` scalar

Indication of valid DAC input data, specified as a scalar.

A value of `1` indicates that the data on the
**dacT*`x`*Ch*`y`*Data**
port is valid or that the data on the
**dacT*`x`*Ch*`y`*IData**
and
**dacT*`x`*Ch*`y`*QData**
ports is valid.

***`x`*** indicates the DAC tile number
and ***`y`*** indicates the DAC channel
number. The **RF interface** parameter sets the number of
**dacT*`x`*Ch*`y`*Valid**
ports.

**Data Types:** `Boolean`

### **adcT*`x`*Ch*`y`*RealTimeCtrlIn** — ADC real-time control input bus

ADC real-time control input, specified as a bus.

***`x`*** indicates the ADC tile number
and ***`y`*** indicates the ADC channel
number. The **RF interface** parameter sets the number of
**adcT*`x`*Ch*`y`*RealTimeCtrlIn**
ports. For example, if you set the **RF interface** parameter to
`ADC & DAC 2x2 RF Interface`, the block has two input
ports, one per ADC channel interface.

#### Dependencies

To enable this port, select **Real-time ports** or
**Real-time NCO ports** on the **Advanced**
tab.

**Data Types:** `DUT2RFDCRealTimeCtrlBusObj`

### **adcT*`x`*NCOUpdateReq** — ADC NCO update request `Boolean` scalar

ADC numerically controlled oscillator (NCO) update request, specified as a Boolean
scalar. To request an update of the ADC NCO settings, set this input signal to
`High`.

***`x`*** indicates the ADC tile number.
The **RF interface** parameter sets the number of
**adcT*`x`*NCOUpdateReq** ports. For
example, if you set the **RF interface** parameter to
`ADC & DAC 2x2 RF Interface`, the block has one input
port, one per ADC tile.

#### Dependencies

To enable this port, select **Real-time NCO ports** under the
**ADC** section on the **Advanced** tab.

**Data Types:** `Boolean`

### **dacT*`x`*Ch*`y`*RealTimeCtrlIn** — DAC real-time control input bus

DAC real-time control input, specified as a bus.

***`x`*** indicates the DAC tile number
and ***`y`*** indicates the DAC channel
number. The **RF interface** parameter sets the number of
**dacT*`x`*Ch*`y`*RealTimeCtrlIn**
ports. For example, if you set the **RF interface** parameter to
`ADC & DAC 2x2 RF Interface`, the block has two input
ports, one per DAC channel interface.

#### Dependencies

To enable this port, select **Real-time NCO ports** under the
**DAC** section on the **Advanced** tab.

**Data Types:** `DUT2RFDCRealTimeCtrlBusObj`

### **dacT*`x`*NCOUpdateReq** — DAC NCO update request `Boolean` scalar

DAC NCO update request, specified as a Boolean scalar. To request an update of the
DAC NCO settings, set this input signal to `High`.

***`x`*** indicates the DAC tile number.
The **RF interface** parameter sets the number of
**dacT*`x`*NCOUpdateReq** ports. For
example, if you set the **RF interface** parameter to
`ADC & DAC 2x2 RF Interface`, the block has one input
port, one per DAC tile.

#### Dependencies

To enable this port, select **Real-time NCO ports** under the
**DAC** section on the **Advanced** tab.

**Data Types:** `Boolean`

### **dacT0SysrefGating** — Synchronous clock gating for MTS mode `Boolean` scalar

Synchronous clock gating for the multi-tile synchronization (MTS) mode, specified
as a Boolean scalar. To disable the DAC tile from the `Sysref` clock
signal, set this input signal to `High`.

#### Dependencies

To enable this port, select **Multi tile sync** under the
**Common Parameters** section and select **Real-time NCO
ports** under the **DAC** section on the
**Advanced** tab.

**Data Types:** `Boolean`

### **dacT0SysrefReEnable** — Synchronous clock re-enabling for MTS mode `Boolean` scalar

Synchronous clock re-enabling for the MTS mode, specified as a Boolean scalar. To
re-enable the `Sysref` clock signal, set this input signal to
`High`.

#### Dependencies

To enable this port, select **Multi tile sync** under the
**Common Parameters** section and select **Real-time NCO
ports** under the **DAC** section on the
**Advanced** tab.

**Data Types:** `Boolean`
### Output

### **dacT*`x`*Ch*`y`*** — DAC output data column vector

DAC output data, returned as a column vector.

- In the **Pass-through** simulation mode, the block returns
  outputs of `int16` data type. In this mode:

  - If you set the **Digital interface** parameter to
    `Real`, the block returns outputs as a
    *N*-element column vector, where *N* is
    the number of samples per clock cycle that you set in the **Samples
    per clock cycle** parameter.

    For example, consider *N* equal to 2 and an input to the
    **dacT0Ch1Data** port with a size of 32 bits. In this case,
    this port returns a vector [*S*0
    *S*1], where
    *S*0 is a16-bit value sliced from 0
    to 15 bits of input data on the **dacT0Ch1Data** port and
    *S*1 is a 16-bit value sliced from
    16 to 31 bits of input data on the **dacT0Ch1Data**
    port.
  - If you set the **Digital interface** parameter to
    `I/Q`, the block returns outputs as a
    2*N*-element column vector, where *N* is
    the number of samples per clock cycle that you set in the **Samples
    per clock cycle** parameter.

    For example, consider *N* equal to 2 and inputs to the
    **dacT0Ch1IData** and **dacT0Ch1QData**
    ports with a size of 32 bits. In this case, this port returns a vector
    [*I*0
    *Q*0
    *I*1
    *Q*1], where
    *I*0 is a16-bit value sliced from 0
    to 15 bits of input data on the **dacT0Ch1IData** port,
    *I*1 is a 16-bit value sliced from
    16 to 31 bits of input data on the **dacT0Ch1IData** port,
    *Q*0 is a16-bit value sliced from 0
    to 15 bits of input data on the **dacT0Ch1QData** port, and
    *Q*1 is a 16-bit value sliced from
    16 to 31 bits of input data on the **dacT0Ch1QData**
    port.

  **Data Types:**
  `int16`
- In the **Behavioral** simulation mode, the block returns
  outputs of `double` data type. The block returns outputs as an
  *R**N*-element column vector, where
  *R* is the interpolation factor that you set in the
  **Interpolation mode (xN)** parameter and *N*
  is the number of samples per clock cycle that you set in the **Samples per
  clock cycle** parameter.

  **Data Types:**
  `double`

***`x`*** indicates the DAC tile number
and ***`y`*** indicates the DAC channel
number. The **RF interface** parameter sets the number of
**dacT*`x`*Ch*`y`***
ports.

**Data Types:** `int16` | `double`

### **adcT*`x`*Ch*`y`*Data** — ADC output data scalar | column vector

ADC output data, returned as a scalar or column vector with a length in the range
[1, *N*], where *N* is the number of samples per
clock cycle that you specify in the **Samples per clock cycle**
parameter.

***`x`*** indicates the ADC tile number
and ***`y`*** indicates the ADC channel
number. The **RF interface** parameter sets the number of
**adcT*`x`*Ch*`y`*Data**
ports.

For more information about the data format, see Data Format Between RF Data Converter Block and Hardware Logic.

#### Dependencies

To enable this port, set the **Digital interface** parameter to
`Real`.

**Data Types:** `uint16` | `uint32` | `uint64` | `fixed point`

### **adcT*`x`*Ch*`y`*IData** — Real part of ADC output scalar | column vector

Real part of the ADC output, returned as a scalar or column vector with a length
in the range [1, *N*], where *N* is the number of
samples per clock cycle that you specify in the **Samples per clock
cycle** parameter.

***`x`*** indicates the ADC tile number
and ***`y`*** indicates the ADC channel
number. The **RF interface** parameter sets the number of
**adcT*`x`*Ch*`y`*IData**
ports.

For more information about the data format, see Data Format Between RF Data Converter Block and Hardware Logic.

#### Dependencies

To enable this port, set the **Digital interface** parameter to
`I/Q`.

**Data Types:** `uint16` | `uint32` | `uint64` | `fixed point`

### **adcT*`x`*Ch*`y`*QData** — Imaginary part of ADC output scalar | column vector

Imaginary part of the ADC output, returned as a scalar or column vector with a
length in the range [1, *N*], where *N* is the
number of samples per clock cycle that you specify in the **Samples per clock
cycle** parameter.

***`x`*** indicates the ADC tile number
and ***`y`*** indicates the ADC channel
number. The **RF interface** parameter sets the number of
**adcT*`x`*Ch*`y`*Qdata**
ports.

For more information about the data format, see Data Format Between RF Data Converter Block and Hardware Logic.

#### Dependencies

To enable this port, set the **Digital interface** parameter to
`I/Q`.

**Data Types:** `uint16` | `uint32` | `uint64` | `fixed point`

### **adcT*`x`*Ch*`y`*Valid** — Indication of valid ADC output data `Boolean` scalar

Indication of valid ADC output data, returned as a Boolean scalar.

A value of `1` indicates that the data on the
**adcT*`x`*Ch*`y`*Data**
port is valid or that the data on the
**adcT*`x`*Ch*`y`*IData**
and
**adcT*`x`*Ch*`y`*QData**
ports is valid.

***`x`*** indicates the ADC tile number
and ***`y`*** indicates the ADC channel
number. The **RF interface** sets the number of
**adcT*`x`*Ch*`y`*Valid**
ports.

**Data Types:** `Boolean`

### **adcT*`x`*Ch*`y`*RealTimeCtrlOut** — ADC real-time control output bus

ADC real-time control output, returned as a bus. In the
**Pass-through** simulation mode, this port always has a value of
`Low`.

***`x`*** indicates the ADC tile number
and ***`y`*** indicates the ADC channel
number. The **RF interface** parameter sets the number of
**adcT*`x`*Ch*`y`*RealTimeCtrlOut**
ports. For example, if you set the **RF interface** parameter to
`ADC & DAC 2x2 RF Interface`, the block has two output
ports, one per ADC channel interface.

#### Dependencies

To enable this port, select **Real-time ports** on the
**Advanced** tab.

**Data Types:** `RFDC2DUTRealTimeCtrlBusObj`

### **dacT*`x`*NCOUpdateBusy** — Indication that DAC NCO update is in progress scalar

Indication that a DAC NCO update is in progress, returned as a Boolean scalar. In
MTS mode, for Tile 0, this value returned as a scalar of type
`fixdt(0,2,0)`. In the **Pass-through** simulation
mode, this port always has a value of `Low`.

***`x`*** indicates the DAC tile number.
The **RF interface** parameter sets the number of
**dacT*`x`*NCOUpdateBusy** ports. For
example, if you set the **RF interface** parameter to
`ADC & DAC 2x2 RF Interface`, the block has one output
port, one per DAC tile.

#### Dependencies

To enable this port, select **Real-time NCO ports** under the
**DAC** section on the **Advanced** tab.

**Data Types:** `Boolean` | `fixdt(0,2,0)`

### **adcT*`x`*NCOUpdateBusy** — Indication that ADC NCO update is in progress `Boolean` scalar

Indication that an ADC NCO update is in progress, returned as a Boolean scalar. In
the **Pass-through** simulation mode, this port always has a value of
`Low`.

***`x`*** indicates the ADC tile number.
The **RF interface** parameter sets the number of
**adcT*`x`*NCOUpdateBusy** ports. For
example, if you set the **RF interface** parameter to
`ADC & DAC 2x2 RF Interface`, the block has one output
port, one per ADC tile.

#### Dependencies

To enable this port, select **Real-time NCO ports** under the
**ADC** section on the **Advanced** tab.

**Data Types:** `Boolean`

## Parameters

### **RFDC simulation** — Simulation mode selection **Pass-through** (default) | **Behavioral**

Select the simulation mode.

- **Pass-through** — In this simulation mode, the block
  outputs the same data as the input. The interpolation, decimation, and mixers
  settings do not impact the block output values.
- **Behavioral** — In this simulation mode, the
  interpolation, decimation, and mixers settings impact the block output
  values.

### **Hardware board** — Option to view selected hardware `None` (default) | supported Xilinx boards

This parameter is read-only.

For details about how to choose a hardware board and configure its parameters, see
Hardware Implementation Pane.

### **RF interface** — RF interface selection `ADC & DAC 2x2 RF Interface` (default) | `ADC & DAC 1x1 RF Interface` | `ADC & DAC 4x4 RF Interface` | `ADC & DAC 8x8 RF Interface` | `ADC & DAC 16x16 RF Interface` | `Customize`

Specify the RF channel interface type.

To select a predefined set of ADC and DAC combinations, set this parameter to
`ADC & DAC 1x1 RF Interface`, `ADC & DAC
2x2 RF Interface`, `ADC & DAC 4x4 RF
Interface`, `ADC & DAC 8x8 RF Interface`, or
`ADC & DAC 16x16 RF Interface`. Available options for
this parameter vary as per the selected hardware board. To select the required number of
DAC or ADC combinations, set this parameter to
`Customize`.

**Example:** `ADC & DAC 2x2 RF Interface` specifies two ADC
and two DAC RF channel interfaces.

### **Digital interface** — Digital interface selection `Real` (default) | `I/Q`

Specify the digital interface type.

- `Real` — Supports real data
- `I/Q` — Supports complex data by using real and
  imaginary ports

### DAC

The number of panes and number of DACs in each pane in the **DAC** tab
depend on the RFSoC device in the selected hardware board. The tiles and DACs shown on the
block mask indicate the corresponding tiles and DACs on the selected hardware board. For
example, if you select the Xilinx
Zynq
UltraScale+ RFSoC ZCU111 evaluation kit, the **DAC** tab contains two
panes (**Tile 0** and **Tile 1**), and each pane contains
four DACs. For a ZCU111 board, **DAC 0**, **DAC 1**,
**DAC 2**, and **DAC 3** in **Tile 0**
correspond to DAC 0, DAC 1, DAC 2, and DAC 3 in DAC tile 228, respectively. **DAC
0**, **DAC 1**, **DAC 2**, and **DAC
3** in **Tile 1** correspond to DAC 0, DAC 1, DAC 2, and DAC 3
in DAC tile 229, respectively.

The selection of tiles and the respective DACs is predefined when you set the
**RF interface** parameter to `ADC & DAC 1x1 RF
Interface`, `ADC & DAC 2x2 RF Interface`,
`ADC & DAC 4x4 RF Interface`, `ADC & DAC 8x8
RF Interface`, or `ADC & DAC 16x16 RF
Interface`. You cannot modify the tile and DAC selection when you select these
predefined options. To modify the tile and DAC selections, set the **RF
interface** parameter to `Customize`.

### **Match parameters of all DACs** — Matching parameters of all DACs `on` (default) | `off`

Select this parameter to apply the same parameter values to all of the selected
DACs.

Clear this parameter to specify different parameter values for each of the
selected DACs.

#### Dependencies

To enable this parameter, set the **RF interface** parameter to
`Customize`.

### **Sample rate (MSPS)** — Data sampling rate `1000` (default) | scalar

Specify the sampling rate as a scalar in a range that is based on the selected
hardware board. Units are in mega samples per second.

This table shows the sampling rate range of the block for the supported
Zynq
UltraScale+ RFSoC Gen 1, Gen 2, Gen 3, and DFE devices.

| Generation | Device | Sampling Rate Range (MSPS) |
| --- | --- | --- |
| Gen 1 | ZU25DR | [500, 6554] |
| ZU27DR |
| ZU28DR |
| ZU29DR |
| Gen 2 | ZU39DR | [500, 6554] |
| Gen 3 | ZU47DR | [500, 7000] |
| ZU48DR |
| ZU49DR |
| DFE | ZU63DR |
| ZU64DR |
| ZU65DR |
| ZU67DR |

### **Interpolation mode (xN)** — Interpolation factor `2` (default) | `1` | `3` | `4` | `5` | `6` | `8` | `10` | `12` | `16` | `20` | `24` | `40`

Specify the interpolation factor.

**Note**

Gen 1 and Gen 2 devices support interpolation factors of 1, 2, 4, and 8. Gen 3
and DFE devices support interpolation factors of 1, 2, 3, 4, 5, 6, 8, 10, 12, 16,
20, 24, and 40.

### **Samples per clock cycle** — Number of samples per clock cycle `2` (default) | `1` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16`

Specify the number of samples per clock cycle. Available options for the number of
samples per clock cycle vary with the selected hardware board and digital interface
type.

The block calculates the stream data width as 16 x **Samples per clock
cycle**.

The block calculates the stream clock frequency as **Sample rate
(MSPS)** / **Interpolation mode (xN)** x **Samples
per clock cycle**.

### **Mixer type** — Mixer type `Bypassed` (default) | `Coarse` | `Fine`

Specify the mixer type.

To use `Bypassed`, set the **Digital
interface** parameter to `Real`.

To select either `Coarse` or
`Fine`, set the **Digital interface**
parameter to `I/Q`.

### **Mixer mode** — Mixer mode type `Real->Real` (default) | `I/Q->Real`

This parameter is read-only.

To use `Real->Real`, set the **Digital
interface** parameter to `Real`.

To use `I/Q->Real`, set the **Digital
interface** parameter to `I/Q`.

### **Mixer frequency** — Frequency of mixer `Fs/2` (default) | `Fs/4` | `-Fs/4`

Specify the mixer frequency.

#### Dependencies

To enable this parameter, set the **Digital interface**
parameter to `I/Q` and **Mixer type**
parameter to `Coarse`.

### **NCO frequency (GHz)** — NCO frequency `[0 0]` (default) | integer in the range [–10, 10]

Specify the NCO frequency values as a scalar or *m*-element row
vector, where *m* is the number of DACs.

When you set the **RF interface** parameter to
`Customize` and clear the **Match parameters of all
DACs** parameter, *m* must be 1.

The block derives the **Analog Nyquist zone** for a DAC channel
based on the NCO frequency and sample rate
(*F*s).

- **Zone 1** — The DAC output is in Nyquist
  zone 1 if NCO frequency is less than
  *F*s/2. In this Nyquist zone, the block
  supports simulation capability.
- **Zone 2** — The DAC output is in Nyquist
  zone 2 if NCO frequency is greater than
  *F*s/2. In this Nyquist zone, the block
  does not support simulation capability. In simulation, the DAC centers the output
  around a folded frequency of the specified NCO frequency in zone 1.

#### Dependencies

To enable this parameter, set the **Digital interface**
parameter to `I/Q` and the **Mixer type**
parameter to `Fine`.

### **NCO phase** — NCO phase `[0 0]` (default) | integer in the range [–180, 180]

Specify the NCO phase as a scalar or *m*-element row vector,
where *m* is the number of DACs.

When you set the **RF interface** parameter to
`Customize` and clear the **Match parameters of all
DACs** parameter, *m* must be 1.

#### Dependencies

To enable this parameter, set the **Digital interface**
parameter to `I/Q` and the **Mixer type**
parameter to `Fine`.

### **Inverse sinc filter** — Flat-out response `off` (default) | `on`

Select this parameter to convert the analog sinc output response from the DAC to a
flat-output response.

### ADC

The number of panes and number of ADCs in each pane in the **ADC** tab
depend on the selected hardware board. The tiles and ADCs shown on the block mask indicate
the corresponding tiles and ADCs on the selected hardware board. For example, if you select
the Xilinx
Zynq
UltraScale+ RFSoC ZCU111 evaluation kit, the **ADC** tab contains four
panes (**Tile 0**, **Tile 1**, **Tile
2**, and **Tile 3**), and each pane contains two ADCs. For a
ZCU111 board, **ADC 0** and **ADC 1** in **Tile
0** correspond to ADC 0 and ADC 1 in ADC tile 224, respectively. **ADC
0** and **ADC 1** in **Tile 1** correspond to
ADC 0 and ADC 1 in ADC tile 225, respectively. **ADC 0** and **ADC
1** in **Tile 2** correspond to ADC 0 and ADC 1 in ADC tile 226,
respectively. **ADC 0** and **ADC 1** in **Tile
3** correspond to ADC 0 and ADC 1 in ADC tile 227, respectively.

The selection of tiles and the respective ADCs is predefined when you set the
**RF interface** parameter to `ADC & DAC 1x1 RF
Interface`, `ADC & DAC 2x2 RF Interface`,
`ADC & DAC 4x4 RF Interface`, `ADC & DAC 8x8
RF Interface`, or `ADC & DAC 16x16 RF
Interface`. You cannot modify the tile and ADC selection when you select these
predefined options. To modify the tile and ADC selections, set the **RF
interface** parameter to `Customize`.

### **Output data as frame** — Option to output data as frame of samples `on` (default) | `off`

Select this parameter to output data as a frame of samples. Clear this parameter
to output data as a scalar.

### **Match parameters of all ADCs** — Matching parameters of all ADCs `on` (default) | `off`

Select this parameter to apply the same parameter values to all of the selected
ADCs.

Clear this parameter to specify different parameter values for each of the
selected ADCs.

#### Dependencies

To enable this parameter, set the **RF interface** parameter to
`Customize`.

### **Sample rate (MSPS)** — Data sampling rate `1000` (default) | scalar

Specify the sampling rate as a scalar in a range that is based on the selected
hardware board. Units are in mega samples per second.

This table shows the sampling rate range of the block for the supported
Zynq
UltraScale+ RFSoC Gen 1, Gen 2, Gen 3, and DFE devices.

| Generation | Device | Sampling Rate Range (MSPS) |
| --- | --- | --- |
| Gen 1 | ZU25DR | [1000, 4096] |
| ZU27DR | [1000, 4096] |
| ZU28DR | [1000, 4096] |
| ZU29DR | [500, 2058] |
| Gen 2 | ZU39DR | [500, 2220] |
| Gen 3 | ZU47DR | [1000, 5000] |
| ZU48DR | [1000, 5000] |
| ZU49DR | [500, 2500] |
| DFE | ZU63DR | [500, 2950] — For quad ADC tiles  [1000, 5900] — For dual ADC tiles |
| ZU64DR | [500, 2950] — For quad ADC tiles  [1000, 5900] — For dual ADC tiles |
| ZU65DR | [1000, 5900] |
| ZU67DR | [500, 2950] — For quad ADC tiles  [1000, 5900] — For dual ADC tiles |

### **Decimation mode (xN)** — Decimation factor `2` (default) | `1` | `3` | `4` | `5` | `6` | `8` | `10` | `12` | `16` | `20` | `24` | `40`

Specify the decimation factor.

**Note**

Gen 1 and Gen 2 devices support decimation factors of 1, 2, 4, and 8. Gen 3 and
DFE devices support decimation factors of 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24,
and 40.

### **Samples per clock cycle** — Number of samples per clock cycle `2` (default) | `1` | `3` | `4` | `5` | `6` | `7` | `8` | `10` | `11` | `12` | `14` | `16`

Specify the number of samples per clock cycle. Available options for the number of
samples per clock cycle vary with the selected hardware board and digital interface
type.

The block calculates the stream data width as: 16 x **Samples per clock
cycle**.

The block calculates the stream clock frequency as: **Sample rate
(MSPS)** / **Decimation mode (xN)** x **Samples
per clock cycle**.

### **Mixer type** — Mixer type `Bypassed` (default) | `Coarse` | `Fine`

Specify the mixer type.

To use `Bypassed`, set the **Digital
interface** parameter to `Real`.

To select either `Coarse` or
`Fine`, set the **Digital interface**
parameter to `I/Q`.

### **Mixer mode** — Mixer mode type `Real->Real` (default) | `Real->I/Q`

This parameter is read-only.

To use `Real->Real`, set the **Digital
interface** parameter to `Real`.

To use `Real->I/Q`, set the **Digital
interface** parameter to `I/Q`.

### **Mixer frequency** — Frequency of mixer `Fs/2` (default) | `Fs/4` | `-Fs/4`

Specify the mixer frequency.

#### Dependencies

To enable this parameter, set the **Digital interface**
parameter to `I/Q` and **Mixer type**
parameter to `Coarse`.

### **NCO frequency (GHz)** — NCO frequency `[0 0]` (default) | integer in the range [–10, 10]

Specify the NCO frequency values as a scalar or *m*-element row
vector, where *m* is the number of ADCs.

When you set the **RF interface** parameter to
`Customize` and clear the **Match parameters of all
ADCs** parameter, *m* must be 1.

#### Dependencies

To enable this parameter, set the **Digital interface**
parameter to `I/Q` and **Mixer type**
parameter to `Fine`.

### **NCO phase** — NCO phase `[0 0]` (default) | integer in the range [–180, 180]

Specify the NCO phase as a scalar or *m*-element row vector,
where *m* is the number of ADCs.

When you set the **RF interface** parameter to
`Customize` and clear the **Match parameters of all
ADCs** parameter, *m* must be 1.

#### Dependencies

To enable this parameter, set the **Digital interface**
parameter to `I/Q` and **Mixer type**
parameter to `Fine`.

### Advanced

**Common Parameters**

### **Multi tile sync** — Multitile synchronization `off` (default) | `on`

Select this parameter to enable MTS.

In generation, the Xilinx
RF Data Converter tool provides synchronization clocks and ADC and DAC
clocks to the RF Data Converter hardware IP. In MTS mode, these synchronization clocks
depend on the ADC and DAC sampling rates. Because, the Xilinx RF Data
Converter tool provides a set of fixed default synchronization clocks in MTS
mode and supports only these sample rates: `737.28`,
`1474.56`, `1966.08`, `2457.6`,
`2949.12`, `3072`, `3932.16`,
`4669.44`, `4915.2`, `5898.24`,
and `6144`.

For more information on MTS mode, see Zynq
UltraScale+ RFSoC RF Data Converter Gen 1/2/3/DFE LogiCORE IP Product Guide
(PG269) in the AMD documentation.

### **External PLL** — Option to enable external PLL `off` (default) | `on`

Select this parameter to enable the external phase-locked loop (PLL).

Each ADC and DAC tile includes an internal PLL. This internal PLL together with a
clocking instance provides ADC and DAC clocks for each tile as per the ADC or DAC
sampling rates. When you select this parameter, the internal PLL disables, and the
clocking circuit directly provides ADC and DAC clocks for each tile. The Xilinx
RF Data Converter tool supports only these external PLL clock
frequencies: `737.28`, `1474.56`,
`1966.08`, `2048`, `2457.6`,
`2949.12`, `3072`, `3194.88`,
`3276.8`, `3686.4`, `3932.16`,
`4096`, `4423.68`, `4669.44`,
`4915.2`, `5734.4`, `5898.24`,
`6144`, `6389.76`, `6400`, and
`6553.6`.

**DAC**

### **Real-time NCO ports** — Option to add real-time NCO ports for DAC `off` (default) | `on`

Select this parameter to add real-time NCO ports for the DAC. You can use these
ports to modify the NCO frequency and phase during run time.

Follow these instructions to modify the NCO frequency and phase for the DAC based
on the MTS mode selection.

****Multi tile sync** is `off`**

1. Set the required NCO frequency, phase, and phase reset values by using the
   **NCOFrequency**, **NCOPhase**,
   and **NCOPhaseReset** signals, respectively, of the **dacTxChyRealTimeCtrlIn** port.
2. Set the update enable bits to determine which NCO frequency and phase bits to
   update by using the **NCOUpdateEnable** signal of the **dacTxChyRealTimeCtrlIn**
   port.
3. Request an update of the DAC NCO settings by setting the **dacTxNCOUpdateReq** port to `High`.
4. Hold the frequency, phase, and phase rest values until the **dacTxNCOUpdateBusy** port remains `High`.

****Multi tile sync** is `on`**

1. Set the required NCO frequency, phase, and phase reset values by using the
   **NCOFrequency**, **NCOPhase**,
   and **NCOPhaseReset** signals, respectively, of all the **dacTxChyRealTimeCtrlIn** ports that you want to update. At the same time,
   set the update enable bits to determine which NCO frequency and phase bits to
   update by using the **NCOUpdateEnable** signal of all the **dacTxChyRealTimeCtrlIn**
   ports.
2. Disable the DAC from the `Sysref` clock signal by setting the
   **dacT0SysrefGating** port to `High`. Let this port remain
   `High` or set it to `Low` after the update is
   complete.
3. Request an update of the DAC NCO settings for Tile 0 by setting the
   **dacT0NCOUpdateReq** port to `High`. It sets Bit 1 of
   the **dacT0NCOUpdateBusy** port to `High`.
4. Set all the **dacTxNCOUpdateReq** ports in MTS mode to `High`.

   The NCO register writes are complete when all the **dacTxNCOUpdateBusy** ports in MTS mode, other than Bit 1 of the
   **dacT0NCOUpdateBusy** port, are `Low`.
5. Re-enable the `Sysref` clock signal by setting the **dacT0SysrefReEnable** port to `High`. The NCO update is
   complete when Bit 1 of the **dacT0NCOUpdateBusy** port goes
   `Low`.

For more information on NCO settings, see NCO Frequency Hopping in the AMD documentation.

#### Dependencies

To enable this parameter, set the **Digital interface**
parameter to `I/Q` and the **Mixer type**
parameter on the **DAC** tab to
`Fine`.

**ADC**

### **Real-time NCO ports** — Option to add real-time NCO ports for ADC `off` (default) | `on`

Select this parameter to add real-time NCO ports for the ADC. You can use these
ports to modify the NCO frequency and phase during run time.

Follow these instructions to modify the NCO frequency and phase for the ADC based
on the MTS mode selection.

****Multi tile sync** is `off`**

1. Set the required NCO frequency, phase, and phase reset values by using the
   **NCOFrequency**, **NCOPhase**,
   and **NCOPhaseReset** signals, respectively, of the **adcTxChyRealTimeCtrlIn** port.
2. Set the update enable bits to determine which NCO frequency and phase bits to
   update by using the **NCOUpdateEnable** signal of the **adcTxChyRealTimeCtrlIn**
   port.
3. Request an update of the ADC NCO settings by setting the **adcTxNCOUpdateReq** port to `High`.
4. Hold the frequency, phase, and phase reset values until the **adcTxNCOUpdateBusy** port remains `High`.

Follow these instructions to modify the NCO frequency and phase for the ADC when
**Multi tile sync** is `on`.

****Multi tile sync** is `on`**

1. Set the required NCO frequency, phase, and phase reset values by using the
   **NCOFrequency**, **NCOPhase**,
   and **NCOPhaseReset** signals, respectively, of all the **adcTxChyRealTimeCtrlIn** ports that you want to update. At the same time,
   set the update enable bits to determine which NCO frequency and phase bits to
   update by using the **NCOUpdateEnable** signal of all the **adcTxChyRealTimeCtrlIn**
   ports.
2. Disable the ADC from the `Sysref` clock signal by setting the
   **dacT0SysrefGating** port to `High`. Let this port remain
   `High` or set it to `Low` after the update is
   complete.
3. Request an update of the DAC NCO settings for Tile 0 by setting the
   **dacT0NCOUpdateReq** port to `High`. It sets Bit 1 of
   the **dacT0NCOUpdateBusy** port to `High`.
4. Set all the **adcTxNCOUpdateReq** ports in MTS mode to `High`.

   The NCO register writes are complete when all the **adcTxNCOUpdateBusy** ports in MTS mode, other than Bit 1 of the
   **dacT0NCOUpdateBusy** port, are `Low`.
5. Re-enable the `Sysref` clock signal by setting the **dacT0SysrefReEnable** port to `High`. The NCO update is
   complete when Bit 1 of the **dacT0NCOUpdateBusy** port goes
   `Low`.

For more information on NCO settings, see NCO Frequency Hopping in the AMD documentation.

#### Dependencies

To enable this parameter, set the **Digital interface**
parameter to `I/Q` and the **Mixer type**
parameter on the **ADC** tab to
`Fine`.

### **Real-time ports** — Option to add real-time ports for ADC `off` (default) | `on`

Select this parameter to add real-time ports for the ADC. Selecting this parameter
enables the threshold monitoring circuit, which compares the ADC sampled data with the
specified threshold values.

For more information on real-time ports and threshold settings, see Zynq
UltraScale+ RFSoC RF Data Converter Gen 1/2/3/DFE LogiCORE IP Product Guide
(PG269) in the AMD documentation.

### **Threshold1 mode** — Threshold mode for first threshold `Sticky over` (default) | `Sticky under` | `Hysteresis`

Select threshold mode for the first threshold as one of these options.

- `Sticky over` — Set the threshold status
  signal to `High` when the ADC sampled data exceeds the threshold
  value that you set in the **Threshold1** parameter. The threshold
  status signal remains `High` until you set the
  `PLEvent` signal in the
  **adcT*`x`*Ch*`y`*RealTimeCtrlIn**
  input bus port to `High`.
- `Sticky under` — Set the threshold status
  signal to `High` when the ADC sampled data remains below the
  threshold value, which you set in the **Threshold1** parameter,
  for the number of samples that you set in the **Number of sample(s) below
  threshold1** parameter. The threshold status signal remains
  `High` until you set the `PLEvent` signal in
  the
  **adcT*`x`*Ch*`y`*RealTimeCtrlIn**
  input bus port to `High`.
- `Hysteresis` — Set the threshold status signal
  to `High` when the ADC sampled data exceeds the upper threshold
  value. Set the threshold status signal to `Low` when the ADC
  sampled data remains below the lower threshold value for the number of samples
  that you specify in the **Number of sample(s) below threshold1**
  parameter.

#### Dependencies

To enable this parameter, select **Real-time ports**.

### **Threshold1** — Threshold value for first threshold `0` (default) | scalar | column vector

Specify the threshold value for the first threshold. For the sticky over threshold
mode, this value serves as the upper threshold value. For the sticky under threshold
mode, this value serves as the lower threshold value. For the hysteresis threshold
mode, specify the threshold values in the format
[*T*lower
*T*upper], where
*T*lower is the lower threshold value and
*T*upper is the upper threshold
value.

#### Dependencies

To enable this parameter, select **Real-time ports**.

### **Number of sample(s) below threshold1** — Number of samples below threshold value for first threshold `0` (default) | positive integer

Specify the number of samples below the threshold value for the first
threshold.

#### Dependencies

To enable this parameter, set the **Threshold1 mode** parameter
to `Sticky under` or
`Hysteresis`.

### **Threshold2 mode** — Threshold mode for second threshold `Sticky over` (default) | `Sticky under` | `Hysteresis`

Select threshold mode for the second threshold as one of these options.

- `Sticky over` — Set the threshold status
  signal to `High` when the ADC sampled data exceeds the threshold
  value that you set in the **Threshold2** parameter. The threshold
  status signal remains `High` until you set the
  `PLEvent` signal in the
  **adcT*`x`*Ch*`y`*RealTimeCtrlIn**
  input bus port to `High`.
- `Sticky under` — Set the threshold status
  signal to `High` when the ADC sampled data remains below the
  threshold value, which you set in the **Threshold2** parameter,
  for the number of samples that you set in the **Number of sample(s) below
  threshold2** parameter. The threshold status signal remains
  `High` until you set the `PLEvent` signal in
  the
  **adcT*`x`*Ch*`y`*RealTimeCtrlIn**
  input bus port to `High`.
- `Hysteresis` — Set the threshold status signal
  to `High` when the ADC sampled data exceeds the upper threshold
  value. Set the threshold status signal to `Low` when the ADC
  sampled data remains below the lower threshold value for the number of samples
  that you specify in the **Number of sample(s) below threshold2**
  parameter.

#### Dependencies

To enable this parameter, select **Real-time ports**.

### **Threshold2** — Threshold value for second threshold `0` (default) | scalar | column vector

Specify the threshold value for the second threshold. For the sticky over
threshold mode, this value serves as the upper threshold value. For the sticky under
threshold mode, this value serves as the lower threshold value. For the hysteresis
threshold mode, specify the threshold values in the format
[*T*lower
*T*upper], where
*T*lower is the lower threshold value and
*T*upper is the upper threshold
value.

#### Dependencies

To enable this parameter, select **Real-time ports**.

### **Number of sample(s) below threshold2** — Number of samples below threshold value for second threshold `0` (default) | positive integer

Specify the number of samples below the threshold value for the second
threshold.

#### Dependencies

To enable this parameter, set the **Threshold2 mode** parameter
to `Sticky under` or
`Hysteresis`.

## Libraries

SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU111 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU208 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU216 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU670

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

To automatically generate HDL code for your design and
execute on an SoC device, use the SoC Builder
tool.

## Version History

**Introduced in R2020a**

### R2025a: DFE devices support

The block now supports the Zynq
UltraScale+ RFSoC DFE devices. For a full list of supported devices, see Supported RFSoC Devices for RF Data Converter.

### R2024b: Simulation support for real-time ports

The block now supports the behavioral simulation of the real-time ports for the DACs and
ADCs.

### R2023b: Simulation support

The block now supports the simulation capability. Open the block mask and select one of
these simulation modes.

- **Pass-through** (default) — In this simulation mode, the
  block outputs the same data as the input. The interpolation, decimation, and mixers
  settings do not impact the input data while the block computes output values.
- **Behavioral** — In this simulation mode, the
  interpolation, decimation, and mixers settings impact the input data while the block
  computes output values.

### R2022a: Maximum of 16 samples per clock cycle, real-time NCO ports, real-time ports, and I/Q digital interface for ZCU208 board support

- Support for more than eight samples per clock cycle — Before R2022a, the
  block supports a maximum of eight samples per clock cycle. Starting from R2022a, the
  block supports a maximum of 16 samples per clock cycle for DACs and ADCs.
- Support for real-time NCO ports — The block now supports real-time NCO ports
  for DACs and ADCs.
- Support for real-time ports — The block now supports real-time ports for
  ADCs.
- Support for I/Q digital interface for ZCU208 board — The block now supports
  the I/Q digital interface for the Xilinx
  Zynq
  UltraScale+ RFSoC ZCU208 Evaluation Kit.

### R2021a: External PLL and extended device support

Starting from R2021a, you can use an external PLL clock source to provide ADC and DAC
clocks for each tile. To use this feature, select the **External PLL**
parameter of the RF Data Converter block.

Starting from R2021a, the RF Data Converter block supports these
generations of Zynq
UltraScale+ RFSoC devices. For a full list of supported devices, see Supported RFSoC Devices for RF Data Converter.

| Generation | Device |
| --- | --- |
| Gen 1 | ZU25DR |
| ZU27DR |
| ZU29DR |
| Gen 2 | ZU39DR |
| Gen 3 | ZU47DR |
| ZU48DR |
| ZU49DR |

### R2020b: Change in output valid port of RF Data Converter block

In R2020a, the RF Data Converter block has two valid ports
**adc*`x`*IValid** and
**adc*`x`*QValid**  corresponding to I and Q
data ports **adc***`x`***IData**
and **adc***`x`***Qdata**,
respectively.

In R2020b, the two valid output ports
**adc*`x`*IValid** and
**adc*`x`*QValid**  are removed and replaced
with one output port **adc*`x`*Valid** that
corresponds to both I and Q data ports. When you open a model containing an RF Data
Converter block that was created in R2020a and has its **Digital
interface** parameter set to `I/Q`, the output ports of
the block might not be correctly connected.

In this case, manually check and correct the port connections in your model to proceed
further.

## Description

Provide RF data path interface to hardware logic

The RF Data Converter block provides an RF data path interface to the
hardware logic. In generation, the SoC Builder tool maps
the block parameters to the RF Data Converter IP on the hardware.

The block consists of interpolation and decimation filters, complex mixers,
analog-to-digital converters (ADCs), and digital-to-analog converters (DACs).

- The interpolation filters upsample the input signal by the specified interpolation
  factor. Specify the interpolation factor by using the **Interpolation mode
  (xN)** parameter.
- The decimation filters downsample the input signal by the specified decimation factor.
  Specify the decimation factor by using the **Decimation mode (xN)**
  parameter.
- A complex mixer shifts the center frequency of the input signal to the specified
  carrier frequency. Specify the carrier frequency by using the **Mixer
  frequency** and **NCO frequency (GHz)** parameters.

The block supports a maximum of 16 ADC and 16 DAC data paths connecting to the hardware
logic. In the **Behavioral** simulation mode, you can simulate the
interpolation and decimation filters and complex mixers.

The block supports Zynq®
UltraScale+™ RFSoC Gen 1, Gen 2, Gen 3, and DFE devices. For a full list of supported
devices, see Supported RFSoC Devices for RF Data Converter. For specific Zynq
UltraScale+ RFSoC device information, see Zynq UltraScale+ RFSoC Product Information from the AMD® website.
