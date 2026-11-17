---
type: simulink-block
title: 'Three-Level Converter (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'threelevelconverterthreephase'
documentation_source_path: 'ref/threelevelconverterthreephase.html'
language: en
---

# Three-Level Converter (Three-Phase)

## Ports
```yaml
ports:
- name: G
  summary: Gate terminals electrical
  direction: conserving
- name: '~'
  summary: Three-phase port electrical
  direction: conserving
- name: a
  summary: '*a*-phase electrical'
  direction: conserving
- name: b
  summary: '*b*-phase electrical'
  direction: conserving
- name: c
  summary: '*c*-phase electrical'
  direction: conserving
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '0'
  summary: Neutral terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
```

### Conserving

### **G** — Gate terminals electrical

Vector input port associated with the gate terminals of the switching
devices. Connect this port to a Twelve-Pulse Gate
Multiplexer block.

### **~** — Three-phase port electrical

Expandable three-phase
port.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **a** — *a*-phase electrical

Electrical conserving port associated with
*a*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b** — *b*-phase electrical

Electrical conserving port associated with
*b*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c** — *c*-phase electrical

Electrical conserving port associated with
*c*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **+** — Positive terminal electrical

Electrical conserving port associated with the DC positive
terminal.

### **0** — Neutral terminal electrical

Electrical conserving port associated with the DC neutral
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the DC negative
terminal.
## Parameters
```yaml
parameters:
- name: Electrical connection
  summary: Electrical connection Composite three-phase ports (default) | Expanded three-phase ports
  group: ''
- name: Switching device
  summary: Switching device Ideal Semiconductor Switch (default) | GTO | IGBT | MOSFET | Averaged Switch
  group: ''
- name: Forward voltage, Vf
  summary: Forward voltage 0.8 V (default)
  group: 'Switching Devices: GTO'
- name: On-state resistance
  summary: On-state resistance 0.001 Ohm (default)
  group: 'Switching Devices: GTO'
- name: Off-state Conductance
  summary: Off-state conductance 1e-6 1/Ohm (default)
  group: 'Switching Devices: GTO'
- name: Gate trigger voltage, Vgt
  summary: Gate trigger voltage 1 V (default)
  group: 'Switching Devices: GTO'
- name: Gate turn-off voltage, Vgt_off
  summary: Gate turn-off voltage -1 V (default)
  group: 'Switching Devices: GTO'
- name: Holding current
  summary: Holding current 1 A (default)
  group: 'Switching Devices: GTO'
- name: On-state resistance
  summary: On-state resistance 0.001 Ohm (default)
  group: 'Switching Devices: Ideal Semiconductor Switch'
- name: Off-state Conductance
  summary: Off-state conductance 1e-6 1/Ohm (default)
  group: 'Switching Devices: Ideal Semiconductor Switch'
- name: Threshold voltage, Vth
  summary: Threshold voltage 6 V (default)
  group: 'Switching Devices: Ideal Semiconductor Switch'
- name: Forward voltage, Vf
  summary: Forward voltage 0.8 V (default)
  group: 'Switching Devices: IGBT'
- name: On-state resistance
  summary: On-state resistance 0.001 Ohm (default)
  group: 'Switching Devices: IGBT'
- name: Off-state Conductance
  summary: Off-state conductance 1e-6 1/Ohm (default)
  group: 'Switching Devices: IGBT'
- name: Threshold voltage, Vth
  summary: Threshold voltage 6 V (default)
  group: 'Switching Devices: IGBT'
- name: Drain-source on resistance, R_DS(on)
  summary: Drain-source on resistance 0.001 Ohm (default)
  group: 'Switching Devices: MOSFET'
- name: Off-state Conductance
  summary: Off-state conductance 1e-6 1/Ohm (default)
  group: 'Switching Devices: MOSFET'
- name: Threshold voltage, Vth
  summary: Threshold voltage 6 V (default)
  group: 'Switching Devices: MOSFET'
- name: On-state resistance
  summary: On-state resistance 0.001 Ohm (default)
  group: 'Switching Devices: Averaged Switch'
- name: Integer for piecewise constant approximation of gate input (0 for disabled)
  summary: Integer mode for FPGA deployment 0 (default) | nonnegative scalar
  group: 'Switching Devices: Averaged Switch'
- name: Integral protection diode
  summary: Integral protection diode Diode with no dynamics (default) | Diode with charge dynamics
  group: Integral Diodes
- name: Forward voltage
  summary: Forward voltage 0.8 V (default)
  group: Integral Diodes
- name: On resistance
  summary: On resistance 0.001 Ohm (default)
  group: Integral Diodes
- name: Off conductance
  summary: Off conductance 1e-5 1/Ohm (default)
  group: Integral Diodes
- name: Junction capacitance
  summary: Junction capacitance 50e-9 F (default)
  group: Integral Diodes
- name: Peak reverse current, iRM
  summary: Peak reverse current -235 A (default) | negative scalar
  group: Integral Diodes
- name: Initial forward current when measuring iRM
  summary: Initial forward current when measuring iRM 300 A (default) | positive scalar
  group: Integral Diodes
- name: Rate of change of current when measuring iRM
  summary: Rate of change of current when measuring iRM -50A/μs (default) | negative scalar
  group: Integral Diodes
- name: Reverse recovery time parameterization
  summary: Reverse recovery time parameterization Specify reverse recovery time directly (default) | Specify stretch factor
    | Specify reverse recovery charge
  group: Integral Diodes
- name: Reverse recovery time, trr
  summary: Reverse recovery time 15 μs (default)
  group: Integral Diodes
- name: Reverse recovery time stretch factor
  summary: Reverse recovery time stretch factor 3 (default)
  group: Integral Diodes
- name: Reverse recovery charge, Qrr
  summary: Reverse recovery charge 1500 μAs (default)
  group: Integral Diodes
- name: Snubber
  summary: Snubber None (default) | RC snubber
  group: Snubbers
- name: Snubber resistance
  summary: Snubber resistance 0.1 Ohm (default)
  group: Snubbers
- name: Snubber capacitance
  summary: Snubber capacitance 1e-7 F (default)
  group: Snubbers
```

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to have composite or expanded three-phase ports.

### **Switching device** — Switching device `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Averaged Switch`

Converter switching device. The default value is `Ideal
Semiconductor Switch`.

The switching devices you can select are:

- Switching Devices: GTO
- Switching Devices: Ideal Semiconductor Switch
- Switching Devices: IGBT
- Switching Devices: MOSFET
- Switching Devices: Averaged Switch

#### Dependencies

Multiple additional parameters will become visible depending on the
choice of the specific switching device.

### Switching Devices: GTO

For more information, see GTO.

The parameters for this switching device will be visible only if you select it in
the **Switching device** parameter.

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

### Switching Devices: Ideal Semiconductor Switch

For more information, see Ideal Semiconductor Switch.

The parameters for this switching device will be visible only if you select it in
the **Switching device** parameter.

### **On-state resistance** — On-state resistance `0.001` `Ohm` (default)

Anode-cathode resistance when the device is on.

### **Off-state Conductance** — Off-state conductance `1e-6` `1/Ohm` (default)

Anode-cathode conductance when the device is off. The value must be
less than 1/R, where R is the value of **On-state
resistance**.

### **Threshold voltage, Vth** — Threshold voltage `6` `V` (default)

Gate-cathode voltage threshold. The device turns on when the
gate-cathode voltage is above this value.

### Switching Devices: IGBT

For more information, see IGBT (Ideal, Switching).

The parameters for this switching device will be visible only if you select it in
the **Switching device** parameter.

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

### **Threshold voltage, Vth** — Threshold voltage `6` `V` (default)

Gate-emitter voltage at which the device turns on.

### Switching Devices: MOSFET

For more information, see MOSFET (Ideal, Switching).

The parameters for this switching device will be visible only if you select it in
the **Switching device** parameter.

### **Drain-source on resistance, R\_DS(on)** — Drain-source on resistance `0.001` `Ohm` (default)

Drain-source resistance when the device is on.

### **Off-state Conductance** — Off-state conductance `1e-6` `1/Ohm` (default)

Drain-source conductance when the device is off. The value must be
less than 1/R, where R is the value of **On-state
resistance**.

### **Threshold voltage, Vth** — Threshold voltage `6` `V` (default)

Gate-source voltage threshold. The device turns on when the
gate-source voltage is above this value.

### Switching Devices: Averaged Switch

The parameters for this switching device will be visible only if you select it in
the **Switching device** parameter.

### **On-state resistance** — On-state resistance `0.001` `Ohm` (default)

Anode-cathode resistance when the device is on.

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — Integer mode for FPGA deployment `0` (default) | nonnegative scalar

Integer used to perform piecewise constant approximation of the gate input for FPGA
deployment.

#### Dependencies

To enable this parameter, set **Switching device** to `Averaged Switch`.

### Integral Diodes

### **Integral protection diode** — Integral protection diode `Diode with no dynamics` (default) | `Diode with charge dynamics`

Integral protection diode for each switching device.

The diodes you can select are:

- `Diode with no dynamics`
- `Diode with charge dynamics`

**Note**

If you select `Averaged Switch` for the
**Switching Device** parameter in the
**Switching Device** setting, this parameter is
not visible and `Diode with no dynamics` is
automatically selected.

### **Forward voltage** — Forward voltage `0.8` `V` (default)

Minimum voltage required across the `+` and
`-` block ports for the gradient of the diode I-V
characteristic to be 1/Ron, where
Ron is the value of **On
resistance**.

### **On resistance** — On resistance `0.001` `Ohm` (default)

Rate of change of voltage versus current above the **Forward
voltage**.

### **Off conductance** — Off conductance `1e-5` `1/Ohm` (default)

Conductance of the reverse-biased diode.

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

Initial forward current when measuring peak reverse current. This
value must be greater than zero.

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

### **Reverse recovery time stretch factor** — Reverse recovery time stretch factor `3` (default)

Value that the block uses to calculate **Reverse recovery
time, trr**. This value must be greater than
`1`. Specifying the stretch factor is an easier way
to parameterize the reverse recovery time than specifying the reverse
recovery charge. The larger the value of the stretch factor, the longer
it takes for the reverse recovery current to dissipate.

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Diode with charge
dynamics` and **Reverse recovery time
parameterization** to `Specify stretch
factor`.

### **Reverse recovery charge, Qrr** — Reverse recovery charge `1500` `μAs` (default)

Value that the block uses to calculate **Reverse recovery
time, trr**. Use this parameter if the data sheet for your
diode device specifies a value for the reverse recovery charge instead
of a value for the reverse recovery time.

The reverse recovery charge is the total charge that continues to
dissipate when the diode turns off. The value must be less than −i2RM2a,

where:

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

The **Snubbers** parameters tab is not visible if you set
**Switching device** to `Averaged
Switch`.

### **Snubber** — Snubber `None` (default) | `RC snubber`

Snubber for each switching device:

- `None` - This is the default
  value.
- `RC snubber`

### **Snubber resistance** — Snubber resistance `0.1` `Ohm` (default)

Snubber resistance.

#### Dependencies

This parameter is visible only when the
**Snubber** parameter is set to `RC
snubber`.

### **Snubber capacitance** — Snubber capacitance `1e-7` `F` (default)

Snubber capacitance.

#### Dependencies

This parameter is visible only when the
**Snubber** parameter is set to `RC
snubber`.
## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`.

As a result of these changes, inside a model saved in an earlier release, review
the **Electrical connection** parameter of this block.

## Description

Twelve-pulse three-phase three-level neutral-point clamped controlled converter

The Three-Level Converter (Three-Phase) block models a
twelve-pulse three-phase three-level neutral-point clamped controlled converter. You can
use this block to connect a three-phase AC network to a three-level DC network.

### Model

The block contains three bridge arms, each of which has four switching devices and
the associated anti-parallel diodes. Options for the type of switching devices
are:

- GTO — Gate turn-off thyristor. For information about the I-V
  characteristic of the device, see GTO.
- Ideal semiconductor switch — For information about the I-V
  characteristic of the device, see Ideal Semiconductor
  Switch.
- IGBT — Insulated-gate bipolar transistor. For information about the
  I-V characteristic of the device, see IGBT (Ideal,
  Switching).
- MOSFET — N-channel metal-oxide-semiconductor field-effect transistor.
  For information about the I-V characteristic of the device, see
  MOSFET (Ideal,
  Switching).
- Averaged Switch — Semiconductor switch with an anti-parallel diode.
  The control signal port, **G**, accepts values in the
  `[0,1]` interval. When the value at port
  **G** is equal to `0` or
  `1`, the averaged switch is either fully opened or
  fully closed, and it behaves similarly to the Ideal Semiconductor Switch
  block with an anti-parallel diode. When the value at port
  **G** is between `0` and
  `1`, the averaged switch is partly opened. You can
  then average the PWM signal over a specified period. This allows for
  undersampling of the model or using modulation waveforms instead of PWM
  signals.

Each component in the three-arm circuit is the same switching device that you
specify. The switching devices are the same as the devices in the **Semiconductors** > **Fundamental Components** sublibrary.

The figure shows the equivalent circuit for the block using an
Ideal Semiconductor block as the switching
device.

You control the gate ports of the 12 switching devices via an input to the
Three-Level Converter (Three-Phase) block
**G** port.

1. Use a Twelve-Pulse Gate
   Multiplexer block to multiplex all 12 gate signals into
   a single vector.
2. Connect the output of the Twelve-Pulse Gate
   Multiplexer block to the Three-Level
   Converter (Three-Phase) block **G**
   port.

You use the **Diodes** tab of the block dialog box to include an
integral protection diode for each switching device. An integral diode protects the
semiconductor device by providing a conduction path for reverse current. An
inductive load can produce a high reverse-voltage spike when the semiconductor
device suddenly switches off the voltage supply to the load.

The table shows how to set the **Integral protection
diode** parameter based on your goals.

| Goals | Value to Select | Integral Protection Diode |
| --- | --- | --- |
| Prioritize simulation speed. | `Diode with no dynamics` | The Diode block |
| Prioritize model fidelity by precisely specifying reverse-mode charge dynamics. | `Diode with charge dynamics` | The dynamic model of the Diode block |

You use the **Snubbers** tab of the block dialog box to include a
snubber circuit for each switching device. Each snubber consists of a resistor and
capacitor connected in series. Typically, a snubber circuit protects a switching
device against very high voltages produced by an inductive load when the device
turns off the voltage supply to the load. Snubber circuits also prevent excessive
rates of change of current when a switching device turns on.

### Piecewise Constant Approximation in Averaged Switch for FPGA Deployment

If you set the **Switching device** parameter to `Averaged switch` and your model uses a partitioning solver, this block produces nonlinear partitions because the average mode equations include modes, *Gsat* that are functions of the input **G**. To make these equations compatible with hardware description language (HDL) code generation, and therefore FPGA deployment, set the **Integer for piecewise constant approximation of gate input (0 for disabled)** parameter to a value greater than `0`. This block then treats the *Gsat* mode as a piecewise constant integer with a fixed range. This turns the previously nonlinear partitions to linear time varying partitions.

An integer value in the range `[0,K]`, where *K* is the value of the **Integer for piecewise constant approximation of gate input (0 for disabled)**, is now associated with each real value mode in the range `[0,1]`. The block computes the piecewise constant mode by dividing the original mode by K to normalize it back to the range `[0,1]`:

uI=(floor(u⋅K))u^=uIK
