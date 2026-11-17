---
type: simulink-block
title: 'S-R Latch'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits / Logic'
documentation_page: 'srlatch'
documentation_source_path: 'ref/srlatch.html'
language: en
---

# S-R Latch

## Ports
```yaml
ports:
- name: S
  summary: Set pin electrical
  direction: conserving
- name: R
  summary: Reset pin electrical
  direction: conserving
- name: Q
  summary: Output pin electrical
  direction: conserving
```

### Conserving

### **S** — Set pin electrical

Electrical conserving port associated with the S-R latch set
pin.

### **R** — Reset pin electrical

Electrical conserving port associated with the S-R latch reset
pin.

### **Q** — Output pin electrical

Electrical conserving port associated with the S-R latch output
pin.
## Parameters
```yaml
parameters:
- name: Low level input voltage
  summary: Low level input voltage 2 V (default)
  group: Inputs
- name: High level input voltage
  summary: High level input voltage 3 V (default)
  group: Inputs
- name: Average input capacitance
  summary: Average input capacitance 5 pF (default)
  group: Inputs
- name: Output current-voltage relationship
  summary: Output current-voltage relationship Linear (default) | Quadratic
  group: Outputs
- name: Low level output voltage
  summary: Low level output voltage 0 V (default)
  group: Outputs
- name: High level output voltage
  summary: High level output voltage 5 V (default)
  group: Outputs
- name: Output resistance
  summary: Output resistance 25 Ohm (default)
  group: Outputs
- name: Supply voltage
  summary: Supply voltage 5 V (default)
  group: Outputs
- name: Measurement voltage
  summary: Measurement voltage 5 V (default)
  group: Outputs
- name: Logic HIGH output resistance at zero current and at I_OH
  summary: Logic HIGH output resistance at zero current and at I_OH [25, 250] Ohm
  group: Outputs
- name: Logic HIGH output current I_OH when shorted to ground
  summary: Logic HIGH output current I_OH when shorted to ground 63 mA (default)
  group: Outputs
- name: Logic LOW output resistance at zero current and at I_OL
  summary: Logic LOW output resistance at zero current and at I_OL [30, 800] Ohm (default)
  group: Outputs
- name: Logic LOW output current I_OL when shorted to Vcc
  summary: Logic LOW output current I_OL when shorted to Vcc -45 mA (default)
  group: Outputs
- name: Propagation delay
  summary: Propagation delay 25 ns (default)
  group: Outputs
- name: Protection diode on resistance
  summary: Protection diode on resistance 5 Ohm (default)
  group: Outputs
- name: Protection diode forward voltage
  summary: Protection diode forward voltage 0.6 V (default)
  group: Outputs
- name: Output initial state
  summary: Output initial state Low (default) | High
  group: Initial Conditions
```

### Inputs

### **Low level input voltage** — Low level input voltage `2` `V` (default)

Voltage value less than which the block interprets the input voltage
as `LOW`.

### **High level input voltage** — High level input voltage `3` `V` (default)

Voltage value greater than which the block interprets the input
voltage as `HIGH`.

### **Average input capacitance** — Average input capacitance `5` `pF` (default)

Fixed capacitance that approximates the input capacitance for a MOSFET
gate. You can usually find this capacitance value on a manufacturer
datasheet. Setting this value to zero can result in faster simulation
times.

### Outputs

### **Output current-voltage relationship** — Output current-voltage relationship `Linear` (default) | `Quadratic`

Select the output model:

- `Linear` - This is the default
  value.
- `Quadratic`

### **Low level output voltage** — Low level output voltage `0` `V` (default)

Voltage value at the output when the output logic level is
`LOW`.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to
`Linear`.

### **High level output voltage** — High level output voltage `5` `V` (default)

Voltage value at the output when the output logic level is
`HIGH`.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to
`Linear`.

### **Output resistance** — Output resistance `25` `Ohm` (default)

Value of the series output resistor that is used to model the drop in
output voltage resulting from the output current. You can derive this
value from a datasheet by dividing the high-level output voltage by the
maximum low-level output current.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to
`Linear`.

### **Supply voltage** — Supply voltage `5` `V` (default)

Supply voltage value applied to the gate in your circuit.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to
`Quadratic`.

### **Measurement voltage** — Measurement voltage `5` `V` (default)

The gate supply voltage for which mask data output resistances and
currents are defined.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to
`Quadratic`.

### **Logic HIGH output resistance at zero current and at I\_OH** — Logic HIGH output resistance at zero current and at I\_OH `[25, 250]` `Ohm`

A row vector [ *R\_OH1**R\_OH2* ] of
two resistance values. The first value *R\_OH1* is the
gradient of the output voltage-current relationship when the gate is
logic HIGH and there is no output current. The second value
*R\_OH2* is the gradient of the output
voltage-current relationship when the gate is logic HIGH and the output
current is *I\_OH*.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to
`Quadratic`.

### **Logic HIGH output current I\_OH when shorted to ground** — Logic HIGH output current I\_OH when shorted to ground `63` `mA` (default)

The resulting current when the gate is in the logic HIGH state, but
the load forces the output voltage to zero.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to
`Quadratic`.

### **Logic LOW output resistance at zero current and at I\_OL** — Logic LOW output resistance at zero current and at I\_OL `[30, 800]` `Ohm` (default)

A row vector [ *R\_OL1**R\_OL2* ] of
two resistance values. The first value *R\_OL1* is the
gradient of the output voltage-current relationship when the gate is
logic LOW and there is no output current. The second value
*R\_OL2* is the gradient of the output
voltage-current relationship when the gate is logic LOW and the output
current is *I\_OL*.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to
`Quadratic`.

### **Logic LOW output current I\_OL when shorted to Vcc** — Logic LOW output current I\_OL when shorted to Vcc `-45` `mA` (default)

The resulting current when the gate is in the logic LOW state, but the
load forces the output voltage to the supply voltage Vcc.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to
`Quadratic`.

### **Propagation delay** — Propagation delay `25` `ns` (default)

Time it takes for the output to swing from `LOW` to
`HIGH` or `HIGH` to
`LOW` after the input logic levels change.

### **Protection diode on resistance** — Protection diode on resistance `5` `Ohm` (default)

The gradient of the voltage-current relationship for the protection
diodes when forward biased.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to
`Quadratic`.

### **Protection diode forward voltage** — Protection diode forward voltage `0.6` `V` (default)

The voltage above which the protection diode is turned on.

#### Dependencies

To enable this parameter, set **Output current-voltage
relationship** to
`Quadratic`.

### Initial Conditions

### **Output initial state** — Output initial state `Low` (default) | `High`

Specify whether the initial output state of the block is
`High` or `Low`.
This parameter is used for both linear and quadratic output states,
provided that the **Propagation delay** parameter is
greater than zero and the Solver
Configuration block does not have the
**Start simulation from steady state** option
selected.
## Libraries

Simscape / Electrical / Integrated Circuits / Logic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009b**

## Description

Behavioral model of S-R Latch

The S-R Latch block is an abstracted behavioral model
of a set-reset latch. It does not model the internal individual MOSFET devices (see
Assumptions and Limitations for details). Therefore, the block runs quickly
during simulation but retains the correct I/O behavior.

If the gate voltage is greater than the threshold voltage VTH, then the input taken is `1`
(`HIGH`). Otherwise, the input is zero (`LOW`). The
gate threshold voltage VTH is halfway between the **Low level input voltage** (VIL) and **High level input voltage** (VIH) parameters.

The block output logic level is either HIGH or LOW, according to the logic levels of
the gate inputs and the S-R latch truth table.

| S | R | Q n |
| --- | --- | --- |
| 0 | 0 | Q n-1 |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

The block models the gate as follows:

- The gate inputs have infinite resistance and finite or zero
  capacitance.
- The gate output offers a selection of two models:
  `Linear` and `Quadratic`.
  For more information, see Selecting the Output Model for Logic Blocks. Use the
  **Output current-voltage relationship** parameter to
  specify the output model.
- You can specify propagation delay for both output models. For
  `Linear` output, the block sets the value of the
  gate output capacitor such that the resistor-capacitor time constant equals the
  **Propagation delay** parameter value. For
  `Quadratic` output, the gate input demand is lagged
  to approximate the **Propagation delay** parameter
  value.

The block initial conditions depend on the output
model selected:

- For `Linear` model, the high initial condition
  corresponds to the **High level output voltage** parameter
  value, `V_OH`, and the low initial condition corresponds to
  the **Low level output voltage** parameter value,
  `V_OL`.
- For `Quadratic` model, the high initial condition
  is a value close to the **Supply voltage** parameter value,
  `Vcc`, and the low initial condition is close to
  `0`.

The block output voltage depends on the output model selected:

- For `Linear` model, output high is the **High
  level output voltage** parameter value, and output low is the
  **Low level output voltage** parameter value.
- For `Quadratic` model, the output voltage for High
  and Low states is a function of the output current, as explained in Quadratic Model Output and Parameters. For zero load current,
  output high is Vcc (the **Supply voltage** parameter value),
  and output low is zero volts.

### Plot Input and Output Waveforms

You can plot the input and output waveforms of the S-R Latch block without building a
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
