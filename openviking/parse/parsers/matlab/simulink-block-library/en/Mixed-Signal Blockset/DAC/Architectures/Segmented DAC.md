---
type: simulink-block
title: 'Segmented DAC'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'DAC / Architectures'
documentation_page: 'segmenteddac'
documentation_source_path: 'ref/segmenteddac.html'
language: en
---

# Segmented DAC

## Ports

### Input

### **digital** — Digital input signal integer

Digital input signal to DAC, specified as an integer.

If the **Input polarity** parameter is set to
`Bipolar`, the allowed range of the signal is
[−2*NBits*-1,
2*NBits*-1].

If the **Input polarity** parameter is set to
`Unipolar`, the allowed range of the signal is [0,
2*NBits*-1].

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **start** — External clock to start conversion scalar

External clock to start conversion, specified as a scalar. The digital to-analog
conversion process starts at the rising edge of the signal at the
**start** port.

#### Dependencies

To enable this port, select **Use external start
clock**.

**Data Types:** `double`
### Output

### **analog** — Converted analog output signal scalar

Converted analog output signal, returned as a scalar.

**Data Types:** `double`

## Parameters

### **Input polarity** — Define DAC input data polarity `Unipolar` (default) | `Bipolar`

Define the polarity of the DAC input data. Set **Input polarity**
to:

- `Unipolar` when the digital input can only be
  positive.
- `Bipolar` when the digital input can be both positive
  and negative.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Polarity` |
| **Type:** character vector |
| **Values:** `Unipolar` | `Bipolar` |
| **Default:** `Unipolar` |

### **Use external start clock** — Connect to external start conversion clock on (default) | off

Select to connect to an external start conversion clock. This option is selected by
default. If you deselect this option, a Sampling Clock
Source block inside the Segmented DAC block is used to generate
the start conversion clock.

### **Conversion start frequency (Hz)** — Frequency of internal start conversion clock `1e6` (default) | real scalar

Frequency of the internal start conversion clock, specified as a real scalar in Hz.
The **Conversion start frequency** parameter determines the conversion
rate at the start of conversion.

#### Dependencies

To enable this parameter, deselect **Use external start
clock**.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `StartFreq` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `1e6` |

### **Reference (V)** — DAC output reference magnitude `0.5` (default) | real scalar

The reference magnitude of the DAC output, specified as a real scalar in volts.
**Reference (V)** is one least significant bit (LSB) greater than the
maximum achievable output.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Ref` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0.5` |

### **Bias (V)** — Difference between analog output for code zero and analog zero `0` (default) | real scalar

The difference between the analog output for code zero and analog zero in an
unimpaired DAC, specified as a real scalar in volts.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Bias` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `0` |

### **Settling time (s)** — Time required for output to settle `2e-7` (default) | nonnegative real scalar

The time required for the output of the DAC to settle to within some fraction of its
final value, specified as a nonnegative real scalar in seconds.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SettlingTime` |
| **Type:** character vector |
| **Values:** real scalar |
| **Default:** `2e-7` |

### **Settling time tolerance (LSB)** — Tolerance for calculating settling time `0.5` (default) | positive real scalar

The tolerance allowed for calculating settling time, specified as a positive real
scalar in LSB. The output of the DAC must settle within the **Settling time
tolerance (LSB)** by **Settling time (s)**.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SettlingTimeTolerance` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `0.5` |

#### Segment settings

### **Bit width** — Number of physical input bits for DAC segment integer scalar greater than or equal to 2

Number of physical input bits for the DAC segment, specified as an integer scalar
greater than or equal to 2. For the first two DAC segments, the default value of
**Bit width** is `4`. For subsequent segments, the
default value is `2`.

### **Bits** — Bit ranges of each segment vector

Bit ranges of each segment, returned as a vector. If you change the index of any
segment by moving it up or down, the bit range of that segment changes accordingly. This
parameter is read-only.

### **Topology** — Topology of base DAC segment `Binary Weighted` (default)

The topology of the base DAC for the segment. The block uses a `Binary
Weighted` DAC. This parameter is read-only.

### **Offset error** — Shift quantization steps `0` (default) | real scalar

Shift quantization steps by the value you provide in **Offset
error** parameter, specified as a real scalar.

### **Offset error unit** — Unit of offset error `LSB` (default) | `FS` | `%FS`

Unit of offset error, specified as `LSB`, full scale
(`FS`), or percentage full scale
(`%FS`).

**Note**

The full scale range of the converter is defined as the difference between the
last and first code on the +0.5 LSB compensated transfer curve. In a +0.5 LSB
compensated transfer curve, first code is 0.5 LSB wide while the last code is 1.5 LSB
wide. The input values must be considered within the full scale range of the
converter.

**Note**

LSB is calculated by the equation LSB = Full scale range of converter2NBits.

### **Gain error** — Error in slope of DAC transfer curve `0` (default) | real scalar

Error in the slope of the DAC transfer curve, specified as a real scalar.

### **Gain error unit** — Unit of gain error `LSB` (default) | `FS` | `%FS`

Unit of gain error, specified as `LSB`, full scale
(`FS`), or percentage full scale
(`%FS`).

**Note**

The full scale range of the converter is defined as the difference between the
last and first code on the +0.5 LSB compensated transfer curve. In a +0.5 LSB
compensated transfer curve, first code is 0.5 LSB wide while the last code is 1.5 LSB
wide. The input values must be considered within the full scale range of the
converter.

**Note**

LSB is calculated by the equation LSB = Full scale range of converter2NBits.

### **Move selected segment up** — Move selected segment up one row button

Click to move the selected segment up one row.

### **Move selected segment down** — Move selected segment down one row button

Click to move the selected segment down one row.

### **New Segment** — Add new DAC segment button

Click to add a new DAC segment with default values. Currently you can add up to five
DAC segments to the Segmented DAC block.

### **Duplicate Selected** — Duplicate selected segment button

Click to add a new DAC segment by duplicating a selected segment. Currently you can
add up to five segments to the Segmented DAC block.

### **Delete Selected** — Delete selected segment button

Click to delete the selected DAC segment from the Segmented DAC
block.

## Libraries

Mixed-Signal Blockset / DAC / Architectures

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Convert large digital input to analog signal using arrangement of smaller DACs

The Segmented DAC block converts a large digital signal into analog output
by splitting it over several smaller DACs. The Segmented DAC block supports up
to five binary-weighted segmented DACs.
