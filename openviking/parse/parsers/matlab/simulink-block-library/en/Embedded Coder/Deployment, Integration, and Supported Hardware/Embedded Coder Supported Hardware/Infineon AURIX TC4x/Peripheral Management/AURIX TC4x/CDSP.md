---
type: simulink-block
title: 'CDSP'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'cdsp'
documentation_source_path: 'infineonaurix/ref/cdsp.html'
language: en
---

# CDSP

## Ports

### Input

### **primary input** — Input data from DSADC block, EXMOD, TMADC block, or GP registers scalar

The port accepts incoming data from the DSADC block, EXMOD, TMADC block, or
GP registers and applies different signal processing techniques based on the
application. For the DSADC block, you must set the Result type
parameter to `Counts` because the CDSP block accepts
data in counts. For GP registers, the block accepts data from Simulink® source blocks such as the Repeating Sequence Stair block.

**Note**

- In a code generation workflow, the port accepts data from the
  DSADC block, EXMOD, TMADC block, or GP registers.
- In a simulation workflow, the port accepts data from any
  Simulink source block with discrete output.

**Data Types:** `uint16` | `int16`

### **secondary input** — Input data to use in Math filter block scalar

The port accepts incoming data from the DSADC block, EXMOD, TMADC block, or
GP registers and uses this secondary input data for addition or subtraction
with CDSP secondary input in the Math filter block. For the DSADC block, you
must set the Result type
parameter to `Counts` because the CDSP block accepts
data in counts.

#### Dependencies

To enable this port, set the **DSP filter chain**
parameter to `Advanced average 1 (FC1)`,
`Basic data accumulation (FC2)`, or
`Advanced average 2 (FC4)`. Any of these options
adds a **Math** tab, where you must set the **Math
operation** parameter to `Addition with CDSP
secondary input` or `subtraction with CDSP
secondary input`

**Data Types:** `uint16` | `int16`
### Output

### **filtereddata** — 16-bit filtered data vector

The block outputs the filtered data as 16-bit values in the form of an
N-by-1 array. N varies based on the timestamp, number of output samples, and
FIFO depth configuration.

The size of the output depends on the values of the other parameters in the block.

| Enable FIFO | Enable timestamp output | Number of output samples | FIFO depth | Size of filtereddata |
| --- | --- | --- | --- | --- |
| Disable | Disable | NA | NA | 1-by-1 |
| Enable | NA | NA | 1-by-1 |
| Enable | Disable | 1 | 4 | 4-by-1 |
| 3 | 3-by-1 |
| 2 | 2-by-1 |
| 1 | 1-by-1 |
| 2 | 4 | 4-by-1 |
| 2 | 2-by-1 |
| Enable | 1 | 4 | 3-by-1 |
| 3 | 2-by-1 |
| 2 | 1-by-1 |
| 2 | 4 | 3-by-1 |

If the FIR coefficients do not change, the CDSP block uses
the default filter coefficients when you set the **DSP Filter
chain** parameter to `Demo FIR (FC0)` in
the Block Parameters dialog box.

**Note**

To avoid data type conversion errors while using the block, make sure to
set the output and input data of the same type.

This table shows the results from the accumulation filter when you provide a
constant input to the CDSP block and set the DSP Filter chain
parameter to `Demo FIR (FC0)` with default
coefficients. The block populates the default coefficient values in the Coefficients
parameter.

| CDSP Input | Output `Data Type` | Accumulation Filter Results | Result Description |
| --- | --- | --- | --- |
| int16(100) | int16 | 100 |  |
| int16(32767) | int16 | 32767 |
| int16(0) | int16 | 0 |
| int16(-32768) | int16 | -32768 |
| uint16(100) | uint16 | 32768 | 100 + 32768 = 32868, CDSP block reports the lower 16 bits of the result |
| uint16(65535) | uint16 | 32767 | 65535 + 32768 = 98303, CDSP block reports the lower 16 bits of 98303 (32767) |
| uint16(0) | uint16 | 32768 | 0 + 32768 = 32768, CDSP block reports the lower 16 bits of the result |
| uint16(32767) | uint16 | 65535 | 32767 + 32768 = 65535, CDSP block reports the lower 16 bits of the result |
| uint16(32768) | uint16 | 0 | 326768 + 32768 = 65536, CDSP block reports the lower 16 bits of the result |

You can observe from the table that when the data type of the output data is
`uint16`, the CDSP hardware adds 32768 (2^15) to the output
result. For example, assume that the CDSP hardware outputs a 1000 0000 0000
0000 (16-bit value). If you set the output data type to
`int16`, the result from the accumulation filter is -32767
((-2^15 \* 1) + (2^14 \* 0) + (2^13 \* 0) + ….. + (2^0 \* 0)). When you set the
output data type to `uint16`, the result from the accumulation
filter is 32768 ((2^15 \* 1) + (2^14 \* 0) + (2^13 \* 0) + ….. + (2^0 \*
0)).

**Data Types:** `uint16` | `int16`

### **timestamp** — Timestamp of 16-bit counter value `scalar`

The port outputs the status of the 16-bit counter value of the timestamp
counter.

#### Dependencies

To enable this port, select the **Enable timestamp
output** parameter.

**Data Types:** `uint16`

## Parameters

### Filter Config

### **Enable timestamp output** — Option to enable timestamp output `off` (default) | `on`

Select this parameter to configure the **timestamp** output
port.

Selecting this parameter enables options in the
**Timestamp** tab and Timestamp event (under
**Events** tab) in the CDSP
Peripheral Configuration.

**Note**

As the timestamp is always associated with the trigger, it is
recommended that you configure and provide the trigger accordingly, when
the timestamp is enabled. Otherwise, the FIFO functionality does not
work, as timestamp is flushed into FIFO first and then to the result
registers.

### **DSP Filter chain** — Option to select filter chain `Demo FIR (FC0)` (default) | `Advanced average 1 (FC1)` | `Basic data accumulation (FC2)` | `Advanced median (FC3)` | `Advanced average 2 (FC4)` | `Basic AURIX (FCM)`

Select the filter chain to be used by the CDSP block.

- `Demo FIR (FC0)` — Select this option to use
  the finite impulse response (FIR) filter block.
- `Advanced average 1 (FC1)` — Select this
  option to use the filter blocks in the predefined sequence of FIR >
  sixth-order infinite impulse response filter (IIR6) > Math filter (MAT) >
  Average filter (AVG).
- `Basic data accumulation (FC2)` — Select this
  option to use the filter blocks in the predefined sequence of FIR > IIR6
  > MAT > Data accumulation filter (DA).
- `Advanced median (FC3)` — Select this option
  to use the filter blocks in the predefined sequence of FIR > IIR6 >
  Median filter (MDN).
- `Advanced average 2 (FC4)` — Select this
  option to use the filter blocks in the predefined sequence of IIR6 > FIR
  > MAT > AVG.
- `Basic AURIX (FCM)` — Select this option to
  use the filter blocks in the predefined sequence of FIR > first-order
  infinite impulse response filter (IIR1) > DA.

The block adds the **FIR, IIR6, IIR1, MAT, AVG**, and
**DA** tabs in the block parameters dialog box, depending
on the choice of the **DSP filter chain** parameter. You can
set the parameters of the filter block in these tabs.

### **Output datatype** — Data type of filtered output `int16` (default) | `uint16`

Select the data type of the filtered output.

### Filter Config > FIFO Configuration

### **Enable FIFO** — Option to enable FIFO register `off` (default) | `on`

Select this parameter to enable first-in first-out (FIFO) register.

### **Elements to retrieve from FIFO** — Output samples to read from FIFO `1` (default) | `2`

Configure whether to read a single sample or double samples at a
time.

Selecting `2` helps in fetching the data faster
from the FIFO.

#### Dependencies

To enable this parameter, select the **Enable FIFO**
parameter.

### **FIFO depth** — FIFO register depth `4` (default) | `3` | `2` | `1` (only if Enable Timestamp is not selected)

Specify the FIFO level after which the module generates service
request.

#### Dependencies

To view this parameter, select the **Enable FIFO**
parameter.

### FIR

### **Bypass FIR block** — Option to bypass FIR block in the filter chain `off` (default) | `on`

Select this parameter to bypass the FIR block in the filter chain.

### **Coefficients** — Coefficients of FIR filter `[8, 13, -39, -130, -170, -135, -68, 27, 220, 424, 400, 124, -268, -617, -763, -604, -74, 655, 1244, 1419, 971, -26, -1390, -2569, -2842, -1783, 736, 4316, 8296, 11711, 13682, 13682, 11711, 8296, 4316, 736, -1783, -2842, -2569, -1390, -26, 971, 1419, 1244, 655, -74, -604, -763, -617, -268, 124, 400, 424, 220, 27, -68, -135, -170, -130, -39, 13, 8]` (default) | scalar in the range (-32767 to 32767) | vector in the range (-32767 to 32768)

Specify the FIR filter coefficients of a size ranging from 1-by-1 to
1-by-128.

#### Dependencies

To enable this parameter, disable the **Bypass FIR
block** parameter.

### **Decimation rate** — Ratio of input data rate to output data rate in FIR filter `1` (default) | `2` | `4` | `8` | `16`

Specify the ratio of input data rate to output data rate in the FIR
filter.

**Note**

- In a code generation workflow, the block supports a decimation
  rate ranging from 1 to 16.
- In a simulation workflow, the block supports a decimation rate
  of 1.

#### Dependencies

To enable this parameter, disable the **Bypass FIR
block** parameter.

### IIR6

### **Bypass IIR6 block** — Option to bypass IIR6 filter block in filter chain `off` (default) | `on`

Select this parameter to bypass the IIR6 filter block in the filter
chain.

### **Coefficients** — Coefficients of IIR6 filter `[16384, 0, 0, 16384, 0, 0, 16384, 0, 0, 16384, 0, 0, 16384, 0, 0, 16384, 0, 0]` (default) | vector in the range (-32767 to 32768)

Specify the 1-by-18 filter coefficients in the sequence of [a00, a01,
a02, a10,
a11, a12,
a20, a21,
a22, b00,
b01, b02,
b10, b11,
b12, b20,
b21, b22]  for the IIR6 filter with the transfer function:

b00+b01z−1+b02z−2a00+a01z−1+a02z−2×b10+b11z−1+b12z−2a10+a11z−1+a12z−2×b20+b21z−1+b22z−2a20+a21z−1+a22z−2

#### Dependencies

To enable this parameter, disable the **Bypass IIR6
block** parameter.

### **Decimation rate** — Ratio of input data rate to output data rate in IIR6 filter `1` (default) | `2` | `4` | `8` | `16`

Specify the ratio of input data rate to output data rate in the IIR6
filter.

**Note**

- In a code generation workflow, the block supports a decimation
  rate ranging from 1 to 16.
- In a simulation workflow, the block supports a decimation rate
  of 1.

#### Dependencies

To enable this parameter, disable the **Bypass IIR6
block** parameter.

### **Bit extension** — Number of bits to shift in input and output data of IIR6 filter block `0` (default) | scalar in the range (0, 7)

Specify the number of bits to shift in the IIR6 filter block to improve
precision.

#### Dependencies

To enable this parameter, disable the **Bypass IIR6
block** parameter.

### Math

### **Bypass math block** — Option to bypass Math filter block in filter chain `off` (default) | `on`

Select to bypass Math filter block in the filer chain.

### **Math operation** — Option to select mathematical operation `Addition with constant` (default) | `Addition with CDSP secondary input` | `Subtraction with constant` | `Subtraction with CDSP secondary input` | `Multiplication with constant`

Specify the mathematical operation for the Math filter.

If you choose the `Addition with CDSP secondary
input` or `Subtraction with CDSP secondary
input`, the CDSP block adds an input port for the secondary
input.

#### Dependencies

To enable this parameter, disable the **Bypass math
block** parameter.

### **Constant value (-32768 to 32767)** — Option to provide constant value for mathematical operation `0` (default) | scalar in the range (-32768 to 32767)

Specify the constant value to use in the Math filter.

#### Dependencies

To enable this parameter, disable the **Bypass math
block** parameter and set the **Math
operation** parameter to `Addition with
constant`, `Subtraction with
constant`, or `Multiplication with
constant`.

### **Bit shift after math operation (-32 to 32)** — Number of bits for arithmetic right-shift on the Math filtered output `0` (default) | scalar in the range (-32 to 32)

Specify the number of bits for arithmetic right-shift operation on the Math
filtered output to correct the output in case of overflow.

#### Dependencies

To enable this parameter, disable the **Bypass math
block** parameter.

### Average

### **Bypass avegare block** — Option to bypass AVG filter block in the filter chain `off` (default) | `on`

Select this parameter to bypass AVG filter block in the filer chain.

### **Number of samples** — Option to select the number of samples for averaging operation `1` (default) | `2` | `4` | `8` | `16` | `32` | `64` | `128`

Specify the number of samples to consider for the averaging operation.

#### Dependencies

To enable this parameter, disable the **Bypass average
block** parameter.

### Median

### **Bypass median block** — Option to bypass MDN filter block in filter chain `off` (default) | `on`

Select this parameter to bypass the MDN filter block in the filter
chain.

### **Number of samples** — Option to select the number of samples median operation `1` (default) | `3` | `5` | `7` | `9`

Specify the number of samples to consider for the median filter.

#### Dependencies

To enable this parameter, disable the **Bypass median
block** parameter.

### IIR1

### **Bypass IIR1 block** — Option to bypass IIR1 filter block in filter chain `off` (default) | `on`

Select this parameter to bypass the IIR1 filter block in the filter
chain.

#### Dependencies

To enable this parameter, disable the **Bypass IIR1
block** parameter.

### **Coefficients** — Coefficients of IIR6 filter `[16384, -12288, 16384, -16384]` (default) | vector in the range (-32767 to 32768)

Specify the 1-by-4 filter coefficients in the sequence of [a0, a1,
b0, b1]  for the IIR1 filter with transfer function:

b0+b1z−1a0+a1z−1

#### Dependencies

To enable this parameter, disable the **Bypass IIR1
block** parameter.

### DA

### **Bypass DA block** — Option to bypass DA filter block in filter chain `off` (default) | `on`

Select this parameter to bypass the DA filter block in the filter
chain.

Disable this parameter to configure data accumulation parameters in the
**Integrator Control** tab in CDSP
Peripheral Configuration tool.

### **Samples in accumulation cycle** — Option to select number of data samples per accumulation cycle `1` (default) | scalar in the range (1, 512)

Specify the number of data samples per accumulation cycle.

#### Dependencies

To enable this parameter, disable the **Bypass DA
block** parameter.

### **Samples to discard** — Option to select number of data samples to discard during accumulation process `0` (default) | scalar in the range (0, 63)

Specify the number of data samples to discard during the accumulation
process.

#### Dependencies

To enable this parameter, disable the **Bypass DA
block** parameter.

### **Adjust gain by right shift on DA result** — Option to select number of bits for right shift operation on data accumulation filter result `0` (default) | scalar in the range (0, 10)

Specify the number of bits to use for a right shift operation on the DA
result for gain adjustment.

#### Dependencies

To enable this parameter, disable the **Bypass DA
block** parameter.

### **Disable filter chain restart** — Option to disable restarting all filter blocks before DA filter block `off` (default) | `on`

Select this parameter to disable the restarting of all the filter blocks
prior to DA filter block in the selected filter chain.

#### Dependencies

To enable this parameter, disable the **Bypass DA
block** parameter.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Process output from ADC peripherals of Infineon AURIX TC4x

The CDSP block applies signal processing techniques to digital data coming from the
DSADC
block (using the on-chip modulator or external modulator (EXMOD)), TMADC
block, or general purpose (GP) registers. Based on the filter properties and the filter
chain that you specify in the Converter Digital Signal Processing (CDSP) block, the block
outputs the filtered data as 16-bit signed and unsigned integers.

When you enable the timestamp output, the block provides an additional output port to
read the timestamp as a 16-bit unsigned value.
