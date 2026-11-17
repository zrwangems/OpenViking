---
type: simulink-block
title: 'PNP Bipolar Transistor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'pnpbipolartransistor'
documentation_source_path: 'ref/pnpbipolartransistor.html'
language: en
---

# PNP Bipolar Transistor

## Ports
```yaml
ports:
- name: B
  summary: Base terminal electrical
  direction: conserving
- name: C
  summary: Collector terminal electrical
  direction: conserving
- name: E
  summary: Emitter terminal electrical
  direction: conserving
- name: H
  summary: Thermal port thermal
  direction: conserving
```

### Conserving

### **B** — Base terminal electrical

Electrical conserving port associated with the transistor base
terminal.

The base terminal is the control terminal that modulates the current
flow between the emitter and the collector.

### **C** — Collector terminal electrical

Electrical conserving port associated with the transistor collector
terminal.

The collector terminal is the terminal through which the main current
flows from the emitter to the collector when the transistor is on. The
collector terminal typically connects to a lower voltage relative to the
emitter.

### **E** — Emitter terminal electrical

Electrical conserving port associated with the transistor emitter
terminal.

The emitter terminal is the terminal through which the current enters
the transistor. The emitter usually connects to a positive
voltage.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to enable thermal port No thermal port (default) | Show thermal port
  group: ''
- name: Parameterization
  summary: Block parameterization Specify from a datasheet (default) | Specify using equation parameters directly
  group: Main
- name: Forward current transfer ratio h_fe
  summary: Forward current transfer ratio 100 (default)
  group: Main
- name: Output admittance h_oe
  summary: Output admittance 50e-6 1/Ohm (default)
  group: Main
- name: Collector current at which h-parameters are defined
  summary: Collector current at which h-parameters are defined -1 mA (default)
  group: Main
- name: Collector-emitter voltage at which h-parameters are defined
  summary: Collector-emitter voltage at which h-parameters are defined -5 V (default)
  group: Main
- name: Voltage Vbe
  summary: Voltage Vbe -0.55 V (default)
  group: Main
- name: Current Ib for voltage Vbe
  summary: Current Ib for voltage Vbe -0.5 mA (default)
  group: Main
- name: Forward current transfer ratio BF
  summary: Forward current transfer ratio 100 (default)
  group: Main
- name: Saturation current IS
  summary: Saturation current 1e-14 A (default)
  group: Main
- name: Forward Early voltage VAF
  summary: Forward Early voltage 200 V (default)
  group: Main
- name: Reverse current transfer ratio BR
  summary: Reverse current transfer ratio 1 (default)
  group: Main
- name: Measurement temperature
  summary: Measurement temperature 25 degC (default)
  group: Main
- name: Collector resistance RC
  summary: Collector resistance 0.01 ohm (default)
  group: Ohmic Resistance
- name: Emitter resistance RE
  summary: Emitter resistance 1e-4 Ohm (default)
  group: Ohmic Resistance
- name: Zero bias base resistance RB
  summary: Zero bias base resistance 1 Ohm (default)
  group: Ohmic Resistance
- name: Base-collector junction capacitance
  summary: Base-collector junction capacitance 5 pF (default)
  group: Capacitance
- name: Base-emitter junction capacitance
  summary: Base-emitter junction capacitance 5 pF (default)
  group: Capacitance
- name: Total forward transit time
  summary: Total forward transit time 0 us (default)
  group: Capacitance
- name: Total reverse transit time
  summary: Total reverse transit time 0 us (default)
  group: Capacitance
- name: Parameterization
  summary: Temperature dependence parameterization None — Simulate at parameter measurement temperature (default) | Model
    temperature dependence
  group: Temperature Dependence
- name: Forward current transfer ratio, h_fe, at second measurement temperature
  summary: Forward current transfer ratio, h_fe, at second measurement temperature 125 (default)
  group: Temperature Dependence
- name: Voltage Vbe at second measurement temperature
  summary: Voltage Vbe at second measurement temperature -0.45 V (default)
  group: Temperature Dependence
- name: Current Ib for voltage Vbe at second measurement temperature
  summary: Current Ib for voltage Vbe at second measurement temperature -0.5 mA (default)
  group: Temperature Dependence
- name: Second measurement temperature
  summary: Second measurement temperature 125 degC (default)
  group: Temperature Dependence
- name: Current gain temperature coefficient, XTB
  summary: Current gain temperature coefficient 0 (default)
  group: Temperature Dependence
- name: Energy gap, EG
  summary: Energy gap 1.11 eV (default)
  group: Temperature Dependence
- name: Saturation current temperature exponent, XTI
  summary: Saturation current temperature exponent 3 (default)
  group: Temperature Dependence
- name: Device simulation temperature
  summary: Device simulation temperature 25 degC (default)
  group: Temperature Dependence
```

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model the effects of generated heat and device temperature.

### Main

### **Parameterization** — Block parameterization `Specify from a datasheet` (default) | `Specify using equation parameters directly`

Select one of the following methods for block parameterization:

- `Specify from a datasheet`
  — Provide parameters that the block converts to
  equations that describe the transistor. The block calculates
  the forward Early voltage *VAF* as
  *Ic/h\_oe*, where
  *Ic* is the **Collector
  current at which h-parameters are defined**
  parameter value, and *h\_oe* is the
  **Output admittance h\_oe** parameter
  value [2]. The block sets *BF* to the
  small-signal **Forward current transfer ratio
  h\_fe** value. The block calculates the
  saturation current *IS* from the
  specified **Voltage Vbe** value and the
  corresponding **Current Ib for voltage
  Vbe** value when *Ic* is
  zero. This is the default method.
- `Specify using equation parameters
  directly` — Provide equation
  parameters *IS*, *BF*,
  and *VAF*.

### **Forward current transfer ratio h\_fe** — Forward current transfer ratio `100` (default)

Small-signal current gain.

#### Dependencies

This parameter is visible only when you select
`Specify from a datasheet` for the
**Parameterization** parameter.

### **Output admittance h\_oe** — Output admittance `50e-6` `1/Ohm` (default)

Derivative of the collector current with respect to the
collector-emitter voltage for a fixed base current.

#### Dependencies

This parameter is visible only when you select
`Specify from a datasheet` for the
**Parameterization** parameter.

### **Collector current at which h-parameters are defined** — Collector current at which h-parameters are defined `-1` `mA` (default)

The h-parameters vary with operating point, and are defined for this
value of the collector current.

#### Dependencies

This parameter is visible only when you select
`Specify from a datasheet` for the
**Parameterization** parameter.

### **Collector-emitter voltage at which h-parameters are defined** — Collector-emitter voltage at which h-parameters are defined `-5` `V` (default)

The h-parameters vary with operating point, and are defined for this
value of the collector-emitter voltage.

#### Dependencies

This parameter is visible only when you select
`Specify from a datasheet` for the
**Parameterization** parameter.

### **Voltage Vbe** — Voltage Vbe `-0.55` `V` (default)

Base-emitter voltage when the base current is *Ib*.
The [ *Vbe*
*Ib* ] data pair must be quoted for when the transistor
is in the normal active region, that is, not in the saturated
region.

#### Dependencies

This parameter is visible only when you select
`Specify from a datasheet` for the
**Parameterization** parameter.

### **Current Ib for voltage Vbe** — Current Ib for voltage Vbe `-0.5` `mA` (default)

Base current when the base-emitter voltage is *Vbe*.
The [ *Vbe*
*Ib* ] data pair must be quoted for when the transistor
is in the normal active region, that is, not in the saturated
region.

#### Dependencies

This parameter is visible only when you select
`Specify from a datasheet` for the
**Parameterization** parameter.

### **Forward current transfer ratio BF** — Forward current transfer ratio `100` (default)

Ideal maximum forward current gain.

#### Dependencies

This parameter is visible only when you select
`Specify using equation parameters
directly` for the
**Parameterization** parameter.

### **Saturation current IS** — Saturation current `1e-14` `A` (default)

Magnitude of the current that the p-n junction approaches
asymptotically for very large reverse bias levels.

#### Dependencies

This parameter is visible only when you select
`Specify using equation parameters
directly` for the
**Parameterization** parameter.

### **Forward Early voltage VAF** — Forward Early voltage `200` `V` (default)

In the standard Ebers-Moll equations, the gradient of the
*Ic* versus *Vce* curve is zero in
the normal active region. The additional forward Early voltage term
increases this gradient. The intercept on the
*Vce*-axis is equal to –*VAF* when
the linear region is extrapolated.

#### Dependencies

This parameter is visible only when you select
`Specify using equation parameters
directly` for the
**Parameterization** parameter.

### **Reverse current transfer ratio BR** — Reverse current transfer ratio `1` (default)

Ideal maximum reverse current gain. This value is often not quoted in
manufacturer datasheets because it is not significant when the
transistor is biased to operate in the normal active region. When the
value is not known and the transistor is not to be operated on the
inverse region, use the default value of `1`.

### **Measurement temperature** — Measurement temperature `25` `degC` (default)

Temperature *T*m1 at which
*Vbe* and *Ib*, or
*IS*, are measured.

### Ohmic Resistance

### **Collector resistance RC** — Collector resistance `0.01` `ohm` (default)

Resistance at the collector.

### **Emitter resistance RE** — Emitter resistance `1e-4` `Ohm` (default)

Resistance at the emitter.

### **Zero bias base resistance RB** — Zero bias base resistance `1` `Ohm` (default)

Resistance at the base at zero bias.

### Capacitance

### **Base-collector junction capacitance** — Base-collector junction capacitance `5` `pF` (default)

Parasitic capacitance across the base-collector junction.

### **Base-emitter junction capacitance** — Base-emitter junction capacitance `5` `pF` (default)

Parasitic capacitance across the base-emitter junction.

### **Total forward transit time** — Total forward transit time `0` `us` (default)

Represents the mean time for the minority carriers to cross the base
region from the emitter to the collector, and is often denoted by the
parameter TF [1].

### **Total reverse transit time** — Total reverse transit time `0` `us` (default)

Represents the mean time for the minority carriers to cross the base
region from the collector to the emitter, and is often denoted by the
parameter TR [1].

### Temperature Dependence

### **Parameterization** — Temperature dependence parameterization `None — Simulate at parameter measurement temperature` (default) | `Model temperature dependence`

Select one of the following methods for temperature dependence parameterization:

- `None — Simulate at parameter
  measurement temperature` —
  Temperature dependence is not modeled, or the model is
  simulated at the measurement temperature
  *T*m1 (as
  specified by the **Measurement
  temperature** parameter on the
  **Main** tab). This is the default
  method.
- `Model temperature dependence`
  — Provide a value for simulation temperature, to
  model temperature-dependent effects. You also have to
  provide a set of additional parameters depending on the
  block parameterization method. If you parameterize the block
  from a datasheet, you have to provide values for a second [
  *Vbe*
  *Ib* ] data pair and
  *h\_fe* at second measurement
  temperature. If you parameterize by directly specifying
  equation parameters, you have to provide the values for
  *XTI*, *EG*, and
  *XTB*.

### **Forward current transfer ratio, h\_fe, at second measurement temperature** — Forward current transfer ratio, h\_fe, at second measurement temperature `125` (default)

Small-signal current gain at second measurement temperature. It must
be quoted at the same collector-emitter voltage and collector current as
for the **Forward current transfer ratio h\_fe**
parameter on the **Main** tab.

#### Dependencies

This parameter is visible only when you select
`Specify from a datasheet` for the
**Parameterization** parameter on the
**Main** tab.

### **Voltage Vbe at second measurement temperature** — Voltage Vbe at second measurement temperature `-0.45` `V` (default)

Base-emitter voltage when the base current is *Ib*
and the temperature is set to the second measurement temperature. The
[*Vbe*
*Ib*] data pair must be quoted for when the transistor
is in the normal active region, that is, not in the saturated
region.

#### Dependencies

This parameter is visible only when you select
`Specify from a datasheet` for the
**Parameterization** parameter on the
**Main** tab.

### **Current Ib for voltage Vbe at second measurement temperature** — Current Ib for voltage Vbe at second measurement temperature `-0.5` `mA` (default)

Base current when the base-emitter voltage is *Vbe*
and the temperature is set to the second measurement temperature. The [
*Vbe*
*Ib* ] data pair must be quoted for when the transistor
is in the normal active region, that is, not in the saturated
region.

#### Dependencies

This parameter is visible only when you select
`Specify from a datasheet` for the
**Parameterization** parameter on the
**Main** tab.

### **Second measurement temperature** — Second measurement temperature `125` `degC` (default)

Second temperature *T*m2 at
which *h\_fe*,*Vbe*, and
*Ib* are measured.

#### Dependencies

This parameter is visible only when you select
`Specify from a datasheet` for the
**Parameterization** parameter on the
**Main** tab.

### **Current gain temperature coefficient, XTB** — Current gain temperature coefficient `0` (default)

Current gain temperature coefficient value.

#### Dependencies

This parameter is visible only when you select
`Specify using equation parameters
directly` for the
**Parameterization** parameter on the
**Main** tab.

### **Energy gap, EG** — Energy gap `1.11` `eV` (default)

Energy gap value.

#### Dependencies

This parameter is visible only when you select
`Specify using equation parameters
directly` for the
**Parameterization** parameter on the
**Main** tab.

### **Saturation current temperature exponent, XTI** — Saturation current temperature exponent `3` (default)

Saturation current temperature coefficient value.

#### Dependencies

This parameter is visible only when you select
`Specify using equation parameters
directly` for the
**Parameterization** parameter on the
**Main** tab.

### **Device simulation temperature** — Device simulation temperature `25` `degC` (default)

Temperature *T*s at which the
device is simulated.
## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

### R2024a: **Base-collector capacitance voltage** and **Base-emitter capacitance voltage** variables replaced with **Base-collector charge** and **Base-emitter charge** variables

You now specify **Initial Targets** and **Nominal
Values** for capacitance and charge modeling using the
**Base-collector charge** and **Base-emitter
charge** variables. The **Base-collector capacitance
voltage** and **Base-emitter capacitance voltage**
variables have been removed.

If a model you created in an earlier release specifies **Initial
Targets** or **Nominal Values** for the
**Base-collector capacitance voltage** or
**Base-emitter capacitance voltage** variables, you must update
the model. For more information on how to calculate base-collector charge and
base-emitter charge, see Modeling Capacitance and Charge.

### R2019b: Thermal network simlog paths

From R2019b forward, it is possible to model the thermal network of this block
either internally or externally.

As a result, the simlog paths corresponding to the thermal network have changed.
If you have a script that programmatically access the simlog, you have to manually
update it to reflect these changes.

## Description

PNP bipolar transistor using enhanced Ebers-Moll equations

The PNP Bipolar Transistor block uses a variant of the
Ebers-Moll equations to represent an PNP bipolar transistor. The Ebers-Moll equations
are based on two exponential diodes plus two current-controlled current sources. The
PNP Bipolar Transistor block provides these
enhancements to that model:

- Early voltage effect
- Optional base, collector, and emitter resistances
- Optional fixed base-emitter and base-collector capacitances

The collector and base currents are [1]:

IC=−IS[(e−qVBE/(kTm1)−e−qVBC/(kTm1))(1+VBCVA)−1βR(e−qVBC/(kTm1)−1)]IB=−IS[1βF(e−qVBE/(kTm1)−1)+1βR(e−qVBC/(kTm1)−1)]

In these equations:

- *IB* and
  *IC* are base and
  collector currents, defined as positive into the device.
- *IS* is the value of the **Saturation current
  IS** parameter.
- *VBE* is the base-emitter voltage
  and *VBC* is the base-collector
  voltage.
- *βF* is the value of the
  **Forward current transfer ratio BF parameter**
  parameter. This term represents the ideal maximum forward current
  gain.
- *βR* is the value of the
  **Reverse current transfer ratio BR parameter**
  parameter. This term represents the ideal maximum reverse current
  gain.
- *VA* is the value of the
  **Forward Early voltage VAF** parameter.
- *q* is the elementary charge on an electron
  (1.602176e-19 Coulombs).
- *k* is the Boltzmann constant (1.3806503e-23
  J/K).
- *T*m1 is the transistor
  temperature, as defined by the **Measurement temperature**
  parameter value.

You can specify the transistor behavior using datasheet parameters that the block uses
to calculate the parameters for these equations, or you can specify the equation
parameters directly.

If –*q**V*BC /
(*k**T*m1) >
40 or –*q**V*BE /
(*k**T*m1) >
40, the corresponding exponential terms in the equations are replaced
with (–*q**V*BC /
(*k**T*m1) –
39)*e*40 and (–*q**V*BE /
(*k**T*m1) –
39)*e*40, respectively. This helps prevent numerical issues associated with the
steep gradient of the exponential function *e*x at large values of *x*. Similarly, if –*q**V*BC /
(*k**T*m1) <
–39 or –*q**V*BE /
(*k**T*m1) <
–39 then the corresponding exponential terms in the equations are replaced
with (–*q**V*BC /
(*k**T*m1) +
40)*e*–39 and (–*q**V*BE /
(*k**T*m1) +
40)*e*–39, respectively.

Optionally, you can specify fixed capacitances across the base-emitter and
base-collector junctions. You also have the option to specify base, collector, and
emitter connection resistances.

### Modeling Capacitance and Charge

You model capacitance and charge using the **Base-collector junction
capacitance** and **Base-emitter junction
capacitance** parameters. You can also represent reverse recovery
charge and dynamics using the **Total forward transit time** and
**Total reverse transit time** parameters. This equation
defines the base-collector charge,

QBC=tRICE+CBCVBC,

where:

- *t*R is the **Total
  reverse transit time** parameter value.
- *I*CE is the collector-emitter
  current.
- *C*BC is the
  **Base-collector junction capacitance**  parameter
  value.
- *V*BC is the base-collector
  voltage.

This equation defines the base-collector charge and capacitor
current,

IQBC=dQBCdt.

This equation defines base-emitter charge,

QBE=tFIC+CBEVBE,

where:

- *t*F is the **Total
  forward transit time** parameter value.
- *I*C is the collector
  current.
- *C*BE is the
  **Base-emitter junction capacitance**  parameter
  value.
- *V*BE is the base-emitter
  voltage.

This equation defines the base-emitter charge and capacitor current,

IQBE=dQBEdt.

### Modeling Temperature Dependence

The default behavior is that dependence on temperature is not modeled, and the
device is simulated at the temperature for which you provide block parameters. You
can optionally include modeling the dependence of the transistor static behavior on
temperature during simulation. Temperature dependence of the junction capacitances
is not modeled, this being a much smaller effect.

When including temperature dependence, the transistor defining equations remain
the same. The measurement temperature value,
*T*m1, is replaced with the simulation
temperature, *T*s. The saturation current,
*IS*, and the forward and reverse gains
(*βF* and
*βR*) become a function of
temperature according to these equations:

ISTs=ISTm1⋅(Ts/Tm1)XTI⋅exp(−EGkTs(1−Ts/Tm1))

βFs=βFm1(TsTm1)XTB

βRs=βRm1(TsTm1)XTB

where:

- *T*m1 is the temperature at
  which the transistor parameters are specified, as defined by the
  **Measurement temperature** parameter value.
- *T*s is the simulation
  temperature.
- *IS*Tm1 is the saturation
  current at the measurement temperature.
- *IS*Ts is the saturation
  current at the simulation temperature. This is the saturation current
  value used in the bipolar transistor equations when temperature
  dependence is modeled.
- *β*Fm1 and
  *β*Rm1 are the forward and
  reverse gains at the measurement temperature.
- *β*Fs and
  *β*Rs are the forward and
  reverse gains at the simulation temperature. These are the values used
  in the bipolar transistor equations when temperature dependence is
  modeled.
- *EG* is the energy gap for the semiconductor type
  measured in Joules. The value for silicon is usually taken to be 1.11
  eV, where 1 eV is 1.602e-19 Joules.
- *XTI* is the saturation current temperature exponent.
- *XTB* is the forward and reverse gain temperature
  coefficient.
- *k* is the Boltzmann constant (1.3806503e–23
  J/K).

Appropriate values for *XTI* and *EG* depend on
the type of transistor and the semiconductor material used. In practice, the values
of *XTI*, *EG*, and *XTB* need
tuning to model the exact behavior of a particular transistor. Some manufacturers
quote these tuned values in a SPICE Netlist, and you can read off the appropriate
values. Otherwise you can determine values for *XTI*,
*EG*, and *XTB* by using a datasheet-defined
data at a higher temperature *T*m2. The
block provides a datasheet parameterization option for this.

You can also tune the values of *XTI*, *EG*, and
*XTB* yourself, to match lab data for your particular device.
You can use Simulink®
Design Optimization™ software to help tune the values.

### Thermal Port

You can expose the thermal port to model the effects of generated heat and device
temperature. To expose the thermal port, set the **Modeling option**
parameter to either:

- `No thermal port` — The block does not contain a
  thermal port and does not simulate heat generation in the device.
- `Show thermal port` — The block contains a thermal
  port that allows you to model the heat that conduction losses generate. For
  numerical efficiency, the thermal state does not affect the electrical behavior
  of the block.

For more information on using thermal ports and on the **Thermal Port**
parameters, see Simulating Thermal Effects in Semiconductors.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

**Note**

To satisfy all your initial targets, do not set the priority to
`High` for more initial targets than the total number of
differential variables in the block equations. If you set the **Base-collector
junction capacitance** or **Total reverse transit time**
parameter to a nonzero value and set the **Base-emitter junction
capacitance** or **Total forward transit time** parameter to a
nonzero value, the number of differential variables in the block equations is two. Choose
one of these options:

- To set the terminal current initial condition, in the **Initial
  Targets** section, set the priority of only the **Base
  current** and **Collector current** variables to
  `High`.
- To set the terminal voltage initial condition, in the **Initial
  Targets** section, set the priority of only the
  **Collector-emitter voltage** and **Base-emitter
  voltage** variables to `High`.
- To set the total charge initial condition,
  in the **Initial Targets** section, set the priority of only
  the **Base-collector charge** and **Base-emitter
  charge** variables to `High`. *(since R2024a)*

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

### Plot Basic I-V Characteristics

You can plot the basic I-V characteristics of the PNP Bipolar Transistor block without building a
complete model. Use the plots to explore the impact of your
parameter choices on device characteristics. If you parameterize the
block from a data sheet, you can compare your plots to the data
sheet to check that you parameterized the block correctly. If you
have a complete working model but do not know which manufactured
part to use, you can compare your plots to data sheets to help you
decide.

To enable this option, set the **Modeling option** parameter of the
PNP Bipolar Transistor block to `No thermal port`. To plot the basic
characteristics, right-click the block and select **Electrical** >
**Basic characteristics** from the context menu. For more
information about the **Basic characteristics** option, see Plot Basic I-V Characteristics of Semiconductor Blocks.
