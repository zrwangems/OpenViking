---
type: simulink-block
title: 'Gazebo Select Entity'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Gazebo Co-Simulation'
documentation_page: 'gazeboselectentity'
documentation_source_path: 'ref/gazeboselectentity.html'
language: en
---

# Gazebo Select Entity

## Ports
```yaml
ports:
- name: model
  summary: Model name of entity model1 (default) | string (uint8[])
  direction: output
  data_types: uint8
- name: Joint/Link
  summary: Associated joint or link name of entity joint1 (default) | string (uint8[])
  direction: output
  data_types: uint8
```

### Output

### **model** — Model name of entity `model1` (default) | string (`uint8[]`)

Model name of entity, output as string scalar. Strings are output as a
variable-size `uint8` array for Gazebo.

**Data Types:** `uint8`

### **Joint/Link** — Associated joint or link name of entity joint1 (default) | string (`uint8[]`)

Associated joint or link, output as a string scalar. Strings are output as a
`uint8` array for Gazebo.

**Data Types:** `uint8`
## Parameters
```yaml
parameters:
- name: Model Name
  summary: Choose model name 'model1/joint1' (default) | string scalar
  group: ''
- name: Output vector size upper bound
  summary: Upper limit of output array 128 (default)
  group: ''
```

### **Model Name** — Choose model name `'model1/joint1'` (default) | string scalar

Choose a model by clicking **Select**, which brings up a list of
available names available on the Gazebo server. The block assumes you are already
connected to a Gazebo simulation. If not, click **Configure Gazebo network and
simulation settings** in the block mask.

### **Output vector size upper bound** — Upper limit of output array `128` (default)

Upper limit of the size of the output `uint8` arrays,
`Model Name` and `Joint/Link`. Increase the
upper bound when the names are longer than the default value
`128`.
## Libraries

Robotics System Toolbox / Gazebo Co-Simulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Select a Gazebo entity

The Gazebo Select Entity block retrieves the model name of a Gazebo
entity, such as a link or joint, from a simulated environment. The block outputs a string for
both the model and associated joint or link name. Use both these names when specifying
commands using the Gazebo Apply
Command block.

Before selecting an entity, connect to a Gazebo simulation. Open the block mask and click
**Configure Gazebo network and simulation settings**. For more information
see Configure Gazebo Simulation.

This block is part of a co-simulation interface between MATLAB® and Gazebo for exchanging data and sending commands. To see a basic example,
check Perform Co-Simulation Between Simulink and Gazebo
