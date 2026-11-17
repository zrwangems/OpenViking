---
type: simulink-block
title: 'Thyristor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'thyristor'
documentation_source_path: 'ref/thyristor.html'
language: en
---

# Thyristor

## Ports
```yaml
ports:
- name: G
  summary: Gate port electrical
  direction: conserving
- name: A
  summary: Anode port electrical
  direction: conserving
- name: K
  summary: Cathode port electrical
  direction: conserving
- name: H
  summary: Thermal port thermal
  direction: conserving
```

### Conserving

### **G** — Gate port electrical

Electrical conserving port associated with the gate.

### **A** — Anode port electrical

Electrical conserving port associated with the anode.

### **K** — Cathode port electrical

Electrical conserving port associated with the cathode.

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
- name: I-V characteristics defined by
  summary: Thyristor representation Fundamental nonlinear equations (default) | Lookup table
  group: Main
- name: On-state voltage, V_T
  summary: On-state Anode-Cathode static voltage 1.2 V (default)
  group: Main
- name: On-state current, I_T
  summary: On-state static load current 1 A (default)
  group: Main
- name: Vector of on-state voltages, V_T
  summary: Vector of on-state voltages [.75, 1, 1.25, 1.5, 1.75, 2, 2.25] V (default)
  group: Main
- name: Vector of corresponding currents, I_T
  summary: Vector of corresponding currents [.015, .22, .75, 1.4, 2, 2.75, 3.45] A (default)
  group: Main
- name: Off-state current, I_DRM
  summary: Off-state anode current 0.01 mA (default)
  group: Main
- name: Corresponding off-state voltage, V_DRM
  summary: Off-state anode-cathode voltage 400 V (default)
  group: Main
- name: Holding current
  summary: Holding current 1 mA (default)
  group: Main
- name: Measurement temperature
  summary: Device simulation temperature 25 degC (default)
  group: Main
- name: Gate trigger current, I_GT
  summary: Critical gate current 3 uA (default)
  group: Gate Triggering
- name: Corresponding gate voltage, V_GT
  summary: Gate-cathode voltage 0.6 V (default)
  group: Gate Triggering
- name: Test voltage, V_D
  summary: Test supply voltage 12 V (default)
  group: Gate Triggering
- name: Test load resistor
  summary: Test load resistor 120 Ohm (default)
  group: Gate Triggering
- name: Critical rate of rise of off-state voltage, dV/dt
  summary: Critical rate of rise of off-state voltage 150 V/us (default)
  group: dV/dt Triggering
- name: Test gate-cathode resistor, R_GK
  summary: Test gate-cathode resistor 1000 Ohm (default)
  group: dV/dt Triggering
- name: NPN device forward transit time parameterization
  summary: NPN device forward transit time parameterization Derive approximate value from gate-controlled turn-on time (default)
    | Specify directly
  group: Time Constants
- name: Gate-controlled turn-on time
  summary: Gate-controlled turn-on time 2 us (default)
  group: Time Constants
- name: Corresponding gate current
  summary: Test gate current 10 mA (default)
  group: Time Constants
- name: NPN device forward transit time
  summary: Mean forward transit time 0.3 us (default)
  group: Time Constants
- name: PNP device forward transit time parameterization
  summary: PNP device forward transit time parameterization Set equal to NPN device forward transit time (default) | Specify
    directly
  group: Time Constants
- name: PNP device forward transit time
  summary: Mean forward transit time 0.3 us (default)
  group: Time Constants
- name: Turn-on delay time
  summary: Time delay 0 s (default)
  group: Time Constants
- name: Gate current for turn-on delay time
  summary: Gate current for turn-on delay time 1 mA (default)
  group: Time Constants
- name: Turn-on rise time
  summary: Turn-on rise time 0 s (default)
  group: Time Constants
- name: Internal shunt resistor, Rs
  summary: Gate-Cathode shunt resistance 87 kOhm (default)
  group: Advanced
- name: Internal series gate resistor, Rg
  summary: Resistance associated with gate connection 10 Ohm (default)
  group: Advanced
- name: Product of NPN and PNP forward current gains
  summary: Product of NPN and PNP forward current gains 10 (default)
  group: Advanced
```

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model the effects of generated heat and device temperature.

### Main

### **I-V characteristics defined by** — Thyristor representation `Fundamental nonlinear equations` (default) | `Lookup table`

Represent the thyristor either by using an equivalent circuit based on
NPN and PNP bipolar transistors or use a lookup table approximation to
the on-state I-V curve.

### **On-state voltage, V\_T** — On-state Anode-Cathode static voltage `1.2` `V` (default)

The anode-cathode static voltage drop when in the on-state, and the
current flowing is equal to the on-state current
*IT*.

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by**
parameter.

### **On-state current, I\_T** — On-state static load current `1` `A` (default)

Static load (or equivalently anode) current that flows when the
anode-cathode voltage is equal to the on-state voltage
*VT*.

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by**
parameter.

### **Vector of on-state voltages, V\_T** — Vector of on-state voltages `[.75, 1, 1.25, 1.5, 1.75, 2, 2.25]` `V` (default)

The vector of on-state voltages, to be used for table lookup. The
vector values must be strictly increasing, and the first value must be
greater than zero. The values can be nonuniformly spaced.

#### Dependencies

This parameter is visible only when you select `Lookup
table` for the **I-V characteristics
defined by** parameter.

### **Vector of corresponding currents, I\_T** — Vector of corresponding currents `[.015, .22, .75, 1.4, 2, 2.75, 3.45]` `A` (default)

The vector of currents corresponding to the on-state voltages vector
values, to be used for 1D table lookup. The two vectors must be of the
same size.

#### Dependencies

This parameter is visible only when you select `Lookup
table` for the **I-V characteristics
defined by** parameter.

### **Off-state current, I\_DRM** — Off-state anode current `0.01` `mA` (default)

The off-state anode current
*IDRM* that flows when the
anode-cathode voltage is equal to the off-state voltage
*VDRM*.

### **Corresponding off-state voltage, V\_DRM** — Off-state anode-cathode voltage `400` `V` (default)

The anode-cathode voltage
*VDRM* applied with the
thyristor in the off-state when quoting the off-state current
*IDRM*

### **Holding current** — Holding current `1` `mA` (default)

This is the minimum current for which the thyristor remains in the
on-state. For the Lookup table option, the latching current is assumed
equal to the holding current, so this is also the maximum current for
which the thyristor remains in the off-state.

#### Dependencies

This parameter is visible only when you select `Lookup
table` for the **I-V characteristics
defined by** parameter.

### **Measurement temperature** — Device simulation temperature `25` `degC` (default)

Device simulation temperature. You must specify all block parameter
values for this temperature.

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by**
parameter.

### Gate Triggering

### **Gate trigger current, I\_GT** — Critical gate current `3` `uA` (default)

Critical gate current *iGT*
required to turn the transistor on, resulting in a gate voltage equal to
the corresponding gate voltage
*vGT*. You must set the
value of the **Internal shunt resistor, Rs** parameter
on the **Advanced** tab to ensure that the gate
triggers at *iGT*, and not for
currents less that *iGT*.

### **Corresponding gate voltage, V\_GT** — Gate-cathode voltage `0.6` `V` (default)

Gate-cathode voltage *vGT*
when the gate current is equal to the gate trigger current
*iGT*.

### **Test voltage, V\_D** — Test supply voltage `12` `V` (default)

Supply voltage used when quoting values for
*vGT* and
*iGT*.

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by**
parameter.

### **Test load resistor** — Test load resistor `120` `Ohm` (default)

Load resistor used when quoting values for
*vGT* and
*iGT*.

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by**
parameter.

### dV/dt Triggering

### **Critical rate of rise of off-state voltage, dV/dt** — Critical rate of rise of off-state voltage `150` `V/us` (default)

If the anode-cathode voltage increases faster than this rate, the
thyristor will experience a parasitic turn-on due to capacitive
effects.

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by**
parameter.

### **Test gate-cathode resistor, R\_GK** — Test gate-cathode resistor `1000` `Ohm` (default)

Gate-cathode resistor used when quoting the critical rate of rise off
off-state voltage.

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by**
parameter.

### Time Constants

### **NPN device forward transit time parameterization** — NPN device forward transit time parameterization `Derive approximate value from gate-controlled turn-on time` (default) | `Specify directly`

Select one of the following options:

- `Derive approximate value from gate-controlled
  turn-on time` — The block calculates the
  NPN device forward transit time based on the values for the
  gate-controlled turn-on time and corresponding gate current that
  you specify.
- `Specify directly` — Provide
  the value directly by using the **NPN device forward
  transit time** parameter.

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by**
parameter.

### **Gate-controlled turn-on time** — Gate-controlled turn-on time `2` `us` (default)

Time for the gate to turn from the off to the on state when a gate
current is applied.

### **Corresponding gate current** — Test gate current `10` `mA` (default)

The gate current used when quoting the gate-controlled turn-on time.
The gate current and turn-on time are used to calculate an approximate
value for the NPN device forward transit time on the assumption that all
of the input charge is used to raise the gate voltage to the
corresponding gate voltage
*vGT*. The default value is
`10` mA.

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by** parameter
and `Derive approximate value from gate-controlled
turn-on time` for **NPN device forward
transit time parameterization**.

### **NPN device forward transit time** — Mean forward transit time `0.3` `us` (default)

Mean time for the minority carriers to cross the base region from the
emitter to the collector of the NPN device [1].

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by** parameter
and `Specify directly` for **NPN
device forward transit time parameterization**.

### **PNP device forward transit time parameterization** — PNP device forward transit time parameterization `Set equal to NPN device forward transit time` (default) | `Specify directly`

Select one of the following options:

- `Set equal to NPN device forward transit
  time` — The block uses the NPN device
  forward transit time value.
- `Specify directly` — Provide
  the value directly by using the **PNP device forward
  transit time** parameter.

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by**
parameter.

### **PNP device forward transit time** — Mean forward transit time `0.3` `us` (default)

Mean time for the minority carriers to cross the base region from the
emitter to the collector of the PNP device [1].

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by** parameter
and `Specify directly` for **PNP
device forward transit time parameterization**.

### **Turn-on delay time** — Time delay `0` `s` (default)

Time delay before the device starts to turn on following a step in
current on the gate from zero to the value specified by the
**Gate current for turn-on delay time**
parameter.

#### Dependencies

This parameter is visible only when you select `Lookup
table` for the **I-V characteristics
defined by**.

### **Gate current for turn-on delay time** — Gate current for turn-on delay time `1` `mA` (default)

The gate current used when measuring the turn-on delay time.

#### Dependencies

This parameter is visible only when you select `Lookup
table` for the **I-V characteristics
defined by**.

### **Turn-on rise time** — Turn-on rise time `0` `s` (default)

Time it takes for the thyristor to turn on fully following the turn-on
delay event.

#### Dependencies

This parameter is visible only when you select `Lookup
table` for the **I-V characteristics
defined by**.

### Advanced

### **Internal shunt resistor, Rs** — Gate-Cathode shunt resistance `87` `kOhm` (default)

Gate-cathode shunt resistance. It is important to set this parameter
value to ensure that the gate triggers at
*iGT*, and not for
currents less that *iGT*. For
details, see the Thyristor Static
Behavior Validation example. If you are using the thyristor
in a circuit where there is an external gate-cathode resistor
RGK, then usually the effect of Rs is small,
and it can be set to `inf`.

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by**.

### **Internal series gate resistor, Rg** — Resistance associated with gate connection `10` `Ohm` (default)

Resistance associated with the gate connection. A typical value is of
the order of a few ohms, and its impact on static and dynamic
characteristics is small. Therefore, its precise value is not important,
but its presence helps avoid numerical simulation issues if the gate is
driven directly by a voltage source. You can specify any positive
value.

### **Product of NPN and PNP forward current gains** — Product of NPN and PNP forward current gains `10` (default)

This is the product of the NPN forward gain
*BFNPN* and the PNP
forward gain *BFPNP*. The value
must be greater than one for latching to occur. The smaller the value,
the larger the latching current becomes. However, latching current is
primarily set by other block parameters, and the total gain has only a
small effect.

#### Dependencies

This parameter is visible only when you select
`Fundamental nonlinear equations` for
the **I-V characteristics defined by**.
## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2010b**

### R2019b: Thermal network simlog paths

From R2019b forward, it is possible to model the thermal network of this block
either internally or externally.

As a result, the simlog paths corresponding to the thermal network have changed.
If you have a script that programmatically access the simlog, you have to manually
update it to reflect these changes.

## Description

Thyristor using NPN and PNP transistors

The Thyristor block provides two ways of modeling a
thyristor:

- As an equivalent circuit based on NPN and PNP bipolar transistors
- By a lookup table approximation to the on-state I-V (current-voltage)
  curve

### Representation by Equivalent Circuit

The equivalent circuit contains a pair of NPN and PNP bipolar transistors, as
shown in the following illustration.

The P-N-P-N structure of a thyristor is matched by the P-N-P and N-P-N structures
of the bipolar transistors, the base of each device being connected to the collector
of the other device. To ensure that this circuit behaves like a thyristor, it is
necessary to pick suitable parameter values of the NPN and PNP devices, plus
external resistors. For example, for the circuit to latch into the on-state, once
triggered by a suitable gate current, the total gain of the two transistors must be
greater than one. This model structure replicates the behavior of a thyristor in
typical application circuits, while at the same time presenting a minimum number of
equations to the solver, to improve simulation speed.

**Note**

It is extremely important that you parameterize the thyristor component
correctly before using it in your model. To help you do this, there are two test
harnesses in the Simscape™
Electrical™ examples, Thyristor Static
Behavior Validation and Thyristor Dynamic Behavior
Validation. Follow the help text for these two examples, plus a
datasheet for your device, to re-parameterize the thyristor component so that it
replicates the required behavior. You can then copy the parameterized component
into your model. Take care to model the gate drive circuitry correctly,
including circuit series resistance. Connecting a controlled voltage source
directly to the thyristor gate gives nonphysical results because it clamps the
gate to the cathode voltage when the gate demand is zero.

The model captures the following thyristor behaviors:

- Off-state currents, *IDRM* and
  *IRRM*. These are typically
  quoted for the maximum off-state voltages
  *VDRM* and
  *VRRM*. It is assumed, as is
  the case for most thyristors, that *IDRM* =
  *IRRM* and *VDRM* =
  *VRRM*.
- The gate trigger voltage is equal to the **Corresponding gate
  voltage, V\_GT** parameter value when the gate current is equal
  to the **Gate trigger current, I\_GT** parameter
  value.
- The thyristor latches on when the gate current is equal to the
  **Gate trigger current, I\_GT**. The thyristor does not
  latch on until the gate current reaches this value. To ensure this is the
  case, you must set the **Internal shunt resistor, Rs**
  parameter correctly. If the resistance is too high, then the gate triggers
  before the gate current reaches
  *iGT*. If the resistance is too
  small, then the gate does not trigger.

  You can determine the value of the internal shunt resistor Rs by running
  the simulation. To see how this can be done, refer to the Thyristor Static Behavior
  Validation example. Alternatively, if you are using the thyristor
  in a circuit where there is an external resistor RGK
  connected from gate to cathode, then the effect of Rs is usually very small,
  and it can be set to `inf`.
- With the thyristor in the on-state, if the gate current is removed, the
  thyristor stays in the on-state, provided that the load current is higher
  than the holding current. You do not specify the holding current directly
  because its value is primarily determined by other block parameters.

  However, the holding current can be influenced by the **Product of
  NPN and PNP forward current gains** parameter on the
  **Advanced** tab. Reducing the gain increases the
  holding current.
- The on-state voltage is equal to the **On-state voltage,
  V\_T** parameter value when the load current is equal to the
  **On-state current, I\_T** parameter value. This is
  ensured by the R\_on resistance value, which takes into account the voltage
  drop seen across the PNP and NPN devices.
- Triggering by rate of rise of off-state voltage. A rapid change in
  anode-cathode voltage induces a current in the base-collector capacitance
  terms. If this current is large enough, it triggers the thyristor into the
  on-state. The thyristor initialization routine calculates a suitable value
  for the base-collector capacitance, so that when the rate of change of
  voltage is equal to the **Critical rate of rise of off-state
  voltage, dV/dt** parameter value, the thyristor triggers on.
  This calculation is based on the approximation that the required current is *vGT* /
  *RGK* where *RGK* is the
  gate-cathode resistance value used when quoting the critical
  *dV/dt* value.
- A nonzero gate-controlled turn-on time, primarily influenced by the
  **NPN device forward transit time, TF**. You either
  specify this parameter directly, or calculate an approximate value for TF
  from the turn-on time.
- A nonzero commuted turn-off time, primarily influenced by the
  **PNP device forward transit time, TF**. You can either
  specify this parameter directly, or set it to be equal to the forward
  transit time for the NPN transistor.

Resistors Gmin1 and Gmin2 improve numerical robustness at large forward and
reverse voltages. Their values influence the off-state currents by no more than 1%
at the maximum off-state forward and reverse voltages.

**Note**

Because this block implementation includes a charge model, you must model the
impedance of the circuit driving the gate to obtain representative turn-on and
turn-off dynamics. Therefore, if you are simplifying the gate drive circuit by
representing it as a controlled voltage source, you must include a suitable
series resistor between the voltage source and the gate.

### Representation by Lookup Table

If using the lookup table representation, you provide tabulated values for
anode-cathode current as a function of anode-cathode voltage when in the on state.
The main advantages of using this option are simulation speed and ease of
parameterization. To further simplify the underlying model, this representation does
not model:

- Device triggering due to rate of rise of off-state voltage
- Commuted turn-off time

The turn-on delay is represented by an input gate-cathode capacitor, the value of
which is calculated so that the delay between gate voltage rising and the device
starting to turn on is equal to the value specified by the **Turn-on delay
time** parameter. The turn-on rise time for the load current is
implemented by ramping nonlinearly between zero and the current determined by
on-state current-voltage profile over a time period specified by the value of the
**Turn-on rise time** parameter. Note that the resulting
turn-on current profile is an approximation to an actual device.

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

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
