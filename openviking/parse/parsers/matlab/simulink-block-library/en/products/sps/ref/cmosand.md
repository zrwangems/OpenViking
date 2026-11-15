---
type: simulink-block
title: 'CMOS AND'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Integrated Circuits / Logic'
documentation_page: 'cmosand'
documentation_source_path: 'ref/cmosand.html'
language: en
---

# CMOS AND

## Ports

### Conserving

### **A** — Input port electrical

Electrical conserving port associated with the CMOS AND input.

### **B** — Input port electrical

Electrical conserving port associated with the CMOS AND input.

### **J** — Output port electrical

Electrical conserving port associated with the CMOS AND output.

## Parameters

### Inputs

### **Low level input voltage** — Low level input voltage `2` `V` (default)

Voltage value below which the block interprets the input voltage as
logic `LOW`.

### **High level input voltage** — High level input voltage `3` `V` (default)

Voltage value above which the block interprets the input voltage as
logic `HIGH`.

### **Average input capacitance** — Average input capacitance `5` `pF` (default)

Fixed capacitance that approximates the input capacitance for a MOSFET
gate. The MOSFET capacitance depends on the applied voltage. When you
drive this block with another gate, the **Average input
capacitance** produces a rise time similar to that of the
MOSFET. You can usually find this capacitance value on a manufacturer
datasheet. Setting this value to zero may result in faster simulation
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

This parameter is visible only when you select
`Linear` for the **Output
current-voltage relationship** parameter.

### **High level output voltage** — High level output voltage `5` `V` (default)

Voltage value at the output when the output logic level is
`HIGH`.

#### Dependencies

This parameter is visible only when you select
`Linear` for the **Output
current-voltage relationship** parameter.

### **Output resistance** — Output resistance `25` `Ohm` (default)

Value of the series output resistor that is used to model the drop in
output voltage resulting from the output current. You can derive this
value from a datasheet by dividing the high-level output voltage by the
maximum low-level output current.

#### Dependencies

This parameter is visible only when you select
`Linear` for the **Output
current-voltage relationship** parameter.

### **Supply voltage** — Supply voltage `5` `V` (default)

Supply voltage value applied to the gate in your circuit.

#### Dependencies

This parameter is visible only when you select
`Quadratic` for the **Output
current-voltage relationship** parameter.

### **Measurement voltage** — Measurement voltage `5` `V` (default)

The gate supply voltage for which mask data output resistances and
currents are defined.

#### Dependencies

This parameter is visible only when you select
`Quadratic` for the **Output
current-voltage relationship** parameter.

### **Logic HIGH output resistance at zero current and at I\_OH** — Logic HIGH output resistance at zero current and at I\_OH `[25, 250]` `Ohm`

A row vector [ *R\_OH1**R\_OH2* ] of
two resistance values. The first value *R\_OH1* is the
gradient of the output voltage-current relationship when the gate is
logic HIGH and there is no output current. The second value
*R\_OH2* is the gradient of the output
voltage-current relationship when the gate is logic HIGH and the output
current is *I\_OH*.

#### Dependencies

This parameter is visible only when you select
`Quadratic` for the **Output
current-voltage relationship** parameter.

### **Logic HIGH output current I\_OH when shorted to ground** — Logic HIGH output current I\_OH when shorted to ground `63` `mA` (default)

The resulting current when the gate is in the logic HIGH state, but
the load forces the output voltage to zero.

#### Dependencies

This parameter is visible only when you select
`Quadratic` for the **Output
current-voltage relationship** parameter.

### **Logic LOW output resistance at zero current and at I\_OL** — Logic LOW output resistance at zero current and at I\_OL `[30, 800]` `Ohm` (default)

A row vector [ *R\_OL1**R\_OL2* ] of
two resistance values. The first value *R\_OL1* is the
gradient of the output voltage-current relationship when the gate is
logic LOW and there is no output current. The second value
*R\_OL2* is the gradient of the output
voltage-current relationship when the gate is logic LOW and the output
current is *I\_OL*.

#### Dependencies

This parameter is visible only when you select
`Quadratic` for the **Output
current-voltage relationship** parameter.

### **Logic LOW output current I\_OL when shorted to Vcc** — Logic LOW output current I\_OL when shorted to Vcc `-45` `mA` (default)

The resulting current when the gate is in the logic LOW state, but the
load forces the output voltage to the supply voltage Vcc.

#### Dependencies

This parameter is visible only when you select
`Quadratic` for the **Output
current-voltage relationship** parameter.

### **Propagation delay** — Propagation delay `25` `ns` (default)

Time it takes for the output to swing from `LOW` to
`HIGH` or `HIGH` to
`LOW` after the input logic levels change.

### **Protection diode on resistance** — Protection diode on resistance `5` `Ohm` (default)

The gradient of the voltage-current relationship for the protection
diodes when forward biased.

#### Dependencies

This parameter is visible only when you select
`Quadratic` for the **Output
current-voltage relationship** parameter.

### **Protection diode forward voltage** — Protection diode forward voltage `0.6` `V` (default)

The voltage above which the protection diode is turned on.

#### Dependencies

This parameter is visible only when you select
`Quadratic` for the **Output
current-voltage relationship** parameter.

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

**Introduced in R2008b**

## Description

Behavioral model of CMOS AND gate

The CMOS AND block represents a CMOS AND logic gate
behaviorally:

- The block output logic level is `HIGH` if the logic levels of
  both of the gate inputs are 1.
- The block output logic level is `LOW` otherwise.

The block determines the logic levels of the gate inputs as follows:

- If the gate voltage is greater than the threshold voltage, the block
  interprets the input as logic 1.
- Otherwise, the block interprets the input as logic 0.

The *threshold voltage* is the voltage value at midpoint between
the **High level input voltage** parameter value and the **Low
level input voltage** parameter value.

**Note**

To improve simulation speed, the block does not model all the internal individual
MOSFET devices that make up the gate. See Assumptions and Limitations for details.

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

You can plot the input and output waveforms of the CMOS AND block without building a
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
