---
type: simulink-block
title: 'Linear Circuit Wizard'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'linearcircuitwizard'
documentation_source_path: 'ref/linearcircuitwizard.html'
language: en
---

# Linear Circuit Wizard

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Circuit design name
  summary: Name of circuit displayed on block icon 'Linear Circuit' (default) | character vector | string scalar
  group: Circuit Definition
  block_parameter: CircuitDesignName
  type: character vector
  values: character string
  default: '''Linear Circuit'''
- name: Block name
  summary: Instance name displayed under block icon 'Linear Circuit' (default) | character vector | string scalar
  group: Circuit Definition
  block_parameter: BlockName
  type: character vector
  values: character string
  default: '''Linear Circuit'''
- name: Netlist file name
  summary: Name of netlist file that defines circuit character vector | string scalar
  group: Circuit Definition
  block_parameter: NetlistFileName
  type: character vector
  values: character string
- name: Configuration name
  summary: Name of configuration file character vector | string scalar
  group: Circuit Definition
  block_parameter: ConfigurationName
  type: character vector
  values: character string
- name: Parse netlist file and start new configuration
  summary: Parse named netlist file button
  group: Circuit Definition
- name: Save configuration
  summary: Save current configuration to file button
  group: Circuit Definition
- name: Load configuration
  summary: Load existing configuration file button
  group: Circuit Definition
- name: Attach configuration to block
  summary: Attach selected configuration file to Simulink block on (default) | off
  group: Circuit Definition
- name: Build Simulink block
  summary: Create Simulink block or object to model circuit defined by netlist button
  group: Circuit Definition
- name: Pole/zero report
  summary: Add pole -zero report to base workspace on (default) | off
  group: Linear Analysis
- name: Transfer function plot
  summary: Plot transfer functions on (default) | off
  group: Linear Analysis
- name: Linear control system
  summary: Add matrices for control system differential equations to base workspace on (default) | off
  group: Linear Analysis
- name: Analyze
  summary: Analyze linear circuit to produce selected outputs button
  group: Linear Analysis
- name: Output port
  summary: Outport port for primary output value drop-down menu created from port definitions
  group: Operating Point Analysis
- name: Steady state output value(s)
  summary: Desired primary output value(s) 0 (default) | scalar | vector
  group: Operating Point Analysis
  block_parameter: OutputValues
  type: character vector
  values: scalar | vector
  default: '0'
- name: Primary control variable
  summary: Variable used to regulate output Duty cycle (default) | Frequency
  group: Operating Point Analysis
  block_parameter: ControlVariable
  type: character vector
  values: Duty cycle | Frequency
  default: Duty cycle
- name: Duty cycle value [min,max]
  summary: Minimum control duty cycle 0 (default) | scalar | 2-element vector
  group: Operating Point Analysis
  block_parameter: DutyCycle
  type: character vector
  values: scalar | 2-element vector
  default: '0'
- name: Frequency [min,max]
  summary: Minimum control frequency 0 (default) | scalar | 2-element vector
  group: Operating Point Analysis
  block_parameter: Frequency
  type: character vector
  values: scalar | 2-element vector
  default: '0'
- name: Phase offset(s)
  summary: Phase of rising edge of control signal as fraction of control cycle 0 (default) | scalar | vector
  group: Operating Point Analysis
  block_parameter: PhaseOffsets
  type: character vector
  values: scalar | vector
  default: '0'
- name: Pulse Duration(s)
  summary: Pulse duration of control signal as function of control cycle 0 (default) | scalar | vector
  group: Operating Point Analysis
  block_parameter: PulseDuration
  type: character vector
  values: scalar | vector
  default: '0'
- name: Samples per waveform
  summary: Number of samples in single switching cycle output wave 1024 (default) | positive integer scalar
  group: Operating Point Analysis
  block_parameter: WaveSamples
  type: character vector
  values: scalar
  default: '1024'
- name: Analyze operating point
  summary: Operating point analysis of switched circuit button
  group: Operating Point Analysis
```

### Circuit Definition

### **Circuit design name** — Name of circuit displayed on block icon `'Linear Circuit'` (default) | character vector | string scalar

Name of the circuit that is displayed on the block icon, specified as a character
vector or string scalar.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CircuitDesignName` |
| **Type:** character vector |
| **Value:** character string |
| **Default:** `'Linear Circuit'` |

### **Block name** — Instance name displayed under block icon `'Linear Circuit'` (default) | character vector | string scalar

Instance name to be displayed under the block icon, specified as a character
vector or string scalar.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `BlockName` |
| **Type:** character vector |
| **Value:** character string |
| **Default:** `'Linear Circuit'` |

### **Netlist file name** — Name of netlist file that defines circuit character vector | string scalar

Name of the netlist file (SPICE syntax) that defines the linear circuit, specified
as a character vector or string scalar.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `NetlistFileName` |
| **Type:** character vector |
| **Value:** character string |

### **Configuration name** — Name of configuration file character vector | string scalar

Name of the configuration file, specified as a character vector or string scalar.
You can save your current configuration to a file.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ConfigurationName` |
| **Type:** character vector |
| **Value:** character string |

### **Parse netlist file and start new configuration** — Parse named netlist file button

Click to parse the named netlist file. This action redefines the existing ports
according to the new SPICE syntax. For more information, see Model Linear Circuit Response from SPICE Netlist.

### **Save configuration** — Save current configuration to file button

Click to save the current circuit configuration to a file whose name is specified
in the **Configuration name**.

### **Load configuration** — Load existing configuration file button

Click to load the current circuit configuration from the file whose name is
specified in the **Configuration name** parameter.

### **Attach configuration to block** — Attach selected configuration file to Simulink block on (default) | off

Select to attach the selected configuration file to the Simulink block when it is built by the Linear Circuit Wizard
block.

### **Build Simulink block** — Create Simulink block or object to model circuit defined by netlist button

Click to create a Simulink block or object to model the circuit defined by SPICE netlist.

If switch states have been defined for the circuit, the constructed block will be
a switched circuit block. Otherwise it will be a linear circuit block.

### Linear Analysis

### **Pole/zero report** — Add pole -zero report to base workspace on (default) | off

Select to add a structure containing the pole-zero report to the base workspace
when the linear circuit is analyzed.

### **Transfer function plot** — Plot transfer functions on (default) | off

Select to plot all transfer functions of the linear circuit when the linear
circuit is analyzed.

### **Linear control system** — Add matrices for control system differential equations to base workspace on (default) | off

Select to add a structure containing the matrices for the control system
differential equations to the base workspace when the linear circuit is
analyzed.

### **Analyze** — Analyze linear circuit to produce selected outputs button

Click to analyze the linear circuit and produce the selected outputs.

### Operating Point Analysis

### **Output port** — Outport port for primary output value drop-down menu created from port definitions

Select the output port for the primary output value from a drop-down menu. The
drop-down menu remains empty until you parse the netlist to define the ports.

### **Steady state output value(s)** — Desired primary output value(s) `0` (default) | `scalar` | `vector`

Desired primary output value(s), specified as a scalar or a vector.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutputValues` |
| **Type:** character vector |
| **Value:** scalar | vector |
| **Default:** `0` |

### **Primary control variable** — Variable used to regulate output **Duty cycle** (default) | **Frequency**

The variable the block uses to regulate the output. Choose between **Duty
Cycle** or **Frequency**.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ControlVariable` |
| **Type:** character vector |
| **Value:** **Duty cycle** | **Frequency** |
| **Default:** **Duty cycle** |

### **Duty cycle value [min,max]** — Minimum control duty cycle `0` (default) | scalar | 2-element vector

Control duty cycle, defined on a scale from 0 to 1. You can specify a scalar to be
applied to all analyses, or you can specify the minimum and maximum of a range of
control duty cycles as a 2-element vector thus producing a plot of output value as a
function of control duty cycle.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `DutyCycle` |
| **Type:** character vector |
| **Value:** scalar | 2-element vector |
| **Default:** `0` |

### **Frequency [min,max]** — Minimum control frequency `0` (default) | scalar | 2-element vector

Control signal frequency. You can specify a scalar to be applied to all analyses,
or you can specify the minimum and maximum of a range of frequencies as a 2-element
vector thus producing a plot of output value as a function of control signal
frequency.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Frequency` |
| **Type:** character vector |
| **Value:** scalar | 2-element vector |
| **Default:** `0` |

### **Phase offset(s)** — Phase of rising edge of control signal as fraction of control cycle `0` (default) | scalar | vector

Phase of the rising edge of the control signal(s) as a fraction of control cycle
(0,1), specified as a scalar (single control signal) or vector (multiple control
signals).

You can use the variable *d* to represent the control duty cycle
or *f* to represent the switching frequency.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PhaseOffsets` |
| **Type:** character vector |
| **Value:** scalar | vector |
| **Default:** `0` |

### **Pulse Duration(s)** — Pulse duration of control signal as function of control cycle `0` (default) | scalar | vector

Pulse duration of the control signals as a function of the control cycle (0,1),
specified as a scalar (single control signal) or vector (multiple control
signals).

You can use the variable *d* to represent the control duty cycle
or *f* to represent the switching frequency.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PulseDuration` |
| **Type:** character vector |
| **Value:** scalar | vector |
| **Default:** `0` |

### **Samples per waveform** — Number of samples in single switching cycle output wave `1024` (default) | positive integer scalar

Number of samples in a single steady state switching cycle output wave, specified
as a positive integer scalar.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `WaveSamples` |
| **Type:** character vector |
| **Value:** scalar |
| **Default:** `1024` |

### **Analyze operating point** — Operating point analysis of switched circuit button

Click to perform the switched-mode power train operating point analysis of the
switched circuit.
## Libraries

Mixed-Signal Blockset / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

### R2025a: Debug Mode for Switched Circuits

You can activate debug mode for switched circuits to record waveforms for all the nodes
in the circuit for a specified time interval during a time domain simulation. You can also
set the initial conditions for nodes in a Switched Circuit block.

## Description

Generate or modify linear circuit

Use the Linear Circuit Wizard block to create or modify a linear,
time-invariant circuit such as a custom-design filter or a circuit with extracted parasitics.
Using this block, you can parse a SPICE netlist file that describes the circuit elements and
the circuit nodes. You can then use the block parameter dialog box to refine the input and
output ports and to model device noise. You can review the port and device noise definitions
from a base workspace output structure.

The Linear Circuit Wizard block sets up and solves linear circuit equations
to produce a set of Laplace domain transfer functions. You can review these transfer functions
either through magnitude vs. frequency plots or through pole-zero location reports.

The Linear Circuit Wizard block creates and configures a MATLAB
System block to represent your circuit as a new block, which is independent of the
Linear Circuit Wizard block, in a Simulink® model. This MATLAB System block is configured using the port and
device noise definitions and the results of the circuit analysis. When you start the
simulation, the MATLAB System block uses fixed-step discrete sample time to
convert the Laplace domain transfer functions into recursive digital filter coefficients for
execution during the simulation.

The Linear Circuit Wizard block can generate:

- a linear circuit block,
- a switched circuit block,
- or a Control System Toolbox™ tunable object.
