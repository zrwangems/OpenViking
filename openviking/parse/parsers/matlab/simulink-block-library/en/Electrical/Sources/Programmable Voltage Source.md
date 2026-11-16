---
type: simulink-block
title: 'Programmable Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'programmablevoltagesource'
documentation_source_path: 'ref/programmablevoltagesource.html'
language: en
---

# Programmable Voltage Source

## Ports

### Input

### **DC** — DC component physical signal

Physical signal input associated with the DC component of the
voltage.

### **F** — Frequency physical signal

Physical signal input associated with the frequency.

### **M** — Magnitude physical signal

Physical signal input associated with the magnitude.

### **Phi** — Phase shift physical signal

Physical signal input associated with the phase shift.
### Conserving

### **+** — Positive voltage electrical

Electrical conserving port associated with the positive
voltage.

### **-** — Negative voltage electrical

Electrical conserving port associated with the negative
voltage.

## Parameters

### AC Magnitude

### **AC magnitude configuration** — AC voltage magnitude configuration `Constant` (default) | `Ramp``Step``Modulation``External`

Configure the magnitude of the AC component of the voltage.

#### Dependencies

Selecting `Constant`,
`Ramp`,
`Step`, or
`Modulation` exposes related
parameters.

Selecting `External` exposes a physical
signal input port.

### **AC voltage peak magnitude** — AC voltage peak magnitude `100` `V` (default)

AC voltage peak magnitude.

#### Dependencies

This parameter is exposed when the **AC magnitude
configuration** parameter is set to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Rate of change** — AC voltage rate of change `1` **V/s** (default)

AC voltage rate of change.

#### Dependencies

This parameter is exposed when the **AC magnitude
configuration** parameter is set to
`Ramp`.

### **Step amplitude** — AC voltage step amplitude `1` **V** (default)

AC voltage step amplitude.

#### Dependencies

This parameter is exposed when the **AC magnitude
configuration** parameter is set to
`Step`.

### **Modulation magnitude** — AC voltage modulation magnitude `1` `V` (default)

AC voltage modulation magnitude.

#### Dependencies

This parameter is exposed when the **AC magnitude
configuration** parameter is set to
`Modulation`.

### **Modulation frequency** — AC voltage modulation frequency `1` `Hz` (default)

AC voltage modulation frequency.

#### Dependencies

This parameter is exposed when the **AC magnitude
configuration** parameter is set to
`Modulation`.

### **Start time** — AC voltage start time `1``s` (default)

Simulation time for start of AC voltage.

#### Dependencies

This parameter is exposed when the **AC magnitude
configuration** parameter is set to
`Ramp`,
`Step`, or
`Modulation`.

### **Stop time** — AC voltage stop time `2``s` (default)

Simulation time for stop of AC voltage.

#### Dependencies

This parameter is exposed when the **AC magnitude
configuration** parameter is set to
`Ramp`,
`Step`, or
`Modulation`.

### Frequency

### **AC frequency configuration** — AC frequency configuration `Constant` (default) | `Ramp``Step``Modulation``External`

Configure the frequency of the AC component of the voltage.

#### Dependencies

Selecting `Constant`,
`Ramp`,
`Step`, or
`Modulation` exposes related
parameters.

Selecting `External` exposes a physical
signal input port.

### **AC voltage frequency** — AC voltage frequency `60` `Hz` (default)

AC voltage frequency.

#### Dependencies

This parameter is exposed when the **AC frequency
configuration** parameter is set to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Rate of change** — AC frequency rate of change `1` `Hz/s` (default)

AC frequency rate of change.

#### Dependencies

This parameter is exposed when the **AC frequency
configuration** parameter is set to
`Ramp`.

### **Step amplitude** — AC frequency step amplitude `1` `Hz` (default)

AC frequency step amplitude.

#### Dependencies

This parameter is exposed when the **AC frequency
configuration** parameter is set to
`Step`.

### **Modulation magnitude** — AC frequency modulation magnitude `1` `Hz` (default)

AC frequency modulation magnitude.

#### Dependencies

This parameter is exposed when the **AC frequency
configuration** parameter is set to
`Modulation`.

### **Modulation frequency** — AC frequency modulation frequency `1` `Hz` (default)

AC frequency modulation frequency.

#### Dependencies

This parameter is exposed when the **AC frequency
configuration** parameter is set to
`Modulation`.

### **Start time** — AC frequency start time `1``s` (default)

Simulation time for starting AC frequency.

#### Dependencies

This parameter is exposed when the **AC frequency
configuration** parameter is set to
`Ramp`,
`Step`, or
`Modulation`.

### **Stop time** — AC frequency start time `2``s` (default)

Simulation time for stopping AC frequency.

#### Dependencies

This parameter is exposed when the **AC frequency
configuration** parameter is set to
`Ramp`,
`Step`, or
`Modulation`.

### Phase

### **AC phase shift configuration** — AC phase shift configuration `Constant` (default) | `Ramp``Step``Modulation``External`

Configure the phase of the AC component of the voltage.

#### Dependencies

Selecting `Constant`,
`Ramp`,
`Step`, or
`Modulation` exposes related
parameters.

Selecting `External` exposes a physical
signal input port.

### **AC voltage phase shift** — AC voltage phase shift `0` `deg` (default)

AC voltage phase shift.

#### Dependencies

This parameter is exposed when the **AC phase shift
configuration** parameter is set to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Rate of change** — AC phase shift rate of change `1` `deg/s` (default)

AC phase shift rate of change.

#### Dependencies

This parameter is exposed when the **AC phase shift
configuration** parameter is set to
`Ramp`.

### **Step amplitude** — AC phase shift step amplitude `1` `deg` (default)

AC phase shift step amplitude.

#### Dependencies

This parameter is exposed when the **AC phase shift
configuration** parameter is set to
`Step`.

### **Modulation magnitude** — AC phase shift modulation magnitude `1` `deg` (default)

AC phase shift modulation magnitude.

#### Dependencies

This parameter is exposed when the **AC phase shift
configuration** parameter is set to
`Modulation`.

### **Modulation frequency** — AC phase shift modulation frequency `1` `Hz` (default)

AC phase shift modulation frequency.

#### Dependencies

This parameter is exposed when the **AC phase shift
configuration** parameter is set to
`Modulation`.

### **Start time** — AC phase shift start time `1``s` (default)

Simulation time for starting AC phase shift.

#### Dependencies

This parameter is exposed when the **AC phase shift
configuration** parameter is set to
`Ramp`,
`Step`, or
`Modulation`.

### **Stop time** — AC phase shift start time `2``s` (default)

Simulation time for stopping AC phase shift.

#### Dependencies

This parameter is exposed when the **AC phase shift
configuration** parameter is set to
`Ramp`,
`Step`, or
`Modulation`.

### DC Voltage

### **DC voltage configuration** — DC voltage configuration `Constant` (default) | `Ramp``Step``Modulation``External`

Configure the DC component of the voltage.

#### Dependencies

Selecting `Constant`,
`Ramp`,
`Step`, or
`Modulation` exposes related
parameters.

Selecting `External` exposes a physical
signal input port.

### **DC voltage** — DC voltage magnitude `0` `V` (default)

DC voltage magnitude.

#### Dependencies

This parameter is exposed when the **DC magnitude
configuration** parameter is set to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Rate of change** — DC voltage rate of change `1` **V/s** (default)

DC voltage rate of change.

#### Dependencies

This parameter is exposed when the **DC magnitude
configuration** parameter is set to
`Ramp`.

### **Step amplitude** — DC voltage step amplitude `1` **V** (default)

DC voltage step amplitude.

#### Dependencies

This parameter is exposed when the **DC magnitude
configuration** parameter is set to
`Step`.

### **Modulation magnitude** — DC voltage modulation magnitude `1` `V` (default)

DC voltage modulation magnitude.

#### Dependencies

This parameter is exposed when the **DC magnitude
configuration** parameter is set to
`Modulation`.

### **Modulation frequency** — DC voltage modulation frequency `1` `Hz` (default)

DC voltage modulation frequency.

#### Dependencies

This parameter is exposed when the **DC magnitude
configuration** parameter is set to
`Modulation`.

### **Start time** — DC voltage start time `1``s` (default)

Simulation time for start of DC voltage.

#### Dependencies

This parameter is exposed when the **DC magnitude
configuration** parameter is set to
`Ramp`,
`Step`, or
`Modulation`.

### **Stop time** — DC voltage stop time `2``s` (default)

Simulation time for stop of DC voltage.

#### Dependencies

This parameter is exposed when the **DC magnitude
configuration** parameter is set to
`Ramp`,
`Step`, or
`Modulation`.

### Harmonics

### **Source harmonics** — Source harmonics configuration `None` (default) | `Generate harmonics`

Configure the source harmonics.

#### Dependencies

Selecting `Generate harmonics` exposes
related parameters.

### **Harmonic orders** — Harmonic orders `[5, 7, 11, 13]` (default)

Harmonic orders.

#### Dependencies

This parameter is exposed when the **Source
harmonics** parameter is set to `Generate
harmonics`.

### **Harmonic to base magnitude ratios** — Harmonic to base magnitude ratios `[.1, .1, .1, .1]` (default)

Harmonic to base magnitude ratios. Specify the same number of elements
as is specified for the **Harmonic orders**
parameter.

#### Dependencies

This parameter is exposed when the **Source
harmonics** parameter is set to `Generate
harmonics`.

### **Harmonic phase shifts** — Harmonic phase shifts `[0, 0, 0, 0]` `deg` (default)

Harmonic phase shifts. Specify the same number of elements as is
specified for the **Harmonic orders** parameter.

#### Dependencies

This parameter is exposed when the **Source
harmonics** parameter is set to `Generate
harmonics`.

### **Start time** — Source harmonics start time `-inf``s` (default)

Simulation time for start of source harmonics.

#### Dependencies

This parameter is exposed when the **Source
harmonics** parameter is set to `Generate
harmonics`.

### **Stop time** — Source harmonics stop time `inf``s` (default)

Simulation time for stop of source harmonics.

#### Dependencies

This parameter is exposed when the **Source
harmonics** parameter is set to `Generate
harmonics`.

### Noise

### **Noise mode** — Option to include noise `Disabled` (default) | `Enabled`

Noise configuration.

#### Dependencies

Selecting `Enabled` exposes related
parameters.

### **Power spectral density** — Power spectral density `0` `V^2/Hz` (default)

Single-sided spectrum noise power. Density function for the square of
the voltage, commonly thought of as a power into a 1 ohm load. To avoid
unit ambiguity, some datasheets quote noise voltage as a noise density
with units of V/√Hz. In this case, enter the square of the noise density
quoted in the datasheet as the parameter value.

Selecting `Enabled` for the **Noise
mode** parameter exposes this parameter.

#### Dependencies

Selecting `Enabled` for the
**Noise mode** parameter exposes this
parameter.

### **Repeatability** — Random number seed control `Not repeatable` (default) | `Repeatable` | `Specify seed`

The random number seed is the number that initializes the random
number generator. The seed is `0` or a positive
integer. To control the random number seed, set this parameter to:

- `Not repeatable` — The
  seed changes every time you simulate your model. The block
  resets the random seed using the MATLAB® random number generator command:

  ```
  seed = randi(2^32-1);
  ```
- `Repeatable` — The seed is
  the same random number at the start of every simulation. The
  block sets the value using the same MATLAB random number generator command used by the
  `Not repeatable`
  parameter.

  When you add a Force Noise Source block to
  your model from the Sources library, the block generates and
  stores a random value for the repeated seed. When you make a
  copy of the Force Noise Source block from an
  existing block in a model, the copy generates a new random
  value for the repeated seed.
- `Specify seed` — The seed
  is a number that you specify using the
  **Seed** parameter. The
  **Seed** parameter is only available
  when you choose `Specify seed` for
  the **Repeatability** parameter.

#### Dependencies

Selecting `Enabled` for the
**Noise mode** parameter exposes this
parameter.

Selecting `Repeatable` or
`Specify seed` exposes related
parameters.

### **Auto-generated seed used for repeatable option** — Auto-generate seed `0` (default)

Seed is auto-generated.

#### Dependencies

Selecting `Enabled` for the
**Noise mode** parameter and
`Repeatable` for the
**Repeatability** parameter exposes this
parameter.

### **Seed** — Random number generation seed value `0` (default)

The seed must be `0` or a positive integer. This
parameter is only available when you select `Specify
seed` for the **Repeatability**
parameter.

#### Dependencies

Selecting `Enabled` for the
**Noise mode** parameter and
`Specify seed` for the
**Repeatability** parameter exposes this
parameter.

### **Sample time** — Time step period and offset `1e-3` `s` (default) | `[step, offset]` `s`

The values of the time *step* period and the initial
time *offset*. If you specify a scalar value for
*step*, the block assumes an
*offset* value of `0`.To specify a
nonzero value for the initial time offset, specify the parameter values
using the vector `[step,
offset]`. The
*offset* value must be less than the
*step* value and greater than or equal to
zero.

#### Dependencies

Selecting `Enabled` for the
**Noise mode** parameter exposes related
parameters.

## Libraries

Simscape / Electrical / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Single-phase AC voltage source with optional programmable magnitude, frequency, phase shift and DC offset

The Programmable Voltage Source block models a
single-phase AC voltage source with programmable magnitude, frequency, phase shift and
DC offset. Choose the external mode to specify these quantities by physical input
signals **M**, **F**, **Phi** and
**DC**. Harmonics and noise can be included in the voltage source.

For relevant equations, see the Voltage Source block.

### Limitations

Simulating with harmonics enabled slows down simulation. If you include harmonics, choose a
sample time such that harmonics are generated only at frequencies of interest, and
not higher.

Simulating with noise enabled slows down simulation. If you include noise, choose
a sample time such that noise is generated only at frequencies of interest, and not
higher.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
