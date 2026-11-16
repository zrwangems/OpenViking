---
type: simulink-block
title: 'Sinusoid'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Sources'
documentation_page: 'sinusoid'
documentation_source_path: 'ref/sinusoid.html'
language: en
---

# Sinusoid

## Ports

Not documented in R2025b.

## Parameters

### **Source type** — Wave type `Ideal voltage` (default) | `Ideal current`

Wave type, specified as:

- `Ideal Voltage` —
  The block simulates a voltage envelope *v*(*t*)
  at the specified **Carrier frequencies**.
- `Ideal Current` —
  The block simulates a current envelope *i*(*t*)
  at the specified **Carrier frequencies**.

### **Offset in-phase** — In-phase offset `0 V` (default) | `0 A` | vector of real or complex numbers | `V` | `mV` | `kV` | `A` | `mA` | `uA` | `kA`

In-phase offset for each of the RF circuit carrier frequencies,
specified as a vector of real or complex numbers. Specify the units
from the corresponding drop-down list. The units are in volts for `Ideal
Voltage` and amperes for `Ideal Current`.

### **Offset quadrature** — Quadrature offset `0 V` (default) | `0 A` | vector of real or complex numbers | `V` | `mV` | `kV` | `A` | `mA` | `uA` | `kA`

Quadrature offset for each of the RF circuit carrier frequencies,
specified as a vector of real or complex numbers. Specify the units
from the corresponding drop-down list. The units are in volts for `Ideal
Voltage` and amperes for `Ideal Current`.

### **Sinusoidal amplitude in-phase** — In-phase amplitude `0` (default) | vector of real or complex numbers | `V` | `mV` | `kV` | `A` | `mA` | `uA` | `kA`

In-phase amplitude, specified as a vector of real number or
a complex number. Specify the units from the corresponding drop-down
list. The units are in volts for `Ideal Voltage` and
amperes for `Ideal Current`.

### **Sinusoidal amplitude quadrature** — Quadrature amplitude `0` (default) | vector of real or complex numbers | `V` | `mV` | `kV` | `A` | `mA` | `uA` | `kA`

Quadrature amplitude, specified as a vector of real number or
a complex number. Specify the units from the corresponding drop-down
list. The units are in volts for `Ideal Voltage` and
amperes for `Ideal Current`.

### **Sinusoidal modulation frequency** — Modulation frequency `0` (default) | vector of real or complex numbers | `Hz` | `kHz` | `MHz` | `GHz`

Modulation frequency at each of the RF circuit carrier frequencies,
specified as a vector of real number or a complex number. Specify
the units from the corresponding drop-down list. Th

### **Time delay** — Time delay of modulation `0` (default) | vector of real | `s` | `ms` | `us` | `ns`

Time delay of modulation, specified as a vector of positive
numbers. Specify the units from the corresponding drop-down list.

### **Carrier frequencies** — Carrier frequencies `0` (default) | vector of real positive numbers | `Hz` | `kHz` | `MHz` | `GHz`

Carrier frequencies, specified as a vector of real positive
numbers. The elements in the carrier frequencies are combinations
of fundamental tones and corresponding harmonics in the Configuration block. The default value is `0` `Hz`.

### **Ground and hide negative terminals** — Ground RF circuit terminals `on` (default) | `off`

Select this parameter to ground and hide the negative terminals.
To expose the negative terminals, clear the parameter. By exposing
these terminals, you can connect them to other parts of your model.

By default, this option is selected.

## Libraries

RF Blockset / Circuit Envelope / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2010b**

### R2021b: Sinusoid block icon updated

Starting in R2021b, the Sinusoid block icon is now updated. When
you open a model created before R2021b containing a Sinusoid block,
the software replaces the block icon with the R2021b version.

## Description

Model DC offset and sinusoidal modulation

The Sinusoid block implements a voltage or current
source that provides a DC offset and sine wave modulation. This block
can be used with each listed block carrier in the circuit envelope
environment.

The block implements the following voltage (or current) relationships
for the in-phase (*ui*), and
quadrature (*uq*), components
of the *k*th listed block
carrier:

uk,i(t)=Di+Aisin(wk(t−τ))uk,q(t)=Dq+Aqsin(wk(t−τ))

where:

- *Di* and *Dq* are
  DC offsets.
- *Ai* and *Aq* are
  in-phase and quadrature amplitudes.
- *τ* is the time delay.
- *ωk* is
  the specified modulation frequency at a given carrier frequency *fk*.
- *t*  is the time.

**Note**

Sinusoid block does not support frame-based processing (supported
by the Configuration blocks) as it uses SL Sine
wave block. This block errors if the **Samples per frame** is more
than 1 in the configuration block.

Sinusoid block mask icons are dynamic and show the current type of
source. This table shows you how the icons on this block vary based on the type of
source you set on the **Source type** parameter on the
block.

| Source type: `Ideal voltage` | Source type: `Ideal current` |
| --- | --- |
| Sinusoid block icon with Source type is set to Ideal voltage. | Sinusoid block icon with Source type is set to Ideal current. |
