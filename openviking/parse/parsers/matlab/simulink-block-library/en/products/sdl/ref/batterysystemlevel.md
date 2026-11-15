---
type: simulink-block
title: 'Battery (System-Level)'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'batterysystemlevel'
documentation_source_path: 'ref/batterysystemlevel.html'
language: en
---

# Battery (System-Level)

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive battery
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative battery
terminal.

### **H** — Heat transfer thermal

Thermal conserving port associated with heat transfer.

#### Dependencies

To expose this port, set **Thermal port** to
`Model`.

## Parameters

### Main

### **Nominal voltage, Vnom** — Output voltage when battery is fully charged `12` `V` (default) | positive scalar

No-load voltage across the battery when it is fully charged.

### **Internal resistance** — Battery internal resistance `2` `Ohm` (default) | positive scalar

Internal connection resistance of the battery.

### **Battery charge capacity** — Option to simulate discharge `Infinite` (default) | `Finite`

Option to simulate finite or infinite battery charge capacity.

### **Cell capacity (Ah rating)** — Rated battery capacity `50` `A*hr` (default) | positive scalar

Maximum battery charge. Ampere-hours refer to the number of hours that
the battery can discharge 1 Amp. You can specify an initial charge
target as a variable.

#### Dependencies

To enable this parameter, set **Battery charge
capacity** to `Finite`.

### **Voltage V1 when charge is AH1** — Output voltage at charge level AH1 `11.5` `V` (default) | positive scalar

Fundamental battery output voltage when the charge level is equal to
the **Charge AH1 when no-load voltage is V1**.

#### Dependencies

To enable this parameter, set **Battery charge
capacity** to `Finite`.

### **Charge AH1 when no-load voltage is V1** — Charge level when no-load output voltage is V1 `25` `A*hr` (default) | positive scalar

Battery charge level corresponding to the no-load output voltage you
specify for the **Voltage V1 when charge is AH1**
parameter.

#### Dependencies

To enable this parameter, set **Battery charge
capacity** to `Finite`.

### **Self-discharge** — Option to simulate self-discharge resistance `Disabled` (default) | `Enabled`

Option to simulate self-discharge resistance. The block simulates this
effect as a resistor across the terminals of the battery.

#### Dependencies

To enable this parameter, set **Battery charge
capacity** to `Finite`.

### **Self-discharge resistance** — Resistance that represents battery self-discharge `2000` `Ohm` (default) | positive scalar

Resistance across the battery terminals that represents
self-discharge.

#### Dependencies

To enable this parameter, set **Battery charge
capacity** to `Finite` and
**Self-discharge** to
`Enabled`.

### Thermal Port

### **Thermal port** — Option to simulate thermal effects `Omit` (default) | `Model`

Option to expose the thermal port and include thermal effects in your
model.

### **Thermal mass** — Thermal mass of battery `30000` `J/K` (default)

Thermal energy required to change the component temperature by a
single degree. The greater the thermal mass, the more resistant the
component is to temperature change.

## Libraries

Simscape / Driveline / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Generic system level battery

The Battery (System-Level) block represents a generic
self-discharging battery. You can use the block to model hybrid and battery electric
drives at a medium-level fidelity for drive cycle analysis. The block is a simplified
version of the Battery (Simscape Electrical) block and uses the same
parameters, where applicable. This will aid your transition to a higher fidelity model,
if necessary. The Battery (System-Level) does not support
battery fade, aging, dynamics, or temperature dependent properties. You can access these
features using the Battery (Simscape Electrical) block.

You can choose to simulate a battery with finite or infinite charge. The block can also help
you to determine how decreased voltage affects performance and control requirements. To
learn more about observing battery performance, see Plot Basic Voltage-Charge Characteristics of Battery Blocks (Simscape Electrical).

### Battery Model

When you set **Battery charge capacity** to
`Infinite`, the block treats the battery like a
resistor and a constant voltage source in series. When you set **Battery
charge capacity** to `Finite`, the block
treats the battery like a resistor and a charge-dependent voltage source in series.
In this case, the voltage is a function of charge and has the following
relationship:

V=V0SOC1−β(1−SOC)

where:

- `SOC` (state-of-charge) is the ratio of current
  charge to rated battery capacity.
- *V*0 is the voltage when the
  battery is fully charged at no load, as defined by the **Nominal
  voltage, Vnom** parameter.
- *β* is a constant that is calculated so that the
  battery voltage is *V1* when the charge is
  *AH1*. Specify the voltage *V1*
  and ampere-hour rating *AH1* using block parameters.
  *AH1* is the charge when the no-load (open-circuit)
  voltage is *V1*, and *V1* is less than
  the nominal voltage.

The equation defines an approximate relationship between voltage and remaining
charge. This approximation replicates the increasing rate of voltage drop at low
charge values and ensures that the battery voltage becomes zero when the charge
level is zero. The advantage of this model is that it requires few parameters, which
are typically available on manufacturer datasheets.

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.

### Assumptions and Limitations

The block assumes that self-discharge resistance does not depend on the number of
discharge cycles.
