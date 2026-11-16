---
type: simulink-block
title: 'Stimulus'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'stimulus'
documentation_source_path: 'ref/stimulus.html'
language: en
---

# Stimulus

## Ports

### Output

### **WaveOut** — Output signal with specific PRBS pattern vector

Output pattern with a specific PRBS pattern, specified as a vector.

**Data Types:** `double`

## Parameters

### Stimulus

### **Number of symbols** — Length of stimulus pattern used for simulation `20000` (default) | positive real integer

Length of the stimulus pattern used for simulation, specified as a positive
integer.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `NumberOfSymbols` |
| **Type:** character vector |
| **Values:** positive real integer |
| **Default:** `20000` |

### **Use recommended simulation stop time** — Set recommended simulation stop time as simulation stop time on (default) | off

Select to directly set the **Recommended simulation stop time**
as the simulation stop time. By default, this option is selected.

**Recommended simulation stop time** defines the minimum time the
simulation must run for meaningful results. It is calculated by multiplying the
**Sample Interval** from the Configuration block with the **Number of symbols**.

### **Waveform creation method** — Define how stimulus waveform is created `Random Symbols` (default) | `Serial PRBS` | `Symbol Pattern` | `Binary Pattern` | `Symbol Voltage Pattern` | `Sampled Voltage` | `Parallel PRBS`

Define how the stimulus waveform is created:

- `Random Symbols` — Randomly generate symbols directly
  from a uniform distribution.
- `Serial PRBS` — Define a binary sequence and map to a
  higher order modulation symbol. The mapping sequence depends on the modulation
  scheme defined in the Configuration block.
- `Symbol Pattern` — Directly define the symbol pattern
  as an integer from 0 to (Number of modulation levels – 1).
- `Binary Pattern` — Directly define the binary pattern
  and map to a higher order modulation symbol. The mapping sequence depends on the
  modulation scheme defined in the Configuration block.
- `Symbol Voltage Pattern` — Directly define the
  voltages of a symbol spaced pattern.
- `Sampled Voltage` — Directly define a sample interval
  spaced waveform.
- `Parallel PRBS` — Utilize multiple PRBS streams to
  form PAM4, PAM8 , PAM16, and PAM32 symbols. You can define up to 5 PRBS streams
  for PAM32. NRZ modulation scheme uses a single PRBS stream. Other modulation
  schemes use the random symbols waveform creation method.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CreationMethod` |
| **Type:** character vector |
| **Values:** `Random Symbols` | `Serial PRBS` | `Symbol Pattern` | `Binary Pattern` | `Symbol Voltage Pattern` | `Sampled Voltage` | `Parallel PRBS` |
| **Default:** `Random Symbols` |

### **Random symbols seed** — Seed for generating random symbol waveform `1431655765` (default) | positive real scalar

Seed for generating the random symbol waveform, specified as a positive real
scalar.

#### Dependencies

- To enable this parameter, set **Waveform creation
  method** parameter to `Random
  Symbols`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `soPAMnSeed` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1431655765` |

### **PRBS order** — Order of pseudorandom binary sequence `11` (default) | `7` | `9` | `13` | `15` | `20` | `23` | `31` | `47`

Order of the pseudorandom binary sequence while creating the stimulus waveform
using serial PRBS or parallel PRBS method.

#### Dependencies

To enable this parameter, set **Waveform creation
method** parameter to `Serial PRBS` or
`Parallel PRBS`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PRBS` |
| **Type:** character vector |
| **Values:** `7` | `9` | `11` | `13` | `15` | `20` | `23` | `31` | `47` |
| **Default:** `11` |

### **PRBS seed** — Seed of pseudorandom binary sequence `1` (default) | integer in the range [1, 2Order-1]

Seed for generating the pseudorandom binary sequence, specified as an integer in
the range of [1, 2Order-1].

#### Dependencies

To enable this parameter, set **Waveform creation
method** parameter to `Serial PRBS` or
`Parallel PRBS`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PRBSSeed` |
| **Type:** character vector |
| **Values:** integer in the range [1, 2Order-1] |
| **Default:** `1` |

### **Reverse PRBS in time** — Reverse PRBS in time by reversing tap positions of characteristic polynomial off (default) | on

Reverse the PRBS in time (along *x*-axis) by reversing the tap
positions of the characteristic polynomial.

#### Dependencies

To enable this parameter, set **Waveform creation
method** parameter to `Serial PRBS` or
`Parallel PRBS`.

### **Invert PRBS in voltage** — Invert PRBS in voltage by flipping the values of 0 and 1 off (default) | on

Invert the PRBS in voltage (along *y*-axis) by converting 0s to
1s and 1s to 0s.

#### Dependencies

To enable this parameter, set **Waveform creation
method** parameter to `Serial PRBS` or
`Parallel PRBS`.

### **Symbol pattern** — Vector of symbol integers spaced at symbol time interval `[0 0 1 0 0 1 1 0 1 0 1 1 1 1 0]` (default) | vector with element values in the range [0, (Number of modulation levels-1)]

Vector of the symbol integers spaced at the symbol time interval. The elements of
the vector must have values in the range [0, (Number of modulation levels-1)]

#### Dependencies

To enable this parameter, set **Waveform creation
method** parameter to `Symbol
Pattern`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SymbolPattern` |
| **Type:** character vector |
| **Values:** vector with element values in the range [0, (Number of modulation levels-1)] |
| **Default:** `[0 0 1 0 0 1 1 0 1 0 1 1 1 1 0]` |

### **Binary pattern** — Vector of 1s and 0s spaced at sample time interval `[0 0 0 1 0 0 1 0 1 1 0 0 1 1 1 1 1 0 0 0 1 1 0 1 1 1 0 1 0 1 0]` (default) | vector with binary elements

Vector of binary elements (1s and 0s) spaced at the symbol time interval.

#### Dependencies

To enable this parameter, set **Waveform creation
method** parameter to `Binary
Pattern`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `BinaryPattern` |
| **Type:** character vector |
| **Values:** vector with binary elements |
| **Default:** `[0 0 0 1 0 0 1 0 1 1 0 0 1 1 1 1 1 0 0 0 1 1 0 1 1 1 0 1 0 1 0]` |

### **Symbol voltage pattern** — Vector of symbol voltages spaced at symbol time interval `1/2*[1 1 1 1 -1 -1 -1 -1]` (default) | vector with decimal values

Vector of symbol voltages spaced at the symbol time interval.

#### Dependencies

To enable this parameter, set **Waveform creation
method** parameter to `Symbol Voltage
Pattern`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SymbolVoltageDataPattern` |
| **Type:** character vector |
| **Values:** vector with decimal values |
| **Default:** `1/2*[1 1 1 1 -1 -1 -1 -1]` |

### **Sampled voltage pattern** — Vector of voltages spaced at sample interval `[zeros(1,(SymbolTime/SampleInterval)),ones(1,(SymbolTime/SampleInterval))]-0.5` (default) | real valued vector

Vector of voltages spaced at the sample interval.

#### Dependencies

To enable this parameter, set **Waveform creation
method** parameter to `Sampled
Voltage`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CustomStimulus` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[zeros(1,(SymbolTime/SampleInterval)),ones(1,(SymbolTime/SampleInterval))]-0.5` |

### **Sub symbol time delay (s)** — Delay stimulus waveform by modulo symbol time `0` (default) | nonnegative real scalar

Delay the stimulus waveform by modulo symbol time to slightly shift the eye
diagram or recovered clock phase.

The modulo operation finds the remainder after division.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `soDelay` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `0` |

### Clock Forwarding

### **Change in IBIS-AMI Manager** — Modify Rx\_Use\_Clock\_Input reserved AMI parameter button

Modify the **Rx\_Use\_Clock\_Input** reserved AMI parameter using
the SerDes IBIS-AMI Manager dialog box. You can change the parameter in the
**AMI-Rx** tab of the SerDes IBIS-AMI Manager.

You can use either a waveform or clock times data to forward as a clock. The
**Current State** parameter shows what type of data you are
forwarding.

### **Generate Clock or Strobe Waveform** — Generate clock or strobe waveform from waveform parameters off (default) | on

Generate a clock or strobe waveform from the specified waveform parameters.

You can define a clock pattern with delay. Alternately, you can define a strobe
pattern with delay, burst length, idle length, pre-amble, and post-amble.

You can also define the transmitter jitter parameters to include when generating
the clock or strobe pattern.

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Wave`.

### **Use External Waveform or Clock Times Array** — Use external waveform to forward on (default) | off

Use an external clock to forward. You can define the external clock in the base or
model workspace and use the **Waveform Name** parameter to point to
it.

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Wave`.

### **Include Analog Channel Model in clock waveform** — Include analog channel model in clock waveform on (default) | off

Select to include the analog channel model in the clock waveform.

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Wave`.

### **Clock Pattern** — Forwarding clock pattern off (default) | on

Select to generate a forwarding clock pattern. You can also define the clock delay
and include transmitter jitter.

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Wave` and select the **Generate Clock or Strobe
Waveform** option.

### **Strobe Pattern** — Forwarding strobe pattern on (default) | off

Select to generate a forwarding strobe pattern. You can also define the strobe
delay, burst length, idle length, pre-amble, post-amble, and include transmitter
jitter.

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Wave` and select the **Generate Clock or Strobe
Waveform** option.

### **Delay (s)** — Delay forwarding clock `0` (default) | nonnegative real scalar

Delay the forwarding clock, specified as a nonnegative real scalar.

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Wave` and select the **Generate Clock or Strobe
Waveform** option.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CF_Delay` |
| **Type:** character vector |
| **Values:** nonnegative real scalar |
| **Default:** `0` |

### **Burst Length** — Number of symbols between strobe burst pattern `16` (default) | nonnegative scalar integer

Number of symbols between the strobe burst pattern or clock pattern, specified as
a nonnegative scalar integer.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CF_BurstLen` |
| **Type:** character vector |
| **Values:** nonnegative scalar integer |
| **Default:** `0` |

### **Idle Length** — Number of symbol between bursts `8` (default) | nonnegative scalar integer

Number of symbol between bursts, specified as a nonnegative scalar integer.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CF_IdleLen` |
| **Type:** character vector |
| **Values:** nonnegative scalar integer |
| **Default:** `0` |

### **Preamble** — Number of additional clock cycles added to beginning of each burst `2` (default) | nonnegative scalar integer

Number of additional clock cycles added to the beginning of each burst, specified
as a nonnegative scalar integer. A clock cycle consists of two symbols.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CF_Preamble` |
| **Type:** character vector |
| **Values:** nonnegative scalar integer |
| **Default:** `2` |

### **Postamble** — Number of additional clock cycles added to end of each burst `0` (default) | nonnegative scalar integer

Number of additional clock cycles added to the end of each burst, specified as a
nonnegative scalar integer. A clock cycle consists of two symbols.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CF_Postamble` |
| **Type:** character vector |
| **Values:** nonnegative scalar integer |
| **Default:** `0` |

### **Include Transmitter Jitter** — Include transmitter jitter in forwarded clock on (default) | off

Select to include transmitter jitter in the forwarded clock.

### **Tx\_Dj (UI)** — Transmitter deterministic jitter `0` (default) | scalar in the range [0 1]

Transmitter deterministic jitter, specified as a scalar in the range [0 1]. It is
defined as half of the peak-to-peak worst case variation.

Deterministic jitter is usually modeled as bounded uniform jitter. It is also
known as *uncorrelated bounded high probability
jitter*.

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Wave` and select the **Generate Clock or Strobe
Waveform** option.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CF_TxDj` |
| **Type:** character vector |
| **Values:** scalar in the range [0 1] |
| **Default:** `0` |

### **Tx\_Rj (UI)** — Transmitter random jitter `0` (default) | scalar in the range [0 1]

Transmitter random jitter, specified as a scalar in the range [0 1]. It is defined
as the standard deviation of a white Gaussian phase noise process.

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Wave` and select the **Generate Clock or Strobe
Waveform** option.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CF_TxRj` |
| **Type:** character vector |
| **Values:** scalar in the range [0 1] |
| **Default:** `0` |

### **Tx\_DCD (UI)** — Transmitter duty cycle distortion `0` (default) | scalar in the range [0 1]

Transmitter duty cycle distortion, specified as a scalar in the range [0 1].It is
defined as half of the peak-to-peak difference in symbol duration between one symbol
and the next.

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Wave` and select the **Generate Clock or Strobe
Waveform** option.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CF_TxDCD` |
| **Type:** character vector |
| **Values:** scalar in the range [0 1] |
| **Default:** `0` |

### **Tx\_Sj (UI)** — Transmitter sinusoidal jitter `0` (default) | scalar in the range [0 1]

Transmitter sinusoidal jitter, specified as a scalar in the range [0 1]. It is
defined as half of the peak-to-peak variation of sinusoidal phase noise
amplitude.

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Wave` and select the **Generate Clock or Strobe
Waveform** option.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CF_Sj` |
| **Type:** character vector |
| **Values:** scalar in the range [0 1] |
| **Default:** `0` |

### **Tx\_Sj\_Frequency (Hz)** — Transmitter sinusoidal jitter frequency `0` (default) | scalar in the range [0 100e9]

Frequency of the transmitter sinusoidal jitter, specified as a scalar in the range
[0 100e9].

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Wave` and select the **Generate Clock or Strobe
Waveform** option.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CF_TxSjFreq` |
| **Type:** character vector |
| **Values:** scalar in the range [0 100e9] |
| **Default:** `0` |

### **Waveform Name** — Name of waveform parameter in workspace `defaultClockWave` (default) | character string

Name of the waveform parameter in the base or model workspace that contains the
external waveform data.

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Wave` and select the **Use External Waveform or
Clock Times Array** option.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CF_WaveformName` |
| **Type:** character vector |
| **Values:** character string |
| **Default:** `0` |

### **Waveform Delay (s)** — Delay forwarding clock `0` (default) | nonnegative scalar integer

Delay the forwarding clock, specified as a nonnegative scalar integer.

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Wave` and select the **Use External Waveform or
Clock Times Array** option.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CF_WaveDelay` |
| **Type:** character vector |
| **Values:** nonnegative scalar integer |
| **Default:** `0` |

### **Clock Times Name** — Name of clock times parameter in workspace `defaultClockTimes` (default) | character string

Name of the clock times parameter in the base or model workspace that contains the
external clock times data.

#### Dependencies

To enable this parameter, select **Current value** of
**Rx\_Use\_Clock\_Input** parameter to
`Time`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CF_ClockTimesName` |
| **Type:** character vector |
| **Values:** character string |
| **Default:** `0` |

## Libraries

SerDes Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

### R2023b: Clock Forwarding

Use the **Clock Forwarding** tab in the Stimulus block
to generate clock stimulus patterns.

## Description

Set waveform generation method and number of symbols to simulate in SerDes model

The Stimulus defines how to create the waveform and the number of symbols
to simulate in a SerDes Toolbox™ model. You can directly specify a PAMn symbol pattern or define a binary to PAMn
mapping scheme.

When you enable clock forwarding in the SerDes IBIS-AMI Manager dialog box, you can use
the Stimulus block to generate clock times from an external clock times array
or waveform.
