---
type: simulink-block
title: 'Programmable Signal Generator (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Sources'
documentation_page: 'programmablesignalgeneratorthreephase'
documentation_source_path: 'ref/programmablesignalgeneratorthreephase.html'
language: en
---

# Programmable Signal Generator (Three-Phase)

## Ports

### Output

### **abc** — Three-phase sinusoidal signal vector

Three-phase sinusoidal signal, returned as a vector.

**Data Types:** `single` | `double`

### **m** — Signal measurements vector

Magnitude, frequency, phase, and angle of the sine wave of all three
phases of the sinusoidal signal, returned as a vector.

**Data Types:** `single` | `double`

## Parameters

### **Sample time** — Block sample time `1e-5` (default) | 0 | positive scalar

Time between consecutive block executions.
During execution, the block produces outputs and, if appropriate, updates
its internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

For discrete-time operation, specify a positive integer. For
continuous-time operation, specify `0`.

### Magnitude

### **Variation configuration** — Type of magnitude variation `Constant` (default) | `Ramp` | `Step` | `Modulation` | `Table`

Type of variation to apply to the signal magnitude.

### **Magnitude (value)** — Magnitude of generated three-phase sine wave `100` (default) | scalar

Magnitude of the generated positive-sequence three-phase sine
wave.

#### Dependencies

To enable this parameter, set **Variation configuration** to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Rate of change (value/s)** — Magnitude rate of change `100` (default) | scalar

Rate of change of the magnitude.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Ramp`.

### **Step value (value)** — Magnitude step value `100` (default) | scalar

Amplitude of the step variation for the signal magnitude.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Step`.

### **Modulation magnitude** — Modulation magnitude `50` (default) | scalar

Magnitude of the modulation for the signal magnitude.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Modulation`.

### **Modulation frequency** — Modulation frequency `10` (default) | scalar

Frequency of the modulation for the signal magnitude.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Modulation`.

### **Start time** — Start time of magnitude variation `0.1` (default) | scalar

Time when the programmed variation on the magnitude starts.

#### Dependencies

To enable this parameter, set **Variation configuration** to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Stop time** — Stop time of magnitude variation `0.6` (default) | scalar

Time when the programmed variation on the magnitude stops.

#### Dependencies

To enable this parameter, set **Variation configuration** to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Table data** — Magnitude table values `[0 30 60 90]` (default) | vector

Values of the signal magnitude that correspond to the time values specified in the
**Time values** parameter.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Table`.

### **Time values** — Magnitude time values `[0 0.3 0.6 0.9]` (default) | vector

Time values when the signal magnitude changes to the values specified
in the **Table data** parameter.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Table`.

### Frequency

### **Variation configuration** — Type of frequency variation `Constant` (default) | `Ramp` | `Step` | `Modulation` | `Table`

Type of variation to apply to the signal frequency.

### **Frequency (Hz)** — Frequency of generated three-phase sine wave `100` (default) | scalar

Frequency of the generated positive-sequence three-phase sine
wave.

#### Dependencies

To enable this parameter, set **Variation configuration** to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Rate of change (Hz/s)** — Frequency rate of change `100` (default) | scalar

Rate of change of the frequency.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Ramp`.

### **Step value (Hz)** — Frequency step value `100` (default) | scalar

Amplitude of the step variation for the signal frequency.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Step`.

### **Modulation magnitude** — Frequency modulation magnitude `50` (default) | scalar

Magnitude of the modulation for the signal frequency.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Modulation`.

### **Modulation frequency** — Frequency modulation frequency `10` (default) | scalar

Frequency of the modulation for the signal frequency.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Modulation`.

### **Start time** — Start time of frequency variation `0.1` (default) | scalar

Time when the programmed variation on the frequency starts.

#### Dependencies

To enable this parameter, set **Variation configuration** to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Stop time** — Stop time of frequency variation `0.6` (default) | scalar

Time when the programmed variation on the frequency stops.

#### Dependencies

To enable this parameter, set **Variation configuration** to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Table data** — Frequency table values `[0 30 60 90]` (default) | vector

Values of the signal frequency that correspond to the time values specified in the
**Time values** parameter.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Table`.

### **Time values** — Frequency time values `[0 0.3 0.6 0.9]` (default) | vector

Time values when the signal frequency changes to the values specified
in the **Table data** parameter.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Table`.

### Phase

### **Variation configuration** — Type of phase variation `Constant` (default) | `Ramp` | `Step` | `Modulation` | `Table`

Type of variation to apply to the phase magnitude.

### **Phase shift (deg)** — Phase shift of generated three-phase sine wave `100` (default) | scalar

Phase shift of the generated positive-sequence three-phase sine
wave.

#### Dependencies

To enable this parameter, set **Variation configuration** to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Rate of change (deg/s)** — Phase rate of change `100` (default) | scalar

Rate of change of the phase.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Ramp`.

### **Step value (deg)** — Phase step value `100` (default) | scalar

Amplitude of the step variation for the signal phase.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Step`.

### **Modulation magnitude** — Phase modulation magnitude `50` (default) | scalar

Magnitude of the modulation for the signal phase.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Modulation`.

### **Modulation frequency** — Phase modulation frequency `10` (default) | scalar

Frequency of the modulation for the signal phase.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Modulation`.

### **Start time** — Start time of phase variation `0.1` (default) | scalar

Time when the programmed variation on the phase starts.

#### Dependencies

To enable this parameter, set **Variation configuration** to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Stop time** — Stop time of phase variation `0.6` (default) | scalar

Time when the programmed variation on the phase stops.

#### Dependencies

To enable this parameter, set **Variation configuration** to
`Constant`,
`Ramp`,
`Step`, or
`Modulation`.

### **Table data** — Phase table values `[0 30 60 90]` (default) | vector

Values of the signal phase that correspond to the time values specified in the
**Time values** parameter.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Table`.

### **Time values** — Phase time values `[0 0.3 0.6 0.9]` (default) | vector

Time values when the signal frequency changes to the values specified
in the **Table data** parameter.

#### Dependencies

To enable this parameter, set **Variation
configuration** to
`Table`.

### Harmonics

### **Enable harmonic A** — Harmonic A overlap `off` (default) | `on`

Whether harmonic A overlaps the fundamental frequency of the generated
signal.

### **Harmonic sequence** — Type of harmonic A sequence `Zero Sequence` (default) | `Positive Sequence` | `Negative Sequence`

Type of sequence for harmonic A.

#### Dependencies

To enable this parameter, select the **Enable harmonic
A** check box.

### **Harmonic order** — Order of harmonic A `3` (default) | scalar

Order of harmonic A that overlaps the signal fundamental frequency.

#### Dependencies

To enable this parameter, select the **Enable harmonic
A** check box.

### **Harmonic magnitude** — Magnitude of harmonic A `50` (default) | scalar

Magnitude of harmonic A that overlaps the signal fundamental frequency.

#### Dependencies

To enable this parameter, select the **Enable harmonic
A** check box.

### **Harmonic phase shift** — Phase shift of harmonic A `180` (default) | scalar

Phase shift of harmonic A that overlaps the signal fundamental frequency.

#### Dependencies

To enable this parameter, select the **Enable harmonic
A** check box.

### **Start time** — Start time of harmonic A overlap `0.1` (default) | scalar

Time when the harmonic A overlaps the signal fundamental
frequency.

#### Dependencies

To enable this parameter, select the **Enable harmonic
A** check box.

### **Stop time** — Stop time of harmonic A overlap `0.6` (default) | scalar

Time when the harmonic A stops overlapping the signal fundamental
frequency.

#### Dependencies

To enable this parameter, select the **Enable harmonic
A** check box.

### **Enable harmonic B** — Harmonic B overlap `off` (default) | `on`

Whether harmonic B overlaps the fundamental frequency of the generated
signal.

### **Harmonic sequence** — Type of sequence of harmonic B `Zero Sequence` (default) | `Positive Sequence` | `Negative Sequence`

Type of sequence for harmonic B.

#### Dependencies

To enable this parameter, select the **Enable harmonic B** check
box.

### **Harmonic order** — Order of harmonic B `3` (default) | scalar

Order of harmonic B that overlaps the signal fundamental frequency.

#### Dependencies

To enable this parameter, select the **Enable harmonic
B** check box.

### **Harmonic magnitude** — Magnitude of harmonic B `50` (default) | scalar

Magnitude of harmonic B that overlaps the signal fundamental frequency.

#### Dependencies

To enable this parameter, select the **Enable harmonic
B** check box.

### **Harmonic phase shift** — Phase shift of harmonic B `180` (default) | scalar

Phase shift of harmonic B that overlaps the signal fundamental frequency.

#### Dependencies

To enable this parameter, select the **Enable harmonic
B** check box.

### **Start time** — Start time of harmonic B overlap `0.1` (default) | scalar

Time when the harmonic B overlaps the signal fundamental
frequency.

#### Dependencies

To enable this parameter, select the **Enable harmonic
B** check box.

### **Stop time** — Stop time of harmonic B overlap `0.6` (default) | scalar

Time when the harmonic B stops overlapping the signal fundamental
frequency.

#### Dependencies

To enable this parameter, select the **Enable harmonic
B** check box.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020a**

## Description

Discrete-time or continuous-time three-phase sinusoidal signal generator with programmable magnitude, phase, frequency, and overlapping harmonics

The Programmable Signal Generator (Three-Phase)
generates a three-phase sinusoidal signal with programmable magnitude, phase, and
frequency over time. You can specify one or two harmonics that can be overlapped on the
signal fundamental frequency.

You can switch between continuous and discrete implementations of the block by using the
**Sample time** parameter. To configure the block for continuous
time, set **Sample time** to `0`. To configure the
block for discrete time, set **Sample time** to a positive, nonzero
value.
