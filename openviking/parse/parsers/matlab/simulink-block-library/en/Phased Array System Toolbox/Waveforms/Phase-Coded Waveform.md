---
type: simulink-block
title: 'Phase Coded Waveform'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveforms'
documentation_page: 'phasecodedwaveform'
documentation_source_path: 'ref/phasecodedwaveform.html'
language: en
---

# Phase Coded Waveform

## Ports

### Input

### **PRFIdx** — PRF Index positive integer

Index to select the pulse repetition frequency (PRF), specified as a
positive integer. The index selects the PRF from the predefined vector
of values specified by the **Pulse repetition frequency
(Hz)** parameter.

**Example:**
`4`

#### Dependencies

To enable this port, select **Enable PRF selection
input**.

**Data Types:** `double`

### **FreqOffset** — Frequency offset scalar

Frequency offset in Hz, specified as a scalar.

**Example:**
`2e3`

#### Dependencies

To enable this port, set **Source of Frequency Offset** to
`Input port`.

**Data Types:** `double`
### Output

### **Y** — Pulse waveform complex-valued vector

Pulse waveform samples, returned as a complex-valued vector.

**Data Types:** `double`

### **PRF** — Pulse repetition frequency positive scalar

Pulse repetition frequency of current pulse, returned as a positive
scalar.

#### Dependencies

To enable this port, set the **Output signal
format** parameter to `Pulses`
and then select the **Enable PRF output**
parameter.

**Data Types:** `double`

### **Coeff** — Matched filter coefficients vector

Matched filter coefficients, returned as a vector.

#### Dependencies

To enable this port, select **Enable Matched Filter
Coefficients Output**.

**Data Types:** `double`
**Complex Number Support:** Yes

## Parameters

### **Sample rate (Hz)** — Sample rate of the output waveform `1e6` (default) | positive scalar

Sample rate of the output waveform, specified as a positive scalar. Set
the ratio of the **Sample rate (Hz)** parameter to the
**Pulse repetition frequency (Hz)** parameter to an
integer.

- The ratio of **Sample rate (Hz)** to each
  element in the **Pulse repetition frequency
  (Hz)** vector must be an integer. This restriction
  is equivalent to requiring that the pulse repetition interval is
  an integral multiple of the sample interval.
- The product of **Sample rate (Hz)** and
  **Chip width (s)** must be an integer. This
  restriction is equivalent to requiring that the chip width is an
  integer multiple of the sample interval.

Units are in Hz.

**Example:** `5e3`

### **Phase code** — Code type used for phase modulation `Frank` (default)

Code type used for phase modulation, specified as one of

- `Barker`
- `Frank`
- `P1`
- `P2`
- `P3`
- `P4`
- `Px`
- `Zadoff-Chu`
- `Maximum Length Sequence`
- `Quadratic Residue Sequence`
- `Custom`

**Example:** `P2`

### **Custom phase code** — Custom phase code `[1,-1]` (default) | *M*-length vector of complex values

Custom phase code, specified as a length-*M* vector of
complex values. Each element in the specified vector corresponds to a single
chip.

**Example:** `[j,2/3,-j]`

#### Dependencies

To enable this parameter, set the **Code**
parameter to `'Custom'`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Chip width (s)** — Chip time duration `1e-5` (default) | positive scalar

Duration of every chip in a phase-coded waveform, specified as a positive
scalar. The value of this parameter must satisfy these constraints:

- The product of **Chip width (s)**,
  **Number of chips**, and **Pulse
  repetition frequency (Hz)** must be less than or equal
  to one. This restriction is equivalent to requiring that the pulse
  length is less than the pulse repetition interval.
- The product of **Sample rate (Hz)** and
  **Chip width (s)** must be an integer. This
  restriction is equivalent to requiring that the chip width is an
  integer multiple of the sample interval.

Units are in seconds.

**Example:** `2e-4`

### **Number of chips** — Number of chips in waveform `4` (default) | positive integer

Number of chips in a phase-coded waveform, specified as a positive
integer. The product of the **Chip width (s)**,
**Number of chips**, and **Pulse repetition
frequency (Hz)** parameters must be less than or equal to one.
This restriction is equivalent to requiring that the chip width is an
integer multiple of the sample interval.

The table shows additional constraints on the number of chips for
different code types.

| If the **Phase code** parameter is... | Then the **Number of chips** parameter must be... |
| --- | --- |
| `Frank`, `P1`, or `Px` | A perfect square |
| `P2` | An even number that is a perfect square |
| `Barker` | `2, 3, 4, 5, 7, 11, or 13` |
| `'Maximum Length Sequence'` | `7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, and 8191` |
| `'Quadratic Residue Sequence'` | A prime number of the form `4`*n*`-1`, where *n* is an integer |

**Example:** `9`

#### Dependencies

To enable this parameter, set the **Code**
parameter to anything other than `'Custom'`.

### **Zadoff-Chu sequence index** — Sequence index for Zadoff-Chu code type `1` (default) | positive integer

Sequence index for Zadoff-Chu code type, specified as a positive integer.
The values of the **Zadoff-Chu sequence index** and the
**Number of chips** parameters must be relatively
prime.

**Example:** `2`

#### Dependencies

To enable this parameter, set **Phase Code** to
`Zadoff-Chu`.

### **Pulse repetition frequency (Hz)** — Pulse repetition frequency `1e4` (default) | positive scalar

Pulse repetition frequency, *PRF*, specified as a scalar or a row vector.
Units are in Hz. The pulse repetition interval, *PRI*, is the inverse of the
pulse repetition frequency, *PRF*. The value of **Pulse repetition
frequency (Hz)** must satisfy these constraints:

- The product of **Pulse width** and **Pulse repetition
  frequency (Hz)** must be less than or equal to one. This condition expresses
  the requirement that the pulse width is less than one pulse repetition interval. For the
  phase-coded waveform, the pulse width is the product of the chip width and number of
  chips.
- The ratio of sample rate to any element of **Pulse repetition
  frequency** must be an integer. This condition expresses the requirement that
  the number of samples in one pulse repetition interval is an integer.

You can select the value of *PRF* by using block parameter settings alone or
in conjunction with the input port, `PRFIdx`.

- When the **Enable PRF selection input** parameter is not selected,
  set the *PRF* using block parameters.

  - To implement a constant *PRF*, specify **Pulse
    repetition frequency (Hz)** as a positive scalar.
  - To implement a staggered *PRF*, specify **Pulse
    repetition frequency (Hz)** as a row vector with positive values. After
    the waveform reaches the last element of the vector, the process continues
    cyclically with the first element of the vector. When *PRF* is
    staggered, the time between successive output pulses cycles through the successive
    values of the *PRF* vector.
- When the **Enable PRF selection input** parameter is selected, you
  can implement a selectable *PRF* by specifying **Pulse
  repetition frequency (Hz)** as a row vector with positive real-valued
  entries. But this time, when you execute the block, select a *PRF* by
  passing an index into the *PRF* vector into the
  `PRFIdx` port.

In all cases, the number of output samples is fixed when you set the
**Output signal format** to `Samples`. When you
use a varying *PRF* and set **Output signal format** to
`Pulses`, the number of output samples can vary.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`PRF` |
| **Type:**double |
| **Values:**positive scalar |
| **Default:**`1e6` |

### **Enable PRF selection input** — Select predefined PRF off (default) | on

Select this parameter to enable the `PRFIdx` port.

- When enabled, pass in an index into a vector of predefined PRFs. Set
  predefined PRFs using the **Pulse repetition frequency
  (Hz)** parameter.
- When not enabled, the block cycles through the vector of PRFs specified by
  the **Pulse repetition frequency (Hz)** parameter. If
  **Pulse repetition frequency (Hz)** is a scalar, the
  PRF is constant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`PRFSelectionInputPort` |
| **Type:**logical |
| **Values:**positive scalar |
| **Default:**`off` |

### **Source of Frequency Offset** — Source of frequency offset `Property` (default) | `Input port`

Source of frequency offset, specified as `Property` or
`Input port`.

- When set to
  `Property`, the offset is
  determined by the value of the **Frequency
  Offset** parameter.
- When set to `Input
  port`, the offset is determined by
  the value of the **FreqOffset**
  port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`FrequencyOffsetSource` |
| **Type:**enum |
| **Values:**`Property`, `Input Port` |
| **Default:**`Property` |

### **Frequency Offset (Hz)** — Frequency offset `0` (default) | scalar

Frequency offset, specified as a scalar. Units are in Hz.

**Example:** `2e3`

#### Dependencies

To enable this parameter set the **Source of Frequency Offset**
parameter to `Input port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`FrequencyOffset` |
| **Type:**double |
| **Values:**`scalar` |
| **Default:**`0` |

### **Source of simulation sample time** — Source of simulation sample time `Derive from waveform parameters` (default) | `Inherit from Simulink engine`

Source of simulation sample time, specified as `Derive from waveform
parameters` or `Inherit from Simulink engine`.
When set to `Derive from waveform parameters`, the block runs
at a variable rate determined by the PRF of the selected waveform. The elapsed time is
variable. When set to `Inherit from Simulink engine`, the
block runs at a fixed rate so the elapsed time is a constant.

#### Dependencies

To enable this parameter, select the **Enable PRF selection
input** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`SimulationTimeSource` |
| **Type:**enum |
| **Values:**`Derive from waveform parameters`, `Inherit from Simulink engine` |
| **Default:**`Derive from waveform parameters` |

### **Output signal format** — Format of the output signal `Pulses` (default) | `Samples`

The format of the output signal, specified as `Pulses` or `Samples`.

If you set this parameter to `Samples`, the output of the block consists of multiple samples. The number of samples is the value of the **Number of samples in output** parameter.

If you set this parameter to `Pulses`, the output of the block consists of multiple pulses. The number of pulses is the value of the **Number of pulses in output** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`OutputFormat` |
| **Type:**enum |
| **Values:**`Pulses` `Samples` |
| **Default:**`Pulses` |

### **Number of samples in output** — Number of samples in output `100` (default) | positive integer

Number of samples in the block output, specified as a positive integer.

**Example:** `1000`

#### Dependencies

To enable this parameter, set the **Output signal format**
parameter to `Samples`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`NumSamples` |
| **Type:**double |
| **Values:**`positive scalar` |
| **Default:**`100` |

**Data Types:** `double`

### **Number of pulses in output** — Number of pulses in output `1` (default) | positive integer

Number of pulses in the block output, specified as a positive integer.

**Example:** `2`

#### Dependencies

To enable this parameter, set the **Output signal
format** parameter to
`Pulses`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`NumPulses` |
| **Type:**double |
| **Values:**`positive scalar` |
| **Default:**`1` |

**Data Types:** `double`

### **Enable PRF Output** — Enable output of PRF `off` (default) | `on`

Select this parameter to enable the `PRF` output port.

#### Dependencies

To enable this parameter, set **Output signal format** to
`Pulses`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`PRFOutputPort` |
| **Type:**enum |
| **Values:**`off` `on` |
| **Default:**`off` |

### **Enable Matched Filter Coefficients Output** — Enable output of matched filter coefficients `off` (default) | `on`

Select this parameter to enable the `Coeff` output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`CoefficientOutputPort` |
| **Type:**enum |
| **Values:**`off` `on` |
| **Default:**`off` |

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or
`Code Generation`. If you want your block to use the
MATLAB® interpreter, choose `Interpreted Execution`. If
you want your block to run as compiled code, choose `Code
Generation`. Compiled code requires time to compile but usually runs
faster.

Interpreted execution is useful when you are developing and tuning a model. The block
runs the underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations run faster with generated code than in
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the
overall simulation behavior.

When the Simulink® model is in `Accelerator` mode, the block mode specified
using **Simulate using** overrides the simulation mode.

**Acceleration Modes**

|  |  |  |  |
| --- | --- | --- | --- |
| Block Simulation | Simulation Behavior | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | The block executes using the MATLAB interpreter. | The block executes using the MATLAB interpreter. | Creates a standalone executable from the model. |
| `Code Generation` | The block is compiled. | All blocks in the model are compiled. |

For more information, see Choosing a Simulation Mode (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimulateUsing` |
| **Type:** enum |
| **Values:** `Interpreted Execution`, `Code Generation` |
| **Default:** `Interpreted Execution` |

## Libraries

Phased Array System Toolbox / Waveforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Phase-coded pulse waveform

The Phase-Coded Waveform block generates samples of a phase-coded pulse
waveform with specified chip width, pulse repetition frequency (PRF), and phase code.
The block outputs an integer number of pulses or samples.
