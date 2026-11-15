---
type: simulink-block
title: 'Clock Generator'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Mix Analog and Digital Signals'
documentation_page: 'clockgenerator'
documentation_source_path: 'ref/clockgenerator.html'
language: en
---

# Clock Generator

## Ports

### Input

### **vctrl** — Voltage to control output frequency scalar | vector

Voltage to control the output frequency, specified as a scalar or vector.

**Data Types:** `double`

### **ReferenceOffset** — Reference frequency offset scalar

Offset for the reference frequency, specified as a scalar. If you select the
**ReferenceOffsetPort** parameter, the
**ReferenceOffset** port uses a reference offset value from
an external block.

**Data Types:** `double`

### **PhaseOffset** — Duty cycle phase offset scalar

Offset for the duty cycle phase offset, specified as a scalar. If you select the
**PhaseOffsetPort** parameter, the
**PhaseOffset** port uses a phase offset value from an
external block.

**Data Types:** `double`
### Output

### **clock0** — Saturated output clock signal scalar

Saturated output clock signal, returned as a scalar. There is one clock output
port for each output phase.

**clock0** is the default name of the port. The nonnegative
scalar that follows the port name clock indicates the clock phase. For example,
**clock1** represents the saturated output clock signal for
phase 1.

The output is a square wave whose amplitude is defined by the **Output
amplitude** parameter.

**Data Types:** `double`

### **clockTime0** — Simulation time at last clock transition scalar

Simulation time at the last clock transition, returned as a scalar. There is one
clockTime output port for each output phase.

**clockTime0** is the default name of the port. The
nonnegative scalar that follows the port name clockTime indicates the clock phase. For
example, **clockTime1** represents the clock transition time
for phase 1.

**Data Types:** `double`

### **Phase** — Most recent clock phase of fundamental clock scalar

Most recent clock phase of the fundamental clock, returned as a scalar.

**Data Types:** `double`

### **clockValid** — Variable-step discrete-sampled clock scalar

Variable-step discrete-sampled clock, specified as a scalar. The edge sample times
of the signal at the **clockValid** port exactly match the
values in the clock time signal.

**Data Types:** `double`

### **clockTime** — Absolute clock time of most recent clock change scalar

Absolute clock time of the most recent clock change at the
**clockValid** port.

**Data Types:** `double`

## Parameters

#### Main

### **Specify using** — Define control sensitivity of clock generator `Voltage sensitivity` (default) | `Output frequency vs. control voltage` | `Period offset`

Define control sensitivity of theclock generator.

- Select `Voltage sensitivity` to specify output
  frequency from the **Voltage sensitivity (Hz/V)** and
  **Free running frequency (Hz)** parameters.
- Select `Output frequency vs. control voltage` to
  interpolate output frequency from the **Control voltage (V)**
  vector versus the **Output frequency (Hz)** vector.
- Select `Period offset` to adjust the cycle time by
  the fraction of a nominal clock period. Use the **Control voltage
  (V)** parameter to specify the fraction. The block determines the
  values of the **Voltage sensitivity (Hz/V)** and **Free
  running frequency (Hz)** parameters using the value set in the
  **Symbol time (s)** parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SpecifyUsing` |
| **Type:** character vector |
| **Values:** `Voltage sensitivity` | `Output frequency vs. control voltage` | `Period offset` |
| **Default:** `Voltage sensitivity` |

### **Voltage sensitivity (Hz/V)** — Measure of change in output frequency `100e6` (default) | positive real scalar

Measure of change in output frequency for input voltage change, specified as a
positive real scalar with units in Hz/V.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Kvco` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `100e6` |

**Data Types:** `double`

### **Free running frequency (Hz)** — Output frequency without control voltage `10e9` (default) | positive real scalar

Frequency of the clock generator without any control voltage input
(`0` V) or the quiescent frequency, specified as a positive real
scalar in hertz.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Fo` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `10e9` |

**Data Types:** `double`

### **Control voltage (V)** — Control voltage values `[-5 0 5]` (default) | real valued vector

Control voltage values of the clock generator, specified as a real valued vector in
volts.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ControlVoltage` |
| **Type:** character vector |
| **Values:** real valued vector |
| **Default:** `[-5 0 5]` |

**Data Types:** `double`

### **Output frequency (Hz)** — Clock generator output frequency values `[9.9e9 10e9 10.5e9]` (default) | positive real valued vector

Output frequency of the clock generator corresponding to the **Control
voltage (V)** vector, specified in hertz.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutputFrequency` |
| **Type:** character vector |
| **Values:** positive real valued vector |
| **Default:** `[9.9e9 10e9 10.5e9]` |

**Data Types:** `double`

### **Output amplitude (V)** — Maximum amplitude of clock generator output voltage `1` (default) | positive real scalar

Maximum amplitude of the clock generator output voltage, specified as a positive
real scalar.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Amplitude` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1` |

**Data Types:** `double`

### **Phase unit** — Units of output phase and duty cycle `Degrees` (default) | `Fraction of a clock cycle`

The units of the output phase and duty cycle, specified as
`Degrees` or `Fraction of a clock
cycle`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PhaseUnits` |
| **Type:** character vector |
| **Values:** `Degrees` | `Fraction of a clock cycle` |
| **Default:** `Degrees` |

### **Output phase** — Phases of output clock signals `[0]` (default) | nonnegative real scalar | nonnegative real valued vector

The phases of the output clock signals, specified as a scalar vector. If specified
as a vector, each element defines one output.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutputPhase` |
| **Type:** character vector |
| **Values:** nonnegative real scalar | nonnegative real valued vector |
| **Default:** `[0]` |

### **Output duty cycle** — Duty cycle of the output clock signals `[180]` (default) | positive real scalar | positive real valued vector

The duty cycles of the output clock signals, specified as a scalar or a vector. The
clock output phase refers to the rising edge of the output clock.

If specified as a vector, each element defines one output. Missing or empty elements
of the vector are given the default duty cycle. Extra elements are ignored.

The duty cycle must be greater than Sample intervalSymbol time but less than 1−Sample intervalSymbol time, defined as a fraction of clock cycle.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutputDutyCycle` |
| **Type:** character vector |
| **Values:** positive real scalar | positive real valued vector |
| **Default:** `[180]` |

### **PhaseOffsetPort** — Define duty cycle phase offset through an input port on (default) | off

Define the duty cycle phase offset through **PhaseOffset**
input port from an external block. If you deselect the
**PhaseOffsetPort** parameter, it is removed from the AMI files. This
effectively hard-codes phase offset to the value defined by the **Phase offset
(symbol time)** parameter.

### **Phase offset (symbol time)** — Duty cycle phase offset `0` (default) | scalar in the range [-0.5,0.5]

Duty cycle phase offset, specified as a scalar in the range [-0.5, 0.5] in fraction
of symbol time. Phase offset manually shifts clock probability distribution function
(PDF) for better bit error rate (BER)..

#### Dependencies

To enable this parameter, deselect
**PhaseOffsetPort**.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PhaseOffset` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `0` |

### **ReferenceOffsetPort** — Define reference frequency offset through an input port on (default) | off

Define the reference frequency offset through
**ReferenceOffset** input port from an external block. If you
deselect the **ReferenceOffsetPort** parameter, it is removed from the
AMI files. This effectively hard-codes **Reference offset**
to the value defined by the **Reference clock frequency offset (ppm)**
parameter.

### **Reference clock frequency offset (ppm)** — Factor by which nominal output frequency is to be offset `0` (default) | scalar in the range of [-300,300]

The factor by which the nominal output frequency is to be offset from 1Symbol time, specified as a scalar in the range of [-300,300] in unit of parts per
million. It is the deviation between the transmitter oscillator frequency and the
receiver oscillator frequency

#### Dependencies

To enable this parameter, deselect
**ReferenceOffsetPort**.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ReferenceOffset` |
| **Type:** character vector |
| **Values:** scalar in the range of [-300,300] |
| **Default:** `0` |

### **Simulate using** — Select simulation mode `Code generation` (default) | `Interpreted execution`

Select the simulation mode. This choice affects the simulation performance.

Simulating the model using the `Code generation` method
requires additional startup time, but the subsequent simulations run faster. Simulating
the model using the `Interpreted execution` method may reduce
the startup time, but the subsequent simulations run slower. For more information, see
Interpreted Execution vs. Code Generation.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SimulateUsing` |
| **Type:** character vector |
| **Values:** `Code generation`| `Interpreted execution` |
| **Default:** `Code generation` |

#### Phase Noise

### **Add phase noise** — Add phase noise as a function of frequency on (default) | off

Select to introduce phase noise as a function of frequency. By default, this option
is selected.

### **Phase noise frequency offset (Hz)** — Frequency offsets of specified phase noise from carrier frequency `[30e3 100e3 1e6 3e6 10e6]` (default) | positive real valued vector

The frequency offsets of the specified phase noise from the carrier frequency,
specified as a positive real valued vector in hertz.

#### Dependencies

To enable this parameter, select **Add phase noise** in the
**Impairments** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Foffset` |
| **Type:** character vector |
| **Values:** positive real valued vector |
| **Default:** `[30e3 100e3 1e6 3e6 10e6]` |

**Data Types:** `double`

### **Phase noise level (dBc/Hz)** — Specified phase noise power at phase noise frequency offsets relative to the carrier `[-56 -106 -132 -143 -152]` (default) | negative real valued vector

The specified phase noise power in a 1 Hz bandwidth centered at the phase noise
frequency offsets relative to the carrier, specified as a negative real valued vector in
dBc/Hz. The elements of **Phase noise level** correspond to relative
elements in the **Phase noise frequency offset (Hz)** parameter.

#### Dependencies

To enable this parameter, select **Add phase noise** in the
**Impairments** tab.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PhaseNoise` |
| **Type:** character vector |
| **Values:** negative real valued vector |
| **Default:** `[-56 -106 -132 -143 -152]` |

**Data Types:** `double`

### **Estimate phase noise parameters** — Estimate phase noise parameters from measured phase noise data button

Click to estimate the phase noise parameters from the phase noise measured phase
noise data. This calculates the **Period jitter (S)** and
**Flicker corner frequency (Hz)** parameters from the
**Phase noise frequency offset (Hz)** and **Phase noise level
(dBc/Hz)** parameters. As a result, the phase noise profile matches a
physical model.

### **Period jitter (S)** — Standard deviation of period jitter `1.7e-15` (default) | positive real scalar

Standard deviation of the period jitter, specified as a positive real scalar in
seconds. Period jitter is the deviation in cycle time of a clock signal with respect to
the ideal period.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PeriodJitter` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1.7e-15` |

### **Flicker corner frequency (Hz)** — Corner frequency of flicker noise `0` (default) | scalar

Corner frequency of the flicker noise, specified as a scalar in hertz.
**Flicker corner frequency (Hz)** is defined as the frequency at
which the phase noise transitions from 1/*f*2 to 1/*f*3 due to flicker noise. At this frequency, the spectral densities of
period jitter and flicker noise are equal.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CornerFrequency` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `0` |

### **Customize flicker exponent (Advanced feature)** — Customize flicker noise power spectral distribution off (default) | on

Select this parameter to customize the power spectral distribution of the flicker
noise. Traditionally, flicker noise is defined as the 1/*f* noise, but it can vary as 1/*fV*, where 0.8<*V*<1.5.

### **Flicker exponent** — Flicker noise power exponent `1.0` (default) | `0.8` | `0.9` | `1.1` | `1.2` | `1.3` | `1.4` | `1.5`

Flicker noise power exponent, specified between `0.8` to
`1.5`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `FlickerExponent` |
| **Type:** character vector |
| **Values:** `1.0` | `0.8` | `0.9` | `1.1` | `1.2` | `1.3` | `1.4` | `1.5` |
| **Default:** `1.0` |

### **Plot fit** — Plot fitted phase noise profile button

Click to plot the fitted phase noise profile. This allows you how the fitted model
matches the specified phase noise data.

#### Advanced

### **Symbol time (s)** — Time of single symbol duration `100e-12` (default) | real positive scalar

Time of a single symbol duration, specified as a real positive scalar in
seconds.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SymbolTime` |
| **Type:** character vector |
| **Values:** real positive scalar |
| **Default:** `100e-12` |

**Data Types:** `double`

### **Sample interval (s)** — Uniform time step of waveform `6.25e-12` (default) | real positive scalar

Uniform time step of the waveform, specified as a real positive scalar in
seconds.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SampleInterval` |
| **Type:** character vector |
| **Values:** real positive scalar |
| **Default:** `6.25e-12` |

**Data Types:** `double`

### **Modulation (2:NRZ, 3:PAM3, 4:PAM4)** — Modulation scheme `2` (default) | `3` | `4`

Number of logic levels in the modulation scheme:

- Select `2` if the modulation scheme is NRZ(non-return
  to zero).
- Select `3` if the modulation scheme PAM3 (pulse
  amplitude modulation level 3).
- Select `4` if the modulation scheme PAM4 (pulse
  amplitude modulation level 4).

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Modulation` |
| **Type:** character vector |
| **Values:** `2`.| `3` | `4` |
| **Default:** `2` |

**Data Types:** `char`

### **Input waveform type** — Type of input waveform `Sample` (default) | `Impulse`

Type of input waveform, either a sample by sample signal or an impulse response
signal.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `WaveType` |
| **Type:** character vector |
| **Values:** `Sample`.| `Impulse` |
| **Default:** `Sample` |

## Libraries

Mixed-Signal Blockset / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Generate clock signal with one or more phases

The Clock Generator block generates a clock signal with multiple output
phases and detailed phase noise modeling. The signals at two output ports together model the
output clock signal for each phase. These signals are: a saturated clock signal at the clock
port and a clock transition time at the clockTime port.

You can use the block to model any clock recovery loop that uses a voltage controlled
oscillator (VCO). The block consistently provides clock times where the noise floor is below
–150 dBC/Hz. You can also use the block to include phase noise that matches a physical
model.
