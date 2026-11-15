---
type: simulink-block
title: 'Variable Capacitor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Basic'
documentation_page: 'variablecapacitor'
documentation_source_path: 'ref/variablecapacitor.html'
language: en
---

# Variable Capacitor

## Ports

### Input

### **C** — Capacitance physical signal

Physical signal input port associated with the capacitance. C must be
finite and greater than zero
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the capacitor positive
voltage.

### **-** — Negative terminal electrical

Electrical conserving port associated with the capacitor negative
voltage.

## Parameters

### **Equation** — Equation for block capacitance `I = C*dV/dt` (default) | `I = C*dV/dt + dC/dt*V`

Select one of the following options for block capacitance:

- `I = C*dV/dt` — This equation
  assumes the capacitance is defined as the local gradient of the
  charge-voltage curve for a given voltage. This option is the
  default.
- `I = C*dV/dt + dC/dt*V` — This
  equation assumes the capacitance is defined as the ratio of the
  charge to the steady-state voltage.

### **Minimum capacitance C>0** — Minimum capacitance `1e-9` `F` (default)

The lower limit on the value of the signal at port C. This limit prevents
the signal from reaching a value that has no physical meaning. The default
value is `1e-09` F.

### **Series resistance** — Series resistance `1e-6` `Ohm` (default)

The value of the resistance placed in series with the variable capacitor.
The default value is `1e-06` Ohm.

### **Initial voltage** — Initial output voltage `0` `V` (default)

The output voltage at the start of the simulation.

#### Dependencies

This parameter is visible only when you select `I =
C*dV/dt` for the **Equation**
parameter.

### **Initial charge** — Initial charge `0` `C` (default)

The charge at the start of the simulation.

#### Dependencies

This parameter is visible only when you select `I =
C*dV/dt + dC/dt*V` for the
**Equation** parameter.

## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Linear time-varying capacitor

The Variable Capacitor block represents a linear
time-varying capacitor. The block provides two options for the relationship between the
current *i* through the capacitor and the voltage *v*
across the device when the capacitance at port **C** is
*C*. The **Equation** parameter determines which
of the following equations the block uses:

- i=Cdvdt

  Use the preceding equation when the capacitance is defined as the local
  gradient of the charge-voltage curve for a given voltage:

  C(v)=dQ(v)dv
- i=dCdtv+Cdvdt

  Use the preceding equation when the capacitance is defined as the ratio of
  the charge *Q* to the steady-state voltage:

  C(v)=Q(v)v

The block includes a resistor in series with the variable capacitor. You can use this
resistor to represent the total ohmic connection resistance of the capacitor. You may
need to use this resistor to prevent numerical issues for some circuit topologies, such
as where a Variable Capacitor block is connected in
parallel with another capacitor block that does not have a series resistance.
