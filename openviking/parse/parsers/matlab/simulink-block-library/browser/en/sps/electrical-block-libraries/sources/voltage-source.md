---
type: simulink-block
title: 'Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sources'
documentation_page: 'voltagesource'
documentation_source_path: 'ref/voltagesource.html'
language: en
---

# Voltage Source

## Ports

### Conserving

### **+** — Positive port electrical

Electrical conserving port associated with the voltage source positive
terminal

### **-** — Negative port electrical

Electrical conserving port associated with the voltage source negative
terminal

## Parameters

### DC & AC Components

### **DC voltage** — DC output voltage `0` `V` (default)

DC component of the output voltage. Specify a nonzero value to add a DC component
to the voltage source.

### **AC voltage peak amplitude** — AC voltage amplitude `0` `V` (default)

Amplitude of the AC component of the output voltage. Specify a nonzero value to
add an AC component to the voltage source.

### **AC voltage phase shift** — AC voltage phase offset `0` `rad` (default)

Phase offset of the AC component of the output voltage.

### **AC voltage frequency** — AC voltage frequency `60` `Hz` (default)

Frequency of the AC component of the output voltage, in Hz.

### Noise

### **Noise mode** — Noise option `Disabled` (default) | `Enabled`

Select the noise option:

- `Disabled` — No noise is produced by the
  voltage source.
- `Enabled` — The voltage source generates
  thermal noise, and the associated parameters become visible on the
  **Noise** tab.

### **Power spectral density** — Power spectral density `0` `V^2/Hz` (default)

The single-sided spectrum noise power. Strictly-speaking, this is a density
function for the square of the voltage, commonly thought of as a power into a 1 ohm
load, and therefore the units are V^2/Hz. To avoid this unit ambiguity, some
datasheets quote noise voltage as a noise density with units of V/√Hz. In this case,
you should enter the square of the noise density quoted in the datasheet as the
parameter value.

### **Repeatability** — Noise control option `Not repeatable` (default) | `Repeatable` | `Specify seed`

Select the noise control option:

- `Not repeatable` — The random sequence used
  for noise generation is not repeatable.
- `Repeatable` — The random sequence used for
  noise generation is repeatable, with a system-generated seed.
- `Specify seed` — The random sequence used for
  noise generation is repeatable, and you control the seed by using the
  **Seed** parameter.

### **Auto-generated seed used for repeatable option** — Auto-generated random number seed `1964622691` (default)

Random number seed stored inside the block to make the random sequence repeatable.
The parameter value is automatically generated using the MATLAB random number generator command. You can modify this parameter value,
but it gets overwritten by a new random value if you copy the block to another block
in the model. Therefore, if you want to control the seed of the random sequence, use
the `Specify seed` option for the
**Repeatability** parameter and specify the desired seed value
using the **Seed** parameter.

#### Dependencies

This parameter is visible only when you select
`Repeatable` for the **Repeatability** parameter.

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

Voltage source with optional DC, AC and noise components

The Voltage Source block implements a voltage source with
DC, AC, and noise components. The voltage across the **+** and
**–** terminals is given by:

v=vDC+vACsin(2πft+ϕ)+vN

where:

- *vDC* is the steady-state DC voltage
  component.
- *vAC* is the amplitude of the AC voltage
  component.
- *f* is the frequency of the AC component.
- *ϕ* is the phase offset of the AC component.
- *vN* is the noise voltage.

You can configure your source as DC-only, AC-only, or a combination of both. By default,
both AC and DC components are set to 0. Define the AC/DC voltage by specifying nonzero
parameter values after placing the block in your model.

The noise component is also optional. If you set the **Noise mode**
parameter to `Enabled`, then the added noise voltage is given
by:

vN=Pv/2N(0,1)h

where:

- *Pv* is the single-sided noise power spectral
  density for a 1 ohm load, in V^2/Hz.
- *N* is a Gaussian random number with zero mean and standard deviation
  of one.
- *h* is the sampling interval.

By default, the **Noise mode** parameter is set to
`Disabled`, and the voltage source generates no thermal
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
  Voltage Source block from the block library to the
  model. When you make a new copy of the Voltage Source
  block from an existing one in a model, a new seed value is generated. The block sets the
  value using the MATLAB random number generator command shown above.
- `Specify seed` — If you select this option, the
  additional **Seed** parameter lets you directly specify the random
  number seed value.
