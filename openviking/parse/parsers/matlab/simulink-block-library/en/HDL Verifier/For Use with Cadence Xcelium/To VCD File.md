---
type: simulink-block
title: 'To VCD File'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'For Use with AMD Vivado Simulator'
documentation_page: 'tovcdfile'
documentation_source_path: 'ref/tovcdfile.html'
language: en
---

# To VCD File

## Ports

### Input

### **Port\_1, Port\_2, ..., Port\_N** — Signal to log to VCD file scalar | vector | matrix

Multi-dimensional signals are flattened to 1-D vectors in the VCD file.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `Fixed-point`

## Parameters

### **VCD file name** — Name of generated VCD file string

Name of the generated VCD file. If you specify a file name only, Simulink places the file in your current MATLAB® folder. To place the generated file in a different location, specify a complete
path name. If you specify the same name for multiple To VCD File blocks,
Simulink automatically adds a numeric postfix to identify each instance uniquely.

**Note**

To save the generated file with the `.vcd` file extension, you must
specify it explicitly.

### **Number of input ports** — Number of input signals to log integer

Number of input signals to log data from. The block can log up to 1000 signals, where
each signal maps to a unique symbol in the VCD file. To support more than 1000 signals,
instantiate more than one To VCD File block.

In some cases, a single input port maps to multiple symbols. This multiple mapping occurs
when the input port receives a multidimensional signal. Because the VCD specification does not
include multidimensional signals, Simulink flattens them to a 1-D vector in the file.

### **Timescale** — Timing relationship between Simulink and the HDL simulator integer and time units

Timing relationship, defined as the correspondence between one second of Simulink time and some quantity of HDL simulator time. You can express this quantity of
HDL simulator time in one of the following ways:

- In *relative* terms, that is, as some number of HDL simulator ticks.
  In this case, the cosimulation operates in *relative timing mode*, which
  is the timing mode default.

  To use relative mode, in the **1 second in Simulink corresponds to {value}
  {unit} in the HDL simulator** parameter, set the unit to
  `Tick`, and the value to the number of ticks you want. The default
  value is 1 tick.
- In *absolute* units, such as milliseconds or nanoseconds. In this
  case, the cosimulation operates in *absolute timing mode*.

  To use absolute mode, in the **1 second in Simulink corresponds to {value}
  {unit} in the HDL simulator** parameter, set the number of resolution units and
  the type of unit (`fs`, `ps`, `ns`,
  `us`, `ms`, `s`). Then, in the
  **1 HDL Tick is defined as** parameter, set the value of the HDL simulator
  tick to `1`, `10`, or
  `100`, and choose a resolution unit.

## Libraries

HDL Verifier / For Use with AMD Vivado Simulator HDL Verifier / For Use with Cadence Xcelium HDL Verifier / For Use with Siemens ModelSim/Questa HDL Verifier / For Use with Synopsys VCS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**HDL Architecture**

This block can be used for simulation visibility in subsystems
that generate HDL code, but is not included in the hardware implementation.

## Version History

**Introduced in R2008a**

### R2024b: Support added for VCS simulator

Add this block to a Simulink testbench to generate a VCD file in a Synopsys®
VCS® cosimulation.

## Description

Generate value change dump (VCD) file

The To VCD File block generates a VCD file that logs changes to its input ports. You can use VCD files during design verification in these ways:

- Compare results of multiple simulation runs, using the same or different simulator environments.
- Provide input to post-simulation analysis tools.
- Porting areas of an existing design to a new design.

You can specify the following parameters:

- Name of the generated VCD file
- Number of block input ports
- Timescale, that relates Simulink® sample times with HDL simulator ticks

VCD files can grow large for large designs or small designs with long simulation runs. The maximum number of signals supported in a generated VCD file is 1000.

You can use the To VCD File block in models running in normal, accelerator, or rapid accelerator simulation modes. The To VCD File parameters are not tunable in any of the simulation modes. For more information about these modes, see How Acceleration Modes Work (Simulink).

The To VCD File block is integrated into the Simulink Viewers and Generators Manager. When you add a VCD block to a model using the manager, the signal name that appears in the VCD file may not be the one you specified. After simulation, open the VCD file and check the signal name. If you cannot find the signal name you specified, look for an automatic signal name such as *`In_1`*. When you use the VCD block directly from the HDL Verifier™ library, the signal names match correctly.

### VCD File Format

The format of generated VCD files adheres to IEEE® Std 1364-2001. The table describes the format.

| VCD File Content | Description |
| --- | --- |
| ``` $date 23-Sep-2003 14:38:11 $end ``` | Date and time the file was generated. |
| ``` $version HDL Verifier version 1.0 $ end ``` | Version of the To VCD File block that generated the file. |
| ``` $timescale 1 ns $ end ``` | Timescale used during the simulation. |
| ``` $scope module manchestermodel $end ``` | Scope of module being dumped. |
| ``` $var wire 1 ! Original Data [0] $end $var wire 1 " Recovered Clock [0] $end $var wire 1 # Recovered Data [0] $end $var wire 1 $ Data Validity [0] $end ``` | Variable definitions. Each definition associates a signal with a character identification code (symbol).  The symbols are derived from printable characters in the ASCII character set from `!` to `~`.  Variable definitions also include the variable type (wire) and size in bits. |
| ``` $upscope $end ``` | Marks a change to the next highest level in the HDL design hierarchy. |
| ``` $enddefinitions $end ``` | Marks the end of the header and definitions section. |
| ``` #0 ``` | Simulation start time. |
| ``` $dumpvars  0!  0"  0#  0$ $end ``` | Lists the values of all defined variables at time 0. |
| ``` #630  1! ``` | Starting point of logged value changes from checks of variable values made at each simulation time increment.  This entry indicates that at 63 nanoseconds, the value of signal `Original Data` changed from 0 to 1. |
| ``` . . . #1160  1#  1$ ``` | At 116 nanoseconds, the values of signals `Recovered Data` and `Data Validity` changed from 0 to 1. |
| ``` $dumpoff  x!  x"  x#  x$ $end ``` | Marks the end of the file by dumping the values of all variables as the value `x`. |

### Display VCD File Data

You can display VCD file data graphically or analyze the data with postprocessing tools. For example, the ModelSim™ `vcd2wlf` tool converts a VCD file to a `WLF` file, which you can view in a ModelSim **wave** window. Other examples of postprocessing include the extraction of data pertaining to a particular section of a design hierarchy or data generated during a specific time interval.
