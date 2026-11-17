---
type: simulink-block
title: 'Assertion'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'For Use with DPI-C SystemVerilog'
documentation_page: 'assertion'
documentation_source_path: 'ref/assertion.html'
language: en
---

# Assertion

## Ports
```yaml
ports:
- name: Port_1
  summary: Signal to check for nonzero value scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### Input

### **Port\_1** — Signal to check for nonzero value scalar | vector | matrix

The Assertion block accepts input signals of any
dimensions and numeric data type that Simulink supports.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Enable assertion
  summary: Enable or disable assertion on (default) | off
  group: ''
- name: Simulation callback when assertion fails
  summary: Expression to evaluate when assertion fails MATLAB expression
  group: ''
- name: Stop simulation when assertion fails
  summary: Stop Simulink simulation when assertion fails off (default) | on
  group: ''
- name: Severity
  summary: Severity of assertion failure error (default) | warning | custom
  group: DPI-C Assertion Options
- name: Assertion fail message
  summary: Custom message when assertion fails no default
  group: DPI-C Assertion Options
- name: Assertion custom command
  summary: Custom command to execute when assertion fails SystemVerilog command
  group: DPI-C Assertion Options
```

### **Enable assertion** — Enable or disable assertion on (default) | off

Selecting this check box enables the block to display a simulation
warning or error. It also enables the block to create a SystemVerilog
assertion in your generated code. Clearing this check box disables the
assertion in simulation, and it does not generate a SystemVerilog
assertion.

### **Simulation callback when assertion fails** — Expression to evaluate when assertion fails MATLAB expression

Specify a MATLAB expression for Simulink to evaluate when the assertion fails. The block ignores this
parameter in the generated DPI-C assertion.

#### Dependencies

To enable this parameter, select the **Enable
assertion** parameter.

### **Stop simulation when assertion fails** — Stop Simulink simulation when assertion fails off (default) | on

Selecting this check box causes Simulink to stop the simulation and
display an error when the block input is zero. Clearing this check box
enables Simulink to continue the simulation, displaying a warning when the
block input is zero. The block ignores this parameter in the generated DPI-C
assertion.

#### Dependencies

To enable this parameter, select the **Enable
assertion** parameter.

### DPI-C Assertion Options

Use these parameters to control the behavior of a generated DPI-C assertion, in a
SystemVerilog simulation environment. To enable generation of DPI-C assertion,
select **Enable assertion**.

### **Severity** — Severity of assertion failure `error` (default) | `warning` | `custom`

Select `error` or `warning` for the
DPI-C assertion to issue a SystemVerilog error or warning message. Set
to `custom` to execute a custom command.

#### Dependencies

To enable this parameter, select the **Enable
assertion** parameter.

### **Assertion fail message** — Custom message when assertion fails no default

Specify a custom SystemVerilog message to be emitted when the
SystemVerilog assertion fails. This feature supports only ASCII
characters.

**Example:** `RX fail`

#### Dependencies

To enable this parameter, set **Severity** to
`error` or
`warning`.

### **Assertion custom command** — Custom command to execute when assertion fails SystemVerilog command

Specify a custom SystemVerilog command to execute when the assertion
fails. You can set this parameter to be a display statement, command, or
script. This feature supports only ASCII characters

**Example:** `$display("RX fail at %0t",
$time);`

#### Dependencies

To enable this parameter, set **Severity** to
`custom`.
## Libraries

HDL Verifier / For Use with DPI-C SystemVerilog

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Generate SystemVerilog assertions from Simulink assertion

The Assertion block asserts that its input signal is nonzero. If its
input is zero, the block halts the simulation by default and displays an error message.
When you generate a DPI-C SystemVerilog component - the block creates an immediate
SystemVerilog assertion. Using the block parameters, you can:

- Enable or disable the assertion.
- Specify a MATLAB® expression for Simulink® to evaluate when the assertion fails.
- Select for Simulink to either stop simulation or continue but display a
  warning when assertion fails.

Use the DPI-C parameters to control runtime options:

- Specify the severity of the generated assertion.
- Specify a custom message or action when the assertion fails.
