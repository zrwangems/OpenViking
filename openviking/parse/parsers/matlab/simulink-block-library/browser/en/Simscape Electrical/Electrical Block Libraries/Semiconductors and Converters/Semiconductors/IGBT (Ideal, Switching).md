---
type: simulink-block
title: 'IGBT (Ideal, Switching)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'igbtidealswitching'
documentation_source_path: 'ref/igbtidealswitching.html'
language: en
---

# IGBT (Ideal, Switching)

## Ports

### Conserving

### **G** — Gate terminal electrical

Port associated with the gate terminal. You can set the port to either a
physical signal or electrical port.

### **C** — Collector terminal electrical

Electrical conserving port associated with the collector terminal.

### **E** — Emitter terminal electrical

Electrical conserving port associated with the emitter terminal.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HDiode** — Thermal port for integral protection diode thermal

*Since R2024b*

Thermal conserving port associated with the integral protection
diode.

#### Dependencies

To enable this port, select the **Separate thermal port for
integral diode** parameter.

## Parameters

### **Modeling option** — Thermal port visibility `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port.

### **Selected part** — Predefined parameterization option `<click to select>` (default)

Option to parameterize the block to represent components by specific suppliers. Click the
**<click to select>** hyperlink to open the Block
Parameterization Manager window. For more information about the Block Parameterization
Manager, see Load Predefined Parameterizations.

### Main

This table shows how the visibility of **Main** parameters depends
on how you configure the **Modeling option** and **On-state
behavior and switching losses** parameters. To learn how to read this table,
see Parameter Dependencies.

**Main Parameter Dependencies**

| Parameters and Options | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Modeling option** | | | | | | | |
| *`No thermal port`* | | | | *`Show thermal port`* | | | |
| Gate-control port | | | | Gate-control port | | | |
| Forward voltage, Vf | | | | Threshold voltage, Vth | | | |
| On-state resistance | | | | **On-state behavior and switching losses** | | | |
| *`Specify constant values`* | *`Tabulate`* | | |
| Off-state conductance | | | | Forward voltage, Vf | On-state voltage, Vce(Tj,Ice) | | |
| Threshold voltage, Vth | | | | On-state resistance | Temperature vector, Tj | | |
| Off-state conductance | Collector-emitter current vector, Ice | | |
| Off-state conductance | | |

### **Gate-control port** — Option to specify physical or electrical control port `PS` (default) | `Electrical`

Option to specify physical or electrical control port for the switch
gate.

### **On-state behavior and switching losses** — On-state behavior and switching loss data `Specify constant values` (default) | `Tabulate`

Parameterization method for on-state behavior and switching losses,
specified as one of these values:

- `Specify constant values` — Use scalar
  values to specify the output current, switch-on loss, and switch-off
  loss data. The block assumes that the energy dissipated during a
  single switch-on or switch-off event scales linearly with the
  off-state voltage and on-state current. The block also assumes that
  the losses are independent of temperature.
- `Tabulate` — Use vectors to specify the
  output current and temperature data. Use arrays to specify the
  switch-on loss and switch-off loss data.

#### Dependencies

See the Main Parameter Dependencies table.

### **Forward voltage, Vf** — Forward voltage `0.8` `V` (default)

Minimum voltage required across the collector and emitter block ports for
the gradient of the diode I-V characteristic to be
1/*Ron*, where
*Ron* is the value of
**On-state resistance**.

#### Dependencies

See the Main Parameter Dependencies table.

### **On-state resistance** — On-state collector-emitter resistance `0.001` `Ohm` (default)

Collector-emitter resistance when the device is on.

#### Dependencies

See the Main Parameter Dependencies table.

### **Off-state conductance** — Off-state collector-emitter conductance `1e-5` `1/Ohm` (default)

Collector-emitter conductance when the device is off. The value must be less
than 1/*R*, where *R* is the value of
**On-state resistance**.

#### Dependencies

See the Main Parameter Dependencies table.

### **Threshold voltage, Vth** — Threshold voltage `6` `V` (default)

Gate-emitter voltage at which the device turns on.

#### Dependencies

See the Main Parameter Dependencies table.

### **On-state voltage, Vce(Tj,Ice)** — On-state voltage `[0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8]` `V` (default) | matrix of nonnegative scalars

Voltage drop across the device in a triggered conductive state. This
parameter is a function of temperature and final on-state output current.

#### Dependencies

See the Main Parameter Dependencies table.

### **Temperature vector, Tj** — Temperature values `[298.15, 398.15]` `K` (default)

Temperature values that correspond to the **On-state voltage,
Vce(Tj,Ice)** parameter.

#### Dependencies

See the Main Parameter Dependencies table.

### **Collector-emitter current vector, Ice** — Collector-emitter current vector `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A` (default)

Collector-emitter currents for which the on-state voltage is defined. The
first element must be zero. Specify this parameter using a vector
quantity.

#### Dependencies

See the Main Parameter Dependencies table.

### Switching Losses

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Switch-on loss** — Switch-on loss `22.86e-3` `J` (default) | positive scalar

Energy dissipated during a single switch-on event.

#### Dependencies

To enable this parameter, set **On-state behavior and switching
losses** to `Specify constant
values`.

### **Switch-off loss** — Switch-off loss `17.14e-3` `J` (default) | positive scalar

Energy dissipated during a single switch-off event.

#### Dependencies

To enable this parameter, set **On-state behavior and switching
losses** to `Specify constant
values`.

### **Off-state voltage for switching loss data** — Off-state voltage for switching loss data `300` `V` (default) | positive scalar

Output voltage of the device during the off state. This value is the
blocking voltage at which you define the switch-on loss and switch-off loss
data.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **On-state behavior and switching losses**
  to `Specify constant values`.
- Set **On-state behavior and switching losses**
  to `Tabulate` and clear the
  **Include switching loss tabulation with off-state
  voltage** parameter.

### **On-state current for switching loss data** — On-state current for switching loss data `600` `A` (default) | positive scalar

Output current at which you define the switch-on loss and switch-off
loss.

#### Dependencies

To enable this parameter, set **On-state behavior and switching
losses** to `Specify constant
values`.

### **Use last on-state current from previous cycle for turn-on loss** — Option to use last on-state current from previous cycle for turn-on loss `Off` (default) | `On`

*Since R2023b*

Option to use the last on-state current from the previous cycle for the
turn-on loss.

### **Use last off-state voltage from previous cycle for turn-off loss** — Option to use last off-state voltage from previous cycle for turn-off loss `Off` (default) | `On`

*Since R2023b*

Option to use the last off-state voltage from the previous cycle for the
turn-off loss.

### **Switch-on loss, Eon(Tj,Ice)** — Switch-on loss `[0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3` `J` (default) | matrix of nonnegative scalars

Energy dissipated during a single switch-on event as a function of
temperature and on-state current.

#### Dependencies

To enable this parameter, set **On-state behavior and switching
losses** to `Tabulate` and clear the
**Include switching loss tabulation with off-state
voltage** parameter.

### **Switch-off loss, Eoff(Tj,Ice)** — Switch-off loss `[0, .0007, .0066, .033, .066, .17, .33, .83, 1.5; 0, .001, .01, .05, .1, .25, .5, 1.2, 2.2] * 1e-3` `J` (default) | matrix of nonnegative scalars

Energy dissipated during a single switch-off event as a function of
temperature and on-state current.

#### Dependencies

To enable this parameter, set **On-state behavior and switching
losses** to `Tabulate` and clear the
**Include switching loss tabulation with off-state
voltage** parameter.

### **Temperature vector for switching losses, Tj** — Temperature for switching losses `[298.15, 398.15]` `K` (default) | vector

Temperature values at which you quote the switch-on loss and switch-off
loss.

#### Dependencies

To enable this parameter, set **On-state behavior and switching
losses** to `Tabulate`.

### **Collector-emitter current vector for switching losses, Ice** — Collector-emitter current vector for switching losses `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A` (default) | vector of nonnegative scalars

Collector-emitter currents at which you quote the switch-on loss and
switch-off-loss. The first element must be `0`.

#### Dependencies

To enable this parameter, set **On-state behavior and switching
losses** to `Tabulate`.

### **Include switching loss tabulation with off-state voltage** — Option to tabulate switching losses with off-state voltage `Off` (default) | `On`

*Since R2023b*

Option to tabulate the switching losses with the off-state voltage.

To tabulate the switch-on loss and switch-off loss with the on-state current
and temperature, clear this parameter. The block assumes that the losses scale
linearly with the off-state voltage.

To tabulate the switch-on loss and switch-off loss with the temperature,
on-state current, and off-state voltage, select this parameter.

#### Dependencies

To enable this parameter, set **On-state behavior and switching
losses** to `Tabulate`.

### **Switch-on loss, Eon(Tj,Ids,Vce)** — Switch-on loss `[zeros(2, 9, 3)]` `J` (default) | 3-D array of nonnegative scalars

*Since R2023b*

Energy dissipated during a single switch-on event as a function of
temperature, on-state current, and off-state voltage.

#### Dependencies

To enable this parameter, set **On-state behavior and switching
losses** to `Tabulate` and select the
**Include switching loss tabulation with off-state
voltage** parameter.

### **Switch-off loss, Eoff(Tj,Ids,Vce)** — Switch-off loss `[zeros(2, 9, 3)]` `J` (default) | 3-D array of nonnegative scalars

*Since R2023b*

Energy dissipated during a single switch-off event as a function of
temperature, current, and off-state voltage.

#### Dependencies

To enable this parameter, set **On-state behavior and switching
losses** to `Tabulate` and select the
**Include switching loss tabulation with off-state
voltage** parameter.

### **Off-state voltage vector for switching loss data, Vce** — Off-state voltage vector for switching loss data `[0, 150, 300]` `V` (default) | vector

*Since R2023b*

Off-state collector-emitter voltages at which you quote the switch-on loss
and switch-off loss.

#### Dependencies

To enable this parameter, set **On-state behavior and switching
losses** to `Tabulate` and select the
**Include switching loss tabulation with off-state
voltage** parameter.

### Integral Diode

### **Integral protection diode** — Integral protection diode `External diode` (default) | `Protection diode with no dynamics` | `Protection diode with charge dynamics`

Model that the IGBT (Ideal, Switching) block uses for the integral protection diode.
Choose one of these options:

- `External diode` — The IGBT (Ideal, Switching) does
  not model an integral protection diode. Use an external Diode block.
- `Diode with no dynamics` — The IGBT (Ideal, Switching)
  block models the integral protection diode using the same equations as
  the Diode block with no
  dynamics. Select this option to prioritize simulation speed.
- `Diode with charge dynamics` — The
  IGBT (Ideal, Switching) block models the integral protection diode using the same
  equations as the Diode block with
  charge dynamics. Select this option to prioritize detailed simulation
  results.

### **Diode model** — Diode model `Piecewise Linear` (default) | `Tabulated I-V curve`

Select one of these diode models:

- `Piecewise Linear` — Use a
  piecewise linear model for the diode, as described in Piecewise Linear Diode. This is the
  default method.
- `Tabulated I-V curve` — Use
  tabulated forward bias I-V data plus fixed reverse bias off
  conductance.

#### Dependencies

This parameter is visible only when the thermal port is exposed and the
**Integral protection diode** parameter is set to
`Protection diode with no dynamics` or
`Protection diode with charge dynamics`.

### **Table type** — Tabulated function `Table in If(Tj,Vf) form` (default) | `Table in Vf(Tj,If) form`

Whether to tabulate the current as a function of temperature and voltage or
the voltage as a function of temperature and current.

#### Dependencies

This parameter is visible only when the thermal port is exposed and the
**Integral protection diode** parameter is set to
`Protection diode with no dynamics` or
`Protection diode with charge dynamics` and
**Diode model** is set to `Tabulated I-V
curve`.

### **Reverse I-V characteristics type** — Type of reverse I-V characteristics `Specify off conductance` (default) | `Tabulate`

*Since R2024a*

Whether to specify the reverse I-V characteristics by using the diode off conductance or by tabulating the current as a function of temperature and voltage or the voltage as a function of temperature and current.

#### Dependencies

This parameter is visible only when the thermal port is exposed and the **Integral protection diode** parameter is set to `Diode with no dynamics` or `Diode with charge dynamics` and **Diode model** is set to `Tabulated I-V curve`.

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

To enable this parameter, expose the thermal port and set **Diode
model** to `Tabulated I-V curve` and
**Table type** to `Table in If(Tj,Vf)
form`.

### **Junction temperatures, Tj** — Vector of junction temperatures `[25, 125]` `degC` (default)

Vector of junction temperatures. This parameter must be a vector of at least
two elements.

#### Dependencies

To enable this parameter, expose the thermal port and set **Diode
model** to `Tabulated I-V
curve`.

### **Forward voltages, Vf** — Vector of forward voltages `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V` (default)

Vector of forward voltages. This parameter must be a vector of at least
three nonnegative values.

#### Dependencies

To enable this parameter, expose the thermal port and set **Diode
model** to `Tabulated I-V curve` and
**Table type** to `Table in If(Tj,Vf)
form`.

### **Forward voltages, Vf(Tj,If)** — Vector of forward voltages `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V` (default) | nonnegative vector

Forward voltages. This parameter must be a vector of at least three
nonnegative elements.

#### Dependencies

To enable this parameter, expose the thermal port and set **Diode
model** to `Tabulated I-V curve` and
**Table type** to `Table in Vf(Tj,If)
form`.

### **Forward currents, If** — Vector of forward currents `[.1, .2, .5, 1, 2, 4, 7, 10]` `A` (default)

Vector of forward currents. This parameter must be a vector of at least
three nonnegative values.

#### Dependencies

To enable this parameter, expose the thermal port and set **Diode
model** to `Tabulated I-V curve` and
**Table type** to `Table in Vf(Tj,If)
form`.

### **Reverse currents, Ir(Tj,Vr)** — Vector of reverse currents `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A` (default) | nonnegative vector

*Since R2024a*

Reverse currents. This parameter must be a vector of at least three nonnegative elements.

#### Dependencies

To enable this parameter, set:

- **Modeling option** to `Show thermal port`
- **Integral protection diode** to `Diode with no dynamics` or `Diode with charge dynamics`
- **Diode model** to `Tabulated I-V
  curve`
- **Table type** to `Table in If(Tj,Vf) form`
- **Reverse I-V characteristics** to `Tabulate`

### **Reverse voltages, Vr** — Vector of reverse voltages `[10, 20, 40, 50, 70, 80, 100]` `V` (default) | nonnegative vector

*Since R2024a*

Vector of reverse voltages. This parameter must be a vector of at least three nonnegative values.

#### Dependencies

To enable this parameter, set:

- **Modeling option** to `Show thermal port`
- **Integral protection diode** to `Diode with no dynamics` or `Diode with charge dynamics`
- **Diode model** to `Tabulated I-V
  curve`
- **Table type** to `Table in If(Tj,Vf) form`
- **Reverse I-V characteristics** to `Tabulate`

### **Reverse voltages, Vr(Tj,Ir)** — Vector of reverse voltages `[10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320]` `V` (default) | nonnegative vector

*Since R2024a*

Reverse voltages. This parameter must be a vector of at least three nonnegative elements.

#### Dependencies

To enable this parameter, set:

- **Modeling option** to `Show thermal port`
- **Integral protection diode** to `Diode with no dynamics` or `Diode with charge dynamics`
- **Diode model** to `Tabulated I-V
  curve`
- **Table type** to `Table in Vf(Tj,If) form`
- **Reverse I-V characteristics** to `Tabulate`

### **Reverse currents, Ir** — Vector of reverse currents `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A` (default) | nonnegative vector

*Since R2024a*

Vector of reverse currents. This parameter must be a vector of at least three nonnegative values.

#### Dependencies

To enable this parameter, set:

- **Modeling option** to `Show thermal port`
- **Integral protection diode** to `Diode with no dynamics` or `Diode with charge dynamics`
- **Diode model** to `Tabulated I-V
  curve`
- **Table type** to `Table in Vf(Tj,If) form`
- **Reverse I-V characteristics** to `Tabulate`

### **Off conductance** — Off conductance `1e-5` `1/Ohm` (default)

Conductance of the reverse-biased diode.

#### Dependencies

This parameter is visible only when the **Integral protection diode**
parameter is set to `Diode with no dynamics` or
`Diode with charge dynamics` and **Reverse I-V
characteristics type** is set to `Specify off
conductance`.

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

### Thermal Port

For more information about using thermal ports and the **Thermal
Port** parameters, see Simulating Thermal Effects in Semiconductors.

### **Separate thermal port for integral diode** — Option to separate thermal port for integral diode `off` (default) | `on`

*Since R2024b*

Whether to separate the thermal port for the integral protection diode of
the device.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Show thermal port` and, in the
**Integral Diode** section, set **Integral
protection diode** to `Diode with no
dynamics` or `Diode with charge
dynamics`.

### **Thermal network** — Options for thermal network modeling `External` (default) | `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

Options for modeling the thermal network of the block.

### **Thermal mass parameterization** — Option to parameterize thermal mass `By thermal time constants` (default) | `By thermal mass`

Options to parameterize the thermal mass:

- `By thermal time constants` — Parameterize
  the thermal masses in terms of thermal time constants.
- `By thermal mass` — Specify the thermal
  mass values directly.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Specify junction and case thermal parameters`,
`Cauer model`, or `Cauer model
parameterized with Foster coefficients`.

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — Junction case and case-ambient (or case-heatsink) thermal resistances `[.08, .5]` `K/W` (default) | vector of positive values

Row vector, [ *R\_JC*
*R\_CA* ], of two thermal resistance values, represented by two
Conductive Heat Transfer blocks. The first value, *R\_JC*, is
the thermal resistance between the junction and the case. The second value,
*R\_CA*, is the thermal resistance between port
**H** and the device case.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Specify junction and case thermal
parameters`.

### **Junction and case thermal time constants, [t\_J t\_C]** — Junction and case thermal time constants `[.001, .2]` `s` (default) | vector of positive values

Row vector, [ *t\_J*
*t\_C* ], of two thermal time constant values. The first value,
*t\_J*, is the junction time constant. The second value,
*t\_C*, is the case time constant.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Specify junction and case thermal parameters`
and **Thermal mass parameterization** to `By
thermal time constants`.

### **Junction and case thermal masses, [M\_J M\_C]** — Junction and case thermal masses `[.01, .5]` `J/K` (default) | vector of positive values

Row vector, [ *M\_J*
*M\_C* ], of two thermal mass values. The first value,
*M\_J*, is the junction thermal mass. The second value,
*M\_C*, is the case thermal mass.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Specify junction and case thermal parameters`
and **Thermal mass parameterization** to `By
thermal mass`.

### **Junction and case initial temperatures, [T\_J T\_C]** — Junction and case initial temperatures `[25, 25]` `degC` (default) | vector of positive values

Row vector, [ *T\_J* *T\_C* ], of two
temperature values. The first value, *T\_J*, is the junction
initial temperature. The second value, *T\_C*, is the case
initial temperature.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Specify junction and case thermal
parameters`.

### **Diode junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — Junction case and case-ambient (or case-heatsink) thermal resistances for integral diode `[.03, .2]` `K/W` (default) | vector of positive values

*Since R2024b*

Row vector, [ *R\_JC*
*R\_CA* ], of two thermal resistance values, represented by two
Conductive Heat Transfer blocks, for the integral protection diode. The first
value, *R\_JC*, is the thermal resistance between the junction
and the case. The second value, *R\_CA*, is the thermal
resistance between port **HDiode** and the diode case.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section, set
  **Integral protection diode** to
  `Diode with no dynamics` or
  `Diode with charge dynamics`.
- In the **Thermal Port** section:

  - Select the **Separate thermal port for integral
    diode** parameter.
  - Set **Thermal network** to
    `Specify junction and case thermal
    parameters`.

### **Thermal time constants of diode junction and case, [t\_J t\_C]** — Junction and case thermal time constants for integral diode `[.1, 5]` `s` (default) | vector of positive values

*Since R2024b*

Row vector, [ *t\_J*
*t\_C* ], of two thermal time constant values for the integral
protection diode. The first value, *t\_J*, is the junction time
constant. The second value, *t\_C*, is the case time constant.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section, set
  **Integral protection diode** to
  `Diode with no dynamics` or
  `Diode with charge dynamics`.
- In the **Thermal Port** section:

  - Select the **Separate thermal port for integral
    diode** parameter.
  - Set **Thermal network** to
    `Specify junction and case thermal
    parameters`.
  - Set **Thermal mass parameterization**
    to `By thermal time
    constants`.

### **Thermal masses of diode junction and case, [M\_J M\_C]** — Thermal masses of diode junction and case `[3, 25]` `J/K` (default) | vector of positive values

*Since R2024b*

Row vector, [ *M\_J*
*M\_C* ], of two thermal mass values for the integral
protection diode. The first value, *M\_J*, is the junction
thermal mass. The second value, *M\_C*, is the case thermal
mass.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section, set
  **Integral protection diode** to
  `Diode with no dynamics` or
  `Diode with charge dynamics`.
- In the **Thermal Port** section:

  - Select the **Separate thermal port for integral
    diode** parameter.
  - Set **Thermal network** to
    `Specify junction and case thermal
    parameters`.
  - Set **Thermal mass parameterization**
    to `By thermal mass`.

### **Initial temperatures of diode junction and case, [T\_J T\_C]** — Initial temperatures of diode junction and case `[25, 25]` `degC` (default) | vector of positive values

*Since R2024a*

Row vector, [ *T\_J* *T\_C* ], of two
temperature values for the integral protection diode. The first value,
*T\_J*, is the junction initial temperature. The second
value, *T\_C*, is the case initial temperature.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section, set
  **Integral protection diode** to
  `Diode with no dynamics` or
  `Diode with charge dynamics`.
- In the **Thermal Port** section:

  - Select the **Separate thermal port for integral
    diode** parameter.
  - Set **Thermal network** to
    `Specify junction and case thermal
    parameters`.

### **Thermal resistances, [R1 R2 … Rn]** — Thermal resistances `[.08, .1, .5]` `K/W` | `[.08, .14, .22, .16]` `K/W` | vector of positive values

Row vector of *n* thermal resistance values, represented by
the Cauer elements used in the thermal network.

If you set **Thermal network** to `Cauer
model`, the default value is `[.08, .1, .5]`.
If you set **Thermal network** to `Cauer model
parameterized with Foster coefficients`, the default value is
`[.08, .14, .22, .16]`.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Cauer model` or `Cauer model
parameterized with Foster coefficients`.

### **Thermal time constants, [t1 t2 … tn]** — Thermal time constants `[.001, .1, .2]` `s` | `[7e-05, .0007, .01, .08]` `s` | vector of positive values

Row vector of *n* thermal time constant values, where
*n* is the number of Cauer elements used in the thermal
network. The length of this vector must match the length of **Thermal
resistances, [R1 R2 … Rn]**. With this parameterization, the
thermal masses are computed as `Mi =
ti/Ri`, where
`Mi`,
`ti` and
`Ri` are the thermal mass,
thermal time, and thermal resistance for the ith
Cauer element (if you set **Thermal network** to
`Cauer model`) or Foster element (if you set
**Thermal network** to `Cauer model
parameterized with Foster coefficients`).

If you set **Thermal network** to `Cauer
model`, the default value is `[.001, .1, .2]`.
If you set **Thermal network** to `Cauer model
parameterized with Foster coefficients`, the default value is
`[7e-05, .0007, .01, .08]`.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Cauer model` or `Cauer model
parameterized with Foster coefficients`and **Thermal
mass parameterization** to `By thermal time
constants`.

### **Thermal masses, [M1 M2 … Mn]** — Thermal masses `[.01, .1, .5]` `J/K` | `[.001, .005, .05, .5]` `J/K` | vector of positive values

Row vector of *n* thermal mass values, where
*n* is the number of Cauer elements in the thermal
network.

If you set **Thermal network** to `Cauer
model`, the default value is `[.01, .1, .5]`.
If you set **Thermal network** to `Cauer model
parameterized with Foster coefficients`, the default value is
`[.001, .005, .05, .5]`.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Cauer model` or `Cauer model
parameterized with Foster coefficients` and
**Thermal mass parameterization** to `By
thermal mass`.

### **Thermal masses initial temperatures, [T1 T2 … Tn]** — Initial temperatures of thermal masses `[25, 25, 25]` `degC` (default) | vector of positive values

Row vector of temperature values that correspond to the temperature drop
across each thermal capacity in the model.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Cauer model`.

### **Diode thermal resistances, [R1 R2 … Rn]** — Thermal resistances for integral diode `[.03, .1, .2]` `K/W` | `[.03, .2]` `K/W` | vector of positive values

*Since R2024b*

Row vector of *n* thermal resistance values for the
integral protection diode, represented by the Cauer elements used in the
thermal network.

If you set **Thermal network** to `Cauer
model`, the default value is `[.03, .1, .2]`.
If you set **Thermal network** to `Cauer model
parameterized with Foster coefficients`, the default value is
`[.03, .2]`.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section, set
  **Integral protection diode** to
  `Diode with no dynamics` or
  `Diode with charge dynamics`.
- In the **Thermal Port** section:

  - Select the **Separate thermal port for integral
    diode** parameter.
  - Set **Thermal network** to
    `Cauer model` or
    `Cauer model parameterized with Foster
    coefficients`.

### **Diode thermal time constants, [t1 t2 … tn]** — Thermal time constants for integral diode `[.1, 1, 5]` `s` | `[1, 10]` `s` | vector of positive values

*Since R2024b*

Row vector of *n* thermal time constant values for the
integral protection diode, where *n* is the number of Cauer
elements used in the thermal network. The length of this vector must match the
length of **Diode thermal resistances, [R1 R2 … Rn]**. With
this parameterization, the thermal masses are computed as
`Mi =
ti/Ri`, where
`Mi`,
`ti` and
`Ri` are the thermal mass,
thermal time, and thermal resistance for the ith
Cauer element (if you set **Thermal network** to
`Cauer model`) or Foster element (if you set
**Thermal network** to `Cauer model
parameterized with Foster coefficients`).

If you set **Thermal network** to `Cauer
model`, the default value is `[.1, 1, 5]`. If
you set **Thermal network** to `Cauer model
parameterized with Foster coefficients`, the default value is
`[1, 10]`.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section, set
  **Integral protection diode** to
  `Diode with no dynamics` or
  `Diode with charge dynamics`.
- In the **Thermal Port** section:

  - Select the **Separate thermal port for integral
    diode** parameter.
  - Set **Thermal network** to
    `Cauer model` or
    `Cauer model parameterized with Foster
    coefficients`.
  - Set **Thermal mass parameterization**
    to `By thermal time
    constants`.

### **Diode thermal masses, [M1 M2 … Mn]** — Thermal masses for integral diode `[3, 10, 25]` `J/K` | `[33, 50]` `J/K` | vector of positive values

*Since R2024b*

Row vector of *n* thermal mass values for the integral
protection diode, where n is the number of Cauer elements in the thermal
network.

If you set **Thermal network** to `Cauer
model`, the default value is `[3, 10, 25]`. If
you set **Thermal network** to `Cauer model
parameterized with Foster coefficients`, the default value is
`[33, 50]`.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section, set
  **Integral protection diode** to
  `Diode with no dynamics` or
  `Diode with charge dynamics`.
- In the **Thermal Port** section:

  - Select the **Separate thermal port for integral
    diode** parameter.
  - Set **Thermal network** to
    `Cauer model` or
    `Cauer model parameterized with Foster
    coefficients`.
  - Set **Thermal mass parameterization**
    to `By thermal mass`.

### **Initial temperatures of diode thermal masses, [T1 T2 … Tn]** — Initial temperatures of diode thermal masses `[25, 25, 25]` `degC` (default) | vector of positive values

*Since R2024b*

Row vector of temperature values for the integral protection diode. This
parameter corresponds to the temperature drop across each thermal capacity in
the model.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section, set
  **Integral protection diode** to
  `Diode with no dynamics` or
  `Diode with charge dynamics`.
- In the **Thermal Port** section:

  - Select the **Separate thermal port for integral
    diode** parameter.
  - Set **Thermal network** to
    `Cauer model`.

### **Initial node temperatures, [T1 T2 ... Tn]** — Initial node temperatures `[25, 25, 25, 25]` `degC` (default) | vector of positive values

Row vector of the temperature values of each node starting from the
junction.

#### Dependencies

To enable this parameter, set **Thermal network** to
`Cauer model parameterized with Foster
coefficients`.

### **Diode initial node temperatures, [T1 T2 ... Tn]** — Initial node temperatures for integral diode `[25, 25, 25, 25]` `degC` (default) | vector of positive values

*Since R2024b*

Row vector of the temperature values of each node starting from the integral
protection diode junction.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section, set
  **Integral protection diode** to
  `Diode with no dynamics` or
  `Diode with charge dynamics`.
- In the **Thermal Port** section:

  - Select the **Separate thermal port for integral
    diode** parameter.
  - Set **Thermal network** to
    `Cauer model parameterized with Foster
    coefficients`.

### **Junction thermal mass** — Thermal mass of junction `0.01` `J/K` (default) | positive scalar

Thermal mass of the junction.

#### Dependencies

To enable this parameter, set **Thermal network** to
`External`.

### **Diode junction thermal mass** — Thermal mass of diode junction `0.1` `J/K` (default) | positive scalar

*Since R2024b*

Thermal mass of the diode junction.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section, set
  **Integral protection diode** to
  `Diode with no dynamics` or
  `Diode with charge dynamics`.
- In the **Thermal Port** section:

  - Select the **Separate thermal port for integral
    diode** parameter.
  - Set **Thermal network** to
    `External`.

## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

### R2024b: Separate thermal port for integral diode

You can now separate the thermal port for the integral protection diode of the
IGBT (Ideal, Switching) block from the **H** port. To separate the thermal ports:

- Set the **Modeling option** parameter to `Show
  thermal port`
- In the **Integral Diode** section, set the
  **Integral protection diode** parameter to
  `Diode with no dynamics` or `Diode with
  charge dynamics`.
- In the **Thermal port** section, select the
  **Separate thermal port for integral diode**
  parameter.

### R2024a: Model tabulated reverse I-V characteristics

You can now model the reverse I-V characteristics for the IGBT (Ideal, Switching) block by
tabulating the current as a function of temperature and voltage or the voltage as a
function of temperature and current.

Before R2024a, you can only model the reverse I-V characteristics by specifying the
off conductance of the reverse-biased diode.

### R2023b: Model a specific IGBT using built-in parameterizations

You can now parameterize the IGBT (Ideal, Switching) block by using built-in
parameterizations that represent components from specific suppliers. The
parameterizations of these ideal insulated-gate bipolar transistors (IGBTs) match the
manufacturer data sheets. To load a predefined parameterization, double-click the IGBT
(Ideal, Switching) block, click the **<click to
select>** hyperlink of the **Selected part** parameter,
and, in the Block Parameterization Manager window, select the part you want to use from
the list of available components.

### R2023b: Scale reverse recovery loss with current and voltage

You can now scale a fixed reverse recovery loss value with current and voltage. To
enable this option, select the **Scale reverse recovery loss with current and
voltage** parameter.

Models you create in R2023a or earlier default to no scaling for backward
compatibility.

### R2023b: Tabulate switching losses with temperature, current, and voltage

You can now tabulate switching losses with temperature, current, and voltage. In
earlier releases, you can tabulate switching losses with temperature and current
only.

To specify the losses as a function of the junction temperature, on-state current,
and off-state voltage, set the **On-state behavior and switching
losses** parameter to `Tabulate` and select the
**Include switching loss tabulation with off-state voltage**
parameter.

### R2023b: Determine switching losses for discontinuous load currents

The IGBT (Ideal, Switching) block now supports
discontinuous load currents.

The block supports discontinuous load currents by measuring the off-state voltage and
on-state current at all turn-on and turn-off events to compute switching losses. New
models behave this way by default. If you use a fixed-step solver, the shortest device
on or off period is now one step. Before R2023b, the minimum period is three steps. To
report switching losses, the minimum period is still three steps.

Before R2023b, the block measures the off-state voltage before turn-on and on-state
current before turn-off only.

You can still use the original method of measuring the off-state voltage before
turn-on and on-state current before turn-off in R2023b. Models you create in R2023a or
earlier default to this behavior for backward compatibility. The original method is
designed for inductive loads with continuous currents. Use the original method if you
are modeling capacitance across the switching device or switching device lead inductance:

- To model capacitance across the switching device, for example, if the
  parallel diode has capacitance or you are using the Lauritzen charge model,
  select the **Use last on-state current from previous cycle for turn-on
  loss** parameter.
- To model switching device lead inductance, select the **Use last
  off-state voltage from previous cycle for turn-off loss**
  parameter.

### R2023b: Plot basic I-V characteristics

You can now plot the basic I-V characteristics for the IGBT (Ideal, Switching) block,
based on the current block parameter values, without simulating the model.

To plot the basic characteristics, right-click the block and select
**Electrical** > **Basic
characteristics** from the context menu.

If you model the switching device with an integral protection diode, the
**Basic characteristics** option plots the I-V characteristics
for both the switching device and the diode. If you enable the thermal port of the
block, the **Basic characteristics** option also generates
surface plots of the turn-on energy loss and turn-off energy loss as functions of the
on-state current and off-state voltage.

### R2023a: Update on integral diode modeling options

From R2023a forward, you can model reverse recovery loss in the IGBT
(Ideal, Switching) block. To enable the **Reverse recovery
loss model** parameter, set the **Modeling option**
parameter to `Show thermal port` and set the **Integral
protection diode** parameter to `Diode with no
dynamics`.

### R2021a: Removal of energy dissipation time constant parameter

From R2021a forward, the **Energy dissipation time constant**
parameter of the IGBT (Ideal, Switching) block is no
longer used. A step in junction temperature now reflects the switching losses. If your
model contains a thermal mass directly connected to this block thermal port, remove it
and model the thermal mass inside the component itself.

### R2020b: Update on switching losses and thermal modeling options

From R2020b forward, the IGBT (Ideal, Switching) block
has improved losses and thermal modeling options.

As a result from these changes:

- Electrical and thermal on-state losses are now always identical. The
  **Thermal loss dependent on** parameter and its options,
  `Voltage and current` and `Voltage,
  current, and temperature`, have been renamed to
  **On-state behavior and switching losses**,
  `Specify constant values` and `Tabulate
  with temperature and current` :

  - If you selected `Voltage and current` for
    **Thermal loss dependent on**, then the electrical
    on-state losses are unchanged and their values are determined using
    the on-state resistance. However, the thermal on-state losses are now
    also determined by the on-state resistance. Prior to R2020b, the
    thermal on-state losses were defined by the product of the
    **On-state voltage** and **Output current,
    Iout** parameters.
  - If you selected `Voltage, current, and
    temperature` for **Thermal loss dependent
    on**, then the thermal on-state losses are unchanged and
    the **On-state voltage, Vds(Tj,Ice)** parameter sets
    their values. However, the electrical on-state losses are now equal to
    the thermal on-state losses. Prior to R2020b, the electrical on-state
    losses were defined by the value of the on-state resistance.
- The **On-state voltage** parameter is no longer
  used.

## Description

Ideal insulated-gate bipolar transistor for switching applications

The IGBT (Ideal, Switching) block models an ideal
insulated-gate bipolar transistor (IGBT) for switching applications. The switching
characteristic of an IGBT is such that if the gate-emitter voltage exceeds the specified
threshold voltage, *Vth*, the IGBT is in the on
state. Otherwise, the device is in the off state. This figure shows a typical
*i-v characteristic*:

To define the I-V characteristic of the IGBT, set the **On-state behavior and
switching losses** parameter to either `Specify constant
values` or `Tabulate`. The
`Tabulate` option is available only if you expose the thermal
port of the block.

In the on state, the collector-emitter path behaves like a linear diode with
forward-voltage drop, *Vf*, and on-resistance,
*Ron*. However, if you expose the thermal
port of the block and parameterize the device using tabulated I-V data, the tabulated
resistance is a function of the temperature and current.

In the off state, the collector-emitter path behaves like a linear resistor with a low
off-state conductance value, *Goff*.

The defining Simscape™ equations for the block
are:

```
     if (v>Vf)&&(G>Vth)
        i == (v - Vf*(1-Ron*Goff))/Ron;
     else
        i == v*Goff;
     end
```

where:

- *v* is the collector-emitter voltage.
- *Vf* is the forward voltage.
- *G* is the gate-emitter voltage.
- *Vth* is the threshold voltage.
- *i* is the collector-emitter current.
- *Ron* is the on-state resistance.
- *Goff* is the off-state conductance.

### Integral Protection Diode Option

Using the **Integral Diode** parameters, you can include an integral
emitter-collector diode. An integral diode protects the semiconductor device by
providing a conduction path for reverse current. An inductive load can produce a high
reverse-voltage spike when the semiconductor device suddenly switches off the voltage
supply to the load.

Set the **Integral protection diode** parameter based on your
goal.

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

You can also expose the thermal port
**HDiode** of the integral protection diode by selecting the
**Separate thermal port for integral diode** parameter. If
you do not expose the diode thermal port, both the device and the diode share the
common thermal port, **H**. *(since R2024b)*

For more information about using thermal ports, see Simulating Thermal Effects in Semiconductors.

### Thermal Losses

The figure shows an idealized representation of the output voltage,
*V*out, and the output current,
*I*out, of the semiconductor device. The
interval in this figure includes the entire *n*th switching cycle,
during which the block turns off and then on.

Switching losses are major sources of thermal loss in semiconductors. During each
on-off switching transition, the IGBT parasitics store and then dissipate energy.

Switching losses depend on the off-state voltage and the on-state current. When a
switching device turns on, the power losses depend on the initial off-state voltage
across the device and the final on-state current when the device is in its fully on
state. Similarly, when a switching device turns off, the power losses depend on the
initial on-state current through the device and the final off-state voltage across the
device in the fully off state.

You can choose when to measure the current and voltage that the block uses to
calculate the switch-on and switch-off losses. For most circuits, you can make the
measurements during the turn-on or turn-off event:

- The switch-on loss is
  *E*on*(I*TurnOn*(n),V*TurnOn*(n))*
- The switch-off loss is
  *E*off*(I*TurnOff*(n),V*TurnOff*(n))*

However, you cannot always use these measurements, for example, in these situations:

- You are modeling a capacitance across the switching device. For example, you
  are modeling the protection diode with capacitance or you are using the
  Lauritzen charge model. The capacitance causes an overshoot transient in the
  current at device turn-on, which means that you cannot use the measurement
  *I*TurnOn*(n)* to
  calculate the switch-on loss. The block requires the value following the
  transient. Do not model capacitance across the switching device, because this
  model mixes an abstracted behavior for the semiconductor switching device with
  detailed physics for the diode. If you must model capacitance across the
  switching device, you can use the current measurement at the end of the last
  on-period,
  *I*TurnOff*(n-1)*.
  To enable this option, select the **Use last on-state current from
  previous cycle for turn-on loss** parameter.
- You are modeling switching device lead inductance. The inductance causes an
  overshoot transient in the voltage at device turn-off, which means that you
  cannot use the measurement
  *V*TurnOff*(n)* to
  calculate the switch-off loss. The block requires the value following the
  transient. Do not model switching device lead inductance, because the time
  constant associated with lead inductance is typically much smaller than the
  pulse-width modulation (PWM) period. This smaller time constant means that the
  simulation requires smaller simulation time steps, slowing down the simulation.
  If you must model switching device lead inductance, use the voltage measurement
  at the end of the last off-period,
  *V*TurnOn*(n)*. To
  enable this option, select the **Use last off-state voltage from
  previous cycle for turn-off loss** parameter.

Examine the simulation results to check that the losses behave as you expect. To
learn how to log and plot simulation data, see the Log and Plot Simulation Data
example. This table defines the names of variables in the logged simulation data that
are relevant to switching loss calculations.

**Voltages and Currents Used to Calculate Switching Losses**

| Quantity | Variable Name in Logged Simulation Data |
| --- | --- |
| *V*TurnOn | `zvOn` |
| *I*TurnOn | `ziOn` |
| *V*TurnOff | `zvOff` |
| *I*TurnOff | `ziOff` |

This block applies switching losses by stepping up the junction temperature with a
value equal to the switching loss divided by the total thermal mass at the junction. You
must specify the energy dissipated during a single switch-on and switch-off event. You
must also specify the corresponding values of the off-state voltage and on-state current
at which you quote the losses. You can parameterize the switching losses, depending on
the data you have. Use tabulated data if they are available.

- To specify a scalar value for the switching losses, set the
  **On-state behavior and switching losses** parameter to
  `Specify constant values`. The **Switch-on
  loss** and **Switch-off loss** parameter values
  set the sizes of the switching losses. The block scales the losses by the
  off-state voltage and the on-state current.
- To specify the losses as a function of the junction temperature and on-state
  current at a fixed off-state voltage, set the **On-state behavior and
  switching losses** parameter to `Tabulate`
  and clear the **Include switching loss tabulation with off-state
  voltage** parameter. The **Switch-on loss,
  Eon(Tj,Ice)** and **Switch-off, Eoff(Tj,Ice)**
  parameters set the size of the losses. The block scales the losses by the
  off-state voltage.
- To specify the losses as a function of the junction temperature, on-state
  current, and off-state voltage, set the **On-state behavior and
  switching losses** parameter to `Tabulate`
  and select the **Include switching loss tabulation with off-state
  voltage** parameter.

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

For all ideal switching devices, the logged simulation data reports the thermal
losses as `lastTurnOffLoss`, `lastTurnOnLoss`, and
`lastReverseRecoveryLoss`. These variables record losses as a
pulse with an amplitude equal to the energy loss. If you use a script to sum the
total losses over a defined simulation period, you must sum the pulse values at each
pulse rising edge. Alternatively, you can extract conduction and switching losses
from logged data using the `ee_getPowerLossSummary` and `ee_getPowerLossTimeSeries` functions.

You can also access the total accumulated switching losses from the
`accumulatedSwitchingLosses` variable in the logged simulation
data. This variable sums all switching losses to date, including reverse recovery
losses for the diode.

The `power_dissipated` variable in the logged simulation data
does not include switching losses or reverse recovery losses because the block models
these losses as instantaneous events. The `power_dissipated`
variable reports ohmic on-state losses.

If you are using a fixed-step solver, the shortest pulse on or pulse off that
supports capture of the switching losses is three time steps long. If the pulse is
shorter than three steps, the block does not report switching losses.

If you use tabulated data to model the switching losses or reverse recovery
losses, check that the temperature, current, and voltage are in the range you
specify. If you do not define a realistic thermal model, for example, if the junction
mass or the conductance from the junction to the case is too small, the temperature
can exceed the range you specify, causing the block to extrapolate the losses to
nonphysical values.

### Parameterization

*Since R2023b*

The IGBT (Ideal, Switching) block supports multiple
predefined parameterizations.

Use this parameterization data to represent components by specific suppliers. The
parameterizations of these IGBTs match the manufacturer data sheets. To load a
predefined parameterization, double-click the IGBT( Ideal, Switching) block, click the
**<click to select>** hyperlink of the
**Selected part** parameter, and, in the Block Parameterization
Manager window, select the part you want to use from the list of available
components.

**Note**

The predefined parameterizations of Simscape components use available data sources for the parameter values. Engineering
judgment and simplifying assumptions are used to fill in for missing data. As a result,
expect deviations between simulated and actual physical behavior. To ensure accuracy,
validate the simulated behavior against experimental data and refine component models as
necessary.

For more information about predefined parameterization and a list of the available
components, see List of Pre-Parameterized Components.

You can also use the `ee_importDeviceParameters` function to extract the device parameters from
an XML file and import them into the block. The XML file must be on the MATLAB® path and must use a parameterization format supported by Hitachi or
Infineon®.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

### Plot Basic I-V Characteristics

*Since R2023b*

You can plot the basic I-V characteristics of the IGBT (Ideal, Switching) block without building a
complete model. Use the plots to explore the impact of your
parameter choices on device characteristics. If you parameterize the
block from a data sheet, you can compare your plots to the data
sheet to check that you parameterized the block correctly. If you
have a complete working model but do not know which manufactured
part to use, you can compare your plots to data sheets to help you
decide.

To plot the basic characteristics, right-click the block and select **Electrical** > **Basic characteristics** from the context menu.

The **Basic characteristics** option generates different plots
depending on the values you specify for the **Modeling option**,
**On-state behavior and losses**, and **Integral protection
diode** parameters of the IGBT (Ideal, Switching) block. If you model the switching device
with an integral protection diode, the **Basic characteristics**
option plots the I-V characteristics for both the switching device and the diode. If you
enable the thermal port of the block, the **Basic characteristics**
option also generates surface plots of the turn-on energy loss and turn-off energy loss as
functions of the on-state current and off-state voltage. For more information about this
option, see Plot Basic I-V Characteristics of Semiconductor Blocks.
