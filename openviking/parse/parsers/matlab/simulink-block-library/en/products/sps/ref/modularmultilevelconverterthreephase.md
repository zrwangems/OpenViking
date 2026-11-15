---
type: simulink-block
title: 'Modular Multilevel Converter (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Converters / Converters, Inverters, Rectifiers, and Choppers'
documentation_page: 'modularmultilevelconverterthreephase'
documentation_source_path: 'ref/modularmultilevelconverterthreephase.html'
language: en
---

# Modular Multilevel Converter (Three-Phase)

## Ports

### Input

### **G** — Submodule gate control matrix of physical signals

Physical signal port associated with the gate signal for all
submodules of the modular multilevel converter, specified as a
matrix.

If you set the **Converter topology** parameter to
`Half-bridge`, the signal is a vector of
length *12 \* Nsm*, where *Nsm* is
the **Number of power submodules**.

If you set the **Converter topology** parameter to
`Full-bridge`, the signal is a vector of
length *24 \* Nsm*.

#### Dependencies

To enable this port, set **Fidelity level** to
`Detailed model - switching devices` or
`Equivalent model -
PWM-controlled`.

### **ref** — Submodule reference waveform vector of physical signals

Physical signal port associated with the reference waveforms of the submodules,
specified as a vector of length *6*.

#### Dependencies

To enable this port, set **Fidelity level** to
`Equivalent model -
waveform-controlled`.
### Output

### **vc** — Capacitor voltages vector of physical signals

Physical signal port associated with the capacitor voltages for each submodule in the
modular multilevel converter, returned as a vector.

#### Dependencies

To enable this port, set **Capacitor voltages**
to `Instrumented`.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive terminal of
the modular multilevel converter.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative terminal of
the modular multilevel converter.

### **~** — Three-phase port electrical

Expandable three-phase
electrical port associated with the three-phase terminal of
the modular multilevel converter.

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

## Parameters

### Main

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to have composite or expanded three-phase ports.

### **Converter topology** — Converter topology `Half-bridge` (default) | `Full-bridge`

Topology of the modular multilevel converter.

### **Fidelity level** — Model fidelity `Detailed model - switching devices` (default) | `Equivalent model - PWM-controlled` | `Equivalent model - waveform-controlled`

Level of fidelity of the model.

### **Capacitor voltages** — Capacitor voltage instrumentation `Instrumented` (default) | `Uninstrumented`

Whether to instrument the capacitor voltages.

### **Number of power submodules** — Number of submodules `1` (default) | positive scalar

Number of power submodules of the modular multilevel converter.

### **Capacitance** — Submodule capacitance `1e-7` `F` (default) | scalar | vector

Capacitance of a submodule. If you enter a vector, the vector must be of length
*6 \* Nsm*, where *Nsm* is the
**Number of power submodules**.

### **Capacitor effective series resistance** — Capacitor effective series resistance `1e-6` `Ohm` (default) | scalar | vector

Capacitor effective series resistance. If you enter a vector, the vector must be of
length *6 \* Nsm*, where *Nsm* is
the **Number of power submodules**.

#### Dependencies

To enable this parameter, set **Fidelity level**
to `Detailed model - switching devices`.

### **Arm inductance** — Arm inductance `1e-6` `H` (default) | scalar

Inductance of the arm.

### **Arm inductance series resistance** — Arm inductance series resistance `0` `Ohm` (default) | scalar

Arm inductance series resistance.

### **Capacitor initial voltage** — Capacitor initial voltage `500` `V` (default) | scalar | vector

Initial voltage of the capacitor. If you enter a vector, the vector must be of length
*6 \* Nsm*, where *Nsm* is the
**Number of power submodules**.

### Switching Devices

This table shows how enabled parameters in the **Switching Devices**
settings depend on the **Switching device** that you select. To
learn how to read the table, see Parameter Dependencies. To enable these settings, set
**Fidelity level** to `Detailed model - switching
devices`.

**Switching Devices Parameter Dependencies**

| Parameters and Options | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Switching device** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| **On-state resistance** | **Forward voltage** | **Forward voltage** | **Drain-source on resistance** | **Forward voltage** | **On-state resistance** |
| **Off-state conductance** | **On-state resistance** | **On-state resistance** | **Off-state conductance** | **On-state resistance** |
| **Threshold voltage** | **Off-state conductance** | **Off-state conductance** | **Threshold voltage** | **Off-state conductance** |
| **Gate trigger voltage, Vgt** | **Threshold voltage** | **Gate trigger voltage, Vgt** | **Integer for piecewise constant approximation of gate input (0 for disabled)** |
| **Gate turn-off voltage, Vgt\_off** | **Holding current** |
| **Holding current** |

### **Switching device** — Switch type `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

Switching device type for the converter.

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Forward voltage** — Voltage `0.8` `V` (default) | scalar

For the different switching device types, the **Forward voltage** is the:

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

For the different switching device types, the **On-state resistance**
is the:

- GTO — Rate of change of the voltage versus the current
  above the forward voltage
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

Resistance between the drain and the source. The gate-to-source voltage also affects the
**Drain-source on resistance** parameter.

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Off-state conductance** — Conductance when device is off `1e-5` `1/Ohm` (default) | scalar

Conductance when the device is off. The value must be less than
1/*R*, where *R* is the value of
**On-state resistance**.

For the different switching device types, the **On-state
resistance** is the:

- GTO — Anode-cathode conductance
- Ideal semiconductor switch — Anode-cathode
  conductance
- IGBT — Collector-emitter conductance
- MOSFET — Drain-source conductance
- Thyristor — Anode-cathode conductance

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Threshold voltage** — Voltage threshold `6` `V` (default) | scalar

Gate voltage threshold. The device turns on when the gate voltage is above this value.
The voltage threshold applies to different devices depending on the
switching device used:

- Ideal semiconductor switch — Gate-cathode voltage
- IGBT — Gate-emitter voltage
- MOSFET — Gate-source voltage

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Gate trigger voltage, Vgt** — Gate-cathode activation voltage threshold `1` `V` (default) | scalar

Gate-cathode voltage threshold. The device turns on when the
gate-cathode voltage is above this value.

#### Dependencies

See the Switching Devices Parameter Dependencies table.

### **Gate turn-off voltage, Vgt\_off** — Gate-cathode deactivation voltage threshold `-1` `V` (default) | scalar

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

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — Integer mode for FPGA deployment `0` (default) | nonnegative scalar

Integer used to perform piecewise constant approximation of the gate input for FPGA
deployment.

#### Dependencies

To enable this parameter, set **Switching device** to `Averaged Switch`.

### Protection Diodes

For more information on these parameters, see Diode.

### **Model dynamics** — Diode model `Diode with no dynamics` (default) | `Diode with charge dynamics` | `None`

Diode type. The options are:

- `None` — The block does not model
  diode dynamics.
- `Diode with no dynamics` — Select
  this option to prioritize simulation speed using the
  Diode
  block.
- `Diode with charge dynamics` —
  Select this option to prioritize model fidelity in terms of
  reverse mode charge dynamics using the commutation diode
  model of the Diode
  block.

**Note**

If you set **Switching device** to
`Averaged Switch` in the
**Switching Device** settings, the
`Diode with no dynamics` setting is
automatically selected.

#### Dependencies

To enable this parameter, set **Switching
device** to `GTO`,
`Ideal Semiconductor Switch`,
`IGBT`,
`MOFSET`, or
`Thyristor`.

### **Forward voltage** — Forward voltage `0.8` `V` (default) | scalar

Minimum voltage required across the `+` and `-` block
ports for the gradient of the diode I-V characteristic to be
1/*Ron*, where
*Ron* is the value of
**On resistance**.

#### Dependencies

To enable this parameter, set **Model dynamics**
to `Diode with no dynamics` or
`Diode with charge dynamics`.

### **On resistance** — On resistance `0.001` `Ohm` (default) | scalar

Rate of change of voltage versus the current above the **Forward
voltage**.

#### Dependencies

To enable this parameter, set **Model dynamics**
to `Diode with no dynamics` or
`Diode with charge dynamics`.

### **Off conductance** — Off conductance `1e-5` `1/Ohm` (default) | scalar

Conductance of the reverse-biased diode.

#### Dependencies

To enable this parameter, set **Model dynamics**
to `Diode with no dynamics` or
`Diode with charge dynamics`.

### **Junction capacitance** — Junction capacitance `50` `nF` (default) | scalar

Diode junction capacitance.

#### Dependencies

To enable this parameter, set **Model dynamics**
to `Diode with charge dynamics`.

### **Peak reverse current, iRM** — Peak reverse current `-235` `A` (default) | negative scalar

Peak reverse current measured by an external test circuit. This value
must be less than zero.

#### Dependencies

To enable this parameter, set **Model dynamics**
to `Diode with charge dynamics`.

### **Initial forward current when measuring iRM** — Initial forward current when measuring iRM `300` `A` (default) | positive scalar

Initial forward current when measuring peak reverse current. This
value must be greater than zero.

#### Dependencies

To enable this parameter, set **Model dynamics**
to `Diode with charge dynamics`.

### **Rate of change of current when measuring iRM** — Rate of change of current when measuring iRM `-50` `A/μs` (default) | negative scalar

Rate of change of the current when measuring the peak reverse current. This value must
be less than zero.

#### Dependencies

To enable this parameter, set **Model dynamics**
to `Diode with charge dynamics`.

### **Reverse recovery time parameterization** — Reverse recovery time option `Specify stretch factor` (default) | `Specify reverse recovery time directly` | `Specify reverse recovery charge`

Determines how you specify reverse recovery time.

If you select `Specify stretch factor` or
`Specify reverse recovery charge`, you
specify a value that the block uses to derive the reverse recovery time.
For more information on these options, see How the Block Calculates TM and Tau.

#### Dependencies

To enable this parameter, set **Model dynamics**
to `Diode with charge dynamics`.

### **Reverse recovery time, trr** — Reverse recovery time `15` `μs` (default) | scalar

Interval between the time when the current initially goes to zero
(when the diode turns off) and the time when the current falls to less
than 10% of the peak reverse current. The value of the **Reverse
recovery time, trr** parameter must be greater than the
value of the **Peak reverse current, iRM** parameter
divided by the value of the **Rate of change of current when
measuring iRM** parameter.

#### Dependencies

To enable this parameter, set **Model dynamics**
to `Diode with charge dynamics` and
**Reverse recovery time parameterization** to
`Specify reverse recovery time
directly`.

### **Reverse recovery time stretch factor** — Reverse recovery time stretch factor `3` (default) | scalar

Value that the block uses to calculate **Reverse recovery
time, trr**. This value must be greater than
`1`. Specifying the stretch factor is an easier way
to parameterize the reverse recovery time than specifying the reverse
recovery charge. The larger the value of the stretch factor, the longer
it takes for the reverse recovery current to dissipate.

#### Dependencies

To enable this parameter, set **Model dynamics**
to `Diode with charge dynamics` and
**Reverse recovery time parameterization** to
`Specify stretch factor`.

### **Reverse recovery charge, Qrr** — Reverse recovery charge `1500` `s*μA` (default) | scalar

Value that the block uses to calculate **Reverse recovery time, trr**.
Use this parameter if the data sheet for your diode specifies a value
for the reverse recovery charge instead of a value for the reverse
recovery time.

The reverse recovery charge is the total charge that continues to dissipate when the
diode turns off. The value must be less than −i2RM2a, where:

- *iRM* is the value
  specified for **Peak reverse current,
  iRM**.
- *a* is the value specified for **Rate
  of change of current when measuring iRM**.

#### Dependencies

To enable this parameter, set **Model dynamics**
to `Diode with charge dynamics` and
**Reverse recovery time parameterization** to
`Specify reverse recovery charge`.

### Snubbers

To enable the **Snubbers** settings, set **Fidelity
level** to `Detailed model - switching
devices` and **Switching device** to
`GTO`, `Ideal Semiconductor
Switch`, `IGBT`,
`MOFSET`, or
`Thyristor`.

### **Snubber** — Snubber `None` (default) | `RC snubber`

Snubber for each switching device:

- `None`
- `RC snubber`

### **Snubber resistance** — Snubber resistance `0.1` `Ohm` (default) | scalar

Snubber resistance.

#### Dependencies

To enable this parameter, set **Snubber** to
`RC snubber`.

### **Snubber capacitance** — Snubber capacitance `1e-7` `F` (default) | scalar

Snubber capacitance.

#### Dependencies

To enable this parameter, set **Snubber** to
`RC snubber`.

## Libraries

Simscape / Electrical / Semiconductors & Converters / Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`.

As a result of these changes, inside a model saved in an earlier release, review
the **Electrical connection** parameter of this block.

## Description

Three-phase modular multilevel converter with series-connected power submodules

The Modular Multilevel Converter (Three-Phase) block
models a three-phase modular multilevel converter. Each phase consists of two arms that
are implemented with a number of series-connected power submodules.

Each submodule consists of a half-bridge or full-bridge converter and a
capacitor.

**Half-Bridge Topology**

**Full-Bridge Topology**

This blocks allows you to select the level of model fidelity by choosing between a
detailed model with switching devices or an equivalent model. You can choose from these
switching devices are:

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

### Piecewise Constant Approximation in Averaged Switch for FPGA Deployment

If you set the **Switching device** parameter to `Averaged switch` and your model uses a partitioning solver, this block produces nonlinear partitions because the average mode equations include modes, *Gsat* that are functions of the input **G**. To make these equations compatible with hardware description language (HDL) code generation, and therefore FPGA deployment, set the **Integer for piecewise constant approximation of gate input (0 for disabled)** parameter to a value greater than `0`. This block then treats the *Gsat* mode as a piecewise constant integer with a fixed range. This turns the previously nonlinear partitions to linear time varying partitions.

An integer value in the range `[0,K]`, where *K* is the value of the **Integer for piecewise constant approximation of gate input (0 for disabled)**, is now associated with each real value mode in the range `[0,1]`. The block computes the piecewise constant mode by dividing the original mode by K to normalize it back to the range `[0,1]`:

uI=(floor(u⋅K))u^=uIK

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
