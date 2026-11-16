---
type: simulink-block
title: 'Diode'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Elements'
documentation_page: 'diode'
documentation_source_path: 'ref/diode.html'
language: en
---

# Diode

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the diode positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the diode negative terminal.

## Parameters

### **Forward voltage** — Minimum voltage for forward-biased diode `0.6 V` (default) | positive scalar

Minimum voltage that needs to be applied for the diode to become forward biased.

### **On resistance** — Resistance of forward-biased diode `0.3 Ohm` (default) | positive scalar

The resistance of the forward-biased diode.

### **Off conductance** — Conductance of reverse-biased diode `1e-8 1/Ohm` (default) | positive scalar

The conductance of the reverse-biased diode.

## Libraries

Simscape / Foundation Library / Electrical / Electrical Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2023b: Reduced chattering near forward voltage

The block equations have been enhanced to reduce zero-crossings when the diode operates
near the forward voltage.

In previous releases, the diode used

```
if v > Vf
```

as the switching condition between the on and off states. Starting with R2023b, the
switching condition has been modified to include a resistance for zero-crossing detection,
*Rzc*:

```
if v + i*Rzc < Vf + Vf*Goff*Rzc
    % Off
      i == v*Goff;
    else
    % On
       v == i*Ron + Vf*(1-Ron*Goff);
```

The new switching condition provides improved on-to-off and off-to-on characteristics
when the diode operates near the forward voltage.

## Description

Piecewise linear diode in electrical systems

The Diode block models a piecewise linear diode. If the
voltage across the diode is bigger than the **Forward voltage** parameter
value, then the diode behaves like a linear resistor with low resistance, given by the
**On resistance** parameter value, plus a constant series voltage source.
If the voltage across the diode is less than the forward voltage, then the diode behaves like
a linear resistor with low conductance given by the **Off conductance**
parameter value.

Diode current plot

When forward biased, the diode behavior is described with the equations:

v=i⋅Ron+Vsource,Vsource=Vf(1−RonGoff),

where:

- *v* is the voltage.
- *i* is the current.
- *V*source is the voltage of the series voltage
  source.
- *V*f is the forward voltage.
- *R*on is the resistance of the forward-biased
  diode.
- *G*off is the conductance of the
  reverse-biased diode.

The reverse behavior is given by*v =
i/Goff*.

The
*Ron.Goff*
term ensures that there is no discontinuity in the diode current when the diode is switching
between the on and off states.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
