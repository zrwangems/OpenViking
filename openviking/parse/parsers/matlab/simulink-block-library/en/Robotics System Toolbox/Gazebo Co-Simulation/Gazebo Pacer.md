---
type: simulink-block
title: 'Gazebo Pacer'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Gazebo Co-Simulation'
documentation_page: 'gazebopacer'
documentation_source_path: 'ref/gazebopacer.html'
language: en
---

# Gazebo Pacer

## Ports
```yaml
ports:
- name: Status
  summary: Status of synchronization 0 | 1
  direction: output
  data_types: uint8
```

### Output

### **Status** — Status of synchronization 0 | 1

Status of synchronization, output as either `0` or
`1`. A value of `0` indicates successful time
syncing. A value of `1` means the simulations are out of sync.

**Data Types:** `uint8`
## Parameters
```yaml
parameters:
- name: Reset behavior
  summary: Reset simulation time or scene Reset Gazebo simulation time (default) | Reset Gazebo simulation time and scene
  group: ''
- name: Sample time
  summary: Sampling time of input 0.001 (default) | positive
  group: ''
```

### **Reset behavior** — Reset simulation time or scene `Reset Gazebo simulation time` (default) | `Reset Gazebo simulation time and scene`

Select from the Reset behavior drop-down.

- `Reset Gazebo simulation time` — Resets the Gazebo
  simulator time.
- `Reset Gazebo simulation time and scene` — Resets
  both the Gazebo simulator time and scene.

### **Sample time** — Sampling time of input `0.001` (default) | positive

Set the Sample time parameter to step the Gazebo simulation at the given rate. This
parameter must be a multiple of the maximum step size of the Gazebo solver.
## Libraries

Robotics System Toolbox / Gazebo Co-Simulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Settings for synchronized stepping between Gazebo and Simulink

The Gazebo Pacer block synchronizes the simulation times between Gazebo and
Simulink®. Synchronization is important for ensuring your Simulink model and the Gazebo simulation behave correctly. The block outputs a Boolean
indicating successful synchronization. Synchronized stepping is only supported for one Gazebo
simulation. Your entire model, including referenced models, can only contain one Gazebo
Pacer block.

To ensure successful synchronization, connect to a Gazebo simulation. Open the block mask
and click **Configure Gazebo network and simulation settings**. For more
information see Configure Gazebo Simulation.

Select the `Reset behavior` to reset the Gazebo simulation on model
restart or only reset simulation time.

This block is part of a co-simulation interface between MATLAB® and Gazebo for exchanging data and sending commands. To see a basic example,
check Perform Co-Simulation Between Simulink and Gazebo.
