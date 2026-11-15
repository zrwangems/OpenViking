---
type: simulink-block
title: 'Track Concatenation'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Trackers'
documentation_page: 'trackconcatenation'
documentation_source_path: 'ref/trackconcatenation.html'
language: en
---

# Track Concatenation

## Ports

### Input

### **In1, In2, ..., InN** — Tracks to combine Simulink® buses containing MATLAB® structures

Tracks to combine, where each track is a Simulink bus containing a MATLAB structure. See Create Nonvirtual Buses (Simulink) for more details.

You can find the definitions of the track lists in the **Confirmed
Tracks** output port descriptions of the tracker blocks, such as the Global
Nearest Neighbor Multi Object Tracker block.

By default, the block includes two ports for input detections. To add more ports,
use the **Number of input sensors to combine** parameter.
### Output

### **Out** — Combined tracks Simulink bus containing MATLAB structure

Combined tacks from all input buses, returned as a Simulink bus containing a MATLAB structure. See Create Nonvirtual Buses (Simulink). You can find the definitions of the track lists
in the **Confirmed Tracks** output port descriptions of the tracker
blocks, such as the Global
Nearest Neighbor Multi Object Tracker block.

## Parameters

### **Number of input tracks to combine** — Number of input track ports `2` (default) | positive integer

Number of input track ports, specified as a positive integer. The input ports
labeled **In1**, **In2**, …, **InN**,
where *N* is the value set by this parameter.

**Data Types:** `double`

### **Source of output bus name** — Source of output bus name `Auto` (default) | `Property`

Source of the output bus name, specified as `Auto` or
`Property`.

- If you select `Auto`, the block automatically generates a bus
  name.
- If you select `Property`, specify the bus name using the
  **Specify an output bus name** parameter.

### **Specify an output bus name** — Name of output bus `BusTrackConcatenation`

Specify a name for the output bus.

#### Dependencies

To enable this parameter, set the **Source of output bus name**
parameter to `Property`.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — Simulate the model using the
  MATLAB interpreter. This option shortens startup time. In
  `Interpreted execution` mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model using generated
  C/C++ code. The first time you run a simulation, Simulink generates C/C++ code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option requires
  additional startup time.

## Libraries

Sensor Fusion and Tracking Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

### R2023a: Simulink buses do not show in workspace

As of R2023a, the Simulink buses created by this block no longer show in MATLAB workspace.

## Description

Concatenate tracks

The Track Concatenation block concatenates track buses originating from
multiple sources into a single list of object tracks. The sources to this block must all use
the `objectTrack` format, and can be sensor blocks, tracker blocks, Track-To-Track Fuser
blocks, or other track concatenation blocks. Use this block to concatenate tracks from
multiple sources before passing them into the Track-To-Track Fuser block.
