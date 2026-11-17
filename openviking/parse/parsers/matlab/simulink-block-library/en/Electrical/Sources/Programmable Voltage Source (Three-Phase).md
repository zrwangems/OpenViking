---
type: simulink-block
title: 'Programmable Voltage Source (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'programmablevoltagesourcethreephase'
documentation_source_path: 'ref/programmablevoltagesourcethreephase.html'
language: en
---

# Programmable Voltage Source (Three-Phase)

## Ports
```yaml
ports:
- name: F
  summary: Frequency physical signal
  direction: input
- name: M
  summary: Magnitude physical signal
  direction: input
- name: Phi
  summary: Phase shift physical signal
  direction: input
- name: n
  summary: Neutral electrical
  direction: conserving
- name: '~'
  summary: Three-phase AC voltage electrical
  direction: conserving
```

### Input

### **F** — Frequency physical signal

Physical signal input associated with the frequency.

### **M** — Magnitude physical signal

Physical signal input associated with the magnitude.

### **Phi** — Phase shift physical signal

Physical signal input associated with the phase shift.
### Conserving

### **n** — Neutral electrical

Electrical conserving port associated with a neutral point.

### **~** — Three-phase AC voltage electrical

Expandable electrical conserving three-phase
port associated with the AC voltage.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to model composite or expanded three-phase ports Composite three-phase ports (default) | Expanded three-phase
    ports
  group: ''
- name: AC magnitude configuration
  summary: AC voltage magnitude configuration Constant (default) | Ramp | Step | Modulation | External
  group: AC Magnitude
- name: Rated voltage (phase-to-phase RMS)
  summary: Rated AC voltage 100 V (default)
  group: AC Magnitude
- name: Rate of change
  summary: AC voltage rate of change 1 V/s (default)
  group: AC Magnitude
- name: Step amplitude
  summary: AC voltage step amplitude 1 V (default)
  group: AC Magnitude
- name: Modulation magnitude
  summary: AC voltage modulation magnitude 1 V (default)
  group: AC Magnitude
- name: Modulation frequency
  summary: AC voltage modulation frequency 1 Hz (default)
  group: AC Magnitude
- name: Start time
  summary: AC voltage start time 1s (default)
  group: AC Magnitude
- name: Stop time
  summary: AC voltage stop time 2s (default)
  group: AC Magnitude
- name: AC frequency configuration
  summary: AC frequency configuration Constant (default) | Ramp | Step | Modulation | External
  group: Frequency
- name: Rated frequency
  summary: Rated frequency 60 Hz (default)
  group: Frequency
- name: Rate of change
  summary: AC frequency rate of change 1 Hz/s (default)
  group: Frequency
- name: Step amplitude
  summary: AC frequency step amplitude 1 Hz (default)
  group: Frequency
- name: Modulation magnitude
  summary: AC frequency modulation magnitude 1 Hz (default)
  group: Frequency
- name: Modulation frequency
  summary: AC frequency modulation frequency 1 Hz (default)
  group: Frequency
- name: Start time
  summary: AC frequency start time 1s (default)
  group: Frequency
- name: Stop time
  summary: AC frequency start time 2s (default)
  group: Frequency
- name: AC phase shift configuration
  summary: AC phase shift configuration Constant (default) | Ramp | Step | Modulation | External
  group: Phase
- name: Phase shift
  summary: AC voltage phase shift 0 deg (default)
  group: Phase
- name: Rate of change
  summary: AC phase shift rate of change 1 deg/s (default)
  group: Phase
- name: Step amplitude
  summary: AC phase shift step amplitude 1 deg (default)
  group: Phase
- name: Modulation magnitude
  summary: AC phase shift modulation magnitude 1 deg (default)
  group: Phase
- name: Modulation frequency
  summary: AC phase shift modulation frequency 1 Hz (default)
  group: Phase
- name: Start time
  summary: AC phase shift start time 1s (default)
  group: Phase
- name: Stop time
  summary: AC phase shift start time 2s (default)
  group: Phase
- name: Source impedance
  summary: Source impedance configuration None (default) | X/R Ratio | Series R | Series L | Series RL
  group: Impedance
- name: Short-circuit power level
  summary: Short-circuit power level 1e6 V*A (default)
  group: Impedance
- name: Source X/R ratio
  summary: X/R ratio 15 (default)
  group: Impedance
- name: Source resistance
  summary: Resistance 0.01 Ohm (default)
  group: Impedance
- name: Source inductance
  summary: Inductance 3.97e-4 H (default)
  group: Impedance
- name: Parasitic parallel conductance
  summary: Parasitic parallel conductance 1e-6 1/Ohm (default)
  group: Impedance
- name: Source harmonics
  summary: Source harmonics configuration None (default) | Generate harmonics
  group: Harmonics
- name: Harmonic orders
  summary: Harmonic orders [5, 7, 11, 13] (default)
  group: Harmonics
- name: Harmonic to base magnitude ratios
  summary: Harmonic to base magnitude ratios [.1, .1, .1, .1] (default)
  group: Harmonics
- name: Harmonic phase shifts
  summary: Harmonic phase shifts [0, 0, 0, 0] deg (default)
  group: Harmonics
- name: Harmonic sequences
  summary: Harmonic sequences [1, 1, 1, 1] (default)
  group: Harmonics
- name: Start time
  summary: Source harmonics start time -infs (default)
  group: Harmonics
- name: Stop time
  summary: Source harmonics stop time infs (default)
  group: Harmonics
```

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### AC Magnitude

### **AC magnitude configuration** — AC voltage magnitude configuration `Constant` (default) | `Ramp` | `Step` | `Modulation` | `External`

Configure the magnitude of the AC component of the voltage.

#### Dependencies

Selecting `Constant`,
`Ramp`,
`Step`, or
`Modulation` exposes related
parameters.

Selecting `External` exposes a physical
signal input port.

### **Rated voltage (phase-to-phase RMS)** — Rated AC voltage `100` `V` (default)

Rated AC voltage (phase-to-phase RMS).

#### Dependencies

To enable this parameter, set **AC magnitude configuration** to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Rate of change** — AC voltage rate of change `1` **V/s** (default)

AC voltage rate of change.

#### Dependencies

To enable this parameter, set **AC magnitude configuration** to
`Ramp`.

### **Step amplitude** — AC voltage step amplitude `1` **V** (default)

AC voltage step amplitude.

#### Dependencies

To enable this parameter, set **AC magnitude configuration** to
`Step`.

### **Modulation magnitude** — AC voltage modulation magnitude `1` `V` (default)

AC voltage modulation magnitude.

#### Dependencies

To enable this parameter, set **AC magnitude
configuration** to
`Modulation`.

### **Modulation frequency** — AC voltage modulation frequency `1` `Hz` (default)

AC voltage modulation frequency.

#### Dependencies

To enable this parameter, set **AC magnitude
configuration** to
`Modulation`.

### **Start time** — AC voltage start time `1``s` (default)

Simulation time for start of AC voltage.

#### Dependencies

To enable this parameter, set **AC magnitude configuration** to
`Ramp`,
`Step`, or
`Modulation`.

### **Stop time** — AC voltage stop time `2``s` (default)

Simulation time for stop of AC voltage.

#### Dependencies

To enable this parameter, set **AC magnitude
configuration** to `Ramp`,
`Step`, or
`Modulation`.

### Frequency

### **AC frequency configuration** — AC frequency configuration `Constant` (default) | `Ramp` | `Step` | `Modulation` | `External`

Configure the frequency of the AC component of the voltage.

#### Dependencies

Selecting `Constant`,
`Ramp`,
`Step`, or
`Modulation` exposes related
parameters.

Selecting `External` exposes a physical
signal input port.

### **Rated frequency** — Rated frequency `60` `Hz` (default)

Rated frequency.

#### Dependencies

To enable this parameter, set **AC frequency configuration** to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Rate of change** — AC frequency rate of change `1` `Hz/s` (default)

AC frequency rate of change.

#### Dependencies

To enable this parameter, set **AC frequency configuration** to
`Ramp`.

### **Step amplitude** — AC frequency step amplitude `1` `Hz` (default)

AC frequency step amplitude.

#### Dependencies

To enable this parameter, set **AC frequency
configuration** to
`Step`.

### **Modulation magnitude** — AC frequency modulation magnitude `1` `Hz` (default)

AC frequency modulation magnitude.

#### Dependencies

To enable this parameter, set **AC frequency
configuration** to
`Modulation`.

### **Modulation frequency** — AC frequency modulation frequency `1` `Hz` (default)

AC frequency modulation frequency.

#### Dependencies

To enable this parameter, set **AC frequency
configuration** to
`Modulation`.

### **Start time** — AC frequency start time `1``s` (default)

Simulation time for starting AC frequency.

#### Dependencies

To enable this parameter, set **AC frequency configuration** to
`Ramp`,
`Step`, or
`Modulation`.

### **Stop time** — AC frequency start time `2``s` (default)

Simulation time for stopping AC frequency.

#### Dependencies

To enable this parameter, set **AC frequency
configuration** to `Ramp`,
`Step`, or
`Modulation`.

### Phase

### **AC phase shift configuration** — AC phase shift configuration `Constant` (default) | `Ramp` | `Step` | `Modulation` | `External`

Configure the phase of the AC component of the voltage.

#### Dependencies

Selecting `Constant`,
`Ramp`,
`Step`, or
`Modulation` exposes related
parameters.

Selecting `External` exposes a physical
signal input port.

### **Phase shift** — AC voltage phase shift `0` `deg` (default)

AC voltage phase shift.

#### Dependencies

To enable this parameter, set **AC phase shift configuration** to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Rate of change** — AC phase shift rate of change `1` `deg/s` (default)

AC phase shift rate of change.

#### Dependencies

To enable this parameter, set **AC phase shift configuration** to
`Ramp`.

### **Step amplitude** — AC phase shift step amplitude `1` `deg` (default)

AC phase shift step amplitude.

#### Dependencies

To enable this parameter, set **AC phase shift
configuration** to
`Step`.

### **Modulation magnitude** — AC phase shift modulation magnitude `1` `deg` (default)

AC phase shift modulation magnitude.

#### Dependencies

To enable this parameter, set **AC phase shift
configuration** to
`Modulation`.

### **Modulation frequency** — AC phase shift modulation frequency `1` `Hz` (default)

AC phase shift modulation frequency.

#### Dependencies

To enable this parameter, set **AC phase shift
configuration** to
`Modulation`.

### **Start time** — AC phase shift start time `1``s` (default)

Simulation time for starting AC phase shift.

#### Dependencies

To enable this parameter, set **AC phase shift configuration** to
`Ramp`,
`Step`, or
`Modulation`.

### **Stop time** — AC phase shift start time `2``s` (default)

Simulation time for stopping AC phase shift.

#### Dependencies

To enable this parameter, set **AC phase shift configuration** to
`Ramp`,
`Step`, or
`Modulation`.

### Impedance

### **Source impedance** — Source impedance configuration `None` (default) | `X/R Ratio` | `Series R` | `Series L` | `Series RL`

Source impedance configuration.

#### Dependencies

Selecting `X/R Ratio`,
`Series R`, `Series
L`, or `Series RL` exposes
related parameters.

### **Short-circuit power level** — Short-circuit power level `1e6` `V*A` (default)

Short-circuit power level.

#### Dependencies

To enable this parameter, set **Source impedance** to `X/R
Ratio`.

### **Source X/R ratio** — X/R ratio `15` (default)

Source X/R ratio.

#### Dependencies

To enable this parameter, set **Source
impedance** to `X/R
Ratio`.

### **Source resistance** — Resistance `0.01` `Ohm` (default)

Source resistance.

#### Dependencies

To enable this parameter, set **Source impedance** to
`Series R` or `Series
RL`.

### **Source inductance** — Inductance `3.97e-4` `H` (default)

Source inductance.

#### Dependencies

To enable this parameter, set **Source impedance** to
`Series L` or `Series
RL`.

### **Parasitic parallel conductance** — Parasitic parallel conductance `1e-6` `1/Ohm` (default)

Parasitic parallel conductance.

#### Dependencies

To enable this parameter, set **Source
impedance** to `X/R Ratio`,
`Series L`, or `Series
RL`.

### Harmonics

### **Source harmonics** — Source harmonics configuration `None` (default) | `Generate harmonics`

Configuration for the source harmonics.

#### Dependencies

Selecting `Generate harmonics` exposes
related parameters.

### **Harmonic orders** — Harmonic orders `[5, 7, 11, 13]` (default)

Harmonic orders.

#### Dependencies

To enable this parameter, set **Source harmonics** to
`Generate harmonics`.

### **Harmonic to base magnitude ratios** — Harmonic to base magnitude ratios `[.1, .1, .1, .1]` (default)

Harmonic to base magnitude ratios. Specify the same number of elements
as is specified for the **Harmonic orders**
parameter.

#### Dependencies

To enable this parameter, set **Source
harmonics** to `Generate
harmonics`.

### **Harmonic phase shifts** — Harmonic phase shifts `[0, 0, 0, 0]` `deg` (default)

Harmonic phase shifts. Specify the same number of elements as is
specified for the **Harmonic orders** parameter.

#### Dependencies

To enable this parameter, set **Source
harmonics** to `Generate
harmonics`.

### **Harmonic sequences** — Harmonic sequences `[1, 1, 1, 1]` (default)

Harmonic sequences:

- `0` indicates zero-sequence
- `1` indicates positive-sequence
- `2` indicates negative-sequence

Specify the same number of elements as is specified for
the **Harmonic orders** parameter.

#### Dependencies

To enable this parameter, set **Source
harmonics** to `Generate
harmonics`.

### **Start time** — Source harmonics start time `-inf``s` (default)

Simulation time for start of source harmonics.

#### Dependencies

To enable this parameter, set **Source
harmonics** to `Generate
harmonics`.

### **Stop time** — Source harmonics stop time `inf``s` (default)

Simulation time for stop of source harmonics.

#### Dependencies

To enable this parameter, set **Source
harmonics** to `Generate
harmonics`.
## Libraries

Simscape / Electrical / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Three-phase voltage source with optional programmable AC magnitude, frequency, and phase shift

The Programmable Voltage Source (Three-Phase) block models a three-phase voltage source with
programmable AC magnitude, frequency, and phase shift. Choose the external mode to
specify these quantities by physical input signals **M**,
**F**, and **Phi**. You can add harmonics and
internal impedance to the voltage source.

For relevant equations, see the Voltage Source (Three-Phase) block.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
