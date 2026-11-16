---
type: simulink-block
title: 'Thyristor (Piecewise Linear)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'thyristorpiecewiselinear'
documentation_source_path: 'ref/thyristorpiecewiselinear.html'
language: en
---

# Thyristor (Piecewise Linear)

## Ports

### Conserving

### **G** — Gate terminal electrical

Port associated with the gate terminal. You can set the port to either
a physical signal or electrical port.

### **A** — Anode terminal electrical

Electrical conserving port associated with the anode terminal.

### **K** — Cathode terminal electrical

Electrical conserving port associated with the cathode
terminal.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

## Parameters

### **Modeling option** — Thermal port visibility `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port.

### Main

This table shows how the visibility of **Main** parameters
depends on how you configure the **Modeling option** and
**On-state behavior and switching losses** parameters. To learn
how to read this table, see Parameter Dependencies.

**Main Parameter Dependencies**

| Parameters and Options | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Modeling option** | | | | | | | |
| *`No thermal port`* | | | | *`Show thermal port`* | | | |
| Gate-control port | | | | Gate-control port | | | |
| Forward voltage, Vf | | | | Gate trigger voltage, Vgt | | | |
| On-state resistance | | | | Holding current | | | |
| Off-state conductance | | | | **On-state behavior and switching losses** | | | |
| *`Specify constant values`* | *`Tabulate`* | | |
| Gate trigger voltage, Vgt | | | | Forward voltage, Vf | On-state voltage, Vak(Tj,Iak) | | |
| Holding current | | | | On-state resistance | Temperature vector, Tj | | |
| Off-state conductance | Anode-cathode current vector, Iak | | |
| Off-state conductance | | |

### **Gate-control port** — Whether to specify physical or electrical control port `PS` (default) | `Electrical`

Whether to specify physical or electrical control port for the switch
gate.

### **On-state behavior and switching losses** — On-state current for switching loss data `Specify constant values` (default) | `Tabulate`

Parameterization method for on-state behavior and switching losses,
specified as one of these values:

- `Specify constant values` — Use
  scalar values to specify the output current, switch-on loss,
  and switch-off loss data.
- `Tabulate` — Use vectors to
  specify the output current and temperature data. Use
  matrices to specify the switch-on loss and switch-off loss
  data.

### **Forward voltage, Vf** — Forward voltage `0.8` `V` (default)

Forward voltage at which the device turns on.

#### Dependencies

See the Main Parameter Dependencies
table.

### **On-state resistance** — On-state resistance `0.001` `Ohm` (default)

Anode-cathode resistance when the device is on.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Off-state conductance** — Off-state conductance `1e-5` `1/Ohm` (default)

Anode-cathode conductance when the device is off. The value must be
less than 1/*R*, where *R* is the
value of **On-state resistance**.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Gate trigger voltage, Vgt** — Gate trigger voltage `6` `V` (default)

Gate-cathode voltage threshold. The device turns on when the
gate-cathode voltage is above this value.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Holding current** — Holding current `1` `A` (default)

Current threshold. The device stays on when the current is above this
value, even when the gate-cathode voltage falls below the gate trigger
voltage.

#### Dependencies

See the Main Parameter Dependencies
table.

### **On-state voltage, Vak(Tj,Iak)** — On-state voltage `[0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8]` `V` (default) | matrix of nonnegative scalars

Voltage drop across the device in a triggered conductive state. This
parameter is a function of temperature and final on-state output
current.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Temperature vector, Tj** — Temperature values `[298.15, 398.15]` `K` (default) | vector

Temperature values at which you quote the on-state voltage.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Anode-cathode current vector, Iak** — Anode-cathode current vector `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A` (default)

Anode-cathode currents for which the on-state voltage is defined. The
first element must be zero. Specify this parameter using a vector
quantity.

#### Dependencies

See the Main Parameter Dependencies
table.

### Switching Losses

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Switch-on loss** — Switch-on loss `22.86e-3` `J` (default) | positive scalar

Energy dissipated during a single switch-on event.

#### Dependencies

To enable this parameter, set **On-state behavior and
switching losses** to `Specify constant
values`.

### **Natural commutation rectification loss** — Natural commutation rectification loss `10e-3` `J` (default) | positive scalar

Rectification loss that applies when the current falls below the
**Holding current** parameter value and the block
switches off.

### **Off-state voltage for switching loss data** — Off-state voltage for loss data `300` `V` (default) | positive scalar

Output voltage of the device during the off state. This value is the
blocking voltage at which you define the switch-on loss and switch-off
loss data.

### **On-state current for switching loss data** — Output current `600` `A` (default) | positive scalar

Output current at which you define the switch-on loss and switch-off
loss.

**Note**

The block measures this parameter at the point that the gate
voltage falls below the **Gate trigger voltage,
Vgt** parameter value. The turn-on pulse is longer than
the time it takes the current to reach its maximum value.

#### Dependencies

To enable this parameter, set **On-state behavior and
switching losses** to `Specify constant
values`.

### **Switch-on loss, Eon(Tj,Iak)** — Switch-on loss `[0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3` `J` (default) | matrix of nonnegative scalars

Energy dissipated during a single switch-on event as a function of
temperature and final on-state output current.

#### Dependencies

To enable this parameter, set **On-state behavior and
switching losses** to
`Tabulate`.

### **Temperature vector for switching losses, Tj** — Temperature for switching losses `[298.15, 398.15]` `K` (default) | vector

Temperature values at which you quote the switch-on loss and
switch-off loss.

#### Dependencies

To enable this parameter, set **On-state behavior and
switching losses** to
`Tabulate`.

### **Anode-cathode current vector for switching losses, Iak** — Anode-cathode current vector for switching losses `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A` (default) | vector of nonnegative scalars

Anode-cathode currents at which you quote the switch-on loss and
switch-off-loss. The first element must be zero.

#### Dependencies

To enable this parameter, set **On-state behavior and
switching losses** to
`Tabulate`.

### **Wait time before switch-on current measurement** — Time before on-state current is measured `1e-4` `s` (default) | nonnegative scalar

Time to wait before recording the on-state current.

### Integral Diode

### **Integral protection diode** — Integral protection diode `External diode` (default) | `Protection diode with no dynamics` | `Protection diode with charge dynamics`

Model that the Thyristor (Piecewise Linear) block uses for the integral protection
diode. Choose one of these options:

- `External diode` — The
  Thyristor (Piecewise Linear) does not model an integral protection diode. Use
  an external Diode
  block.
- `Diode with no dynamics` — The
  Thyristor (Piecewise Linear) block models the integral protection diode using
  the same equations as the Diode
  block with no dynamics. Select this option to prioritize
  simulation speed.
- `Diode with charge dynamics` —
  The Thyristor (Piecewise Linear) block models the integral protection diode
  using the same equations as the Diode
  block with charge dynamics. Select this option to prioritize
  detailed simulation results.

### **Diode model** — Diode model `Piecewise Linear` (default) | `Tabulated I-V curve`

Select one of these diode models:

- `Piecewise Linear` — Use a
  piecewise linear model for the diode, as described in Piecewise Linear Diode.
- `Tabulated I-V curve` —
  Use tabulated forward bias I-V data plus fixed reverse bias
  off conductance.

#### Dependencies

This parameter is visible only when the thermal port is exposed
and the **Integral protection diode** parameter is
set to `Protection diode with no dynamics`
or `Protection diode with charge dynamics`.

### **Table type** — Tabulated function `Table in If(Tj,Vf) form` (default) | `Table in Vf(Tj,If) form`

Whether to tabulate the current as a function of temperature and
voltage or the voltage as a function of temperature and current.

#### Dependencies

This parameter is visible only when the thermal port is exposed
and the **Integral protection diode** parameter is
set to `Protection diode with no dynamics`
or `Protection diode with charge dynamics`
and **Diode model** is set to
`Tabulated I-V curve`.

### **Forward voltage** — Forward voltage `0.8` `V` (default)

Minimum voltage required across the `+` and `-` block ports
for the gradient of the diode I-V characteristic to be
1/*R*on, where
*R*on is the value of the **On
resistance** parameter.

#### Dependencies

To enable this parameter:

- If the thermal port is hidden, set **Integral protection
  diode** to `Diode with no
  dynamics` or `Diode with charge
  dynamics`.
- If the thermal port is exposed, set **Integral protection
  diode** to `Diode with no
  dynamics` or `Diode with charge
  dynamics` and **Diode model** to
  `Piecewise linear`.

### **On resistance** — On resistance `0.001` `Ohm` (default)

Rate of change of voltage versus current above the **Forward voltage**
parameter value.

#### Dependencies

To enable this parameter:

- If the thermal port is hidden, set **Integral protection
  diode** to `Diode with no
  dynamics` or `Diode with charge
  dynamics`.
- If the thermal port is exposed, set **Integral protection
  diode** to `Diode with no
  dynamics` or `Diode with charge
  dynamics` and **Diode model** to
  `Piecewise linear`.

### **Forward currents, If(Tj,Vf)** — Vector of forward currents `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A` (default) | nonnegative vector

Forward currents. This parameter must be a vector of at least three
nonnegative elements.

#### Dependencies

To enable this parameter, expose the thermal port and set
**Diode model** to `Tabulated I-V
curve` and **Table type** to
`Table in If(Tj,Vf) form`.

### **Junction temperatures, Tj** — Vector of junction temperatures `[25, 125]` `degC` (default)

Vector of junction temperatures. This parameter must be a vector of at
least two elements.

#### Dependencies

To enable this parameter, expose the thermal port and set
**Diode model** to `Tabulated I-V
curve`.

### **Forward voltages, Vf** — Vector of forward voltages `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V` (default)

Vector of forward voltages. This parameter must be a vector of at
least three nonnegative values.

#### Dependencies

To enable this parameter, expose the thermal port and set
**Diode model** to `Tabulated I-V
curve` and **Table type** to
`Table in If(Tj,Vf) form`.

### **Forward voltages, Vf(Tj,If)** — Vector of forward voltages `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V` (default) | nonnegative vector

Forward voltages. This parameter must be a vector of at least three
nonnegative elements.

#### Dependencies

To enable this parameter, expose the thermal port and set
**Diode model** to `Tabulated I-V
curve` and **Table type** to
`Table in Vf(Tj,If) form`.

### **Forward currents, If** — Vector of forward currents `[.1, .2, .5, 1, 2, 4, 7, 10]` `A` (default)

Vector of forward currents. This parameter must be a vector of at
least three nonnegative values.

#### Dependencies

To enable this parameter, expose the thermal port and set
**Diode model** to `Tabulated I-V
curve` and **Table type** to
`Table in Vf(Tj,If) form`.

### **Off conductance** — Off conductance `1e-5` `1/Ohm` (default)

Conductance of the reverse-biased diode.

#### Dependencies

This parameter is visible only when the **Integral
protection diode** parameter is set to
`Diode with no dynamics` or
`Diode with charge dynamics`.

### **Reverse recovery loss model** — Model for reverse recovery loss `Fixed loss` (default) | `Tabulated loss`

*Since R2023a*

Whether to model fixed or tabulated reverse recovery losses.

#### Dependencies

To enable this parameter, set the **Modeling option** parameter
to `Show thermal port` and set the **Integral
protection diode** parameter to `Diode with no
dynamics`.

### **Reverse recovery loss** — Reverse recovery loss `0` `J` (default) | nonnegative scalar

*Since R2023a*

Dissipated energy in each turn-off event. The block dissipates this energy regardless
of the state of the diode before or after the switching event.

#### Dependencies

To enable this parameter, set the **Reverse recovery loss model**
parameter to `Fixed loss`.

### **Scale reverse recovery loss with current and voltage** — Option to scale reverse recovery loss `On` (default) | `Off`

*Since R2023b*

Option to scale reverse recovery loss with current and voltage.

#### Dependencies

To enable this parameter:

- Set **Modeling option** to `Show thermal port`.
- Set **Integral protection diode** to `Diode with no dynamics`.
- Set **Reverse recovery loss model** to `Fixed loss`.

### **Reverse recovery loss table, Erect(Tj), If** — Reverse recovery loss `zeros(2,3)` `J` (default) | vector of nonnegative scalars

*Since R2023a*

Dissipated energy as a function of the forward current *If* just
before the switching event, and final off-state voltage once the diode is in off
state.

#### Dependencies

To enable this parameter, set the **Reverse recovery loss model**
parameter to `Tabulated loss`.

### **Temperature vector for recovery loss table, Tj** — Temperature vector for recovery loss table `[298.15 398.15]` `K` (default) | vector

*Since R2023a*

Temperature vector that the block uses to tabulate the reverse recovery loss.

#### Dependencies

To enable this parameter, set the **Reverse recovery loss model**
parameter to `Tabulated loss`.

### **Forward current vector for recovery loss table, If** — Forward current vector for recovery loss table `[.1, 1, 10]` `K` (default) | vector of nonnegative scalars

*Since R2023a*

Forward current vector that the block uses to tabulate reverse recovery loss.

#### Dependencies

To enable this parameter, set the **Reverse recovery loss model**
parameter to `Tabulated loss`.

### **Forward current when measuring recovery loss, Irec** — Forward current when block measures recovery loss `10` `A` (default) | positive scalar

*Since R2023b*

Forward current through the diode before the reverse recovery event that the block
uses to measure recovery loss.

#### Dependencies

To enable this parameter, set **Reverse recovery loss model** to
`Fixed loss` and select the **Scale reverse
recovery loss with current and voltage** parameter.

### **Turn-off voltage when measuring recovery loss, Vrec** — Turn-off voltage when measuring recovery loss `10` `V` (default) | positive scalar

*Since R2023a*

Voltage across the diode after the reverse recovery event that the block uses to
measure recovery loss.

#### Dependencies

To enable this parameter, choose from one of these options:

- Set **Reverse recovery loss model** to
  `Fixed loss` and select the **Scale
  reverse recovery loss with current and voltage** parameter.
- Set the **Reverse recovery loss model** parameter to
  `Tabulated loss`.

### **Filter time constant for voltage and current values** — Filter time constant for voltage and current values `1 / 1000 / 100` `s` (default) | positive scalar

*Since R2023a*

Filter time constant for the voltage and current values that the block uses to
calculate reverse recovery loss. Set this parameter to a value that is lower than the
fastest switching period.

#### Dependencies

To enable this parameter, choose from one of these options:

- Set **Reverse recovery loss model** to
  `Fixed loss` and select the **Scale
  reverse recovery loss with current and voltage** parameter.
- Set the **Reverse recovery loss model** parameter to
  `Tabulated loss`.

### **Junction capacitance** — Junction capacitance `50e-9` `F` (default)

Diode junction capacitance.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics`.

### **Peak reverse current, iRM** — Peak reverse current `-235` `A` (default) | negative scalar

Peak reverse current measured by an external test circuit. This value must be less than zero. The default value is `-235` `A`.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics`.

### **Initial forward current when measuring iRM** — Initial forward current when measuring iRM `300` `A` (default) | positive scalar

Initial forward current when measuring peak reverse current.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics`.

### **Rate of change of current when measuring iRM** — Rate of change of current when measuring iRM `-50``A/μs` (default) | negative scalar

Rate of change of current when measuring peak reverse current. This value must be less than zero.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics`.

### **Reverse recovery time parameterization** — Reverse recovery time parameterization `Specify reverse recovery time directly` (default) | `Specify stretch factor` | `Specify reverse recovery charge`

Determines how you specify reverse recovery time in the block. The default value is `Specify reverse recovery time directly`.

If you select `Specify stretch factor` or `Specify reverse recovery charge`, you specify a value that the block uses to derive the reverse recovery time. For more information on these options, see How the Block Calculates TM and Tau.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics`.

### **Reverse recovery time, trr** — Reverse recovery time `15` `μs` (default) | scalar

Interval between the time when the current initially goes to zero (when the diode turns off) and the time when the current falls to less than 10% of the peak reverse current. The value of the **Reverse recovery time, trr** parameter must be greater than the value of the **Peak reverse current, iRM** parameter divided by the value of the **Rate of change of current when measuring iRM** parameter.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics` and the
**Reverse recovery time parameterization** parameter is set to
`Specify reverse recovery time directly`.

### **Reverse recovery time stretch factor** — Reverse recovery time stretch factor `3` (default) | scalar greater than `1`

Stretch factor that the block uses to calculate the reverse recovery time. Specifying
the stretch factor is an easier way to parameterize the reverse recovery time than
specifying the reverse recovery charge. The larger the value of the stretch factor, the
longer it takes for the reverse recovery current to dissipate.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics` and the
**Reverse recovery time parameterization** parameter is set to
`Specify stretch factor`.

### **Reverse recovery charge, Qrr** — Reverse recovery charge `1500` `μAs` (default)

Reverse recovery charge that the block uses to calculate the reverse recovery time.
Use this parameter if the data sheet for your diode device specifies a value for the
reverse recovery charge instead of a value for the reverse recovery time.

The reverse recovery charge is the total charge that continues to dissipate when the diode
turns off. The value must be less than −i2RM2a, where:

- *iRM* is the value specified for **Peak reverse current, iRM**.
- *a* is the value specified for **Rate of change of current when measuring iRM**.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with charge dynamics` and the
**Reverse recovery time parameterization** parameter is set to
`Specify reverse recovery charge`.

### **Diode turn-off voltage when measuring Erec** — Diode turn-off voltage when measuring Erec `-600` `V` (default)

Voltage between the diode in steady-state.

#### Dependencies

This parameter is visible only when the **Integral protection
diode** parameter is set to `Diode with
charge dynamics` and the **Reverse
recovery time parameterization** parameter is set
to `Specify reverse recovery energy`.

### **Stray inductance when measuring Erec** — Stray inductance when measuring Erec `150` `nH` (default)

Total unintended inductance in the measurement circuit. The block uses this
value to calculate **Reverse recovery energy,
Erec**.

#### Dependencies

This parameter is visible only when the **Integral protection
diode** parameter is set to `Diode with
charge dynamics` and the **Reverse
recovery time parameterization** parameter is set
to `Specify reverse recovery energy`.

### **Reverse recovery energy, Erec** — Reverse recovery energy `0.03` `J` (default)

Total switching losses due to the diode reverse recovery.

#### Dependencies

This parameter is visible only when the **Integral protection
diode** parameter is set to `Diode with
charge dynamics` and the **Reverse
recovery time parameterization** parameter is set
to `Specify reverse recovery energy`.

For more information on these parameters, see Diode.

### Thermal Port

To enable these parameters, set **Modeling option** to
`Show thermal port`.

For more information about using thermal ports and the **Thermal
Port** parameters, see Simulating Thermal Effects in Semiconductors.

### **Thermal network** — Options for thermal network modeling `External` (default) | `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

Options for modeling the thermal network of the block.

### **Thermal mass parameterization** — Option to parameterize thermal mass `By thermal time constants` (default) | `By thermal mass`

Options to parameterize the thermal mass:

- `By thermal time constants` —
  Parameterize the thermal masses in terms of thermal time
  constants.
- `By thermal mass` — Specify the
  thermal mass values directly.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Specify junction and case thermal
parameters`, `Cauer
model`, or `Cauer model parameterized with
Foster coefficients`.

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — Junction case and case-ambient (or case-heatsink) thermal resistances `[.08, .5]` `K/W` (default) | vector of positive values

Row vector, [ *R\_JC*
*R\_CA* ], of two thermal resistance values, represented
by two Conductive Heat Transfer blocks. The first value,
*R\_JC*, is the thermal resistance between the
junction and the case. The second value, *R\_CA*, is the
thermal resistance between port **H** and the device
case.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Specify junction and case thermal
parameters`.

### **Junction and case thermal time constants, [t\_J t\_C]** — Junction and case thermal time constants `[.001, .2]` `s` (default) | vector of positive values

Row vector, [ *t\_J*
*t\_C* ], of two thermal time constant values. The first
value, *t\_J*, is the junction time constant. The second
value, *t\_C*, is the case time constant.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Specify junction and case thermal
parameters` and **Thermal mass
parameterization** to `By thermal time
constants`.

### **Junction and case thermal masses, [M\_J M\_C]** — Junction and case thermal masses `[.01, .5]` `J/K` (default) | vector of positive values

Row vector, [ *M\_J*
*M\_C* ], of two thermal mass values. The first value,
*M\_J*, is the junction thermal mass. The second
value, *M\_C*, is the case thermal mass.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Specify junction and case thermal
parameters` and **Thermal mass
parameterization** to `By thermal
mass`.

### **Junction and case initial temperatures, [T\_J T\_C]** — Junction and case initial temperatures `[25, 25]` `degC` (default) | vector of positive values

Row vector, [ *T\_J* *T\_C* ], of two
temperature values. The first value, *T\_J*, is the
junction initial temperature. The second value, *T\_C*,
is the case initial temperature.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Specify junction and case thermal
parameters`.

### **Thermal resistances, [R1 R2 … Rn]** — Thermal resistances `[.08,.1,.5]` `K/W` | `[.08,.14,.22,.16]` `K/W` | vector of positive values

Row vector of *n* thermal resistance values,
represented by the Cauer elements used in the thermal network.

If you set **Thermal network** to `Cauer
model`, the default value is
`[.08,.1,.5]`. If you set **Thermal
network** to `Cauer model parameterized with
Foster coefficients`, the default value is
`[.08,.14,.22,.16]`.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Cauer model` or `Cauer
model parameterized with Foster
coefficients`.

### **Thermal masses, [M1 M2 … Mn]** — Thermal masses `[.01,.1,.5]` `J/K` | `[.001,.005,.05,.5]` `J/K` | vector of positive values

Row vector of *n* thermal mass values, where
*n* is the number of Cauer elements in the thermal
network.

If you set **Thermal network** to `Cauer
model`, the default value is
`[.01,.1,.5]`. If you set **Thermal
network** to `Cauer model parameterized with
Foster coefficients`, the default value is
`[.001,.005,.05,.5]`.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Cauer model` or `Cauer
model parameterized with Foster coefficients` and
**Thermal mass parameterization** to
`By thermal mass`.

### **Thermal masses initial temperatures, [T1 T2 … Tn]** — Initial temperatures of thermal masses `[25, 25, 25]` `degC` (default) | vector of positive values

Row vector of temperature values that correspond to the temperature
drop across each thermal capacity in the model.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Cauer model`.

### **Thermal time constants, [t1 t2 … tn]** — Thermal time constants `[.001,.1,.2]` `s` | `[7e-05, .0007, .01, .08]` `s` | vector of positive values

Row vector of *n* thermal time constant values,
where *n* is the number of Cauer elements in the
thermal network. The length of this vector must match the length of
**Thermal resistances, [R1 R2 … Rn]**. With this
parameterization, the block computes the thermal masses as
`Mi =
ti/Ri`,
where `Mi`,
`ti` and
`Ri` are the thermal
mass, thermal time, and thermal resistance for the
ith Cauer element (if you set
**Thermal network** to `Cauer
model`) or Foster element (if you set **Thermal
network** to `Cauer model parameterized with
Foster coefficients`).

If you set **Thermal network** to `Cauer
model`, the default value is
`[.001,.1,.2]`. If you set **Thermal
network** to `Cauer model parameterized with
Foster coefficients`, the default value is
`[7e-05, .0007, .01, .08]`.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Cauer model` or `Cauer
model parameterized with Foster coefficients`and
**Thermal mass parameterization** to
`By thermal time constants`.

### **Initial node temperatures, [T1 T2 ... Tn]** — Initial node temperatures `[25, 25, 25, 25]` `degC` (default) | vector of positive values

Row vector of the temperature values of each node starting from the
junction.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Cauer model parameterized with Foster
coefficients`.

### **Junction thermal mass** — Thermal mass of junction `0.01` `J/K` (default) | positive scalar

Thermal mass of the junction.

#### Dependencies

To enable this parameter, set **Thermal network**
to `External`.

## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

### R2023b: Scale reverse recovery loss with current and voltage

You can now scale a fixed reverse recovery loss value with current and voltage. To
enable this option, select the **Scale reverse recovery loss with current
and voltage** parameter.

Models you create in R2023a or earlier default to no scaling for backwards
compatibility.

### R2023a: Update on integral diode modeling options

From R2023a forward, you can model reverse recovery loss in the
Thyristor (Piecewise Linear) block. To enable the
**Reverse recovery loss model** parameter, set the
**Modeling option** parameter to `Show thermal
port` and set the **Integral protection diode** to
`Diode with no dynamics`.

### R2021a: Removal of energy dissipation time constant parameter

From R2021a forward, the **Energy dissipation time constant**
parameter of the Thyristor (Piecewise Linear) block
is no longer used. A step in junction temperature now reflects the switching losses.
If your model contains a thermal mass directly connected to this block thermal port,
remove it and model the thermal mass inside the component itself.

### R2020b: Update on switching losses and thermal modeling options

From R2020b forward, the Thyristor (Piecewise
Linear) block has improved losses and thermal modeling
options.

As a result of these changes:

- Electrical and thermal on-state losses are now always identical. The
  **Thermal loss dependent on** parameter and its
  options, `Voltage and current` and
  `Voltage, current, and temperature`, have
  been renamed to **On-state behavior and switching
  losses**, `Specify constant
  values`, and `Tabulate`:

  - If you selected `Voltage and
    current` for **Thermal loss
    dependent on**, then the electrical on-state
    losses are unchanged and their values are determined using
    the on-state resistance. However, the thermal on-state
    losses are now also determined by the on-state resistance.
    Prior to R2020b, the thermal on-state losses were defined by
    the product of the **On-state voltage** and
    **Output current, Iout**
    parameters.
  - If you selected `Voltage, current, and
    temperature` for **Thermal loss
    dependent on**, then the thermal on-state
    losses are unchanged and the **On-state voltage,
    Vak(Tj,Iak)** parameter sets their values.
    However, the electrical on-state losses are now equal to the
    thermal on-state losses. Prior to R2020b, the electrical
    on-state losses were defined by the value of the on-state
    resistance.
- The **On-state voltage** and the switch-off
  parameters are no longer used.

## Description

Thyristor

The Thyristor (Piecewise Linear) block models a
thyristor. The I-V characteristic for a thyristor is such that the thyristor turns on if
the gate-cathode voltage exceeds the specified gate trigger voltage. The device turns
off if the load current falls below the specified holding-current value.

To define the I-V characteristic of the thyristor, set the **On-state behavior
and switching losses** parameter to either `Specify constant
values` or `Tabulate`. The
`Tabulate` option is available only if you expose the
thermal port of the block.

In the on state, the anode-cathode path behaves like a linear diode with
forward-voltage drop, *Vf*, and on-resistance,
*Ron*. However, if you expose the
thermal port of the block and parameterize the device using tabulated I-V data, the
tabulated resistance is a function of the temperature and current.

In the off state, the anode-cathode path behaves like a linear resistor with a low
off-state conductance, *Goff*.

The defining Simscape™ equations for the block
are:

```
    if (v > Vf)&&((G>Vgt)||(i>Ih))
        i == (v - Vf*(1-Ron*Goff))/Ron;
    else
        i == v*Goff;
    end
```

where:

- *v* is the anode-cathode voltage.
- *Vf* is the forward voltage.
- *G* is the gate voltage.
- *Vgt* is the gate trigger voltage.
- *i* is the anode-cathode current.
- *Ih* is the holding current.
- *Ron* is the on-state resistance.
- *Goff* is the off-state conductance.

Using the Integral Diode tab of the block dialog box, you can include an integral
cathode-anode diode. An integral diode protects the semiconductor device by providing a
conduction path for reverse current. An inductive load can produce a high
reverse-voltage spike when the semiconductor device suddenly switches off the voltage
supply to the load.

The table shows you how to set the **Integral protection
diode** parameter based on your goals.

| Goal | Value to Select | Block Behavior |
| --- | --- | --- |
| Prioritize simulation speed. | `Diode with no dynamics` | The block includes an integral copy of the Diode block. To parameterize the internal Diode block, use the **Protection** parameters. |
| Precisely specify reverse-mode charge dynamics. | `Diode with charge dynamics` | The block includes an integral copy of the dynamic model of the Diode block. To parameterize the internal Diode block, use the **Protection** parameters. |

### Model Gate Port and Thermal Effects

You can choose between physical or electrical ports to control the gate terminal and expose
the thermal port to model the heat that switching events and conduction losses
generate. To choose the gate-control port, set the **Gate-control
port** parameter to `PS` or
`Electrical`. To expose the thermal port, set the
**Modeling option** parameter to `No thermal
port` or `Show thermal port`.

For more information about using thermal ports, see Simulating Thermal Effects in Semiconductors.

### Thermal Losses

Switching losses are major sources of thermal loss in semiconductors. During each
on-off switching transition, the thyristor parasitics store and then dissipate
energy.

Switching losses depend on the off-state voltage and the on-state current. When a
switching device turns on, the power losses depend on the initial off-state voltage
across the device and the final on-state current when the device is in its fully on
state.

This block applies switching losses by stepping up the junction temperature with a
value equal to the switching loss divided by the total thermal mass at the junction.
You must specify the energy dissipated during a single switch-on event. You must
also specify the corresponding values of the off-state voltage and on-state current
at which you quote the losses. You can parameterize the switch-on loss, depending on
the data you have. Use tabulated data if they are available.

- To specify a scalar value for the switch-on loss, set the
  **On-state behavior and switching losses** parameter to
  `Specify constant values`. The
  **Switch-on loss** parameter value sets the sizes of
  the switch-on loss. The block scales the loss by the off-state voltage and
  the on-state current.
- To specify the switch-on loss as a function of the junction temperature
  and on-state current, set the **On-state behavior and switching
  losses** parameter to `Tabulate`. The
  **Switch-on loss, Eon(Tj,Iak)** parameter sets the size
  of the loss. The block scales the loss by the off-state voltage.

When the current falls below the **Holding current** parameter
value, the device switches off. The **Natural commutation rectification
loss** parameter value defines the switch-off loss. The block does not
scale this loss by the off-state voltage or on-state current because it is not
possible to know when to measure the starting current or final voltage for the
rectification loss.

Reverse recovery loss can be a significant source of thermal loss in diodes. The diode
dissipates energy every time it turns off, from its conducting state to the open-circuit
state. To model reverse recovery loss:

- Set **Modeling option** to `Show thermal
  port`.
- Set **Integral protection diode** to `Diode with
  no dynamics`.

If you set the **Reverse recovery loss model** parameter to
`Tabulated loss`, the value of the **Reverse recovery
loss table, Erec(Tj, If)** parameter specifies the dissipated energy as a
function of the junction temperature and the forward current just before the switching
event. The off-state voltage linearly scales the losses relative to the **Turn-off
voltage when measuring recovery loss, Vrec**  parameter value. The table uses
delayed values for the current and voltage. To use a value in the lookup table that is close
to the instantaneous value, set the **Filter time constant for voltage
and current values** parameter to a value that is lower than the fastest
switching period.

If you set the **Reverse recovery loss model** parameter to
`Fixed loss`, the value of the **Reverse recovery
loss** parameter specifies the energy dissipated during each turn-off event. If
you select the **Scale reverse recovery loss with current and voltage**
parameter, then the block scales this loss value linearly by the on-state current and the
off-state voltage. To use scaling values that are close to the instantaneous values, set
**Filter time constant for voltage and current values** to
a value that is lower than the fastest switching period.

As an alternative method to model reverse recovery, you can set the **Integral
protection diode** parameter to `Diode with charge
dynamics`. However, this approach requires smaller simulation time steps
than using the first approach.

**Note**

The block does not know the current after a switching event during the
simulation, so the block records the on-state current once the current is
greater than the holding current for a time longer than the value specified by
the **Wait time before switch-on current measurement**
parameter. Similarly, the block records the off-state voltage at the point that
the devices switches on. For this reason, the logged simulation data does not
report the switching losses to the thermal network until one switching cycle
later. To learn how to log and plot simulation data, see the Log and Plot Simulation Data example.

For all ideal switching devices, the logged simulation data reports the
thermal losses as `lastTurnOffLoss`,
`lastTurnOnLoss`, and
`lastReverseRecoveryLoss`. For the Thyristor
(Piecewise Linear) block, the
`lastTurnOnLoss` is equal to the **Natural
commutation rectification loss** parameter value. These variables
include losses as a pulse with an amplitude equal to the energy loss. If you use
a script to sum the total losses over a defined simulation period, you must sum
the pulse values at each pulse rising edge. Alternatively, you can extract
conduction and switching losses from logged data using the `ee_getPowerLossSummary` and
`ee_getPowerLossTimeSeries`
functions.

You can also access the total accumulated switching losses from the
`accumulatedSwitchingLosses` variable in the logged
simulation data. This variable sums all switching losses to date, including
reverse recovery losses for the diode.

The `power_dissipated` variable in the logged simulation data
does not include switching losses because the block models these losses as
instantaneous events. The `power_dissipated` variable reports
ohmic on-state losses.

If you use tabulated data to model the switching losses or reverse recovery
losses, check that the temperature and current are in the range you specify. If
you do not define a realistic thermal model, for example, if the junction mass
or the conductance from the junction to the case is too small, the temperature
can exceed the range you specify, causing the block to extrapolate the losses to
nonphysical values.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
