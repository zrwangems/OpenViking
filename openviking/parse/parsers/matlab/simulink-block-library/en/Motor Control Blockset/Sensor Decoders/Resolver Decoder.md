---
type: simulink-block
title: 'Resolver Decoder'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensor Decoders'
documentation_page: 'resolverdecoder'
documentation_source_path: 'ref/resolverdecoder.html'
language: en
---

# Resolver Decoder

## Ports
```yaml
ports:
- name: V Sin
  summary: Sampled secondary sine signal vector
  direction: input
  data_types: single | double | fixed point
- name: V Cos
  summary: Sampled secondary cosine signal vector
  direction: input
  data_types: single | double | fixed point
- name: Reset
  summary: Reset PLL scalar
  direction: input
  data_types: single | double | fixed point
- name: θm
  summary: Motor mechanical position scalar
  direction: output
  data_types: single | double | fixed point
- name: sinθe
  summary: Sine of electrical motor position scalar
  direction: output
  data_types: single | double | fixed point
- name: cosθe
  summary: Cosine of electrical motor position scalar
  direction: output
  data_types: single | double | fixed point
- name: ωm
  summary: Motor mechanical speed scalar
  direction: output
  data_types: single | double | fixed point
- name: PLLEn
  summary: PLL status scalar
  direction: output
  data_types: single | double | fixed point
```

### Input

### **V Sin** — Sampled secondary sine signal vector

Sampled secondary sine waveform output from the resolver. When using sinusoidal
excitation, normalize this signal so that it lies in the range [-1, 1] and is centred
at 0.

**Data Types:** `single` | `double` | `fixed point`

### **V Cos** — Sampled secondary cosine signal vector

Sampled secondary cosine waveform output from the resolver. When using sinusoidal
excitation, normalize this signal so that it lies in the range [-1, 1] and is centred
at 0.

**Data Types:** `single` | `double` | `fixed point`

### **Reset** — Reset PLL scalar

Reset the phase-locked loop that the block uses internally.

#### Dependencies

To enable this port, set the **Computation method** parameter
to `PLL`.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **θm** — Motor mechanical position scalar

Mechanical angular position of the resolver (and the motor) in either degrees,
radians, or per-unit.

**Data Types:** `single` | `double` | `fixed point`

### **sinθe** — Sine of electrical motor position scalar

Sine of the electrical angular position of the motor.

**Data Types:** `single` | `double` | `fixed point`

### **cosθe** — Cosine of electrical motor position scalar

Cosine of the electrical angular position of the motor.

**Data Types:** `single` | `double` | `fixed point`

### **ωm** — Motor mechanical speed scalar

Mechanical speed of the motor in either degrees/sec, radians/sec, RPM, or
per-unit.

**Data Types:** `single` | `double` | `fixed point`

### **PLLEn** — PLL status scalar

This port indicates the readiness of the PLL that the block uses internally. The
port can provide the following values:

- `1` — Indicates that the PLL (and the other block outputs)
  are ready to use.
- `0` — Indicates that the PLL (and the other block outputs)
  are not yet ready.

#### Dependencies

To enable this port, set the **Computation method** parameter
to `PLL`.

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters:
- name: Computation method
  summary: Computation method used by block Arithmetic (default) | PLL
  group: ''
- name: Block Output
  summary: Output of block Mechanical position (default) | Sine and Cosine electrical position | Mechanical speed
  group: ''
- name: Number of pole-pairs for resolver
  summary: Resolver pole pair count 1 (default) | scalar
  group: Input Parameters
- name: Type of excitation method
  summary: Resolver excitation method Sinusoidal Excitation (default) | Square Pulse Excitation
  group: Input Parameters
- name: Enable input normalization
  summary: Enable block to normalize inputs off (default) | on
  group: Input Parameters
- name: Discrete step size (s)
  summary: Sample time after which block executes again 50e-6 (default) | scalar
  group: Input Parameters
- name: Number of pole-pairs for motor
  summary: Motor pole pair count 3 (default) | scalar
  group: Inputs for Sine and Cosine electrical position
- name: Position offset (mechanical radians)
  summary: Resolver mechanical position offset (in radians) 0 (default) | scalar
  group: Inputs for Sine and Cosine electrical position
- name: Integer rounding mode
  summary: Rounding mode for fixed-point operations Zero (default) | Simplest
  group: Inputs for Sine and Cosine electrical position
- name: Phase delay (electrical radians)
  summary: Phase delay for input signals 0.1746 (default) | scalar
  group: Inputs for sinusoidal excitation method
- name: Number of samples per excitation cycle
  summary: Samples per cycle of input signal 16 (default) | even scalar greater than zero
  group: Inputs for sinusoidal excitation method
- name: Maximum application frequency (Hz)
  summary: Maximum applicable input frequency 7500 (default) | scalar
  group: PLL Parameters
- name: Speed filter cutoff frequency (Hz)
  summary: Cutoff frequency of lowpass filter 10 (default) | scalar
  group: PLL Parameters
- name: Number of data points for lookup table
  summary: Size of lookup table array 1024 (default) | scalar
  group: PLL Parameters
- name: Proportional (P)
  summary: Proportional controller gain 942.4778 (default) | scalar
  group: PLL Parameters
- name: Integral (I)
  summary: Integral controller gain 222066.099 (default) | scalar
  group: PLL Parameters
- name: Error threshold (Hz)
  summary: PLL error threshold 2e-2 (default) | scalar
  group: PLL Parameters
- name: Position unit
  summary: Unit of position output Radians (default) | Degrees | Per-unit
  group: Output Parameters
- name: Position data type
  summary: Data type of angular position output single (default) | double | fixed point
  group: Output Parameters
- name: Table data type
  summary: Data type of sine-cosine lookup table single (default) | double | fixed point
  group: Output Parameters
- name: Speed unit
  summary: Unit of speed output Degrees/Sec (default) | Radians/Sec | RPM | Per-unit
  group: Output Parameters
- name: Speed data type
  summary: Data type of angular speed output single (default) | double | fixed point
  group: Output Parameters
- name: Base speed (RPM)
  summary: Base speed of the motor (RPM) 2000 (default) | scalar
  group: Output Parameters
```

### **Computation method** — Computation method used by block `Arithmetic` (default) | `PLL`

Set the Resolver Decoder block to use one of the following
computation techniques:

- `Arithmetic` — Use an algorithm based on arithmetic
  equations and atan2 based operations to compute the block outputs. For more
  information about this technique, see the  section on this
  page.
- `PLL` — Use a PLL based algorithm to compute the block
  outputs. For more information about this technique, see PLL with Feed
  Forward.

### **Block Output** — Output of block `Mechanical position` (default) | `Sine and Cosine electrical position` | `Mechanical speed`

Set the Resolver Decoder block to output one of more of the
following:

- `Mechanical position` — Enable the block to compute
  motor mechanical position.
- `Sine and Cosine electrical position` — Enable the
  block to compute sine and cosine values of motor electrical position. If you select
  this value, the block enables the **Inputs for Sine and Cosine electrical
  position** section in the **Input Parameters**
  tab.
- `Mechanical speed` — Enable the block to compute the
  mechanical speed of the motor.

**Note**

When you use the PLL computation technique, if you enable all the three block
outputs, then the block uses PLL to compute the sine and cosine electrical positions
and mechanical speed but uses the `atan2` function to compute the
mechanical position.

### Input Parameters

### **Number of pole-pairs for resolver** — Resolver pole pair count `1` (default) | scalar

The number of pole pairs available in the resolver.

### **Type of excitation method** — Resolver excitation method `Sinusoidal Excitation` (default) | `Square Pulse Excitation`

The resolver excitation method used to obtain the secondary sine and cosine
waveforms.

### **Enable input normalization** — Enable block to normalize inputs `off` (default) | `on`

When using square-pulse excitation method, the block normalizes the secondary sine
and cosine inputs only if you select this parameter.

#### Dependencies

To enable this parameter, set **Type of excitation method** to
`Square Pulse Excitation`.

### **Discrete step size (s)** — Sample time after which block executes again `50e-6` (default) | scalar

The fixed time interval (in seconds) between every two consecutive instances of
block execution.

#### Dependencies

- If you configure the block to use arithmetic computation method, you can
  enable this parameter by selecting the **Mechanical speed**
  parameter available in the **Block Output** section.
- If you configure the block to use PLL computation method, the block always
  enables this parameter.

### Inputs for Sine and Cosine electrical position

### **Number of pole-pairs for motor** — Motor pole pair count `3` (default) | scalar

The number of pole pairs available in the motor.

#### Dependencies

To enable this parameter, set **Block Output** to
`Sine and Cosine electrical position`.

### **Position offset (mechanical radians)** — Resolver mechanical position offset (in radians) `0` (default) | scalar

The offset between the resolver mechanical position and motor mechanical position
(in radians).

#### Dependencies

To enable this parameter, set **Block Output** to
`Sine and Cosine electrical position`.

### **Integer rounding mode** — Rounding mode for fixed-point operations `Zero` (default) | `Simplest`

Select the rounding mode for fixed-point operations used when computing the sine
and cosine of the motor electrical position.

- `Simplest` — The block generates compact rounding
  code with faster computation. However, with time, this mode may add bias in the
  sine and cosine electrical position output.
- `Zero` — The block ensures that the rounding code
  does not add any bias in the sine and cosine electrical position output. However,
  this results in slower computation.

#### Dependencies

To enable this parameter, set **Block Output** to
`Sine and Cosine electrical position`.

### Inputs for sinusoidal excitation method

### **Phase delay (electrical radians)** — Phase delay for input signals `0.1746` (default) | scalar

The phase delay that the block adds to the `Sin` and
`Cos` input port signals.

#### Dependencies

To enable this parameter, set **Type of excitation method** to
`Sinusoidal Excitation`.

### **Number of samples per excitation cycle** — Samples per cycle of input signal `16` (default) | even scalar greater than zero

Number of samples available in one cycle of the `Sin` and
`Cos` input port signals.

#### Dependencies

To enable this parameter, set **Type of excitation method** to
`Sinusoidal Excitation`.

### PLL Parameters

### **Maximum application frequency (Hz)** — Maximum applicable input frequency `7500` (default) | scalar

Maximum possible frequency of the input signals (in hertz).

#### Dependencies

To enable this parameter set the **Computation method**
parameter to `PLL`

### **Speed filter cutoff frequency (Hz)** — Cutoff frequency of lowpass filter `10` (default) | scalar

Cutoff frequency of the lowpass filter that the block uses to filter the estimated
angular frequency (in hertz).

#### Dependencies

To enable this parameter set the **Computation method**
parameter to `PLL`

### **Number of data points for lookup table** — Size of lookup table array `1024` (default) | scalar

Size of the lookup table array that the block provides to the SinCos Embedded Optimized block, which is used
internally. This parameter accepts a value between 125 and 4095.

#### Dependencies

To enable this parameter:

- Set the **Computation method** parameter to
  `PLL`.
- Select the **Mechanical position** parameter available in
  the **Block Output** section.
- Clear the **Sine and Cosine electrical position**
  parameter available in the **Block Output** section.

### **Proportional (P)** — Proportional controller gain `942.4778` (default) | scalar

Proportional gain (*Kp*) of the PI
controller used by the block to compute the angular frequency.

#### Dependencies

To enable this parameter set the **Computation method**
parameter to `PLL`

### **Integral (I)** — Integral controller gain `222066.099` (default) | scalar

Integral gain (*Ki*) of the PI controller
used by the block to compute the angular frequency.

#### Dependencies

To enable this parameter set the **Computation method**
parameter to `PLL`

Click **Compute default parameters** to calculate an approximate
proportional gain (*Kp*) and integral gain
(*Ki*) and update these fields.

### **Error threshold (Hz)** — PLL error threshold `2e-2` (default) | scalar

Due to dynamics in the closed loop phase-locked loop (PLL), output of PLL takes
time to reach steady state. This parameter defines a threshold that the block uses to
determine if the PLL has reached steady state.

#### Dependencies

To enable this parameter set the **Computation method**
parameter to `PLL`

### Output Parameters

### **Position unit** — Unit of position output `Radians` (default) | `Degrees` | `Per-unit`

The unit of the mechanical position output of the block.

#### Dependencies

For both arithmetic and PLL computation methods, the block enables this
parameter only if you select the **Mechanical position** parameter
available in the **Block Output** section.

### **Position data type** — Data type of angular position output `single` (default) | `double` | `fixed point`

The data type for the angular position output.

#### Dependencies

To enable this parameter, set the **Computation method**
parameter to `PLL` and select the **Mechanical
position** parameter available in the **Block Output**
section.

### **Table data type** — Data type of sine-cosine lookup table `single` (default) | `double` | `fixed point`

Data type of the sine-cosine lookup table used by the block.

#### Dependencies

To enable this parameter, set the **Computation method**
parameter to `PLL` and select the **Mechanical
position** parameter available in the **Block Output**
section.

### **Speed unit** — Unit of speed output `Degrees/Sec` (default) | `Radians/Sec` | `RPM` | `Per-unit`

The unit of the mechanical speed output of the block.

#### Dependencies

For both arithmetic and PLL computation methods, the block enables this
parameter only if you select the **Mechanical speed** parameter
available in the **Block Output** section.

### **Speed data type** — Data type of angular speed output `single` (default) | `double` | `fixed point`

The data type for the angular speed output.

#### Dependencies

To enable this parameter, set the **Computation method**
parameter to `PLL` and select the **Mechanical
speed** parameter available in the **Block Output**
section.

### **Base speed (RPM)** — Base speed of the motor (RPM) `2000` (default) | scalar

The rated speed of the motor (in RPM).

#### Dependencies

For both arithmetic and PLL computation methods, the block enables this
parameter only if you select the **Mechanical speed** parameter
available in the **Block Output** section and then set
**Speed unit** to `Per-Unit`.
## Libraries

Motor Control Blockset / Sensor Decoders

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Compute motor mechanical position and speed and sine and cosine values of motor electrical position

The Resolver Decoder block computes the following for a resolver connected
to the motor shaft:

- Mechanical angular position of motor
- Sine and cosine values of electrical angular position of motor
- Mechanical speed of motor

A resolver uses a primary excitation input signal to generate the modulated secondary sine
and cosine waveforms, which are then sampled by the ADC. The resolver utilizes one winding to
two winding transformations. The sine and cosine modulation occurs in the secondary windings
because of the design and construction of these windings, which places them at positions that
are 90 degrees apart.

For more details about the algorithm used by the block, see .
