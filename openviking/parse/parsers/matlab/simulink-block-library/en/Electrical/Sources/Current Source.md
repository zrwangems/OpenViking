---
type: simulink-block
title: 'Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'currentsource'
documentation_source_path: 'ref/currentsource.html'
language: en
---

# Current Source

## Ports
```yaml
ports:
- name: +
  summary: Positive port electrical
  direction: conserving
- name: '-'
  summary: Negative port electrical
  direction: conserving
```

### Conserving

### **+** — Positive port electrical

Electrical conserving port associated with the current source positive
terminal

### **-** — Negative port electrical

Electrical conserving port associated with the current source negative
terminal
## Parameters
```yaml
parameters:
- name: DC current
  summary: DC current 0 A (default)
  group: DC & AC Components
- name: AC current peak amplitude
  summary: AC current amplitude 0 A (default)
  group: DC & AC Components
- name: AC current phase shift
  summary: AC current phase offset 0 rad (default)
  group: DC & AC Components
- name: AC current frequency
  summary: AC current frequency 60 Hz (default)
  group: DC & AC Components
- name: Noise mode
  summary: Noise option Disabled (default) | Enabled
  group: Noise
- name: Power spectral density
  summary: Power spectral density 0 A^2/Hz (default)
  group: Noise
- name: Repeatability
  summary: Noise control option Not repeatable (default) | Repeatable | Specify seed
  group: Noise
- name: Auto-generated seed used for repeatable option
  summary: Auto-generated random number seed 3241354618 (default)
  group: Noise
- name: Seed
  summary: Random number seed 0 (default)
  group: Noise
- name: Sample time
  summary: Sample time 1e-3 s (default)
  group: Noise
```

### DC & AC Components

### **DC current** — DC current `0` `A` (default)

DC component of the output current. Specify a nonzero value to add a DC component
to the current source.

### **AC current peak amplitude** — AC current amplitude `0` `A` (default)

Amplitude of the AC component of the output current. Specify a nonzero value to
add an AC component to the current source.

### **AC current phase shift** — AC current phase offset `0` `rad` (default)

Phase offset of the AC component of the output current.

### **AC current frequency** — AC current frequency `60` `Hz` (default)

Frequency of the AC component of the output current.

### Noise

### **Noise mode** — Noise option `Disabled` (default) | `Enabled`

Select the noise option:

- `Disabled` — No noise is produced by the
  current source. This is the default.
- `Enabled` — The current source generates
  thermal noise, and the associated parameters become visible on the
  **Noise** tab.

### **Power spectral density** — Power spectral density `0` `A^2/Hz` (default)

The single-sided spectrum noise power. Strictly-speaking, this is a density
function for the square of the current, commonly thought of as a power into a 1 ohm
load, and therefore units are A^2/Hz. To avoid this unit ambiguity, some datasheets
quote noise current as a noise density with units of A/√Hz. In this case, you should
enter the square of the noise density quoted in the datasheet as the parameter
value.

### **Repeatability** — Noise control option `Not repeatable` (default) | `Repeatable` | `Specify seed`

Select the noise control option:

- `Not repeatable` — The random sequence used
  for noise generation is not repeatable. This is the default.
- `Repeatable` — The random sequence used for
  noise generation is repeatable, with a system-generated seed.
- `Specify seed` — The random sequence used for
  noise generation is repeatable, and you control the seed by using the
  **Seed** parameter.

### **Auto-generated seed used for repeatable option** — Auto-generated random number seed `3241354618` (default)

Random number seed stored inside the block to make the random sequence repeatable.
The parameter value is automatically generated using the MATLAB random number generator command. You can modify this parameter value,
but it gets overwritten by a new random value if you copy the block to another block
in the model. Therefore, if you want to control the seed of the random sequence, use
the `Specify seed` option for the
**Repeatability** parameter and specify the desired seed value
using the **Seed** parameter.

#### Dependencies

This parameter is visible only when you select
`Repeatable` for the **Repeatability**
parameter.

### **Seed** — Random number seed `0` (default)

Random number seed used by the noise random number generator.

#### Dependencies

This parameter is visible only when you select `Specify
seed` for the **Repeatability** parameter.

### **Sample time** — Sample time `1e-3` `s` (default)

Defines the rate at which the noise source is sampled. Choose it to reflect the
frequencies of interest in your model. Making the sample time too small will
unnecessarily slow down your simulation.
## Libraries

Simscape / Electrical / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Current source with optional DC, AC, and noise components

The Current Source block implements a current source with
DC, AC, and noise components. The current flowing through the source from the
**–** terminal to the **+** terminal is given by:

i=iDC+iACsin(2πft+ϕ)+iN

where:

- *i*DC is the steady-state DC current
  component.
- *i*AC is the amplitude of the AC current
  component.
- *f* is the frequency of the AC component.
- *ϕ* is the phase offset of the AC component.
- *i*N is the noise current.

You can configure your source as DC-only, AC-only, or a combination of both. By default,
both AC and DC components are set to 0. Define the AC/DC current by specifying nonzero
parameter values after placing the block in your model.

The noise component is also optional. If you set the **Noise mode**
parameter to `Enabled`, then the added noise current is given
by:

iN=Pi/2N(0,1)h

where:

- *P*i is the single-sided noise power spectral
  density for a 1 ohm load, in A^2/Hz.
- *N* is a Gaussian random number with zero mean and standard deviation
  of one.
- *h* is the sampling interval.

By default, the **Noise mode** parameter is set to
`Disabled`, and the current source generates no thermal
noise.

### Noise Options

The block generates Gaussian noise by using the PS
Random Number source in the Simscape™ Foundation library. You can control the random number seed by setting the
**Repeatability** parameter:

- `Not repeatable` — Every time you simulate your
  model, the block resets the random seed using the MATLAB® random number generator:

  ```
  seed = randi(2^32-1);
  ```
- `Repeatable` — The block automatically generates a
  seed value and stores it inside the block, to always start the simulation with the same
  random number. This auto-generated seed value is set when you add a
  Current Source block from the block library to the
  model. When you make a new copy of the Current Source
  block from an existing one in a model, a new seed value is generated. The block sets the
  value using the MATLAB random number generator command shown above.
- `Specify seed` — If you select this option, the
  additional **Seed** parameter lets you directly specify the random
  number seed value.
