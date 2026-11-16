---
type: simulink-block
title: 'OQPSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PSK'
documentation_page: 'oqpskmodulatorbaseband'
documentation_source_path: 'ref/oqpskmodulatorbaseband.html'
language: en
---

# OQPSK Modulator Baseband

## Ports

### Input

### **In** — Input data integer column vector | bit column vector

Input data, specified as an integer or bit column vector.

The input signal is processed based on the setting selected for
Input type.

**Data Types:** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out** — Output baseband waveform column vector

Output baseband waveform, returned as a column vector of complex data.
The **Output data
type** parameter specifies the data type of the output
signal.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Modulation

### **Input type** — Input type `Integer` (default) | `Bit`

Input type, specified as `Integer` or
`Bit`.

- When you set **Input type** to
  `Integer`, the input can be a
  scalar value or column vector, the length of which is the number
  of input symbols.
- When you set **Input type** to
  `Bit`, the input width must be an
  integer multiple of two.

The output sample period is the period of each integer or bit pair in
the input divided by Samples per symbol.

### **Symbol mapping** — Signal constellation bit mapping `Gray` (default) | `Binary` | custom 4-element numeric vector of integers with values from 0 to 3

Signal constellation bit mapping, specified as
`Gray`, `Binary`,
or a custom 4-element numeric vector of integers with values from 0 to
3.

| Setting | Constellation Mapping for Integers | Constellation Mapping for Bits | Comment |
| --- | --- | --- | --- |
| `Gray` | Integer order Q1: 0, Q2: 1, Q3: 3, and Q4: 2 | Bit order Q1: 00, Q2: 01, Q3: 11 and Q4: 10 | The signal constellation mapping is Gray-encoded. |
| `Binary` | Integer order Q1: 0, Q2: 1, Q3: 2, and Q4: 3 | Bit order Q1: 00, Q2: 01, Q3: 10 and Q4: 11 | The signal constellation mapping for the input integer `m` (0 ≤ `m` ≤ 3) is the complex value `e(j*(PhaseOffset+π/4) + j*2*π*m/4)`. |
| Custom 4-element numeric vector of integers with values from 0 to 3 | Integer order Q1: a, Q2: b, Q3: c, and Q4: d | Bit order Q1: a, Q2: b, Q3: c, and Q4: d | Elements [a b c d] must be composed of the set of values [0, 1, 2, 3] in any order. |

### **Phase offset (rad)** — Phase of zeroth point of signal constellation `0` (default) | scalar

Phase offset from π/4, specified as a scalar in radians. The phase
offset is applied to the zeroth point of the signal constellation before
delay of quadrature component. After the OQPSK imaginary-component
delay, the signal is normalized with unity power.

**Example:** Setting **Phase offset (rad)** to
`pi/4` aligns the zeroth point of the QPSK signal
constellation point on the axes, {(1,0), (0,j), (-1,0),
(0,-j)}.

### **View Constellation** — Option to plot reference constellation button

Click **View
Constellation** on the block mask to visualize a signal constellation for the
specified block parameters. Before viewing a constellation, apply the parameter settings. For
more information, see View Constellation of Modulator Block.

**Note**

The constellation that displays does not depict the IQ delay
introduced by the OQPSK modulator.

### Filtering

### **Pulse shape** — Filtering pulse shape `Half sine` (default) | `Normal raised cosine` | `Root raised cosine` | `Custom`

Select the filtering pulse shape: `Half
sine`, `Normal raised cosine`,
`Root raised cosine`, or
`Custom`.

### **Rolloff factor** — Raised cosine filter rolloff factor `0.2` (default) | scalar

Raised cosine filter rolloff factor, specified as a scalar in the
range [`0`, `1`].

#### Dependencies

This property is enabled when **Pulse
shape** is `Normal raised
cosine` or `Root raised
cosine`.

### **Filter span (in symbols)** — Filter length `10` (default) | scalar

Filter length in symbols, specified as a scalar. An ideal raised
cosine filter has an infinite impulse response. However, to realize a
practical implementation of this filter, the object truncates the
impulse response to **Filter span (in symbols)**
symbols.

#### Dependencies

This property is enabled when Pulse shape is `Normal raised
cosine` or `Root raised
cosine`.

### **Filter numerator** — Filter numerator `[0.7071 0.7071]` (default) | row vector

FIR filter numerator, specified as a row vector.

#### Dependencies

This parameter is enabled when Pulse shape is `Custom`.

### **Filter Denominator** — Filter denominator `1` (default) | row vector

FIR filter denominator, specified as a row vector.

#### Dependencies

This parameter is enabled when Pulse shape is `Custom`.

### **Samples per symbol** — Number of samples per symbol `4` (default) | positive even integer

Number of samples per symbol, specified as a positive even
integer.

### Other Parameters

### **Rate options** — Processing rate option `Enforce single-rate processing` (default) | `Allow multirate processing`

- `Enforce single-rate processing`
  — Executes the model, ensuring that the input and output
  signals have the same port sample time. The block implements
  the rate change by making a size change at the output when
  compared to the input. For integer inputs, the output width
  equals Samples per symbol times the number of
  symbols.

  For an example, see Single-Rate Processing with OQPSK Modulator Block.
- `Allow multirate processing`
  — Executes the model, allowing the input and output
  signals to have different port sample times. The output
  sample time equals the symbol period divided by Samples per symbol.

  For an example, see Multirate Processing with OQPSK Modulator Block.

### **Output data type** — Output data type `double` (default) | `single`

Select the output data type: `double` or
`single`.

## Libraries

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Modulate using OQPSK method

The OQPSK Modulator Baseband block modulates the input signal using the offset quadrature phase
shift keying (OQPSK) method and applies pulse shape filtering to the waveform. For more
information, see Pulse Shaping Filter. The output is a baseband
representation of the modulated signal.

For information about delays incurred by modulator-demodulator pair processing, see
Modulation Delays.
