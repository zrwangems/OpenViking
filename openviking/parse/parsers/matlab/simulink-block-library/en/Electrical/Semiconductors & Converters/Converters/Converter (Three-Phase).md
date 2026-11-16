---
type: simulink-block
title: 'Converter (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'converterthreephase'
documentation_source_path: 'ref/converterthreephase.html'
language: en
---

# Converter (Three-Phase)

## Ports

### Conserving

### **G** — Gate terminals electrical

Vector input port associated with the gate terminals of the switching
devices. Connect this port to a Six-Pulse Gate
Multiplexer block.

### **~** — Three-phase port electrical

Composite three-phase port.

For more information about composite and expanded three-phase ports,
see Three-Phase Ports.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **a** — *a*-phase electrical

Electrical conserving port associated with the
*a*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b** — *b*-phase electrical

Electrical conserving port associated with the
*b*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c** — *c*-phase electrical

Electrical conserving port associated with the
*c*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **+** — Positive terminal electrical

Electrical conserving port associated with the DC positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the DC negative
terminal.

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

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Option to have composite or expanded three-phase ports. For more
information, see Three-Phase Ports.

### **Fidelity level** — Fidelity level `Detailed model - switching devices` (default) | `Equivalent model - PWM-controlled`

*Since R2024a*

Level of fidelity of the model.

To prioritize simulation accuracy or to obtain results for the
individual switching devices, set this parameter to
`Detailed model - switching
devices`.

To prioritize simulation speed, set this parameter to
`Equivalent model - PWM-controlled`.

### Switching Devices: GTO

To enable these parameters, set **Fidelity level** to
`Detailed model - switching devices` and
**Switching device** to `GTO`.

### **Switching device** — Switching device `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

Converter switching device.

### **Model thermal effects** — Option to model thermal effects `Off` (default) | `On`

Option to model thermal effects.

### **Gate trigger voltage, Vgt** — Gate trigger voltage `1` `V` (default)

Gate-cathode voltage threshold. The device turns on when the
gate-cathode voltage is above this value.

### **Gate turn-off voltage, Vgt\_off** — Gate turn-off voltage `-1` `V` (default)

Gate-cathode voltage threshold. The device turns off when the
gate-cathode voltage is below this value.

### **Holding current** — Holding current `1` `A` (default)

Current threshold. The device stays on when the current is above this
value, even when the gate-cathode voltage falls below the gate trigger
voltage.

### **Forward voltage, Vf** — Forward voltage `0.8` `V` (default)

Minimum voltage required across the anode and cathode block ports for
the gradient of the device i-v characteristic to be
1/Ron, where Ron is
the value of **On-state resistance**.

### **On-state resistance** — On-state resistance `0.001` `Ohm` (default)

Rate of change of voltage versus current above the forward
voltage.

### **Off-state Conductance** — Off-state conductance `1e-6` `1/Ohm` (default)

Anode-cathode conductance when the device is off. The value must be
less than 1/R, where R is the value of **On-state
resistance**.

### Switching Devices: Ideal Semiconductor Switch

To enable these parameters, set **Fidelity level** to
`Detailed model - switching devices` and
**Switching device** to `Ideal semiconductor
switch`.

### **Switching device** — Switching device `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

Converter switching device.

### **Threshold voltage, Vth** — Threshold voltage `6` `V` (default)

Gate-cathode voltage threshold. The device turns on when the
gate-cathode voltage is above this value.

### **On-state resistance** — On-state resistance `0.001` `Ohm` (default)

Anode-cathode resistance when the device is on.

### **Off-state Conductance** — Off-state conductance `1e-6` `1/Ohm` (default)

Anode-cathode conductance when the device is off. The value must be
less than 1/R, where R is the value of **On-state
resistance**.

### Switching Devices: IGBT

To enable these parameters, set **Fidelity level** to
`Detailed model - switching devices` and
**Switching device** to `IGBT`.

### **Switching device** — Switching device `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

Converter switching device.

### **Model thermal effects** — Option to model thermal effects `Off` (default) | `On`

Option to model thermal effects.

### **Threshold voltage, Vth** — Threshold voltage `6` `V` (default)

Gate-emitter voltage at which the device turns on.

### **Forward voltage, Vf** — Forward voltage `0.8` `V` (default)

Minimum voltage required across the collector and emitter block ports
for the gradient of the diode i-v characteristic to be
1/Ron, where Ron is
the value of **On-state resistance**.

### **On-state resistance** — On-state resistance `0.001` `Ohm` (default)

Collector-emitter resistance when the device is on.

### **Off-state Conductance** — Off-state conductance `1e-6` `1/Ohm` (default)

Collector-emitter conductance when the device is off. The value must
be less than 1/R, where R is the value of **On-state
resistance**.

### Switching Devices: MOSFET

To enable these parameters, set **Fidelity level** to
`Detailed model - switching devices` and
**Switching device** to
`MOSFET`.

### **Switching device** — Switching device `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

Converter switching device.

### **Model thermal effects** — Option to model thermal effects `Off` (default) | `On`

Option to model thermal effects.

### **Threshold voltage, Vth** — Threshold voltage `6` `V` (default)

Gate-source voltage threshold. The device turns on when the
gate-source voltage is above this value.

### **Drain-source on resistance, R\_DS(on)** — Drain-source on resistance `0.001` `Ohm` (default)

Drain-source resistance when the device is on.

### **Off-state Conductance** — Off-state conductance `1e-6` `1/Ohm` (default)

Drain-source conductance when the device is off. The value must be
less than 1/R, where R is the value of **On-state
resistance**.

### Switching Devices: Thyristor

To enable these parameters, set **Fidelity level** to
`Detailed model - switching devices` and
**Switching device** to
`Thyristor`.

### **Switching device** — Switching device `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

Converter switching device.

### **Model thermal effects** — Option to model thermal effects `Off` (default) | `On`

Option to model thermal effects.

### **Gate trigger voltage, Vgt** — Gate trigger voltage `1` `V` (default)

Gate-cathode voltage threshold. The device turns on when the
gate-cathode voltage is above this value.

### **Holding current** — Holding current `1` `A` (default)

Current threshold. The device stays on when the current is above this
value, even when the gate-cathode voltage falls below the gate trigger
voltage.

### **Forward voltage, Vf** — Forward voltage `0.8` `V` (default)

Forward voltage at which the device turns on.

### **On-state resistance** — On-state resistance `0.001` `Ohm` (default)

Anode-cathode resistance when the device is on.

### **Off-state Conductance** — Off-state conductance `1e-6` `1/Ohm` (default)

Anode-cathode conductance when the device is off. The value must be
less than 1/*R*, where *R* is the
value of **On-state resistance**.

### Switching Devices: Averaged Switch

To enable these parameters, set **Fidelity level** to
`Detailed model - switching devices` and
**Switching device** to `Averaged
switch`.

### **Switching device** — Switching device `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

Converter switching device.

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — Integer mode for FPGA deployment `0` (default) | nonnegative scalar

Integer used to perform piecewise constant approximation of the gate
input for FPGA deployment.

### **On-state resistance** — On-state resistance `0.001` `Ohm` (default)

Anode-cathode resistance when the device is on.

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

### **Switch-on loss** — Switch-on loss `22.86e-3` `J` (default) | positive scalar

*Since R2024b*

Energy dissipated during a single switch-on event.

#### Dependencies

To enable this parameter, set **Switching
Device** to `GTO`,
`IGBT`,
`MOSFET`, or
`Thyristor`.

### **Switch-off loss** — Forced commutation switch-off loss `17.14e-3` `J` (default) | positive scalar

*Since R2024b*

Energy dissipated during a single switch-off event.

#### Dependencies

To enable this parameter, set **Switching
Device** to `GTO`,
`IGBT`, or
`MOSFET`.

### **Natural commutation rectification loss** — Natural commutation rectification loss `10e-3` `J` (default) | positive scalar

*Since R2024b*

Rectification loss that applies when the current falls below the
**Holding current** parameter value and the block
switches off.

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

### Integral Diodes

To enable these parameters, set **Fidelity level** to
`Detailed model - switching devices`.

### **Integral protection diode** — Integral protection diode model `None` (default) | `Diode with no dynamics` | `Diode with charge dynamics`

Model that the Converter (Three-Phase) block uses for the protection diode for
each switching device. Choose one of these options:

- `None` — The Converter (Three-Phase) does not
  model protection diodes.
- `Diode with no dynamics` — The
  Converter (Three-Phase) block models protection diodes using the same
  equations as the Diode
  block with no dynamics. Select this option to prioritize
  simulation speed.
- `Diode with charge dynamics` —
  The Converter (Three-Phase) block models protection diodes using the
  same equations as the Diode
  block with charge dynamics. Select this option to prioritize
  detailed simulation results.

### **Forward voltage** — Forward voltage `0.8` `V` (default)

Minimum voltage required across the `+` and
`-` block ports for the gradient of the diode I-V
characteristic to be 1/Ron, where
Ron is the value of the **On
resistance** parameter.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **Switching device** to
  `Averaged Switch`.
- Set **Integral protection diode** to
  `Diode with no dynamics` or
  `Diode with charge
  dynamics`.

### **On resistance** — On resistance `0.001` `Ohm` (default)

Rate of change of voltage versus current above the **Forward
voltage** parameter value.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **Switching device** to
  `Averaged Switch`.
- Set **Integral protection diode** to
  `Diode with no dynamics` or
  `Diode with charge
  dynamics`.

### **Off conductance** — Off conductance `1e-5` `1/Ohm` (default)

Conductance of the reverse-biased diode.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **Switching device** to
  `Averaged Switch`.
- Set **Integral protection diode** to
  `Diode with no dynamics` or
  `Diode with charge
  dynamics`.

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

Dissipated energy in each turn-off event. The block dissipates this
energy regardless of the state of the diode before or after the
switching event.

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

Voltage across the diode after the reverse recovery event that the
block uses to measure recovery loss.

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

Filter time constant for the voltage and current values that the block
uses to calculate reverse recovery loss. Set this parameter to a value
that is lower than the fastest switching period.

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
- Set the **Reverse recovery loss
  model** parameter to `Tabulated
  loss`.

### **Temperature vector for recovery loss table, Tj** — Temperature vector for recovery loss table `[298.15, 398.15]` `K` (default) | vector

*Since R2024b*

Temperature vector that the block uses to tabulate the reverse
recovery loss.

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
- Set the **Reverse recovery loss
  model** parameter to `Tabulated
  loss`.

### **Forward current vector for recovery loss table, If** — Forward current vector for recovery loss table `[.1, 1, 10]` `A` (default) | vector of nonnegative scalars

*Since R2024b*

Forward current vector that the block uses to tabulate reverse
recovery loss.

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
- Set the **Reverse recovery loss
  model** parameter to `Tabulated
  loss`.

### **Junction capacitance** — Junction capacitance `50e-9` `F` (default)

Diode junction capacitance.

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Diode with charge
dynamics`.

### **Peak reverse current, iRM** — Peak reverse current `-235` `A` (default) | negative scalar

Peak reverse current measured by an external test circuit. This value
must be less than zero. The default value is `-235`
`A`.

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Diode with charge
dynamics`.

### **Initial forward current when measuring iRM** — Initial forward current when measuring iRM `300` `A` (default) | positive scalar

Initial forward current when measuring peak reverse current.

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Diode with charge
dynamics`.

### **Rate of change of current when measuring iRM** — Rate of change of current when measuring iRM `-50``A/μs` (default) | negative scalar

Rate of change of current when measuring peak reverse current. This
value must be less than zero.

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Diode with charge
dynamics`.

### **Reverse recovery time parameterization** — Reverse recovery time parameterization `Specify reverse recovery time directly` (default) | `Specify stretch factor` | `Specify reverse recovery charge`

Determines how you specify reverse recovery time in the block. The
default value is `Specify reverse recovery time
directly`.

If you select `Specify stretch factor` or
`Specify reverse recovery charge`, you
specify a value that the block uses to derive the reverse recovery time.
For more information on these options, see How the Block Calculates TM and Tau.

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Diode with charge
dynamics`.

### **Reverse recovery time, trr** — Reverse recovery time `15` `μs` (default)

Interval between the time when the current initially goes to zero
(when the diode turns off) and the time when the current falls to less
than 10% of the peak reverse current. The value of the **Reverse
recovery time, trr** parameter must be greater than the
value of the **Peak reverse current, iRM** parameter
divided by the value of the **Rate of change of current when
measuring iRM** parameter.

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Diode with charge
dynamics` and **Reverse recovery time
parameterization** to `Specify reverse
recovery time directly`.

### **Reverse recovery time stretch factor** — Reverse recovery time stretch factor `3` (default) | scalar greater than `1`

Stretch factor that the block uses to calculate the reverse recovery
time. Specifying the stretch factor is an easier way to parameterize the
reverse recovery time than specifying the reverse recovery charge. The
larger the value of the stretch factor, the longer it takes for the
reverse recovery current to dissipate.

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Diode with charge
dynamics` and **Reverse recovery time
parameterization** to `Specify stretch
factor`.

### **Reverse recovery charge, Qrr** — Reverse recovery charge `1500` `μAs` (default)

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

To enable this parameter, set **Integral protection
diode** to `Diode with charge
dynamics` and **Reverse recovery time
parameterization** to `Specify reverse
recovery charge`.

For more information on these parameters, see Diode.

### Snubbers

To enable these parameters, set **Fidelity level** to
`Detailed model - switching devices` and
**Switching device** to one of these options:

- `Ideal Semiconductor Switch`
- `GTO`
- `IGBT`
- `MOSFET`
- `Thyristor`

### **Snubber** — Snubber `None` (default) | `RC snubber`

Snubber for each switching device.

### **Snubber resistance** — Snubber resistance `0.1` `Ohm` (default)

Snubber resistance.

#### Dependencies

To enable this parameter, set **Snubber** to
`RC snubber`.

### **Snubber capacitance** — Snubber capacitance `1e-7` `F` (default)

Snubber capacitance.

#### Dependencies

To enable this parameter, set **Snubber** to
`RC snubber`.

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

Row vector, [ *T\_J* *T\_C* ], of two
temperature values. The first value, *T\_J*, is the
junction initial temperature. The second value, *T\_C*,
is the case initial temperature.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Specify junction and case thermal
parameters`.

### **Thermal resistances, [R1 R2 … Rn]** — Thermal resistances `[.08,.1,.5]` `K/W` (default) | `[.08,.14,.22,.16]` `K/W` | vector of positive values

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

*Since R2024b*

Row vector of temperature values that correspond to the temperature
drop across each thermal capacity in the model.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Cauer model`.

### **Thermal time constants, [t1 t2 … tn]** — Thermal time constants `[.001,.1,.2]` `s` | `[7e-05, .0007, .01, .08]` `s` | vector of positive values

*Since R2024b*

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
model parameterized with Foster coefficients` and
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

**Introduced in R2013b**

### R2024b: Model thermal effects by using the thermal port

You can now use the thermal port to model the effects of generated heat and device
temperature. When you expose the thermal port, the Converter (Three-Phase) block models the
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

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`.

As a result of these changes, inside a model saved in an earlier release, review
the **Electrical connection** parameter of this block.

## Description

Controller-driven bidirectional AC/DC three-arm converter

The Converter (Three-Phase) block models a six-pulse
three-phase controlled converter that consists of three bridge arms. Each bridge arm
comprises with two switching devices. The converter circuit connects a three-phase AC
network to a DC network.

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

If you choose the detailed model, each component in the three-arm circuit is the same
switching device, which you specify by setting the **Switching device**
parameter. The switching devices that you can specify are implementations of blocks in
the **Simscape** > **Electrical** > **Semiconductors & Converters** library:

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

This figure shows the equivalent circuit for a converter with fully controlled
switching devices (e.g. IGBTs, GTOs).

This figure shows the equivalent circuit for a converter with partially controlled
switching devices (e.g. thyristors).

Control the gate ports of the six switching devices via an input to port
**G** on the Converter (Three-Phase)
block:

1. Multiplex all six gate signals into a single vector with a Six-Pulse Gate Multiplexer
   block.
2. Connect the output of the Six-Pulse Gate
   Multiplexer block to the Converter
   (Three-Phase) block **G** port.

You can specify an integral protection diode for each switching device. An integral
diode protects the semiconductor device by providing a conduction path for reverse
current. An inductive load can produce a high reverse-voltage spike when the
semiconductor device suddenly switches off the voltage supply to the load.

The table shows you how to set the **Integral protection
diode** parameter based on your goals.

| Goals | | Value to Select | Integral Protection Diode |
| --- | --- | --- | --- |
| Do not include protection. | | `None` | None |
| Include protection. | Prioritize simulation speed. | `Diode with no dynamics` | The Diode block |
| Prioritize model fidelity by precisely specifying reverse-mode charge dynamics. | `Diode with charge dynamics` | The dynamic model of the Diode block |

**Note**

If you set the **Switching device** parameter to
`Averaged Switch`, the block models protection diodes
with no dynamics and the **Integral protection diode** parameter is
not visible.

You can include a snubber circuit, consisting of a resistor and capacitor connected in
series, for each switching device. Snubber circuits protect switching devices against
high voltages that inductive loads produce when the device turns off the voltage supply
to the load. Snubber circuits also prevent excessive rates of change of current when a
switching device turns on.

To use the equivalent model as a rectifier, set all the elements of the PWM signal to
zero. The model behaves as a three-phase diode rectifier.

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

For more information on using thermal ports and the **Thermal
Port** parameters, see Simulating Thermal Effects in Semiconductors.

When you expose the thermal port, the Converter (Three-Phase) block models conduction losses
and the turn-on and turn-off losses of the switching devices. The block uses the
same methods to calculate these losses as these blocks with the **On-state
behavior and switching losses** parameter set to `Specify
constant values`:

- GTO
- IGBT (Ideal,
  Switching)
- MOSFET (Ideal,
  Switching)
- Thyristor (Piecewise
  Linear)

For more information about how the Converter (Three-Phase) block calculates these
losses, see the documentation for the block that matches the option you select for
the **Switching device** parameter.

If you enable the thermal port and you set the **Integral protection
diode** parameter to `Diode with no dynamics`,
the block also models reverse recovery loss for the protection diodes. The block
uses the same method to calculate these losses as the Diode block with the **Fidelity level**
parameter set to `Ideal switching` and the **Diode
model** parameter to `Piecewise
linear`.

With ideal switching, the block does not use a physics-based charge model. The
block represents the losses that the charge creates during reverse recovery as an
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

### Piecewise Constant Approximation in Averaged Switch for FPGA Deployment

If you set the **Switching device** parameter to `Averaged switch` and your model uses a partitioning solver, this block produces nonlinear partitions because the average mode equations include modes, *Gsat* that are functions of the input **G**. To make these equations compatible with hardware description language (HDL) code generation, and therefore FPGA deployment, set the **Integer for piecewise constant approximation of gate input (0 for disabled)** parameter to a value greater than `0`. This block then treats the *Gsat* mode as a piecewise constant integer with a fixed range. This turns the previously nonlinear partitions to linear time varying partitions.

An integer value in the range `[0,K]`, where *K* is the value of the **Integer for piecewise constant approximation of gate input (0 for disabled)**, is now associated with each real value mode in the range `[0,1]`. The block computes the piecewise constant mode by dividing the original mode by K to normalize it back to the range `[0,1]`:

uI=(floor(u⋅K))u^=uIK

### Assumptions and Limitations

- If, in the Solver Configuration block inside your model, you set the
  **Solver type** parameter to
  `Partitioning`, the averaged switches introduce
  instability during dead time, when all gate inputs are set to 0. Where
  possible, use the open-zero state by setting all high-side switches to 0 and
  all low-side switches to 1.
- To use the Converter (Three-Phase) block as
  an active front end rectifier, if you set the **Fidelity
  level** parameter to `Equivalent model -
  PWM-controlled` or you set the **Switching
  device** parameter to `Averaged
  Switch`, you must add a mid-point ground system on the DC
  side. This figure shows how to build a mid-point ground system with either
  two resistors or two capacitors.
