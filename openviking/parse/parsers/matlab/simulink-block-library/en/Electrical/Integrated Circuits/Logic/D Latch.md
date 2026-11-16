---
type: simulink-block
title: 'D Latch'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Flip Flops'
documentation_page: 'dlatch'
documentation_source_path: '../sps/ref/dlatch.html'
language: en
---

# D Latch

## Ports

### Conserving

### **D** — Data pin electrical

Electrical conserving port associated with the data pin.

### **E** — Enable pin electrical

Electrical conserving port associated with the enable pin.

### **Q** — Output pin electrical

Electrical conserving port associated with the output pin.

### **!Q** — Inverted output pin electrical

Electrical conserving port associated with the inverted output pin.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Inputs

### **Low level input voltage** — Input voltage below which logic is `0` `2` `V` (default) | nonnegative scalar

Input voltage below which the block interprets the input logic as
`0`.

### **High level input voltage** — Input voltage above which logic is `1` `3` `V` (default) | positive scalar

Input voltage above which the block interprets the input logic as
`1`.

### **Average input capacitance** — Input capacitance for MOSFET gate `5` `pF` (default) | nonnegative scalar

Fixed capacitance that approximates the input capacitance for a MOSFET gate. The
MOSFET capacitance depends on the applied voltage. When you drive this block with
another gate, the **Average input capacitance** parameter produces a
rise time similar to that of the MOSFET. You can find this capacitance value on a
manufacturer datasheet. For fast simulation, set this parameter to zero.

### Outputs

### **Output current-voltage relationship** — Model for output current-voltage relationship `Linear` (default) | `Quadratic`

Model that determines the relationship between the output current and output
voltage. Set this parameter to `Linear` for faster simulation
and `Quadratic` for more accurate results. For more
information, see Selecting the Output Model for Logic Blocks.

### **Low level output voltage** — Output voltage when logic is `0` `0` `V` (default) | nonnegative scalar

Output voltage when the logic level at the output pin is
`0`.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to `Linear`.

### **High level output voltage** — Output voltage when logic is `1` `5` `V` (default) | positive scalar

Output voltage when the logic level at the output pin is
`1`.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to `Linear`.

### **Output resistance** — Output resistance `25` `Ohm` (default) | nonnegative scalar

Output resistance that the block uses to model the drop in output voltage
resulting from the output current. You can calculate this value from a datasheet by
dividing the high-level output voltage by the maximum low-level output current.

If you set the **Propagation delay** parameter to zero, you must
set the **Output resistance** parameter to a positive value.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to `Linear`.

### **Supply voltage** — Supply voltage `5` `V` (default) | positive scalar

Voltage you supply to the gate in the circuit.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to `Quadratic`.

### **Measurement voltage** — Measurement supply voltage `5` `V` (default) | positive scalar

Gate supply voltage at which you quote the output resistances and currents.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to `Quadratic`.

### **Logic HIGH output resistance at zero current and at I\_OH** — Resistance when output logic is `1` `[25, 250]` `Ohm` | 2-D vector of positive scalars

Resistance when the logic level at the output is `1`. Specify
this parameter as a row vector of two resistance values [*R\_OH1*,
*R\_OH2*]. The first value, *R\_OH1*, is the
gradient of the output voltage-current relationship when there is no output current.
The second value, *R\_OH2*, is the gradient of the output
voltage-current relationship when the output is shorted to ground.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to `Quadratic`.

### **Logic HIGH output current I\_OH when shorted to ground** — Output current when logic is `1` `63` `mA` (default) | positive scalar

Output current when the logic level at the output is `1`, but the
load forces the output voltage to zero.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to `Quadratic`.

### **Logic LOW output resistance at zero current and at I\_OL** — Resistance when output logic is `0` `[30, 800]` `Ohm` (default) | 2-D vector of positive scalars

Resistance when the logic level at the output is `0`. Specify
this parameter as a row vector of two resistance values [*R\_OL1*,
*R\_OL2*]. The first value, *R\_OL1*, is the
gradient of the output voltage-current relationship when there is no output current.
The second value, *R\_OL2*, is the gradient of the output
voltage-current relationship when the load forces the output voltage to the
**Supply voltage** parameter value.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to `Quadratic`.

### **Logic LOW output current I\_OL when shorted to Vcc** — Output current when logic is `0` `-45` `mA` (default) | negative scalar

Output current when the logic level at the output is `0`, but the
load forces the output voltage to the **Supply voltage** parameter
value.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to `Quadratic`.

### **Propagation delay** — Time for output voltage to change states `25` `ns` (default) | nonnegative scalar

Time it takes for the output voltage to change from the `low` to
`high` or `high` to `low` states
after the input logic levels change.

If you set the **Propagation delay** parameter to zero, you must
set the **Output resistance** parameter to a positive value.

### **Protection diode on resistance** — Protection diode on resistance `5` `Ohm` (default) | positive scalar

Gradient of the voltage-current relationship for the protection diodes when they
are forward biased.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to `Quadratic`.

### **Protection diode forward voltage** — Protection diode forward voltage `0.6` `V` (default) | positive scalar

Voltage above which the protection diode turns on.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to `Quadratic`.

## Libraries

Simscape / Electrical / Integrated Circuits / Logic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Behavioral model of D latch

The D Latch block implements a behavioral model of a D-type
latch. The block stores a one-bit value, either `0` (`low`)
or `1` (`high`).

The block has two input ports that control the latch: the data pin **D** and the
enable pin **E**. When the logic level at **E** is `1`, the
block transfers the data to the output pin **Q**. When the logic level at
**E** is `0`, the block holds the output in its previous state.
This truth table summarizes the logic levels at the inputs and output. The subscript
`n` represents the value at the current time step and
`n-1` represents the value at the previous time step. The logic level at
the inverted output pin **!Q** is the inverse of the logic level at
**Q**.

| En | Dn | Qn |
| --- | --- | --- |
| `0` | `0` | Qn-1 |
| `0` | `1` | Qn-1 |
| `1` | `0` | `0` |
| `1` | `1` | `1` |

To specify the logic level at **Q** at the start of the simulation, in the
**Initial Targets** section, set the value of the **Output
logic** parameter to `0` or `1`.
The block uses this value as the initial logic level at **Q** only if the initial
logic level at **E** is `0`. In this situation, the block
normally holds the output in its previous state. For more information about initial targets,
see Set Priority and Initial Target for Block Variables.

The gate inputs have an infinite resistance and a finite or zero capacitance.

If the gate voltage is greater than the threshold voltage, then the block takes the logic
level at the input as `1`. Otherwise, the block takes the logic level at the
input as `0`. The block calculates the threshold voltage as the average of
the **Low level input voltage** and the **High level input
voltage** parameter values.

The gate output depends on the **Output current-voltage relationship**
parameter. Set this parameter to `Linear` for faster simulation and
`Quadratic` for more accurate results. For most models, use the
`Linear` option. You can use the
`Quadratic` option to validate the results that you obtain using
the simpler linear model. For more information, see Selecting the Output Model for Logic Blocks.

If you set the **Output current-voltage relationship** parameter to
`Linear`:

- If the logic level at the **Q** port is `0`, the output
  voltage is equal to the **Low level output voltage** parameter
  value.
- If the logic level at the **Q** port is `1`, the output
  voltage is equal to the **High level output voltage** parameter
  value.
- The resistor-capacitor time constant of the gate output capacitor is equal to the
  **Propagation delay** parameter value.

If you set the **Output current-voltage relationship** parameter to
`Quadratic`:

- The output voltage is a function of the output current. For zero-load current:

  - If the logic level at the **Q** port is `0`, the
    output voltage is zero.
  - If the logic level at the **Q** port is `1`, the
    output voltage is equal to the **Supply voltage** parameter
    value.
- The gate input demand lags to approximate the **Propagation delay**
  parameter value.

For more information, see Quadratic Model Output and Parameters.

### Plot Input and Output Waveforms

You can plot the input and output waveforms of the D Latch block without building a
complete model. Use the plots to explore the impact of your parameter choices on
device characteristics. If you parameterize the block from a datasheet, you can
compare your plots to the datasheet to check that you parameterized the block
correctly. If you have a complete working model but do not know which manufactured
part to use, you can compare your plots to datasheets to help you decide.

To plot the basic characteristics, right-click the block and select
**Electrical** > **Basic
characteristics** from the context menu.

**Note**

The plots you create using the **Basic
characteristics** option do not show the effect
of the **Propagation delay** parameter on the
output voltage of logic blocks.

### Assumptions and Limitations

- To improve simulation speed, the block does not model all the internal
  metal-oxide-semiconductor field-effect transistor (MOSFET) devices in the gate
  individually. The block therefore does not accurately model the response of the gate to
  input noise and input voltages that are close to the threshold voltage.
- If you are modeling a circuit that has a feedback path around a set of logic gates,
  you must set the **Propagation delay** parameter to a nonzero value on
  one or more of the gates.
