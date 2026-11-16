---
type: simulink-block
title: 'FIL Simulation'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'Algorithm Verification / FPGA-in-the-Loop'
documentation_page: 'filsimulation'
documentation_source_path: 'ref/filsimulation.html'
language: en
---

# FIL Simulation

## Ports

### Input

### **HDL\_input\_port\_name** — Signal passed from Simulink to FPGA scalar | vector

The ports on the block correspond with ports on your HDL design. You can configure the
**Sample time** and **Data type**

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `Fixed-point`
### Output

### **HDL\_output\_port\_name** — Signal passed from the FPGA to Simulink scalar | vector

The ports on the block correspond with ports on your HDL design. You can configure the
**Sample time** and **Data type**

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `Fixed-point`

## Parameters

The parameters displayed in the **Hardware Information** section
reflect your selections when you generated the FIL Simulation block
from a subsystem. These parameters are informational only.

- **Connection**: Either Ethernet or PCI Express®.
  Some boards can use only one connection type or the other; with other
  boards, you may have the option of using either connection. You configure
  the **MAC address** and **IP address** of
  the board when you generate the block.
- **Board**: The make and model of
  FPGA board. For supported boards, see Supported FPGA Devices for FPGA Verification.
- **FPGA part**: Chip identification
  number.
- **FPGA project file**: The location
  of the FPGA project file generated for your design.

To download the generated FPGA programming file onto the FPGA,
set the parameters in **FPGA Programming File**.
This step is required before you can run a FIL simulation. See Load Programming File onto FPGA.

To configure data rate parameters, set options in the **Runtime
Options** group.

On the **Signal Attributes** pane, you can
configure **Sample time** and **Data type** for
each output port. The direction and bit width of the signals, and
the sample time and data type of the input ports, are informational
only.

#### FPGA Programming File

### **File name** — Location of programming file string

Location of the FPGA programming file generated for your design.
To load this design to the FPGA for simulation, click **Load**.

#### Runtime Options

### **Overclocking factor** — FPGA sample rate relative to Simulink clock 1 (default) | integer

Ratio of FPGA clock rate to the Simulink clock rate. The FPGA clock samples inputs to the FPGA this many times for each
Simulink time step.

### **Output frame size** — Amount of data returned to Simulink `Inherit: auto` (default)

Output signals are returned as **Output frame size**-by-1
column vectors. Increasing the frame size can speed up your simulation
by reducing the communication time between Simulink and the FPGA
board.

Note these limitations on the frame size :

- The input frame size must be an integer multiple of
  the output frame size.
- The output frame size must be less than the input
  frame size.
- The input frame size and output frame size cannot
  vary during simulation.

#### Signal Attributes

### **Sample Time** — Sample time of each port `Inherit: Inherit via internal rule` (default)

Explicitly set sample times for the output signals, or use `Inherit:
Inherit via internal rule`. The internal rule is to set
the output sample times to the input base sample time divided by the
scaling factor.

### **Data type** — Data type of each port `fixdt(0,N,0)` (default) | data type expression

How Simulink interprets the bits in the output signal from
the FPGA. You can explicitly set output data types, use the default
unscaled and unsigned type, or specify `Inherit: auto` to
inherit a data type from context.

## Libraries

Generated

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012b**

## Description

Simulate HDL code on FPGA hardware from Simulink

The generated FPGA-in-the-loop (FIL) simulation block is the
communication interface between the FPGA and your Simulink® model.
It integrates the hardware into the simulation loop and allows it
to participate in simulation as any other block.

You can generate a FIL Simulation block from
existing HDL code using the FPGA-in-the-Loop
Wizard, or, generate HDL code and an accompanying FIL
Simulation block using HDL Workflow Advisor. Generating HDL
code requires an HDL Coder™ license.

For the generation and simulation workflow, see Block Generation with the FIL Wizard.
If you encounter any issues during FIL simulation, refer to Troubleshooting FIL for
help in diagnosing the problem.

You can use the FIL Simulation block in models
running in Normal, Accelerator, or Rapid Accelerator simulation modes.
The FIL Simulation parameters are not tunable in any
of the simulation modes. For more information about these modes, see How Acceleration Modes Work (Simulink).
