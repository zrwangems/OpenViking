---
type: simulink-block
title: 'Fuse'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers'
documentation_page: 'fuse'
documentation_source_path: 'ref/fuse.html'
language: en
---

# Fuse

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the fuse positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the fuse negative terminal.
### Output

### **x** — Fuse state physical signal

Outputs the fuse state as a unitless physical signal. The port outputs
0 if the fuse is intact, and 1 if the fuse is blown.

#### Dependencies

Exposed when the **PS output for fuse state**
parameter is set to `Visible`.

## Parameters

### **Parameterization** — Model dependence of opening time on current `Opening time is independent of current` (default) | `Opening time depends on I^2*t` | `Opening time is tabulated`

Select whether opening time depends on current:

- `Opening time is independent of current`
  — The fuse opens when the current through the fuse exceeds
  the threshold current continuously for longer than the specified
  amount of time.
- `Opening time depends on I^2*t` —
  Makes fuse opening dependent on the energy dissipated in the fuse.
  Use this option for high-current range of operation.
- `Opening time is tabulated` —
  Makes fuse opening dependent on the average time-current tabulated
  data. Use this option for small currents.

### **Rated current, I\_rated** — Nominal operating current 1 A (default)

The fuse rating from the datasheet, or nominal operating current.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Opening time is independent of current`
or `Opening time depends on I^2*t`.

### **Ratio of minimum melting current to rated current, I\_melt/I\_rated** — Defined threshold current for melting 1 (default)

Minimum melting current defines the fuse operating threshold. If the
current through the fuse does not exceed this threshold, the fuse stays in
low-ohmic state. With the default parameter value, `1`, the
threshold current is the same as the rated current. In most cases, this
parameter value should be greater than 1. You can also set it to a value
less than 1, for situations where the fuse may blow at a current level below
the rated current (for example, due to high temperature, or due to
repetitive pulses). The parameter value must be greater than 0.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Opening time is independent of current`
or `Opening time depends on I^2*t`.

### **Time to fuse** — Time needed for the fuse to blow 0 s (default)

The amount of time needed for the fuse to blow. If the current through the
fuse exceeds the threshold current continuously for longer than this amount
of time, the fuse enters the high-ohmic state and breaks the circuit. If the
current falls below the threshold before the time elapsed, the fuse stays in
the low-ohmic state. If the current exceeds the threshold again, the time
counter restarts. With the default parameter value, `0`,
the fuse blows immediately as soon as the current exceeds the minimum
melting current. The parameter value must be greater than or equal to 0.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Opening time is independent of
current`.

### **Nominal melting, I^2\*t** — Dissipated energy needed for the fuse to blow 1 s\*A^2 (default)

The amount of energy dissipated in the fuse that is needed for the fuse to
blow. This is the nominal melting, or I2t, parameter from the datasheet. The
value must be greater than or equal to 0.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Opening time depends on I^2*t`.

### **Tabulated currents** — Currents data from the time-current curves [1.9, 2, 2.5, 30] A (default)

The tabulated current values from a time-current curve on the manufacturer
datasheet. Every element in this vector must be greater than 0, and the
vector must be strictly ascending.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Opening time is tabulated`.

### **Tabulated opening times** — Times data from the time-current curves [10000, 1, 0.3, 0.001] s (default)

The tabulated time values from a time-current curve on the manufacturer
datasheet. Every element in this vector must be greater than or equal to 0,
and the vector must be strictly descending. The vector must be of the same
size as the **Tabulated currents** vector.

#### Dependencies

Enabled when the **Parameterization** parameter is
set to `Opening time is tabulated`.

### **Fuse resistance R** — Resistance of the fuse 0.01 Ω (default)

The fuse resistance in low-ohmic state. The parameter value must be
greater than 0.

### **Open-circuit conductance G** — Open-circuit fuse conductance 1e-8 1/Ω (default)

The open-circuit fuse conductance in high-ohmic state, when the fuse has
blown. The parameter value must be greater than 0.

### **PS output for fuse state** — Controls the visibility of the output port for fuse state `Hidden` (default) | `Visible`

When set to `Visible`, a PS output port
**x** appears on the block icon. The port outputs 0 if
the fuse is intact, and 1 if the fuse is blown.

## Libraries

Simscape / Electrical / Switches & Breakers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008b**

## Description

Fuse that protects against excessive current

The Fuse block breaks the circuit, to protect it
against excessive current. The block provides the following modeling options:

- `Opening time is independent of current` — The
  fuse opens when the current through the fuse exceeds the threshold current
  continuously for longer than the specified amount of time. This option assumes
  that the time to open is independent of the current. It also implicitly assumes
  that heat in the fuse is instantaneously dissipated once the current drops below
  a certain threshold.
- `Opening time depends on I^2*t` — Makes fuse
  opening dependent on the energy dissipated in the fuse. The nominal melting
  value (I^2\*t) is usually available on manufacturer datasheets. If you select
  this option, the fuse blows when:

  ∫toverti2dt≥I2t

  where *t*over is the time when the
  current crosses over the threshold current, *i* is
  instantaneous current through the fuse, and *I2t* is the
  nominal melting value from the datasheet. Use this option for high-current range
  of operation.
- `Opening time is tabulated` — Makes fuse
  opening dependent on the average time-current tabulated data. This data
  indicates the time that it takes for the fuse to open given a certain current,
  and is available on manufacturer datasheets as time-current curves.

  For example, these are the time-current curves from a
  Littelfuse® 218 Series fuse datasheet.

  Select the appropriate curve and enter the corresponding current and time
  values into the **Tabulated currents** and **Tabulated
  opening time** parameter vectors, respectively. Use this option for
  small currents.
