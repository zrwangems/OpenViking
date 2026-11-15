---
type: simulink-block
title: 'Four-Quadrant Chopper'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Converters / Converters, Inverters, Rectifiers, and Choppers'
documentation_page: 'fourquadrantchopper'
documentation_source_path: 'ref/fourquadrantchopper.html'
language: en
---

# Four-Quadrant Chopper

## Ports

### Conserving

### **G** — Switching device gate control electrical | vector

Electrical conserving port associated with the gate terminals of the
switching devices.

**Data Types:** `double`

### **1+** — Positive DC voltage 1 electrical | scalar

Electrical conserving port associated with the positive terminal of
the first DC voltage.

**Data Types:** `double`

### **1-** — Negative DC voltage 1 electrical | scalar

Electrical conserving port associated with the negative terminal of
the first DC voltage.

**Data Types:** `double`

### **2+** — Positive DC voltage 2 electrical | scalar

Electrical conserving port associated with the positive terminal of
the second DC voltage.

**Data Types:** `double`

### **2-** — Negative DC voltage 2 electrical | scalar

Electrical conserving port associated with the negative terminal of
the second DC voltage.

**Data Types:** `double`

### **H** — Thermal port thermal

*Since R2024b*

Thermal conserving port associated with the thermal mass of the
switching devices.

#### Dependencies

To enable this port:

- In the **Main** settings, set
  the **Fidelity level** parameter to
  `Detailed model - switching
  devices`.
- In the **Switching Devices**
  settings, set the **Switching device**
  parameter to one of these options:

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- In the **Switching Devices**
  settings, select the **Model thermal
  effects** parameter.

## Parameters

### Main

### **Fidelity level** — Fidelity level `Detailed model - switching devices` (default) | `Equivalent model - PWM-controlled`

*Since R2024a*

Level of fidelity of the model.

To prioritize simulation accuracy or to obtain results for the
individual switching devices, set this parameter to
`Detailed model - switching
devices`.

To prioritize simulation speed, set this parameter to `Equivalent model -
PWM-controlled`.

### Switching Devices

To enable these parameters, set **Fidelity level** to
`Detailed model - switching devices`.

This table shows how the visibility of **Switching Devices** parameters
depends on the switching devices that you select. To learn how to read the table,
see Parameter Dependencies.

**Switching Devices Parameter Dependencies**

| Parameters and Options | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Switching device** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| On-state resistance | Model thermal effects | Model thermal effects | Model thermal effects | Model thermal effects | On-state resistance |
| Gate trigger voltage, Vgt | Gate trigger voltage, Vgt |
| Gate turn-off voltage, Vgt\_off | Gate turn-off voltage, Vgt\_off |
| Holding current | Holding current |
| Forward voltage | Forward voltage | Forward voltage |
| On-state resistance | On-state resistance | Drain-source on resistance | On-state resistance |
| Off-state conductance | Off-state conductance | Off-state conductance | Off-state conductance | Off-state conductance | Integer for piecewise constant approximation of gate input (0 for disabled) |
| Threshold voltage | Threshold voltage | Threshold voltage |

### **Switching device** — Switch type `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

Switching device type for the converter.

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Model thermal effects** — Option to model thermal effects `Off` (default) | `On`

Option to model thermal effects.

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Gate trigger voltage, Vgt** — Voltage threshold `1` `V` (default) | scalar

Gate-cathode voltage threshold. The device turns on when the
gate-cathode voltage is above this value.

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Gate turn-off voltage, Vgt\_off** — Voltage threshold `-1` `V` (default) | scalar

Gate-cathode voltage threshold. The device turns off when the
gate-cathode voltage is below this value.

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Holding current** — Current threshold `1` `A` (default) | scalar

Gate current threshold. The device stays on when the current is above
this value, even when the gate-cathode voltage falls below the gate
trigger voltage.

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Forward voltage** — Voltage `0.8` `Ohm` (default) | scalar

For the different switching device types, the **Forward
voltage** is taken as:

- GTO — Minimum voltage required across the anode and
  cathode block ports for the gradient of the device I-V
  characteristic to be
  1/*Ron*, where
  *Ron* is the
  value of **On-state resistance**
- IGBT — Minimum voltage required across the collector and
  emitter block ports for the gradient of the diode I-V
  characteristic to be
  1/*Ron*, where
  *Ron* is the
  value of **On-state resistance**
- Thyristor — Minimum voltage required for the device to
  turn on

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **On-state resistance** — Resistance `0.001` `Ohm` (default) | scalar

For the different switching device types, the **On-state
resistance** is taken as:

- GTO — Rate of change of voltage versus current above the
  forward voltage
- Ideal semiconductor switch — Anode-cathode resistance when
  the device is on
- IGBT — Collector-emitter resistance when the device is
  on
- Thyristor — Anode-cathode resistance when the device is
  on
- Averaged switch — Anode-cathode resistance when the device
  is on

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Drain-source on resistance** — Resistance `0.001` `Ohm` (default) | scalar

Resistance between the drain and the source, which also depends on the
gate-to-source voltage.

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Off-state conductance** — Conductance `1e-5` `1/Ohm` (default) | scalar

Conductance when the device is off. The value must be less than
1/*R*, where *R* is the value of
**On-state resistance**.

For the different switching device types, the **On-state
resistance** is taken as:

- GTO — Anode-cathode conductance
- Ideal semiconductor switch — Anode-cathode
  conductance
- IGBT — Collector-emitter conductance
- MOSFET — Drain-source conductance
- Thyristor — Anode-cathode conductance

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Threshold voltage** — Voltage threshold `6` `V` (default) | scalar

Gate voltage threshold. The device turns on when the gate voltage is
above this value. For the different switching device types, the device
voltage of interest is:

- Ideal semiconductor switch — Gate-cathode voltage
- IGBT — Gate-emitter voltage
- MOSFET — Gate-source voltage

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — Integer mode for FPGA deployment `0` (default) | nonnegative scalar

Integer used to perform piecewise constant approximation of the gate input for FPGA
deployment.

#### Dependencies

To enable this parameter, set **Switching device** to `Averaged Switch`.

### Switching Losses

To enable these parameters:

- In the **Main** settings, set the
  **Fidelity level** parameter to
  `Detailed model - switching
  devices`.
- In the **Switching Devices** settings, set the
  **Switching device** parameter to one of these options:

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- In the **Switching Devices** settings, select
  the **Model thermal effects** parameter.

This table shows how the visibility of **Switching
Loss** parameters depends on the **Switching device**
parameter in the **Switching Devices** settings. To learn how
to read the table, see Parameter Dependencies.

**Switching Losses Parameter Dependencies**

| Parameters and Options | | | |
| --- | --- | --- | --- |
| **Switching device** | | | |
| *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* |
| Switch-on loss | Switch-on loss | Switch-on loss | Switch-on loss |
| Switch-off loss | Switch-off loss | Switch-off loss |
| Natural commutation rectification loss | Natural commutation rectification loss |
| Off-state voltage for switching loss data | Off-state voltage for switching loss data | Off-state voltage for switching loss data | Off-state voltage for switching loss data |
| On-state current for switching loss data | On-state current for switching loss data | On-state current for switching loss data | On-state current for switching loss data |
| Wait time before switch-on current measurement | Wait time before switch-on current measurement |
| Use last on-state current from previous cycle for turn-on loss | Use last on-state current from previous cycle for turn-on loss | Use last on-state current from previous cycle for turn-on loss |
| Use last off-state voltage from previous cycle for turn-on loss | Use last on-state current from previous cycle for turn-on loss | Use last on-state current from previous cycle for turn-on loss |

### **Switch-on loss** — Switch-on loss `22.86e-3` `J` (default) | positive scalar

*Since R2024b*

Energy dissipated during a single switch-on event.

#### Dependencies

To enable this parameter, set **Switching
Device** to `GTO`,
`IGBT`,
`MOSFET`, or
`Thyristor`.

### **Switch-off loss** — Switch-off loss `17.14e-3` `J` (default) | positive scalar

*Since R2024b*

Energy dissipated during a single switch-off event.

#### Dependencies

To enable this parameter, set **Switching
Device** to `GTO`,
`IGBT`, or
`MOSFET`.

### **Natural commutation rectification loss** — Natural commutation rectification loss `10e-3` `J` (default) | positive scalar

*Since R2024b*

Rectification loss that applies when the current falls below the **Holding
current** parameter value and the block switches
off.

#### Dependencies

To enable this parameter, set **Switching
Device** to `GTO` or
`Thyristor`.

### **Off-state voltage for switching loss data** — Off-state voltage for loss data `300` `V` (default) | positive scalar

*Since R2024b*

Output voltage of the device during the off state. This value is the
blocking voltage at which you define the switch-on loss and switch-off
loss data.

#### Dependencies

To enable this parameter, set **Switching
Device** to `GTO`,
`IGBT`,
`MOSFET`, or
`Thyristor`.

### **On-state current for switching loss data** — Output current `600` `A` (default) | positive scalar

*Since R2024b*

Output current at which you define the switch-on loss and switch-off
loss.

**Note**

The block measures this parameter at the point that the gate
voltage falls below the **Gate trigger voltage,
Vgt** parameter value. The turn-on pulse is longer than
the time it takes the current to reach its maximum value.

#### Dependencies

To enable this parameter, set **Switching
Device** to `GTO`,
`IGBT`,
`MOSFET`, or
`Thyristor`.

### **Wait time before switch-on current measurement** — Wait time before switch-on current measurement `0` `s` (default) | nonnegative scalar

*Since R2024b*

Time to wait before recording the on-state current.

#### Dependencies

To enable this parameter, set **Switching
Device** to `GTO` or
`Thyristor`.

### **Use last on-state current from previous cycle for turn-on loss** — Option to use last on-state current from previous cycle for turn-on loss `Off` (default) | `On`

*Since R2024b*

Option to use the last on-state current from previous cycle for
turn-on loss.

#### Dependencies

To enable this parameter, set **Switching
Device** to `GTO`,
`IGBT`, or
`MOSFET`.

### **Use last off-state current from previous cycle for turn-offloss** — Option to use last off-state current from previous cycle for turn-off loss `Off` (default) | `On`

*Since R2024b*

Option to use the last off-state current from previous cycle for
turn-off loss.

#### Dependencies

To enable this parameter, set **Switching
Device** to `GTO`,
`IGBT`, or
`MOSFET`.

### Protection Diodes

To enable these parameters, set **Fidelity level** to
`Detailed model - switching devices`.

The visibility of the **Diode** parameters depends on how you configure
the **Model dynamics** and **Reverse recovery time
parameterization** parameters. To learn how to read this table, see
Parameter Dependencies.

**Protection Diodes Parameter Dependencies**

| Parameters and Options | | | | |
| --- | --- | --- | --- | --- |
| **Model dynamics** | | | | |
| *None* | *Diode with no dynamics* | *Diode with charge dynamics* | | |
| Forward voltage | Forward voltage | | |
| On resistance | On resistance | | |
| Off conductance | Off conductance | | |
| Junction capacitance | | |
| Peak reverse current, iRM | | |
| Initial forward current when measuring iRM | | |
| Rate of change of current when measuring iRM | | |
| **Reverse recovery time parameterization** | | |
| *`Specify stretch factor`* | *`Specify reverse recovery time directly`* | *`Specify reverse recovery charge`* |
| Reverse recovery time stretch factor | Reverse recovery time, trr | Reverse recovery charge, Qrr |

**Note**

If you set the **Switching device** parameter to
`Averaged Switch`, the block models protection
diodes with no dynamics and the **Model dynamics**
parameter is not visible.

### **Model dynamics** — Diode model `None` (default) | `Diode with no dynamics` | `Diode with charge dynamics`

Model that the Four-Quadrant Chopper block uses for the protection diode for each switching
device. Choose one of these options:

- `None` — The Four-Quadrant Chopper does not
  model protection diodes.
- `Diode with no dynamics` — The
  Four-Quadrant Chopper block models protection diodes using the same
  equations as the Diode
  block with no dynamics. Select this option to prioritize
  simulation speed.
- `Diode with charge dynamics` —
  The Four-Quadrant Chopper block models protection diodes using the
  same equations as the Diode
  block with charge dynamics. Select this option to prioritize
  detailed simulation results.

#### Dependencies

See the Protection Diodes Parameter Dependencies table.

### **Forward voltage** — Forward Voltage `0.8` `V` (default) | scalar

Minimum voltage required across the positive and negative block ports
for the gradient of the diode I-V characteristic to be
1/*Ron*, where
*Ron* is the value of
the **On resistance** parameter.

#### Dependencies

See the Protection Diodes Parameter Dependencies table.

### **On resistance** — On resistance `0.001` `Ohm` (default) | scalar

Rate of change of voltage versus current above the **Forward
voltage** parameter value.

#### Dependencies

See the Protection Diodes Parameter Dependencies table.

### **Off conductance** — Off conductance `1e-5` `1/Ohm` (default) | scalar

Conductance of the reverse-biased diode.

#### Dependencies

See the Protection Diodes Parameter Dependencies table.

### **Reverse recovery loss model** — Model for reverse recovery loss `Fixed loss` (default) | `Tabulated loss`

*Since R2024b*

Whether to model fixed or tabulated reverse recovery losses.

#### Dependencies

To enable this parameter:

- Set the **Switching device**
  parameter to one of these options:

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- Select the **Model thermal effects
  parameter** parameter.
- Set **Integral protection diode** to
  `Diode with no
  dynamics`.

### **Reverse recovery loss** — Reverse recovery loss `0` `J` (default) | nonnegative scalar

*Since R2024b*

Dissipated energy in each turn-off event. The block dissipates this energy regardless of
the state of the diode before or after the switching event.

#### Dependencies

To enable this parameter:

- Set the **Switching device**
  parameter to one of these options:

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- Select the **Model thermal effects
  parameter** parameter.
- Set **Integral protection diode** to
  `Diode with no
  dynamics`.
- Set **Reverse recovery loss model**
  to `Fixed loss`.

### **Scale reverse recovery loss with current and voltage** — Option to scale reverse recovery loss `On` (default) | `Off`

*Since R2024b*

Option to scale reverse recovery loss with current and voltage.

#### Dependencies

To enable this parameter:

- Set the **Switching device**
  parameter to one of these options:

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- Select the **Model thermal effects
  parameter** parameter.
- Set **Integral protection diode** to
  `Diode with no
  dynamics`.
- Set **Reverse recovery loss model**
  to `Fixed loss`.

### **Forward current when measuring recovery loss, Irec** — Forward current when block measures recovery loss `10` `A` (default) | positive scalar

*Since R2024b*

Forward current through the diode before the reverse recovery event
that the block uses to measure recovery loss.

#### Dependencies

To enable this parameter:

- Set the **Switching device**
  parameter to one of these options:

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- Select the **Model thermal effects
  parameter** parameter.
- Set **Integral protection diode** to
  `Diode with no
  dynamics`.
- Set **Reverse recovery loss model**
  to `Fixed loss`.
- Select the **Scale reverse recovery loss with
  current and voltage** parameter.

### **Turn-off voltage when measuring recovery loss, Vrec** — Turn-off voltage when measuring recovery loss `10` `V` (default) | positive scalar

*Since R2024b*

Voltage across the diode after the reverse recovery event that the block uses to measure
recovery loss.

#### Dependencies

To enable this parameter:

- Set the **Switching device** parameter to one of these options:

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- Select the **Model thermal effects
  parameter** parameter.
- Set **Integral protection diode** to
  `Diode with no
  dynamics`.
- Choose from one of these options:

  - Set **Reverse recovery loss
    model** to `Fixed
    loss` and select the **Scale
    reverse recovery loss with current and
    voltage** parameter.
  - Set the **Reverse recovery loss
    model** parameter to
    `Tabulated loss`.

### **Filter time constant for voltage and current values** — Filter time constant for voltage and current values `1 / 1000 / 100` `s` (default) | positive scalar

*Since R2024b*

Filter time constant for the voltage and current values that the block uses to calculate
reverse recovery loss. Set this parameter to a value that is lower than
the fastest switching period.

#### Dependencies

To enable this parameter:

- Set the **Switching device** parameter to one of these options:

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- Select the **Model thermal effects
  parameter** parameter.
- Set **Integral protection diode** to
  `Diode with no
  dynamics`.
- Choose from one of these options:

  - Set **Reverse recovery loss
    model** to `Fixed
    loss` and select the **Scale
    reverse recovery loss with current and
    voltage** parameter.
  - Set the **Reverse recovery loss
    model** parameter to
    `Tabulated loss`.

### **Reverse recovery loss table, Erec(Tj, If)** — Reverse recovery loss `zeros(2, 3)` `J` (default) | vector of nonnegative scalars

*Since R2024b*

Dissipated energy as a function of the forward current
*If* just before the switching event, and final
off-state voltage once the diode is in off state.

#### Dependencies

To enable this parameter:

- Set the **Switching device** parameter to one of these options:

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- Select the **Model thermal effects
  parameter** parameter.
- Set **Integral protection diode** to
  `Diode with no
  dynamics`.
- Set the **Reverse recovery loss
  model** parameter to `Tabulated
  loss`.

### **Temperature vector for recovery loss table, Tj** — Temperature vector for recovery loss table `[298.15, 398.15]` `K` (default) | vector

*Since R2024b*

Temperature vector that the block uses to tabulate the reverse recovery loss.

#### Dependencies

To enable this parameter:

- Set the **Switching device** parameter to one of these options:

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- Select the **Model thermal effects
  parameter** parameter.
- Set **Integral protection diode** to
  `Diode with no
  dynamics`.
- Set the **Reverse recovery loss
  model** parameter to `Tabulated
  loss`.

### **Forward current vector for recovery loss table, If** — Forward current vector for recovery loss table `[.1, 1, 10]` `A` (default) | vector of nonnegative scalars

*Since R2024b*

Forward current vector that the block uses to tabulate reverse
recovery loss.

#### Dependencies

To enable this parameter:

- Set the **Switching device** parameter to one of these options:

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- Select the **Model thermal effects
  parameter** parameter.
- Set **Integral protection diode** to
  `Diode with no
  dynamics`.
- Set the **Reverse recovery loss
  model** parameter to `Tabulated
  loss`.

### **Junction capacitance** — Junction capacitance `50` `nF` (default) | scalar

Diode junction capacitance.

#### Dependencies

See the Protection Diodes Parameter Dependencies table.

### **Peak reverse current, iRM** — Peak reverse current `-235` `A` (default) | negative scalar

Peak reverse current measured by an external test circuit.

#### Dependencies

See the Protection Diodes Parameter Dependencies table.

### **Initial forward current when measuring iRM** — Initial forward current when measuring iRM `300` `A` (default) | positive scalar

Initial forward current when measuring peak reverse current.

#### Dependencies

See the Protection Diodes Parameter Dependencies table.

### **Rate of change of current when measuring iRM** — Current change rate `-50` `A/us` (default) | scalar

Rate of change of current when measuring peak reverse current.

#### Dependencies

See the Protection Diodes Parameter Dependencies table.

### **Reverse recovery time parameterization** — Recovery-time model `Specify stretch factor` (default) | `Specify reverse recovery time directly` | `Specify reverse recovery charge`

Model for parameterizing the recovery time. When you select
`Specify stretch factor` or
`Specify reverse recovery charge`, you can
specify a value that the block uses to derive the reverse recovery time.
For more information on these options, see How the Block Calculates TM and Tau.

#### Dependencies

See the Protection Diodes Parameter Dependencies table.

### **Reverse recovery time stretch factor** — Reverse recovery time stretch factor `3` (default) | scalar greater than `1`

Stretch factor that the block uses to calculate the reverse recovery
time. Specifying the stretch factor is an easier way to parameterize the
reverse recovery time than specifying the reverse recovery charge. The
larger the value of the stretch factor, the longer it takes for the
reverse recovery current to dissipate.

#### Dependencies

See the Protection Diodes Parameter Dependencies table.

### **Reverse recovery time, trr** — Reverse recovery time `15` `us` (default) | scalar

Interval between the time when the current initially goes to zero
(when the diode turns off) and the time when the current falls to less
than 10 percent of the peak reverse current.

The value of the **Reverse recovery time, trr**
parameter must be greater than the value of the **Peak reverse
current, iRM** parameter divided by the value of the
**Rate of change of current when measuring iRM**
parameter.

#### Dependencies

See the Protection Diodes Parameter Dependencies table.

### **Reverse recovery charge, Qrr** — Reverse recovery charge `1500` `s*uA` (default) | scalar

Reverse recovery charge that the block uses to calculate the reverse
recovery time. Use this parameter if the data sheet for your diode
device specifies a value for the reverse recovery charge instead of a
value for the reverse recovery time.

The reverse recovery charge is the total charge that continues to
dissipate when the diode turns off. The value must be less than −i2RM2a, where:

- *iRM* is the value
  specified for **Peak reverse current,
  iRM**.
- *a* is the value specified for **Rate
  of change of current when measuring iRM**.

#### Dependencies

See the Protection Diodes Parameter Dependencies table.

### Snubbers

To enable these parameters, set **Fidelity level** to
`Detailed model - switching devices` and
**Switching device** to one of these options:

- `Ideal Semiconductor Switch`
- `GTO`
- `IGBT`
- `MOSFET`
- `Thyristor`

### **Snubber** — Snubber model `None` (default) | `RC snubber`

Switching device snubber.

### **Snubber resistance** — Resistance `0.1` `Ohm` (default) | scalar

Resistance of the switching device snubber.

#### Dependencies

To enable this parameter, set **Snubber** to `RC
Snubber`.

### **Snubber capacitance** — Capacitance `1e-7` (default) | `F` | scalar

Capacitance of the switching device snubber.

#### Dependencies

To enable this parameter, set **Snubber** to `RC
Snubber`.

### Thermal Port

To enable these parameters:

- In the **Main** settings, set the
  **Fidelity level** parameter to
  `Detailed model - switching
  devices`.
- In the **Switching Devices** settings, set the
  **Switching device** parameter to one of these options:

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- In the **Switching Devices** settings, select
  the **Model thermal effects** parameter.

For more information about using thermal ports and the
**Thermal Port** parameters, see Simulating Thermal Effects in Semiconductors.

### **Thermal network** — Options for thermal network modeling `External` (default) | `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

*Since R2024b*

Options for modeling the thermal network of the block.

### **Thermal mass parameterization** — Option to parameterize thermal mass `By thermal time constants` (default) | `By thermal mass`

*Since R2024b*

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

*Since R2024b*

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

*Since R2024b*

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

*Since R2024b*

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

*Since R2024b*

Row vector, [ *T\_J* *T\_C* ], of two temperature
values. The first value, *T\_J*, is the junction initial
temperature. The second value, *T\_C*, is the case
initial temperature.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Specify junction and case thermal
parameters`.

### **Thermal resistances, [R1 R2 … Rn]** — Thermal resistances `[.08,.1,.5]` `K/W` | `[.08,.14,.22,.16]` `K/W` | vector of positive values

*Since R2024b*

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

*Since R2024b*

Row vector of *n* thermal mass values, where *n* is
the number of Cauer elements in the thermal network.

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

*Since R2024b*

Row vector of temperature values that correspond to the temperature
drop across each thermal capacity in the model.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Cauer model`.

### **Thermal time constants, [t1 t2 … tn]** — Thermal time constants `[.001,.1,.2]` `s` | `[7e-05, .0007, .01, .08]` `s` | vector of positive values

*Since R2024b*

Row vector of *n* thermal time constant values, where
*n* is the number of Cauer elements in the thermal
network. The length of this vector must match the length of
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

*Since R2024b*

Row vector of the temperature values of each node starting from the
junction.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Cauer model parameterized with Foster
coefficients`.

### **Junction thermal mass** — Thermal mass of junction `0.01` `J/K` (default) | positive scalar

*Since R2024b*

Thermal mass of the junction.

#### Dependencies

To enable this parameter, set **Thermal network**
to `External`.

## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024b: Model thermal effects by using the thermal port

You can now use the thermal port to model the effects of generated heat and device
temperature. When you expose the thermal port, the Four-Quadrant Chopper block models the
conduction losses and the turn-on and turn-off losses of the switching devices. If
you enable the thermal port and you set the **Integral protection
diode** parameter to `Diode with no dynamics`,
the block also models reverse recovery loss of the protection diodes.

### R2024a: Increase simulation speed using an equivalent model

You can now choose from two fidelity levels for the converter model. The
equivalent model option does not model the individual switching devices but returns
equivalent results. If you need detailed results for the switching device dynamics,
use the detailed model option. Otherwise, use the equivalent model for faster
simulation. To simulate in real time, use the equivalent model. To validate the
results, use the detailed model with a variable-step solver.

To use the detailed model, set the **Fidelity level** parameter
to `Detailed model - switching devices`. To use the
equivalent model, set the **Fidelity level** parameter to
`Equivalent model - PWM-controlled`.

Before R2024a, you can use the detailed model only.

## Description

Controller-driven four quadrant DC-DC chopper

The Four-Quadrant Chopper block represents a four-quadrant
controlled chopper for converting a fixed DC input to a variable DC output. The block
contains two bridge arms. Each bridge arm each has two switching devices.

You can choose from two fidelity levels for the converter model. The equivalent model
option does not model the individual switching devices but returns equivalent results.
If you need detailed results for the switching device dynamics, use the detailed model
option. Otherwise, use the equivalent model for faster simulation. To simulate in real
time, use the equivalent model. To validate the results, use the detailed model with a
variable-step solver. To use the detailed model, set the **Fidelity
level** parameter to `Detailed model - switching
devices`. To use the equivalent model, set the **Fidelity
level** parameter to `Equivalent model -
PWM-controlled`.

If you choose the detailed model, each component is the same switching device, which you
specify by setting the **Switching device** parameter. The switching
devices that you can specify are implementations of blocks in the **Simscape** > **Electrical** > **Semiconductors & Converters** library:

- GTO — Gate turn-off thyristor. For information about the I-V characteristic of the
  device, see GTO.
- Ideal semiconductor switch — For information about the I-V characteristic of the
  device, see Ideal Semiconductor Switch.
- IGBT — Insulated-gate bipolar transistor. For information about the I-V characteristic
  of the device, see IGBT (Ideal, Switching).
- MOSFET — N-channel metal-oxide-semiconductor field-effect transistor. For information
  about the I-V characteristic of the device, see MOSFET (Ideal, Switching).
- Thyristor — For information about the I-V characteristic of the device, see
  Thyristor (Piecewise Linear).
- Averaged Switch — Semiconductor switch with an antiparallel diode. The control signal
  port **G** accepts values in the interval [0,1]. When
  **G** is equal to `0` or `1`, the
  averaged switch is fully opened or fully closed respectively. The switch behaves
  similarly to the Ideal Semiconductor Switch block with
  an antiparallel diode. When **G** is between 0 and 1, the averaged
  switch is partly opened. You can average the pulse-width modulation (PWM) signal over a
  specified period. You can then undersample the model and use modulation waveforms
  instead of PWM signals.

The figures show the equivalent circuit and the operation for the block.

To use the equivalent model as a rectifier, set all the elements of the PWM signal to
zero. The model behaves as a diode rectifier.

### Protection

The block contains an integral protection diode for each switching device. The
integral diode protects the semiconductor device by providing a conduction path for
reverse current. An inductive load can produce a high reverse-voltage spike when the
semiconductor device suddenly switches off the voltage supply to the load.

To configure the internal protection diode block, use the **Protection
Diode** parameters. This table shows how to set the **Model
dynamics** parameter based on your goals.

| Goals | | Value to Select | Integral Protection Diode |
| --- | --- | --- | --- |
| Do not include protection. | | `None` | None |
| Include protection. | Prioritize simulation speed. | `Diode with no dynamics` | The Diode block |
| Prioritize model fidelity by precisely specifying reverse-mode charge dynamics. | `Diode with charge dynamics` | The dynamic model of the Diode block |

**Note**

If you set the **Switching device** parameter to
`Averaged Switch`, the block automatically models
protection diodes with no dynamics and the **Model dynamics**
parameter is not visible.

You can also include a snubber circuit for each switching device. Snubber circuits contain a series-connected resistor and capacitor. They protect switching devices against high voltages that inductive loads produce when the device turns off the voltage supply to the load. Snubber circuits also prevent excessive rates of current change when a switching device turns on.

To include and configure a snubber circuit for each switching device, use the
**Snubbers** parameters.

### Modeling Thermal Effects

*Since R2024b*

You can expose the thermal port to model the effects of generated heat and device
temperature. To expose the thermal port:

- In the **Main** settings, set the
  **Fidelity level** parameter to
  `Detailed model - switching
  devices`.
- In the **Switching Devices** settings, set the
  **Switching device** parameter to one of these options:

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- In the **Switching Devices** settings, select
  the **Model thermal effects** parameter.

For more information on using thermal ports and the **Thermal Port**
parameters, see Simulating Thermal Effects in Semiconductors.

When you expose the thermal port, the Four-Quadrant Chopper block models the conduction losses and
the turn-on and turn-off losses of the switching devices. The block uses the same
methods to calculate these losses as these blocks with the **On-state
behavior and switching losses** parameter set to `Specify
constant values`:

- GTO
- IGBT (Ideal,
  Switching)
- MOSFET (Ideal,
  Switching)
- Thyristor (Piecewise
  Linear)

For more information about how the Four-Quadrant Chopper block calculates these
losses, see the documentation for the block that matches the option you select for
the **Switching device** parameter.

If you enable the thermal port and you set the **Integral protection
diode** parameter to `Diode with no dynamics`,
the block also models reverse recovery loss for the protection diodes. The block
uses the same method to calculate these losses as the Diode block with the **Fidelity level**
parameter set to `Ideal switching` and the **Diode
model** parameter to `Piecewise
linear`.

With ideal switching, the block does not use a physics-based charge model. The block
represents the losses that the charge creates during reverse recovery as an
instantaneous loss.

The block applies reverse recovery losses by stepping up the junction temperature
with a value equal to the reverse recovery loss divided by the total thermal mass at
the junction.

If you set the **Reverse recovery loss model**
parameter to `Tabulated loss`, the value of the
**Reverse recovery loss table, Erec(Tj, If)** parameter
specifies the dissipated energy as a function of the junction temperature and the
forward current just before the switching event. The off-state voltage linearly
scales the losses relative to the **Turn-off voltage when measuring recovery
loss, Vrec** parameter value. The table uses delayed values for the
current and voltage. To use a value in the lookup table that is close to the
instantaneous value, set the **Filter time constant for voltage
and current values** parameter to a value that is lower than the
fastest switching period.

If you set the **Reverse recovery loss model**
parameter to `Fixed loss`, the value of the
**Reverse recovery loss** parameter specifies the energy
dissipated during each turn-off event. If you select the **Scale reverse
recovery loss with current and voltage** parameter, then the block
scales this loss value linearly by the on-state current and the off-state voltage.
To use scaling values that are close to the instantaneous values, set **Filter time constant for voltage and current values** to a
value that is lower than the fastest switching period.

### Gate Control

To connect Simulink® gate-control voltage signals to the gate ports of the internal
switching devices:

1. Convert each voltage signal using a Simulink-PS
   Converter block.
2. Multiplex the converted gate signals into a single vector using a
   Four-Pulse Gate Multiplexer block.
3. Connect the vector signal to the **G** port.

### Piecewise Constant Approximation in Averaged Switch for FPGA Deployment

If you set the **Switching device** parameter to `Averaged switch` and your model uses a partitioning solver, this block produces nonlinear partitions because the average mode equations include modes, *Gsat* that are functions of the input **G**. To make these equations compatible with hardware description language (HDL) code generation, and therefore FPGA deployment, set the **Integer for piecewise constant approximation of gate input (0 for disabled)** parameter to a value greater than `0`. This block then treats the *Gsat* mode as a piecewise constant integer with a fixed range. This turns the previously nonlinear partitions to linear time varying partitions.

An integer value in the range `[0,K]`, where *K* is the value of the **Integer for piecewise constant approximation of gate input (0 for disabled)**, is now associated with each real value mode in the range `[0,1]`. The block computes the piecewise constant mode by dividing the original mode by K to normalize it back to the range `[0,1]`:

uI=(floor(u⋅K))u^=uIK
